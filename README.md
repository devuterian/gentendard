# Gentendard

일본어·한자는 [Gen Interface JP](https://github.com/yamatoiizuka/gen-interface-jp) 쪽을 베이스로, 라틴·한글 관련 코드포인트는 [Pretendard](https://github.com/orioncactus/pretendard) 글리프로 덮어 쓴 병합 폰트입니다. UI·본문용 **Gentendard**와 디스플레이용 **Gentendard Display** 각각 8웨이트(100–800)입니다.

[한국어](README.md) | [English](README.en.md) | [日本語](README.ja.md)

---

## 받기

**[Releases](https://github.com/devuterian/gentendard/releases)** 에서 **v0.1.1** 아티팩트(zip)를 받을 수 있어요. zip 안에는 `OFL.txt`, `ttf/`, `otf/`, `webfont/`(WOFF2)가 들어 있습니다.

**이 빌드는 자동·수동 품질 검증이 끝나지 않은 초기 버전이에요.** 프로덕션에 쓰기 전에 반드시 화면에서 직접 확인해 주세요.

---

## 소스에서 빌드

[`docs/build.md`](docs/build.md) 를 봐 주세요. 요약:

```bash
python3 -m pip install -r requirements.txt
make build
make package   # build-release/gentendard-0.1.1.zip
```

---

## 출처·라이선스

| 구분 | 출처 | 비고 |
| --- | --- | --- |
| 일본어·CJK 베이스 | [yamatoiizuka/gen-interface-jp](https://github.com/yamatoiizuka/gen-interface-jp) 릴리스 **v0.1.1** | 산출물 OFL 1.1; 업스트림 Inter·Noto Sans JP 등 ([저장소 LICENSE](https://github.com/yamatoiizuka/gen-interface-jp/blob/main/LICENSE)) |
| 라틴·한글 오버레이 | [orioncactus/pretendard](https://github.com/orioncactus/pretendard) 릴리스 **v1.3.9** 정적 TTF | OFL 1.1; 예약 폰트명 Pretendard·Inter·Source·M PLUS 1 등 ([LICENSE](https://github.com/orioncactus/pretendard/blob/main/LICENSE)) |
| 본 저장소 스크립트·문서 | [devuterian/gentendard](https://github.com/devuterian/gentendard) | [MIT](LICENSE) (폰트 바이너리는 OFL만 적용, 예외 조항 참고) |
| 병합 산출 폰트 | 위 조합의 **파생물** | **SIL OFL 1.1** — 전문은 루트 [`OFL.txt`](OFL.txt) 및 릴리스 zip 동일 파일 |

동일 코드포인트의 **한자(한·일 공통 영역)** 는 한 벌의 글리프만 들어가므로, 이 병합에서는 Gen Interface JP 쪽 형태가 유지됩니다. 한글 한자 혼용 UI에서는 기대와 다를 수 있어요. 또한 글리프만 일부 바꾸는 방식이라 GSUB/GPOS 등 레이아웃 기능은 업스트림 대비 달라질 수 있습니다.

**OTF 생성**에 FontForge CLI를 씁니다. FontForge 자체는 GPL 계열이지만, 그로 생성한 폰트 파일의 배포 조건은 위 OFL 고지를 따릅니다.

---

## 저장소·기여

- 저장소: [github.com/devuterian/gentendard](https://github.com/devuterian/gentendard)
- 빌드: [`docs/build.md`](docs/build.md)
- 기여·커밋 형식: [`CONTRIBUTING.md`](CONTRIBUTING.md)

버그·질문은 [Issues](https://github.com/devuterian/gentendard/issues)에 남겨 주세요.

---

저장소 운영·문서 골격은 [LPFchan/repo-template](https://github.com/LPFchan/repo-template)을 참고했어요. 템플릿을 공개해 주셔서 고마워요.
