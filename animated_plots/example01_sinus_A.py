# Knihovny Numpy a matplotlib
#
# První demonstrační příklad:
# - vykreslení animovaného průběhu funkce sin

import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage


# parametry animace
DURATION = 10
FPS = 15

# hodnoty na x-ové ose
x = np.linspace(0, 2 * np.pi, 100)

# vytvoření objektu reprezentujícího průběh funkce
fig, axis = plt.subplots()


def make_frame(t):
    axis.clear()

    # offset v rozmezí 0 .. 2*Pi
    offset = 2 * np.pi * t / DURATION

    # hodnoty na y-ové ose
    y = np.sin(x + offset)

    # vykreslení průběhu funkce
    axis.plot(x, y)

    # konverze na objekt typu "frame"
    return mplfig_to_npimage(fig)


animation = VideoClip(make_frame, duration=DURATION)
animation.write_gif('sinus_A.gif', fps=FPS)
