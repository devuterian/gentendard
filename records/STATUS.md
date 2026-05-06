# Gentendard Status

## Snapshot

- **Last updated:** 2026-05-06
- **Overall posture:** `active`
- **Current focus:** Initial public release v0.1.0 (untested); reproducible build and license clarity.
- **Highest-priority blocker:** None for source publication; downstream users must validate rendering.
- **Next operator decision needed:** Whether to add CI font build and/or automated smoke tests.

## Current state summary

The repository contains the merge pipeline, documentation, and repo-template governance files. Font binaries are produced locally and distributed via GitHub Releases, not committed to git.

## Active phases or tracks

### Release v0.1.0

- **Goal:** Publish zip with TTF, OTF, WOFF2 and accurate OFL attribution.
- **Status:** `in progress`
- **Exit criteria:** Release asset uploaded; README links live.

## Recent changes to project reality

- **2026-05-06:** Initial repo content: fetch script, `build_gentendard.py`, packaging script, tri-lingual README.

## Active blockers and risks

- **Glyph-only overlay** may leave some OpenType features misaligned with either upstream.
- **FontForge** OTF conversion may emit warnings; output should still be spot-checked.

## Immediate next steps

- Push to GitHub and attach `build-release/gentendard-0.1.0.zip` to tag `v0.1.0`.
- Optionally add GitHub Actions workflow for commit standards only (fonts build is heavy).
