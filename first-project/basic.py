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
        
class BoxWithInfo(Scene):
    def construct(self):
        eq = MathTex("ln(2)")
        rect = always_redraw(lambda: SurroundingRectangle(eq, color=BLUE, fill_opacity=0.4,fill_color=RED, buff=2))
        name = always_redraw(lambda:Tex("Marzouk").next_to(rect, DOWN, buff=0.25))
        
        self.play(Create(VGroup(eq, rect, name)))
        self.play(eq.animate.shift(RIGHT * 2), run_time=2)
        self.wait()
        
class ValueTrackers(Scene):
    def construct(self):
        n = ValueTracker(3.5)
        num = always_redraw(lambda:DecimalNumber().set_value(n.get_value()))
        
        self.play(FadeIn(num))
        self.play(n.animate.set_value(0), run_time=3, rate_func=smooth)
        self.wait()
        
class Graphing(Scene):
    def construct(self):
        plane = (
            NumberPlane(x_range = [-10,10, 2], x_length=8, y_range=[0,16,2], y_length=5)
            .add_coordinates()
            .to_edge(DOWN)
        )
        
        labels = plane.get_axis_labels(x_label="X", y_label="f(x)")
        parab = plane.plot(lambda x : x**2, x_range=[-4, 4], color=GREEN)
        func_label = MathTex("f(x)={x}^{2}").scale(0.6).next_to(parab,UR, buff=0.5).set_color(GREEN)
        area = plane.get_riemann_rectangles(graph=parab, x_range=[-4,4], dx=0.2, stroke_width=0.1, stroke_color=WHITE)
        
        self.play(DrawBorderThenFill(plane), rate_func=linear)
        self.play(Create(VGroup(labels, parab, func_label)), run_time=3)
        self.play(Create(area), run_time=5)
        self.wait()