#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2018  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

# Knihovny Numpy a matplotlib
#
# - zobrazení kontur funkce typu z=f(x,y)

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

# parametry obrázků / rámců
WIDTH = 400
HEIGHT = 400
DPI = 100

# parametry animace
DURATION = 10
FPS = 15

# vytvoření objektu reprezentujícího průběh funkce
# + nastavení rozlišení obrázku (resp. jednotlivých rámců)
fig, axis = plt.subplots(figsize=(1.0 * WIDTH / DPI, 1.0 * HEIGHT / DPI), dpi=DPI)


def make_frame(t):
    """Deklarace callback funkce zavolane pri renderingu kazdeho snimku videa."""
    axis.clear()

    # offset v rozmezí 0 .. 2*Pi
    offset1 = 3 * 2 * np.pi * t / DURATION
    offset2 = 2 * 2 * np.pi * t / DURATION

    delta = 0.1

    # průběh nezávislé proměnné x
    x = np.arange(-10.0, 10.0, delta)

    # průběh nezávislé proměnné y
    y = np.arange(-10.0, 10.0, delta)

    # vytvoření dvou polí se souřadnicemi [x,y]
    X, Y = np.meshgrid(x, y)

    # vzdálenost od bodu [0,0]
    R1 = np.sqrt(X*X+Y*Y)

    # vzdálenost od bodu [3,3]
    R2 = np.sqrt((X-3)*(X-3)+(Y-3)*(Y-3))

    # výpočet funkce, kterou použijeme při vykreslování grafu
    Z = np.sin(R1 + offset1) - np.cos(R2 + offset2)

    # povolení zobrazení mřížky
    axis.grid(True)

    # vytvoření grafu s konturami funkce z=f(x,y)
    axis.contour(X, Y, Z)


    # konverze na objekt typu "frame"
    return mplfig_to_npimage(fig)


# vytvoreni video klipu
animation = VideoClip(make_frame, duration=DURATION)

# export videa do formatu GIF
animation.write_gif('contour.gif', fps=FPS)
