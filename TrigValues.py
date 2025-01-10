from manim import *

class TrigValues(Scene):
    def construct(self):
        title = Text("Trigonometric Values").scale(0.8)
        self.play(Write(title), run_time=2)
        self.play(title.animate.to_edge(UP), run_time=1.5)

        table = MathTable(
            [["\\theta", "0°", "30°", "45°", "60°", "90°"],
             ["\\text{rad}", "0", "\\frac{\\pi}{6}", "\\frac{\\pi}{4}", "\\frac{\\pi}{3}", "\\frac{\\pi}{2}"],
             ["\\cos \\theta", "1", "\\frac{\\sqrt{3}}{2}", "\\frac{\\sqrt{2}}{2}", "\\frac{1}{2}", "0"],
             ["\\sin \\theta", "0", "\\frac{1}{2}", "\\frac{\\sqrt{2}}{2}", "\\frac{\\sqrt{3}}{2}", "1"],
             ["\\tan \\theta", "0", "\\frac{1}{\\sqrt{3}}", "1", "\\sqrt{3}", "\\infty"]],
            include_outer_lines=True,
            element_to_mobject_config={"font_size": 24}
        ).scale(0.7)

        labels = VGroup(
            Text("Angle →", font_size=20),
            Text("↓ Values", font_size=20)
        )
        
        labels[0].next_to(table, UP, buff=0.2)
        labels[1].next_to(table, LEFT, buff=0.2)

        self.play(
            AnimationGroup(
                *[Write(mob) for mob in table.get_entries()],
                lag_ratio=0.1
            ),
            run_time=5
        )
        self.play(
            Create(table.get_horizontal_lines()),
            Create(table.get_vertical_lines()),
            run_time=2
        )
        self.play(Write(labels), run_time=2)
        self.wait(5)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )
        self.wait(1)