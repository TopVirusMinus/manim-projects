from manim import *

class Test(Scene):
    def construct(self):
        title=Tex("Marzoukium").to_edge(UL,buff=0.5)
        sq = Square(side_length=0.5, stroke_color=GREEN, fill_color=BLUE, fill_opacity=0.4).shift(LEFT*3)
        circ = Circle(radius=2.4, color=RED)
        tri = Triangle().scale(0.6).to_edge(DR)
        
        self.play(Write(title))
        self.play(DrawBorderThenFill(sq),Create(circ),Create(tri), run_time=1.5)
        self.wait()
        self.play(title.animate.to_edge(UR),sq.animate.scale(2),sq.animate.rotate(90), tri.animate.to_edge(DL), run_time=1.5)
        self.wait()
        
class Arrows(Scene):
    def construct(self):
        rect = Rectangle(color=WHITE, height=3, width = 3).to_edge(UL).scale(0.5)
        circ = Circle(radius=2).scale(0.5).to_edge(DOWN)
        arrow = always_redraw(lambda: Line(start=rect.get_bottom(), end=circ.get_top(), buff=0.1).add_tip())
        
        self.play(Create(VGroup(rect, circ,arrow)))
        self.wait()
        self.play(rect.animate.to_edge(UR), run_time=1.5)