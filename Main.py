from manim import *

class UnitCirclePresentation(Scene):
    def construct(self):
        # SOH-CAH-TOA Section
        # Title
        title = Text("SOH-CAH-TOA", color=BLUE).to_edge(UP)
        subtitle = Text("Understanding Trigonometric Ratios", 
                       color=BLUE_B, font_size=24).next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait()
        
        triangle = Polygon(
            ORIGIN, 4*RIGHT, 4*RIGHT + 3*UP,
            color=WHITE
        ).shift(DOWN + LEFT*2)
        
        # Right angle square
        square = Square(side_length=0.4, color=WHITE)
        square.next_to(triangle.get_vertices()[1], UP, buff=0).shift(LEFT*0.2)
        
        # Color-coded sides
        opposite = Line(triangle.get_vertices()[1], triangle.get_vertices()[2], color=RED)
        adjacent = Line(triangle.get_vertices()[0], triangle.get_vertices()[1], color=GREEN)
        hypotenuse = Line(triangle.get_vertices()[0], triangle.get_vertices()[2], color=YELLOW)
        
        # Labels
        opp_label = MathTex("\\text{Opposite}", color=RED).next_to(opposite, RIGHT, buff=0.3)
        adj_label = MathTex("\\text{Adjacent}", color=GREEN).next_to(adjacent, DOWN, buff=0.3)
        hyp_label = MathTex("\\text{Hypotenuse}", color=YELLOW)
        hyp_label.next_to(hypotenuse.get_center(), UL, buff=0.3)
        
        # Store copies of labels for later transformation
        opp_label_copy = opp_label.copy()
        adj_label_copy = adj_label.copy()
        hyp_label_copy = hyp_label.copy()

        # Angle label
        angle_label = MathTex("\\theta", color=BLUE).move_to(
            triangle.get_vertices()[0] + 0.5 * (RIGHT + 0.3*UP)
        )
        
        # Animate the construction
        self.play(Create(triangle))
        self.play(Create(square))
        self.wait()
        
        # Show each side with its label
        for side, label in [(opposite, opp_label), 
                          (adjacent, adj_label), 
                          (hypotenuse, hyp_label)]:
            self.play(
                Create(side),
                Write(label)
            )
        
        self.play(Write(angle_label))
        self.wait()
        
        # Move labels to the left side of the screen
        labels_group = VGroup(opp_label, adj_label, hyp_label).copy()
        target_positions = VGroup(
            MathTex("\\text{Opposite}", color=RED),
            MathTex("\\text{Adjacent}", color=GREEN),
            MathTex("\\text{Hypotenuse}", color=YELLOW)
        ).arrange(DOWN, buff=0.5).to_edge(LEFT, buff=1)

        self.play(
            *[
                label.animate.move_to(target)
                for label, target in zip(labels_group, target_positions)
            ],
            run_time=1.5
        )
        self.wait()

        # Store the positioned labels for transformation
        opp_label_copy = labels_group[0].copy()
        adj_label_copy = labels_group[1].copy()
        hyp_label_copy = labels_group[2].copy()

        # Fade out the triangle and labels
        self.play(
            FadeOut(triangle),
            FadeOut(square),
            FadeOut(angle_label),
            FadeOut(opposite),
            FadeOut(adjacent),
            FadeOut(hypotenuse),
            FadeOut(opp_label),
            FadeOut(adj_label),
            FadeOut(hyp_label),
            run_time=1
        )

        # Part 2: Trig Ratios Section
        formula_parts = VGroup(
            VGroup(
                MathTex("\\sin(\\theta)", "=", color=WHITE),
                # Each fraction as a single MathTex object
                MathTex("\\frac{\\text{Opposite}}{\\text{Hypotenuse}}")
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex("\\cos(\\theta)", "=", color=WHITE),
                MathTex("\\frac{\\text{Adjacent}}{\\text{Hypotenuse}}")
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex("\\tan(\\theta)", "=", color=WHITE),
                MathTex("\\frac{\\text{Opposite}}{\\text{Adjacent}}")
            ).arrange(RIGHT, buff=0.2)
        ).arrange(DOWN, buff=0.5).to_edge(RIGHT, buff=1)

        # Apply colors to each fraction
        colors = {
            "\\text{Opposite}": RED,
            "\\text{Adjacent}": GREEN,
            "\\text{Hypotenuse}": YELLOW
        }
        
        # Apply colors to each fraction
        for i in range(3):
            formula_parts[i][1].set_color_by_tex_to_color_map(colors)

        # Add mnemonic labels
        mnemonics = VGroup(
            Text("SOH", color=BLUE_A, font_size=24),
            Text("CAH", color=BLUE_B, font_size=24),
            Text("TOA", color=BLUE_C, font_size=24)
        )

        for i, (mnemonic, formula) in enumerate(zip(mnemonics, formula_parts)):
            mnemonic.next_to(formula, LEFT, buff=0.5)

        # SOH animation
        self.play(Write(mnemonics[0]), Write(formula_parts[0][0]), run_time=1)
        
        fraction_line = Line(LEFT, RIGHT, color=WHITE).scale(0.5).next_to(formula_parts[0][0]).shift(RIGHT)
        soh_num = MathTex("\\text{Opposite}", color=RED).next_to(fraction_line, UP, buff=0.2)
        soh_den = MathTex("\\text{Hypotenuse}", color=YELLOW).next_to(fraction_line, DOWN, buff=0.2)
        
        self.play(
            Create(fraction_line),
            ReplacementTransform(opp_label_copy, soh_num),
            ReplacementTransform(hyp_label_copy, soh_den),
            run_time=1
        )
        self.wait(0.5)

        # CAH animation
        self.play(Write(mnemonics[1]), Write(formula_parts[1][0]), run_time=1)
        
        fraction_line2 = Line(LEFT, RIGHT, color=WHITE).scale(0.5).next_to(formula_parts[1][0]).shift(RIGHT)
        cah_num = MathTex("\\text{Adjacent}", color=GREEN).next_to(fraction_line2, UP, buff=0.2)
        cah_den = MathTex("\\text{Hypotenuse}", color=YELLOW).next_to(fraction_line2, DOWN, buff=0.2)
        
        self.play(
            Create(fraction_line2),
            ReplacementTransform(adj_label_copy, cah_num),
            ReplacementTransform(hyp_label.copy(), cah_den),
            run_time=1
        )
        self.wait(0.5)

        # TOA animation
        self.play(Write(mnemonics[2]), Write(formula_parts[2][0]), run_time=1)
        
        fraction_line3 = Line(LEFT, RIGHT, color=WHITE).scale(0.5).next_to(formula_parts[2][0]).shift(RIGHT)
        toa_num = MathTex("\\text{Opposite}", color=RED).next_to(fraction_line3, UP, buff=0.2)
        toa_den = MathTex("\\text{Adjacent}", color=GREEN).next_to(fraction_line3, DOWN, buff=0.2)
        
        self.play(
            Create(fraction_line3),
            ReplacementTransform(opp_label.copy(), toa_num),
            ReplacementTransform(adj_label.copy(), toa_den),
            run_time=1
        )
        self.wait(0.5)

        # Final pause
        self.wait(2)
        
        # Clean fadeout
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )
        self.wait(1)

        # Part 1: Reference Angles Section
        title1 = Text("Common Reference Angles").scale(0.8)
        self.play(Write(title1), run_time=2)
        self.play(title1.animate.to_edge(UP), run_time=1.5)

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
        self.wait(3)

        # Transition to Trig Values
        self.play(
            FadeOut(angles),
            ReplacementTransform(title1, Text("Trigonometric Values").scale(0.8).to_edge(UP)),
            run_time=2
        )

        # Part 2: Trig Values Section
        trig_table = MathTable(
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
        labels[0].next_to(trig_table, UP, buff=0.2)
        labels[1].next_to(trig_table, LEFT, buff=0.2)

        self.play(
            AnimationGroup(
                *[Write(mob) for mob in trig_table.get_entries()],
                lag_ratio=0.1
            ),
            run_time=5
        )
        self.play(
            Create(trig_table.get_horizontal_lines()),
            Create(trig_table.get_vertical_lines()),
            run_time=2
        )
        self.play(Write(labels), run_time=2)
        self.wait(3)

        # Transition to Unit Circle
        self.play(
            *[FadeOut(mob) for mob in [trig_table, labels[0], labels[1]]],
            run_time=2
        )

        # Part 3: Unit Circle Section
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
        self.play(Write(x_label), Write(y_label))
        self.play(Create(line))
        self.play(Write(coord_text))
        self.add(dot)

        self.play(
            angle.animate.set_value(2 * PI),
            rate_func=linear,
            run_time=8
        )
        self.wait(2)

        # Transition to Special Angles
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )

        # Part 4: Special Angles demonstration
        title4 = Text("Special Angles").scale(0.8).to_edge(UP)
        self.play(Write(title4), run_time=1.5)

        # Copy the special angles demonstration code
        circle = Circle(radius=2, color=BLUE)
        axes = Axes(
            x_range=[-2.5, 2.5],
            y_range=[-2.5, 2.5],
            x_length=5,
            y_length=5,
            axis_config={"include_tip": True}
        )

        special_angles = [0, PI/6, PI/4, PI/3, PI/2, 2*PI/3, 3*PI/4, 5*PI/6, PI, 
                         7*PI/6, 5*PI/4, 4*PI/3, 3*PI/2, 5*PI/3, 7*PI/4, 11*PI/6, 2*PI]
        angle_names = ["0°", "30°", "45°", "60°", "90°", "120°", "135°", "150°", "180°",
                      "210°", "225°", "240°", "270°", "300°", "315°", "330°", "360°"]
        angle_rads = ["0", "\\pi/6", "\\pi/4", "\\pi/3", "\\pi/2", "2\\pi/3", "3\\pi/4", "5\\pi/6", "\\pi",
                     "7\\pi/6", "5\\pi/4", "4*PI/3", "3\\pi/2", "5\\pi/3", "7\\pi/4", "11\\pi/6", "2\\pi"]

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

        # Add special angle dots in the presentation
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

        # Create the axes and circle for the special angles demonstration
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

        # Define info_box before using it
        info_box = VGroup(
            MathTex("\\text{Angle: }"), 
            MathTex("\\text{Radians: }"),
            MathTex("\\cos \\theta = "),
            MathTex("\\sin \\theta = ")
        ).arrange(DOWN, aligned_edge=LEFT, buff = 1).to_edge(RIGHT, buff = 1.5)

        self.play(Create(axes), Create(circle))
        self.play(Write(axes.get_x_axis_label("x")), Write(axes.get_y_axis_label("y")), Write(Text("Special Angles").scale(0.8).to_edge(UP)))
        self.play(Create(line))
        self.play(Create(special_dots))  # Add the special angle dots
        self.add(dot)
        self.play(Write(info_box))

        # Add the same triangle creation function
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

        # Use the same modified loop in the special angles section
        for i, special_angle in enumerate(special_angles):
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
            
            # Create and show angle info
            angle_info = VGroup(
                MathTex(f"\\text{{{angle_names[i]}}}"),
                MathTex(f"{angle_rads[i]}"),
                MathTex(f"{exact_values[special_angle]['cos']}"),
                MathTex(f"{exact_values[special_angle]['sin']}")
            ).arrange(DOWN, aligned_edge=LEFT)
            
            for j in range(4):
                angle_info[j].next_to(info_box[j], RIGHT)

            self.play(Write(angle_info))
            self.wait(2)
            
            # Remove triangle and info (except for last angle)
            if i < len(special_angles) - 1:
                if special_angle != 0 and special_angle != PI/2 and special_angle != PI and special_angle != 3*PI/2 and special_angle != 2*PI:
                    self.play(FadeOut(angle_info), FadeOut(triangle))
                else:
                    self.play(FadeOut(angle_info))

        self.wait()
        
        # Final fadeout
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )

        
        self.wait(1)  # Add final pause

        # Part 5: ASTC Rule Section
        title5 = Text("ASTC Rule in Trigonometry", font_size=36)
        title5.to_edge(UP)
        self.play(Write(title5))

        # Create axes and circle for ASTC demonstration
        axes = Axes(
            x_range=[-2.5, 2.5], y_range=[-2.5, 2.5],
            axis_config={"color": GREY}
        )
        circle = Circle(radius=2, color=WHITE)
        
        self.play(Create(axes), Create(circle))

        # Create quadrant regions
        quadrants = []
        angles = [0, PI/2, PI, 3*PI/2, 2*PI]
        colors = [BLUE_E, GREEN_E, RED_E, YELLOW_E]
        
        for i in range(4):
            sector = Sector(
                radius=2,
                angle=PI/2,
                start_angle=angles[i],
                color=colors[i],
                fill_opacity=0.2
            )
            quadrants.append(sector)
        
        self.play(*[FadeIn(quad) for quad in quadrants])

        # Create angle markers
        angle_lines = VGroup()
        for angle in angles[:-1]:
            line = Line(ORIGIN - RIGHT, ORIGIN + RIGHT).rotate(angle)
            angle_lines.add(line)
            self.play(Create(line), run_time=0.5)

        # Define and create ASTC labels
        quad_info = [
            (PI/4, "A", "All (+)", BLUE),
            (3*PI/4, "S", "Sine (+)", GREEN),
            (5*PI/4, "T", "Tangent (+)", RED),
            (7*PI/4, "C", "Cosine (+)", YELLOW)
        ]

        letter_labels = VGroup()
        word_labels = VGroup()
        
        for angle, letter, word, color in quad_info:
            letter_label = Text(letter, font_size=48, color=color)
            word_label = Text(word, font_size=24, color=color)
            
            letter_label.move_to(2.5 * np.array([np.cos(angle), np.sin(angle), 0]))
            word_label.next_to(letter_label, 
                             UP if angle > PI else DOWN,
                             buff=0.3)
            
            letter_labels.add(letter_label)
            word_labels.add(word_label)
            
            self.play(Write(letter_label), Write(word_label), run_time=1)

        # Create final explanation
        explanation = VGroup(
            Text("ASTC Rule:", font_size=16, weight=BOLD),
            VGroup(
                Text("• ", font_size=24),
                Text("A", font_size=24, color=BLUE),
                Text(" - All trig functions are positive in Quadrant ", font_size=24),
                Text("I", font_size=24, color=BLUE)
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("• ", font_size=24),
                Text("S", font_size=24, color=GREEN),
                Text(" - Only Sine is positive in Quadrant ", font_size=24),
                Text("II", font_size=24, color=GREEN)
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("• ", font_size=24),
                Text("T", font_size=24, color=RED),
                Text(" - Only Tangent is positive in Quadrant ", font_size=24),
                Text("III", font_size=24, color=RED)
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("• ", font_size=24),
                Text("C", font_size=24, color=YELLOW),
                Text(" - Only Cosine is positive in Quadrant ", font_size=24),
                Text("IV", font_size=24, color=YELLOW)
            ).arrange(RIGHT, buff=0.1)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        explanation.to_corner(DL, buff=0.5)

        # Transform to final explanation
        self.play(
            FadeOut(circle),
            FadeOut(axes),
            FadeOut(VGroup(*quadrants)),
            FadeOut(word_labels),
            FadeOut(title5),
            FadeOut(angle_lines),
            run_time=1
        )

        # Show final explanation with transformed letters
        self.play(
            ReplacementTransform(letter_labels[0], explanation[1][1]),
            ReplacementTransform(letter_labels[1], explanation[2][1]),
            ReplacementTransform(letter_labels[2], explanation[3][1]),
            ReplacementTransform(letter_labels[3], explanation[4][1]),
            Write(explanation[0]),
            *[Write(explanation[i][j]) for i in range(1, 5) for j in [0, 2, 3]],
            run_time=2
        )

        # Add final diagram
        h_line = Line(LEFT * 2, RIGHT * 2, color=GREY).shift(UP*1.5)
        v_line = Line(UP * 2, DOWN * 2, color=GREY).shift(UP*1.5)
        
        quad_numbers = VGroup(
            Text("I", font_size=36, color=BLUE).move_to(RIGHT * 2 + UP * 1.5).shift(UP*1).shift(LEFT),
            Text("II", font_size=36, color=GREEN).move_to(LEFT * 2 + UP * 1.5).shift(UP*1).shift(RIGHT),
            Text("III", font_size=36, color=RED).move_to(LEFT * 2 + DOWN * 1.5).shift(UP*2).shift(RIGHT),
            Text("IV", font_size=36, color=YELLOW).move_to(RIGHT * 2 + DOWN * 1.5).shift(UP*2).shift(LEFT)
        )
        
        self.play(
            Create(h_line),
            Create(v_line),
            Write(quad_numbers),
            run_time=1
        )

        # Final pause and fadeout
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2)
        self.wait(1)
