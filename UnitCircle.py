from manim import *

class UnitCircle(Scene):
    def construct(self):
        circle = Circle(radius=2, color=BLUE)
        axes = Axes(
            x_range=[-2.5, 2.5],
            y_range=[-2.5, 2.5],
            x_length=5,
            y_length=5,
            axis_config={"include_tip": True}
        )

        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        circle_label = Text("Unit Circle").scale(0.8).to_edge(UP)

        angle = ValueTracker(0)
        line = always_redraw(
            lambda: Line(
                start=ORIGIN,
                end=[
                    2 * np.cos(angle.get_value()),
                    2 * np.sin(angle.get_value()),
                    0
                ],
                color=YELLOW
            )
        )

        dot = always_redraw(
            lambda: Dot(
            point=[
                2 * np.cos(angle.get_value()),
                2 * np.sin(angle.get_value()),
                0
            ],
            color=RED
            )
        )

        coord_text = always_redraw(
            lambda: MathTex(
                f"(\\cos \\theta, \\sin \\theta) = ({np.cos(angle.get_value()):.2f}, {np.sin(angle.get_value()):.2f})"
            ).scale(0.8).to_edge(DOWN)
        )

        self.play(Create(axes), Create(circle))
        self.play(Write(x_label), Write(y_label), Write(circle_label))
        self.play(Create(line))
        self.play(Write(coord_text))
        self.add(dot)  # Add dot last to ensure it's on top

        self.play(
            angle.animate.set_value(2 * PI),
            rate_func=linear,
            run_time=8
        )
        self.wait()

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )