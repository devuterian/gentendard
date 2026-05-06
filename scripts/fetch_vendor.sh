#!/bin/sh
set -eu
ROOT=$(CDPATH= cd "$(dirname "$0")/.." && pwd)
VENDOR="$ROOT/vendor"
mkdir -p "$VENDOR"

GEN_VER="${GEN_INTERFACE_JP_VERSION:-0.1.1}"
PRET_VER="${PRETENDARD_VERSION:-1.3.9}"

GEN_ZIP="$VENDOR/GenInterfaceJP-${GEN_VER}.zip"
PRET_ZIP="$VENDOR/Pretendard-${PRET_VER}.zip"

if [ ! -f "$GEN_ZIP" ]; then
  curl -sL -o "$GEN_ZIP" \
    "https://github.com/yamatoiizuka/gen-interface-jp/releases/download/v${GEN_VER}/GenInterfaceJP-${GEN_VER}.zip"
fi

if [ ! -f "$PRET_ZIP" ]; then
  curl -sL -o "$PRET_ZIP" \
    "https://github.com/orioncactus/pretendard/releases/download/v${PRET_VER}/Pretendard-${PRET_VER}.zip"
fi

rm -rf "$VENDOR/gen-interface-jp" "$VENDOR/pretendard"
unzip -q -o "$GEN_ZIP" -d "$VENDOR/gen-interface-jp"
unzip -q -o "$PRET_ZIP" -d "$VENDOR/pretendard"

echo "Vendor unpacked under $VENDOR/gen-interface-jp and $VENDOR/pretendard"
