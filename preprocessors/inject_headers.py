import json
import sys
from typing import Any
import re


DIRECTIVE_REGEX = re.compile(r"\{\{#header\s*(.+)\s*}}")
# matches parameters of the form `title="my string"` and `level=3`,
# while handling escapes for the `"` character.
PARAM_REGEX = re.compile(r'\s*(\w+)=(".*?(?<![^"]")"(?!")|\w+)')

def create_header(
    title: str,
    level: int,
    hidden: bool,
) -> str:
    fmt_title = re.sub(r'\W+', '-', title)
    hidden_str = ' hidden' if hidden else ''
    level_str = f'h{level}'
    # the newlines ensure the contents immediately preceding/following
    # the header are processed correctly.
    return (
        f'\n'
        f'<{level_str}{hidden_str}>'
        f'<a class="header" href="#{fmt_title}">{title}</a>'
        f'</{level_str}>'
        #
        f'<a id="{fmt_title}"></a>'
        f'\n'
    )


def inject_header(
    match: re.Match[str],
) -> str:
    params = {
        # default values
        "level": 1,
        "hidden": False,
    }
    for pmatch in re.finditer(PARAM_REGEX, match.group(1)):
        key = pmatch.group(1)

        if key not in {'title', 'level', 'hidden'}:
            raise TypeError(
                f'Unexpected paramater {key!r} in {match.group()!r}'
            )

        value = pmatch.group(2)

        if value.startswith('"'):
            value = value[1:-1].replace('""', '"')
        elif value in {'true', 'false'}:
            value = value == 'true'
        else:
            value = int(value)

        params[key] = value

    if 'title' not in params:
        raise TypeError(
            f'Missing required parameter \'title\' in {match.group()}'
        )

    if not all((
        isinstance(params['title'], str),
        isinstance(params['level'], int),
        isinstance(params['hidden'], bool)
    )):
        raise TypeError(
            f'Incorrect type for value in {match.group()}'
        )

    if not (0 < params['level'] < 7):
        raise ValueError(
            f'Parameter \'level\' must be between 1 and 6 in {match.group()}'
        )

    return create_header(**params)


def inject_headers(
    text: str,
) -> str:
    if not re.search(DIRECTIVE_REGEX, text):
        return text

    return re.sub(DIRECTIVE_REGEX, inject_header, text)


def process_section(section: dict[str, dict[str, Any]]):
    if "Chapter" not in section:
        return

    section["Chapter"]["content"] = inject_headers(section["Chapter"]["content"])

    if "sub_items" in section["Chapter"]:
        for subsection in section["Chapter"]["sub_items"]:
            process_section(subsection)


def process_book(book: dict[str, Any]):
    for section in book["sections"]:
        process_section(section)


def main() -> None:
    if len(sys.argv) > 1:
        if sys.argv[1] == "supports":
            sys.exit(0)

    _context, book = tuple(json.load(sys.stdin))

    process_book(book)

    print(json.dumps(book))
    sys.exit(0)


if __name__ == '__main__':
    main()
