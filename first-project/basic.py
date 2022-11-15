from manim import *

class Test(Scene):
    def construct(self):
        title=Tex("Marzoukium").to_edge(UL,buff=0.5)
        sq = Square(side_length=0.5, stroke_color=GREEN, fill_color=BLUE, fill_opacity=0.4).shift(LEFT*3)
        circ = Circle(radius=2.4, color=RED)
        tri = Triangle().scale(0.6).to_edge(DR)
        
        self.play(Write(title))
        self.play(DrawBorderThenFill(sq), run_time=3)
        self.play(Create(circ), run_time=3)
        self.play(Create(tri), run_time=3)
        self.wait()
        
        self.play(name.animate.to_edge(UR))