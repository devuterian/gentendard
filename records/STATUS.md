# Gentendard Status

## Snapshot

- **Last updated:** 2026-05-06
- **Overall posture:** `active`
- **Current focus:** Post–v0.1.1 maintenance; optional CI for font builds.
- **Highest-priority blocker:** None for source publication; downstream users must validate rendering.
- **Next operator decision needed:** Whether to add CI font build and/or automated smoke tests.

## Current state summary

The repository contains the merge pipeline, documentation, and repo-template governance files. Font binaries are produced locally and distributed via GitHub Releases, not committed to git.

## Active phases or tracks

### Release v0.1.1

- **Goal:** Same artifacts as v0.1.0 with `name` IDs 3, 16, 17 set so **Gentendard** appears (not Gen Interface JP) in macOS Font Book and pickers.
- **Status:** `done`
- **Exit criteria:** GitHub Release v0.1.1 zip published; user Fonts folder can be refreshed from zip or local `make build`.

## Recent changes to project reality

- **2026-05-06:** v0.1.1 — `name` 테이블 ID 3·16·17을 덮어 서체 메뉴에 **Gentendard**가 보이도록 수정.

## Active blockers and risks

- **Glyph-only overlay** may leave some OpenType features misaligned with either upstream.
- **FontForge** OTF conversion may emit warnings; output should still be spot-checked.

## Immediate next steps

- Optionally add GitHub Actions workflow for commit standards only (fonts build is heavy).