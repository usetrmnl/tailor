### Tailor your TRMNL

This repository contains the source code that lets you tailor your TRMNL. This works by creating a brand binary on your browser and updating the brand binary on the device directly without downloading / installing / modifying the [firmware](https://github.com/usetrmnl/trmnl-firmware) source code.

## Supported Changes
You can make customizations to the following brand attributes 
1. API Base URL (coming soon)
2. Logo
3. Loading Icon

### How to get started?
1. Clone this repository
2. `git submodule init`
3. `git submodule update`
4. Install emscripten eg: `brew install emscripten`
5. Compile and create a wasm file `bash build.sh`
6. open `index.html` on your browser.
