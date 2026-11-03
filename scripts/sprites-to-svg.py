#!/usr/bin/env python3
"""Export PhoneNap sprites from the app's SpriteCatalog Swift sources to transparent SVGs.

Usage: python3 scripts/sprites-to-svg.py <path to pixelpet/Packages/PixelPetKit/Sources/DesignSystem> <out dir>
Re-run whenever the app's sprites change.
"""
import pathlib
import re
import sys

HEX = {"K": "1E3A3F", "O": "F2D3AB", "B": "AD7757", "P": "F0B6C0", "W": "FFFFFF", "G": "75A743",
       "L": "D0DA91", "Y": "F2D3AB", "F": "4F8FBA", "R": "D26471", "N": "494D7E", "A": "E8C25A"}
SPRITE = re.compile(r'name:\s*"([^"]+)",\s*rows:\s*\[(.*?)\]', re.S)


def svg(rows):
    w, h = len(rows[0]), len(rows)
    rects = []
    for y, row in enumerate(rows):
        x = 0
        while x < w:
            c = row[x]
            run = 1
            while x + run < w and row[x + run] == c:
                run += 1
            if c in HEX:
                rects.append(f'<rect x="{x}" y="{y}" width="{run}" height="1" fill="#{HEX[c]}"/>')
            x += run
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w * 8}" height="{h * 8}" '
            f'shape-rendering="crispEdges">{"".join(rects)}</svg>\n')


def main(src, out):
    out = pathlib.Path(out)
    out.mkdir(parents=True, exist_ok=True)
    count = 0
    for f in sorted(pathlib.Path(src, "Sprites").glob("SpriteCatalog*.swift")):
        for name, body in SPRITE.findall(f.read_text()):
            rows = re.findall(r'"([^"]*)"', body)
            assert rows and all(len(r) == len(rows[0]) for r in rows), f"ragged sprite {name}"
            (out / f"{name.removeprefix('icon.')}.svg").write_text(svg(rows))
            count += 1
    assert count > 0, "no sprites found"
    print(f"{count} sprites -> {out}")


if __name__ == "__main__":
    main(*sys.argv[1:3])
