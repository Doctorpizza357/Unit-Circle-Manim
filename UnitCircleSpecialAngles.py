from manim import *

class UnitCircleSpecialAngles(Scene):
    def construct(self):
        # Setup circle and axes
        circle = Circle(radius=2, color=BLUE)
        axes = Axes(
            x_range=[-2.5, 2.5],
            y_range=[-2.5, 2.5],
            x_length=5,
            y_length=5,
            axis_config={"include_tip": True}
        )

        # Labels
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        circle_label = Text("Special Angles").scale(0.8).to_edge(UP)

        # Extended special angles in radians
        special_angles = [0, PI/6, PI/4, PI/3, PI/2, 2*PI/3, 3*PI/4, 5*PI/6, PI, 
                         7*PI/6, 5*PI/4, 4*PI/3, 3*PI/2, 5*PI/3, 7*PI/4, 11*PI/6, 2*PI]
        angle_names = ["0°", "30°", "45°", "60°", "90°", "120°", "135°", "150°", "180°",
                      "210°", "225°", "240°", "270°", "300°", "315°", "330°", "360°"]
        angle_rads = ["0", "\\pi/6", "\\pi/4", "\\pi/3", "\\pi/2", "2\\pi/3", "3\\pi/4", "5\\pi/6", "\\pi",
                     "7\\pi/6", "5\\pi/4", "4*PI/3", "3\\pi/2", "5\\pi/3", "7\\pi/4", "11\\pi/6", "2\\pi"]

        # Extended exact values dictionary
        exact_values = {
            0: {"cos": "1", "sin": "0"},
            PI/6: {"cos": "\\frac{\\sqrt{3}}{2}", "sin": "\\frac{1}{2}"},
            PI/4: {"cos": "\\frac{\\sqrt{2}}{2}", "sin": "\\frac{\\sqrt{2}}{2}"},
            PI/3: {"cos": "\\frac{1}{2}", "sin": "\\frac{\\sqrt{3}}{2}"},
            PI/2: {"cos": "0", "sin": "1"},
            2*PI/3: {"cos": "-\\frac{1}{2}", "sin": "\\frac{\\sqrt{3}}{2}"},
            3*PI/4: {"cos": "-\\frac{\\sqrt{2}}{2}", "sin": "\\frac{\\sqrt{2}}{2}"},
            5*PI/6: {"cos": "-\\frac{\\sqrt{3}}{2}", "sin": "\\frac{1}{2}"},
            PI: {"cos": "-1", "sin": "0"},
            7*PI/6: {"cos": "-\\frac{\\sqrt{3}}{2}", "sin": "-\\frac{1}{2}"},
            5*PI/4: {"cos": "-\\frac{\\sqrt{2}}{2}", "sin": "-\\frac{\\sqrt{2}}{2}"},
            4*PI/3: {"cos": "-\\frac{1}{2}", "sin": "-\\frac{\\sqrt{3}}{2}"},
            3*PI/2: {"cos": "0", "sin": "-1"},
            5*PI/3: {"cos": "\\frac{1}{2}", "sin": "-\\frac{\\sqrt{3}}{2}"},
            7*PI/4: {"cos": "\\frac{\\sqrt{2}}{2}", "sin": "-\\frac{\\sqrt{2}}{2}"},
            11*PI/6: {"cos": "\\frac{\\sqrt{3}}{2}", "sin": "-\\frac{1}{2}"},  # Fixed typo: \1 -> 1
            2*PI: {"cos": "1", "sin": "0"}
        }

        # Setup angle tracker and moving parts
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

        # Add special angle dots
        special_dots = VGroup(*[
            Dot(
                point=[
                    2 * np.cos(angle),
                    2 * np.sin(angle),
                    0
                ],
                color=YELLOW,
                radius=0.05
            )
            for angle in special_angles
        ])
        
        # Display info box template first
        info_box = VGroup(
            MathTex("\\text{Angle: }"), 
            MathTex("\\text{Radians: }"),
            MathTex("\\cos \\theta = "),
            MathTex("\\sin \\theta = ")
        ).arrange(DOWN, aligned_edge=LEFT, buff = 1).to_edge(RIGHT, buff = 1.5)
        
        # Initial setup with dots (modified order)
        self.play(Create(axes), Create(circle))
        self.play(Write(x_label), Write(y_label), Write(circle_label))
        self.play(Create(line))
        self.play(Create(special_dots))  # Add the special angle dots
        self.play(Write(info_box))

        # Add function to create triangle
        def create_triangle(angle_value):
            x = 2 * np.cos(angle_value)
            y = 2 * np.sin(angle_value)
            
            vertical = DashedLine(
                start=[x, 0, 0],
                end=[x, y, 0],
                color=WHITE,
                dash_length=0.1
            )
            
            horizontal = DashedLine(
                start=[0, 0, 0],
                end=[x, 0, 0],
                color=WHITE,
                dash_length=0.1
            )
            
            return VGroup(vertical, horizontal)

        # Animate through special angles
        for i, special_angle in enumerate(special_angles):
            # Update angle
            self.play(
                angle.animate.set_value(special_angle),
                run_time=1
            )
            
            # Add triangle
            if special_angle != 0 and special_angle != PI/2 and special_angle != PI and special_angle != 3*PI/2 and special_angle != 2*PI:
                triangle = create_triangle(special_angle)
                self.play(Create(triangle), run_time=0.5)
            
            # Always ensure dot is on top
            self.remove(dot)  # Remove existing dot if any
            self.add(dot)     # Add dot on top
            
            # Create info text for current angle
            angle_info = VGroup(
                MathTex(f"\\text{{{angle_names[i]}}}"),
                MathTex(f"{angle_rads[i]}"),
                MathTex(f"{exact_values[special_angle]['cos']}"),
                MathTex(f"{exact_values[special_angle]['sin']}")
            ).arrange(DOWN, aligned_edge=LEFT)
            
            # Position info next to template
            for j in range(4):
                angle_info[j].next_to(info_box[j], RIGHT)

            # Show info
            self.play(Write(angle_info))
            self.wait(2)
            
            # Remove triangle and info (except for last angle)
            if i < len(special_angles) - 1:
                if special_angle != 0 and special_angle != PI/2 and special_angle != PI and special_angle != 3*PI/2 and special_angle != 2*PI:
                    self.play(FadeOut(angle_info), FadeOut(triangle))
                else:
                    self.play(FadeOut(angle_info))

        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
