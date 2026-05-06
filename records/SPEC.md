# Gentendard Spec

- **Project:** Gentendard — merged OpenType fonts combining Gen Interface JP (Japanese / shared CJK base) with Pretendard glyphs for Latin and Hangul-related Unicode ranges, per weight.
- **Canonical repo:** https://github.com/devuterian/gentendard
- **Project id:** `gentendard`
- **Operator:** Repository owner (`devuterian`).
- **Last updated:** 2026-05-06

## Thesis

Ship a single font family (plus Display) for UI that pairs Japanese typography from Gen Interface JP with Latin and Hangul from Pretendard, under a new OFL-compliant name (**Gentendard**) that does not use upstream Reserved Font Names.

## Core capabilities

- Reproducible build from pinned upstream release zips (`scripts/fetch_vendor.sh`).
- Outputs: TTF (primary), OTF (via FontForge), WOFF2.
- Two families × eight weights: Gentendard, Gentendard Display.

## Invariants

- Redistributed font binaries must stay under **SIL OFL 1.1** with accurate copyright stack in `OFL.txt`.
- Do not name the derivative **Pretendard**, **Inter**, **Source**, **Noto**, **Gen Interface JP**, or other reserved names as the primary font name.

## Non-goals (current)

- Perfect per-locale Hanja/CJK alternates for both Japanese and Korean in one glyph set.
- Full re-merging of GSUB/GPOS from both sources beyond practical glyph replacement.

## Main surfaces

- GitHub **Releases** for zip artifacts; git tracks source and docs only.

## Success criteria

- Build completes from clean vendor fetch; release zip contains `ttf/`, `otf/`, `webfont/`, and `OFL.txt`.
- README (ko/en/ja) states provenance and licenses without hand-wavy disclaimers.
