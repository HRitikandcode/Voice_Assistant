# gui/face.py

import math
from gui.theme import *


class Face:

    def __init__(self, canvas):

        self.canvas = canvas

        self.cx = 350
        self.cy = 200

        self.outer_radius = 120
        self.inner_radius = 45

        self.rotation = 0
        self.pulse = 0

    # -------------------------------------------------

    def clear(self):
        self.canvas.delete("face")

    # -------------------------------------------------

    def satellite(self, angle, radius=145, size=10):

        rad = math.radians(angle)

        x = self.cx + radius * math.cos(rad)
        y = self.cy + radius * math.sin(rad)

        self.canvas.create_oval(
            x-size,
            y-size,
            x+size,
            y+size,
            fill=CORE,
            outline="",
            tags="face"
        )

    # -------------------------------------------------

    def draw_crosshair(self):

        self.canvas.create_line(
            self.cx-180,
            self.cy,
            self.cx+180,
            self.cy,
            fill=CORE_DIM,
            width=1,
            tags="face"
        )

        self.canvas.create_line(
            self.cx,
            self.cy-180,
            self.cx,
            self.cy+180,
            fill=CORE_DIM,
            width=1,
            tags="face"
        )

    # -------------------------------------------------

    def draw_core(self, r=None):

        if r is None:
            r = self.inner_radius

        self.canvas.create_oval(
            self.cx-r,
            self.cy-r,
            self.cx+r,
            self.cy+r,
            fill=CORE,
            outline=CORE,
            tags="face"
        )

    # -------------------------------------------------

    def draw_ring(self):

        r = self.outer_radius

        self.canvas.create_oval(
            self.cx-r,
            self.cy-r,
            self.cx+r,
            self.cy+r,
            outline=CORE,
            width=3,
            tags="face"
        )

    # -------------------------------------------------

    def draw_sleep(self):

        self.clear()

        self.draw_crosshair()

        self.canvas.create_oval(
            self.cx-18,
            self.cy-18,
            self.cx+18,
            self.cy+18,
            fill=CORE_DIM,
            outline="",
            tags="face"
        )

    # -------------------------------------------------

    def draw_listening(self):

        self.clear()

        self.draw_crosshair()

        self.draw_ring()

        self.draw_core(self.inner_radius + self.pulse)

    # -------------------------------------------------

    def draw_thinking(self):

        self.clear()

        self.draw_crosshair()

        self.canvas.create_arc(
            self.cx-125,
            self.cy-125,
            self.cx+125,
            self.cy+125,
            start=self.rotation,
            extent=300,
            style="arc",
            outline=CORE,
            width=4,
            tags="face"
        )

        self.draw_core()

        for i in range(4):

            self.satellite(
                self.rotation + i*90
            )

    # -------------------------------------------------

    def draw_talking(self):

        self.clear()

        self.draw_crosshair()

        self.draw_core()

        for i in range(3):

            r = self.inner_radius + 25*i + self.pulse

            self.canvas.create_oval(
                self.cx-r,
                self.cy-r,
                self.cx+r,
                self.cy+r,
                outline=CORE,
                width=2,
                tags="face"
            )

    # -------------------------------------------------

    def draw_happy(self):

        self.clear()

        self.draw_crosshair()

        self.draw_ring()

        self.draw_core()

        for angle in [45,135,225,315]:

            self.satellite(angle)