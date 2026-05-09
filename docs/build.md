# 빌드하기

## 필요한 것

- Python 3.11+ 권장
- [FontForge](https://fontforge.org) CLI (`fontforge` 명령). OTF는 FontForge로 TTF를 내보냅니다. FontForge는 **빌드 도구**로만 쓰이며, 산출 폰트 파일의 라이선스는 OFL 1.1입니다.
- macOS에서 Homebrew 예: `brew install fontforge`

## 한 번에

```bash
python3 -m pip install -r requirements.txt
make build
```

`make build`는 `scripts/fetch_vendor.sh`로 업스트림 zip을 받고, `scripts/build_gentendard.py`로 `dist/ttf`, `dist/otf`, `dist/webfont`을 만듭니다.

## 개별 단계

```bash
sh scripts/fetch_vendor.sh
python3 scripts/build_gentendard.py
```

OTF나 WOFF2를 건너뛰려면:

```bash
python3 scripts/build_gentendard.py --no-otf
python3 scripts/build_gentendard.py --no-woff2
```

## 릴리스 zip

```bash
make package
```

`build-release/gentendard-0.1.1.zip`에 `OFL.txt`, `ttf/`, `otf/`, `webfont/`가 들어갑니다. 버전은 `GENTENDARD_RELEASE_VERSION`으로 바꿀 수 있습니다.
