# Build

## Requirements

- Python 3.11+ recommended
- [FontForge](https://fontforge.org) CLI (`fontforge`). OTF files are generated from merged TTF. FontForge is used only as a **build tool**; output fonts remain under SIL OFL 1.1.
- Example on macOS: `brew install fontforge`

## All-in-one

```bash
python3 -m pip install -r requirements.txt
make build
```

`make build` runs `scripts/fetch_vendor.sh` then `scripts/build_gentendard.py`, producing `dist/ttf`, `dist/otf`, and `dist/webfont`.

## Release zip

```bash
make package
```

Writes `build-release/gentendard-0.1.1.zip` (override with `GENTENDARD_RELEASE_VERSION`).
