alias b := build
alias o := open
alias gca := generate-custom-admonish

install-mdbook:
    curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf -y | sh
    rustup update
    cargo install --version ${MDBOOK_VERSION} mdbook
    cargo install --version ${MDBOOK_PAGETOC_VERSION} mdbook-pagetoc
    cargo install --version ${MDBOOK_ADMONISH_VERSION} mdbook-admonish

build:
    mdbook-admonish generate-custom ./assets/gen/css/mdbook-admonish-custom.css
    mdbook build

open:
    mdbook-admonish generate-custom ./assets/gen/css/mdbook-admonish-custom.css
    mdbook serve --open

generate-custom-admonish:
    mdbook-admonish generate-custom ./assets/gen/css/mdbook-admonish-custom.css
