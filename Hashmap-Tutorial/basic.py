from manim import *
class SequentialSearch(Scene):
    def construct(self):
        title=Tex("Linear Search").to_edge(UL,buff=0.5)
        self.play(Write(title))
        self.wait()