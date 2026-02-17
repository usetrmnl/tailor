# Tailor your TRMNL

This repository contains the source code that lets you tailor your TRMNL. This works by creating a brand binary on your browser and updating the brand binary on the device directly without downloading / installing / modifying the [firmware](https://github.com/usetrmnl/trmnl-firmware) source code.

## Supported Changes
You can make customizations to the following brand attributes 
1. API Base URL (coming soon)
2. Logo
3. Loading Icon

## How to get started?
1. Clone this repository
2. `git submodule init`
3. `git submodule update`
4. Install emscripten eg: `brew install emscripten`
5. Compile and create a wasm file `bash build.sh`
6. open `index.html` on your browser.

# Community Screens
[tailor.trmnl.com](https://tailor.trmnl.com/)
Customize TRMNL with Tailor, our firmware tool that writes custom splash and loading screens for your TRMNL device.

## Devices Supported
- TRMNL OG (800x480)

## Folder and File Structure
```
screens/
├─ 800x480/
│  ├─ CATEGORY/
│  │  ├─ splash/
│  │  ├─ loading/
```
> New categories and subsequent folders can be created as part of a Pull Request.

### Filename Structure
Hyphen separated sections, with underscore for spaces within a section. _Credit is optional._
**WIDTHxHEIGHT-TYPE-UNIQUE_NAME-CREDIT?.png**
_e.g._ 
`800x480-splash-dungeon_crawler_carl_safehouse-mashermello.png`
`800x480-loading-dungeon_crawler_carl_princess_donut.png`

## License
Any PR'd screens will fall under either CC0 (you own the rights and choose this license) or Public Domain licensing for us to be able to host them and have traceability.

## View the Gallery
- [800x480 Screens](https://github.com/usetrmnl/tailor/blob/master/GALLERY_800x480.md)