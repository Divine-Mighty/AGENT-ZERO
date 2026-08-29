#!/usr/bin/env python3
"""Cut the hero figure out of the lookbook frame -> assets/hero-model.webp

    pip install rembg onnxruntime pillow numpy
    python3 cutout.py

Run once, when the source shot changes. build.py consumes only the .webp.

The shot is a black hoodie on a near-black gradient, so a luminance or
difference key tears through the hood and shoulders -- there is almost no
contrast there to find. u2net segments it properly instead.
"""

import os

import numpy as np
from PIL import Image
from rembg import new_session, remove

SRC = "assets/hero-source.png"
OUT = "assets/hero-model.webp"
TARGET_H = 1240
FADE_FROM = 0.90   # feather the hem over the last tenth
QUALITY = 84


def main():
    if not os.path.exists(SRC):
        raise SystemExit("missing " + SRC)

    cut = remove(Image.open(SRC).convert("RGB"),
                 session=new_session("u2net"), post_process_mask=True)

    ys, xs = np.nonzero(np.asarray(cut)[..., 3] > 6)
    pad = 6
    cut = cut.crop((max(0, xs.min() - pad), max(0, ys.min() - pad),
                    min(cut.width, xs.max() + pad + 1),
                    min(cut.height, ys.max() + pad + 1)))

    # the matte ends on a flat cut at the hem; feather it so he dissolves into
    # the void instead of stopping on a hard line
    w, h = cut.size
    arr = np.asarray(cut).astype(np.float32).copy()
    start = int(h * FADE_FROM)
    ramp = np.ones(h, dtype=np.float32)
    ramp[start:] = np.linspace(1.0, 0.0, h - start)
    arr[..., 3] *= ramp[:, None]

    fig = Image.fromarray(arr.astype(np.uint8), "RGBA")
    fig = fig.resize((round(w * TARGET_H / h), TARGET_H), Image.LANCZOS)
    fig.save(OUT, quality=QUALITY, method=6)
    print("{}  {:,} bytes  {}".format(OUT, os.path.getsize(OUT), fig.size))


if __name__ == "__main__":
    main()
