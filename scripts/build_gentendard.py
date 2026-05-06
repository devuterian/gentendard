#!/usr/bin/env python3
"""
Build Gentendard: Gen Interface JP (Japanese / shared CJK base) + Pretendard
glyphs for Latin and Hangul-related Unicode ranges (matched by weight).
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict, Iterable, Set, Tuple

from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont

WEIGHTS: Tuple[str, ...] = (
    "Thin",
    "ExtraLight",
    "Light",
    "Regular",
    "Medium",
    "SemiBold",
    "Bold",
    "ExtraBold",
)

SUBFAMILY_LABEL: Dict[str, str] = {
    "Thin": "Thin",
    "ExtraLight": "Extra Light",
    "Light": "Light",
    "Regular": "Regular",
    "Medium": "Medium",
    "SemiBold": "Semi Bold",
    "Bold": "Bold",
    "ExtraBold": "Extra Bold",
}

PS_SUFFIX: Dict[str, str] = {
    "Thin": "Thin",
    "ExtraLight": "ExtraLight",
    "Light": "Light",
    "Regular": "Regular",
    "Medium": "Medium",
    "SemiBold": "SemiBold",
    "Bold": "Bold",
    "ExtraBold": "ExtraBold",
}


def _in_pretendard_takeover(cp: int) -> bool:
    if 0x0020 <= cp <= 0x007F:
        return True
    if 0x00A0 <= cp <= 0x024F:
        return True
    if 0x0250 <= cp <= 0x02FF:
        return True
    if 0x0300 <= cp <= 0x036F:
        return True
    if 0x0370 <= cp <= 0x052F:
        return True
    if 0x1E00 <= cp <= 0x1EFF:
        return True
    if 0x2000 <= cp <= 0x206F:
        return True
    if 0x2070 <= cp <= 0x209F:
        return True
    if 0x20A0 <= cp <= 0x20CF:
        return True
    if 0x2100 <= cp <= 0x214F:
        return True
    if 0x2150 <= cp <= 0x218F:
        return True
    if 0x2190 <= cp <= 0x21FF:
        return True
    if 0x2200 <= cp <= 0x22FF:
        return True
    if 0x2300 <= cp <= 0x23FF:
        return True
    if 0x2400 <= cp <= 0x24FF:
        return True
    if 0x25A0 <= cp <= 0x25FF:
        return True
    if 0x2600 <= cp <= 0x26FF:
        return True
    if 0x2700 <= cp <= 0x27BF:
        return True
    if 0x2C60 <= cp <= 0x2C7F:
        return True
    if 0x2DE0 <= cp <= 0x2DFF:
        return True
    if 0xA640 <= cp <= 0xA69F:
        return True
    if 0xA720 <= cp <= 0xA7FF:
        return True
    if 0xAB30 <= cp <= 0xAB6F:
        return True
    if 0xFB00 <= cp <= 0xFB06:
        return True
    if 0x1100 <= cp <= 0x11FF:
        return True
    if 0x302E <= cp <= 0x302F:
        return True
    if 0x3130 <= cp <= 0x318F:
        return True
    if 0x3200 <= cp <= 0x321E:
        return True
    if 0x3260 <= cp <= 0x327E:
        return True
    if 0xAC00 <= cp <= 0xD7A3:
        return True
    if 0xFFA0 <= cp <= 0xFFDC:
        return True
    return False


def _best_unicode_cmap(font: TTFont) -> Dict[int, str]:
    cmap = font["cmap"]
    for t in cmap.tables:
        if t.platformID == 3 and t.platEncID in (1, 10) and t.isUnicode():
            return dict(t.cmap)
    return dict(cmap.getBestCmap())


def _set_unicode_cmap(font: TTFont, cp: int, gname: str) -> None:
    for t in font["cmap"].tables:
        if t.isUnicode():
            t.cmap[cp] = gname


def _copy_decomposed_glyf(src: TTFont, dst: TTFont, src_g: str, dst_g: str) -> None:
    src_gs = src.getGlyphSet()
    decomp = DecomposingRecordingPen(src_gs)
    src_gs[src_g].draw(decomp)
    pen = TTGlyphPen(None)
    decomp.replay(pen)
    dst["glyf"][dst_g] = pen.glyph()


def _copy_hmtx(src: TTFont, dst: TTFont, src_g: str, dst_g: str) -> None:
    adv, lsb = src["hmtx"].metrics[src_g]
    dst["hmtx"].metrics[dst_g] = (adv, lsb)


def _ensure_vmtx(dst: TTFont, gname: str, default: Tuple[int, int]) -> None:
    if "vmtx" not in dst:
        return
    if gname not in dst["vmtx"].metrics:
        dst["vmtx"].metrics[gname] = default


def _rename_family(font: TTFont, family: str, subfamily: str, ps_name: str) -> None:
    name = font["name"]
    for nid, s in (
        (1, family),
        (2, subfamily),
        (4, f"{family} {subfamily}"),
        (6, ps_name),
    ):
        name.setName(s, nid, 3, 1, 0x409)
        try:
            name.setName(s, nid, 1, 0, 0)
        except Exception:
            pass


def merge_pair(
    gen_path: Path,
    pret_path: Path,
    out_ttf: Path,
    *,
    family: str,
    subfamily: str,
    ps_name: str,
) -> None:
    base = TTFont(gen_path)
    pret = TTFont(pret_path)

    pret_map = _best_unicode_cmap(pret)
    base_map = _best_unicode_cmap(base)

    takeover: Set[int] = {cp for cp in pret_map if _in_pretendard_takeover(cp)}
    default_v = (0, 0)
    if "vmtx" in base and ".notdef" in base["vmtx"].metrics:
        default_v = base["vmtx"].metrics[".notdef"]

    glyph_order = list(base.getGlyphOrder())
    order_set = set(glyph_order)

    for cp in sorted(takeover):
        src_g = pret_map.get(cp)
        if not src_g or src_g == ".notdef":
            continue
        if cp in base_map:
            dst_g = base_map[cp]
            _copy_decomposed_glyf(pret, base, src_g, dst_g)
            _copy_hmtx(pret, base, src_g, dst_g)
            _ensure_vmtx(base, dst_g, default_v)
            continue

        new_g = f"_pret.{src_g}"
        while new_g in order_set:
            new_g = new_g + "_"
        _copy_decomposed_glyf(pret, base, src_g, new_g)
        _copy_hmtx(pret, base, src_g, new_g)
        glyph_order.append(new_g)
        order_set.add(new_g)
        base_map[cp] = new_g
        _set_unicode_cmap(base, cp, new_g)
        _ensure_vmtx(base, new_g, default_v)

    base.setGlyphOrder(glyph_order)
    _rename_family(base, family, subfamily, ps_name)
    out_ttf.parent.mkdir(parents=True, exist_ok=True)
    base.save(out_ttf, reorderTables=True)


def _which_ff() -> str | None:
    return shutil.which("fontforge")


def ttf_to_otf(ttf: Path, otf: Path) -> None:
    ff = _which_ff()
    if not ff:
        raise RuntimeError("fontforge binary not found; install FontForge to build OTF.")
    otf.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        ff,
        "-lang=py",
        "-c",
        f"import fontforge; f=fontforge.open({str(ttf)!r}); f.generate({str(otf)!r})",
    ]
    subprocess.run(cmd, check=True)


def ttf_to_woff2(ttf: Path, woff2: Path) -> None:
    woff2.parent.mkdir(parents=True, exist_ok=True)
    font = TTFont(ttf)
    font.flavor = "woff2"
    font.save(woff2)


def _find_gen_ttf(vendor_gen: Path, weight: str, *, display: bool) -> Path:
    roots = list(vendor_gen.glob("GenInterfaceJP-*"))
    if not roots:
        raise FileNotFoundError(f"No GenInterfaceJP-* under {vendor_gen}")
    root = roots[0]
    sub = "Gen Interface JP Display" if display else "Gen Interface JP"
    prefix = "GenInterfaceJPDisplay" if display else "GenInterfaceJP"
    p = root / sub / f"{prefix}-{weight}.ttf"
    if not p.is_file():
        raise FileNotFoundError(p)
    return p


def _find_pret_ttf(vendor_pret: Path, weight: str) -> Path:
    p = vendor_pret / "public" / "static" / "alternative" / f"Pretendard-{weight}.ttf"
    if not p.is_file():
        raise FileNotFoundError(p)
    return p


def build_all(
    vendor: Path,
    dist: Path,
    *,
    otf: bool,
    woff2: bool,
) -> None:
    vendor_gen = vendor / "gen-interface-jp"
    vendor_pret = vendor / "pretendard"
    dist_ttf = dist / "ttf"
    dist_otf = dist / "otf"
    dist_web = dist / "webfont"

    for display in (False, True):
        fam = "Gentendard Display" if display else "Gentendard"
        file_fam = "GentendardDisplay" if display else "Gentendard"
        for w in WEIGHTS:
            gen_ttf = _find_gen_ttf(vendor_gen, w, display=display)
            pret_ttf = _find_pret_ttf(vendor_pret, w)
            sub = SUBFAMILY_LABEL[w]
            ps = f"{file_fam}-{PS_SUFFIX[w]}"
            out_name = f"{file_fam}-{PS_SUFFIX[w]}.ttf"
            out_path = dist_ttf / out_name
            merge_pair(
                gen_ttf,
                pret_ttf,
                out_path,
                family=fam,
                subfamily=sub,
                ps_name=ps,
            )
            if otf:
                ttf_to_otf(out_path, dist_otf / out_name.replace(".ttf", ".otf"))
            if woff2:
                ttf_to_woff2(out_path, dist_web / out_name.replace(".ttf", ".woff2"))


def main(argv: Iterable[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vendor", type=Path, default=Path("vendor"))
    ap.add_argument("--dist", type=Path, default=Path("dist"))
    ap.add_argument("--no-otf", action="store_true")
    ap.add_argument("--no-woff2", action="store_true")
    args = ap.parse_args(list(argv))
    build_all(
        args.vendor.resolve(),
        args.dist.resolve(),
        otf=not args.no_otf,
        woff2=not args.no_woff2,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
