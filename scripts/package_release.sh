#!/bin/sh
set -eu
ROOT=$(CDPATH= cd "$(dirname "$0")/.." && pwd)
VERSION="${GENTENDARD_RELEASE_VERSION:-0.1.0}"
OUT_DIR="${ROOT}/build-release"
STAGING="${OUT_DIR}/gentendard-${VERSION}"

[ -d "${ROOT}/dist/ttf" ] || {
  echo "run \`make build\` first" >&2
  exit 1
}

rm -rf "$STAGING"
mkdir -p "$STAGING/ttf" "$STAGING/otf" "$STAGING/webfont"
cp "${ROOT}/OFL.txt" "$STAGING/"
cp "${ROOT}/dist/ttf/"*.ttf "$STAGING/ttf/"
cp "${ROOT}/dist/otf/"*.otf "$STAGING/otf/"
cp "${ROOT}/dist/webfont/"*.woff2 "$STAGING/webfont/"

mkdir -p "$OUT_DIR"
( cd "$OUT_DIR" && rm -f "gentendard-${VERSION}.zip" && zip -qr "gentendard-${VERSION}.zip" "gentendard-${VERSION}" )
echo "Wrote ${OUT_DIR}/gentendard-${VERSION}.zip"
