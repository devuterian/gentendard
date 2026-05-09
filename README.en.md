# Gentendard

**Gentendard** merges **[Gen Interface JP](https://github.com/yamatoiizuka/gen-interface-jp)** (Japanese and shared CJK base) with **Latin and Hangul-related codepoints** taken from **[Pretendard](https://github.com/orioncactus/pretendard)** static TTFs, per weight. Two families ship in eight weights (100–800): **Gentendard** (UI/body) and **Gentendard Display**.

[Korean](README.md) | English | [Japanese](README.ja.md)

---

## Download

See **[Releases](https://github.com/devuterian/gentendard/releases)** for the **v0.1.1** zip. It contains `OFL.txt`, `ttf/`, `otf/`, and `webfont/` (WOFF2).

**This is an early, untested build.** Validate in your own environment before production use.

---

## Build from source

See [`docs/build.en.md`](docs/build.en.md) (or [`docs/build.md`](docs/build.md) in Korean).

```bash
python3 -m pip install -r requirements.txt
make build
make package
```

---

## Provenance and license

| Part | Source | Notes |
| --- | --- | --- |
| Japanese / CJK base | [yamatoiizuka/gen-interface-jp](https://github.com/yamatoiizuka/gen-interface-jp) release **v0.1.1** | Font binaries OFL 1.1; upstream Inter, Noto Sans JP, etc. ([repo LICENSE](https://github.com/yamatoiizuka/gen-interface-jp/blob/main/LICENSE)) |
| Latin + Hangul overlay | [orioncactus/pretendard](https://github.com/orioncactus/pretendard) release **v1.3.9** static TTF | OFL 1.1; Reserved Font Names include Pretendard, Inter, Source, M PLUS 1 ([LICENSE](https://github.com/orioncactus/pretendard/blob/main/LICENSE)) |
| This repository (scripts, docs) | [devuterian/gentendard](https://github.com/devuterian/gentendard) | [MIT](LICENSE); font outputs are **not** under MIT (see license exceptions there) |
| Merged font files | Derivative of the above | **SIL OFL 1.1** — see [`OFL.txt`](OFL.txt) and the same file inside the release zip |

**CJK Unified Ideographs** map to a single glyph per code point; this build keeps the **Japanese-oriented** shapes from Gen Interface JP. Mixed Korean Hanja may not match Pretendard. OpenType layout tables may differ from either upstream after partial glyph replacement.

OTF files are produced with **FontForge** CLI (GPL-licensed **tool** only); redistributed fonts follow OFL as stated above.

---

## Repository

- [github.com/devuterian/gentendard](https://github.com/devuterian/gentendard)
- Build: [`docs/build.en.md`](docs/build.en.md)
- Contributing: [`CONTRIBUTING.md`](CONTRIBUTING.md)

Issues: [github.com/devuterian/gentendard/issues](https://github.com/devuterian/gentendard/issues)

---

Repo operating conventions follow [LPFchan/repo-template](https://github.com/LPFchan/repo-template). Thank you for publishing the template.
