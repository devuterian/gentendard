# Gentendard

日本語・漢字ベースは [Gen Interface JP](https://github.com/yamatoiizuka/gen-interface-jp)、ラテン文字・ハングル関連のコードポイントは [Pretendard](https://github.com/orioncactus/pretendard) のグリフで上書きした合成フォントです。**Gentendard**（本文・UI）と **Gentendard Display**（ディスプレイ）の2ファミリー、各8ウェイト（100–800）です。

[한국어](README.md) | [English](README.en.md) | 日本語

---

## 入手

**[Releases](https://github.com/devuterian/gentendard/releases)** の **v0.1.0** に zip があります。`OFL.txt`、`ttf/`、`otf/`、`webfont/`（WOFF2）を含みます。

**本バージョンは十分に検証されていない初期ビルドです。** 本番利用前に必ず表示を確認してください。

---

## ソースからビルド

[`docs/build.md`](docs/build.md)（韓国語）を参照してください。

```bash
python3 -m pip install -r requirements.txt
make build
make package
```

---

## 由来・ライセンス

| 区分 | 出典 | 備考 |
| --- | --- | --- |
| 日本語・CJKベース | [yamatoiizuka/gen-interface-jp](https://github.com/yamatoiizuka/gen-interface-jp) リリース **v0.1.1** | フォントは OFL 1.1。上流に Inter・Noto Sans JP 等（[LICENSE](https://github.com/yamatoiizuka/gen-interface-jp/blob/main/LICENSE)） |
| ラテン・ハングル | [orioncactus/pretendard](https://github.com/orioncactus/pretendard) リリース **v1.3.9** 静的 TTF | OFL 1.1。予約フォント名に Pretendard・Inter・Source・M PLUS 1 等（[LICENSE](https://github.com/orioncactus/pretendard/blob/main/LICENSE)） |
| 本リポジトリのスクリプト・文書 | [devuterian/gentendard](https://github.com/devuterian/gentendard) | [MIT](LICENSE)（フォントバイナリは OFL。例外条項を参照） |
| 合成結果のフォント | 上記の **派生物** | **SIL OFL 1.1** — [`OFL.txt`](OFL.txt) および zip 内の同ファイル |

CJK 統合漢字はコードポイントごとに1グリフのみのため、本合成では Gen Interface JP 側の字形が残ります。ハングルと漢字が混じる文脈では期待と異なる場合があります。グリフのみ差し替えるため、GSUB/GPOS 等は上流と異なることがあります。

**OTF** は FontForge CLI で生成します（ビルド**ツール**としてのみ利用）。配布フォントの条件は OFL に従います。

---

## リポジトリ

- [github.com/devuterian/gentendard](https://github.com/devuterian/gentendard)
- ビルド: [`docs/build.md`](docs/build.md)
- コントリビューション: [`CONTRIBUTING.md`](CONTRIBUTING.md)

不具合・質問は [Issues](https://github.com/devuterian/gentendard/issues) へ。

---

運用・文書の骨格は [LPFchan/repo-template](https://github.com/LPFchan/repo-template) を参考にしました。
