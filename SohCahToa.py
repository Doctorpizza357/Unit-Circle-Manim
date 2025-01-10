from manim import *

class SohCahToa(Scene):
    def construct(self):
        # Title
        title = Text("SOH-CAH-TOA", color=BLUE).to_edge(UP)
        subtitle = Text("Understanding Trigonometric Ratios", 
                       color=BLUE_B, font_size=24).next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait()
        
        # Create a larger, better positioned right triangle
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
        
        # Labels with better positioning and colors
        opp_label = MathTex("\\text{Opposite}", color=RED).next_to(opposite, RIGHT, buff=0.3)
        adj_label = MathTex("\\text{Adjacent}", color=GREEN).next_to(adjacent, DOWN, buff=0.3)
        hyp_label = MathTex("\\text{Hypotenuse}", color=YELLOW)
        hyp_label.next_to(hypotenuse.get_center(), UL, buff=0.3)
        
        # Store copies of labels for later transformation
        opp_label_copy = opp_label.copy()
        adj_label_copy = adj_label.copy()
        hyp_label_copy = hyp_label.copy()

        # Remove the angle arc section and just keep the label
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
        
        # First move labels to the left side
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

        # Now fade out the triangle and original labels
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

        # Modified formulas section with proper LaTeX syntax
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

        # Color the terms using tex_to_color_map
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

        # Modified animation sequence - keep separate parts
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