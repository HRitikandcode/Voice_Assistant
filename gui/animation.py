import math


class Animator:

    def __init__(self, root, face):

        self.root = root
        self.face = face

        self.mode = "sleep"

        self.direction = 1

    def set_mode(self, mode):

        self.mode = mode

    def start(self):

        self.animate()

    def animate(self):

        if self.mode == "sleep":

            self.face.draw_sleep()

        elif self.mode == "listen":

            self.face.pulse += self.direction

            if self.face.pulse > 8:
                self.direction = -1

            if self.face.pulse < 0:
                self.direction = 1

            self.face.draw_listening()

        elif self.mode == "think":

            self.face.rotation += 4

            self.face.draw_thinking()

        elif self.mode == "talk":

            self.face.pulse += self.direction

            if self.face.pulse > 12:
                self.direction = -1

            if self.face.pulse < 0:
                self.direction = 1

            self.face.draw_talking()

        elif self.mode == "happy":

            self.face.rotation += 2

            self.face.draw_happy()

        self.root.after(30, self.animate)