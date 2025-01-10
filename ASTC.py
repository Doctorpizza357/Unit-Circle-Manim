from manim import *

class ASTC(Scene):
    def construct(self):
        # Create title
        title = Text("ASTC Rule in Trigonometry", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # Create axes
        axes = Axes(
            x_range=[-2.5, 2.5], y_range=[-2.5, 2.5],
            axis_config={"color": GREY}
        )
        self.play(Create(axes))

        # Create the unit circle
        circle = Circle(radius=2, color=WHITE)
        self.play(Create(circle))

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

        # Define the quadrant labels
        quad_info = [
            (PI/4, "A", "All (+)", BLUE),
            (3*PI/4, "S", "Sine (+)", GREEN),
            (5*PI/4, "T", "Tangent (+)", RED),
            (7*PI/4, "C", "Cosine (+)", YELLOW)
        ]

        # Create and animate the labels
        letter_labels = VGroup()  # Create a group for letter labels
        word_labels = VGroup()    # Create a group for word labels
        
        for angle, letter, word, color in quad_info:
            letter_label = Text(letter, font_size=48, color=color)
            word_label = Text(word, font_size=24, color=color)
            
            letter_label.move_to(2.5 * np.array([np.cos(angle), np.sin(angle), 0]))
            word_label.next_to(letter_label, 
                             UP if angle > PI else DOWN,
                             buff=0.3)
            
            letter_labels.add(letter_label)
            word_labels.add(word_label)
            
            self.play(
                Write(letter_label),
                Write(word_label),
                run_time=1
            )

        # Create explanation text with colored letters
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

        # Fade out circle components and transform ASTC
        self.play(
            FadeOut(circle),
            FadeOut(axes),
            FadeOut(VGroup(*quadrants)),
            FadeOut(word_labels),
            FadeOut(title),
            FadeOut(angle_lines),
            run_time=1
        )

        # Transform letter labels to explanation text (update indices for the new VGroup structure)
        self.play(
            ReplacementTransform(letter_labels[0], explanation[1][1]),  # A
            ReplacementTransform(letter_labels[1], explanation[2][1]),  # S
            ReplacementTransform(letter_labels[2], explanation[3][1]),  # T
            ReplacementTransform(letter_labels[3], explanation[4][1]),  # C
            Write(explanation[0]),  # "ASTC Rule:"
            Write(explanation[1][0]),  # "• "
            Write(explanation[1][2]),  # rest of line
            Write(explanation[2][0]),
            Write(explanation[2][2]),
            Write(explanation[3][0]),
            Write(explanation[3][2]),
            Write(explanation[4][0]),
            Write(explanation[4][2]),
            run_time=2
        )

        # Create bigger axis lines
        h_line = Line(LEFT * 2, RIGHT * 2, color=GREY).shift(UP*1.5)
        v_line = Line(UP * 2, DOWN * 2, color=GREY).shift(UP*1.5)
        
        # Add quadrant numbers with matching colors
        quad_numbers = VGroup(
            Text("I", font_size=36, color=BLUE).move_to(RIGHT * 2 + UP * 1.5).shift(UP*1).shift(LEFT),
            Text("II", font_size=36, color=GREEN).move_to(LEFT * 2 + UP * 1.5).shift(UP*1).shift(RIGHT),
            Text("III", font_size=36, color=RED).move_to(LEFT * 2 + DOWN * 1.5).shift(UP*2).shift(RIGHT),
            Text("IV", font_size=36, color=YELLOW).move_to(RIGHT * 2 + DOWN * 1.5).shift(UP*2).shift(LEFT)
        )
        
        # Animate the new elements
        self.play(
            [ReplacementTransform(Line(ORIGIN - RIGHT, ORIGIN + RIGHT).rotate(angle), v_line if angle % PI == 0 else h_line) for angle in angles[:-1]],
            Write(quad_numbers),
            run_time=1
        )
        
        # Final pause
        self.wait(2)