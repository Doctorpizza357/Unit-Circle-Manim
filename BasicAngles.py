from manim import *

class BasicAngles(Scene):
    def construct(self):
        title = Text("Common Reference Angles").scale(0.8)
        self.play(Write(title), run_time=2)
        self.play(title.animate.to_edge(UP), run_time=1.5)

        angles = MathTable(
            [["Angle", "Reference Angle", "Radians"],
             ["0°", "0°", "0"],
             ["30°", "30°", "\\pi/6"],
             ["45°", "45°", "\\pi/4"],
             ["60°", "60°", "\\pi/3"],
             ["90°", "90°", "\\pi/2"],
             ["120°", "60°", "2\\pi/3"],
             ["135°", "45°", "3\\pi/4"],
             ["150°", "30°", "5\\pi/6"]],
            include_outer_lines=True
        ).scale(0.6).shift(DOWN * 0.5)

        self.play(
            AnimationGroup(
                *[Write(mob) for mob in angles.get_entries()],
                lag_ratio=0.1
            ),
            run_time=5
        )
        self.play(
            Create(angles.get_horizontal_lines()),
            Create(angles.get_vertical_lines()),
            run_time=2
        )
        self.wait(5)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )
        self.wait(1)