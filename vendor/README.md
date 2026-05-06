# Vendor fonts (not committed)

Run from the repository root:

```bash
sh scripts/fetch_vendor.sh
```

This downloads and unpacks:

| Source | Version | Release |
| --- | --- | --- |
| Gen Interface JP | 0.1.1 | [GenInterfaceJP-0.1.1.zip](https://github.com/yamatoiizuka/gen-interface-jp/releases/download/v0.1.1/GenInterfaceJP-0.1.1.zip) |
| Pretendard | 1.3.9 | [Pretendard-1.3.9.zip](https://github.com/orioncactus/pretendard/releases/download/v1.3.9/Pretendard-1.3.9.zip) |

Override versions with `GEN_INTERFACE_JP_VERSION` and `PRETENDARD_VERSION` if needed.

The unpacked trees live in `vendor/gen-interface-jp/` and `vendor/pretendard/`. Zip archives are kept under `vendor/*.zip` for reproducibility and are ignored by git.
