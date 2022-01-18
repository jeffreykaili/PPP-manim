from manim import *
import time 
from math import pi as PI 
class Momentum(Scene):
    def construct(self):
        momentum = Tex("Momentum: ", 'The quantity of motion that an object has.', font_size = 38)
        momentum.set_color_by_tex("The quantity of motion that an object has.", RED)
        self.wait(2.8)
        self.play(Write(momentum[0]))
        self.wait(0.5)
        self.play(Write(momentum[1]))
        self.play(FadeOut(momentum), run_time = 1)
        momentum_definition = MathTex(r"\vec{p} = m\vec{v}", font_size=86)
        p_definition = MathTex(r"\vec{p} = momentum", font_size=26)
        m_definition = MathTex(r"m = mass", font_size=26)
        v_definition = MathTex(r"\vec{v} = velocity", font_size=26)
        group = VGroup(momentum_definition, p_definition, m_definition, v_definition)
        group.arrange(DOWN, center=True)
        self.play(Write(group[0]))
        self.play(FadeIn(group[1:]), run_time=0.5)
        self.wait(1)
        self.play(group.animate.shift(2.25*UP))
        square = Square(fill_opacity=1.0).set_fill(TEAL).shift(0.5*DOWN)
        arrow = Arrow(start=ORIGIN, end=3.5*RIGHT, color=RED).shift(0.5*DOWN).shift(LEFT/4)
        anno = Text("20 kg", font_size = 26, color = BLUE).shift(UP * 0.75)
        velocity_anno = Text("5 m/s", font_size = 18, color = RED).shift(DOWN * 0.25).shift(1.75*RIGHT)
        box_group = VGroup(square, arrow, anno, velocity_anno).shift(5*LEFT).shift(0.2*DOWN)
        momentum_calculation = MathTex(r"\vec{p} = ","20 kg"," \cdot ", "5 m/s", font_size = 35)
        momentum_calculation.set_color_by_tex('20 kg', BLUE)
        momentum_calculation.set_color_by_tex('5 m/s', RED)
        momentum_calculation_2 = MathTex(r"\vec{p} = ", "100 kg \cdot m/s", font_size = 35)
        lines = VGroup(momentum_calculation, momentum_calculation_2).arrange(DOWN).shift(2.4*DOWN)
        box_group.generate_target()
        box_group.target.shift(8.5*RIGHT)

        self.add(square)
        self.play(DrawBorderThenFill(square), run_time=0.8)
        self.play(FadeIn(arrow), FadeIn(anno), FadeIn(velocity_anno))

        self.play(
            LaggedStart(
                *[
                    MoveToTarget(box_group, run_time = 5, rate_func = linear),
                    LaggedStart(
                        *[
                            Write(lines[0], run_time = 1.25),
                            LaggedStart(
                                *[
                                    TransformFromCopy(lines[0][0], lines[1][0], run_time = 1.25), 
                                    TransformFromCopy(lines[0][1:], lines[1][1], run_time = 1.25), 
                                ], lag_ratio = 0
                            ),           
                        ], lag_ratio = 1.1
                    ), 
          
                ],
                lag_ratio = 0.2, 
            )
        )
        self.wait(2) 

class TwoClasses(Scene):
    def construct(self):
        shape_anno = Text("Shapes", font_size = 48)
        poly = Polygon(
            [-0.35, 0.5, 0], 
            [0.5, 0.75, 0],
            [1.4, 0.3, 0], 
            [2.4, -0.8, 0],
            [1.2, -1.9, 0],
            [-0.1, -1.5, 0], 
            [-0.6, -0.4, 0], color = BLUE_D, fill_opacity = 1.0
        ).set_fill(BLUE_D).shift(3.1*LEFT).shift(UP * 0.55)
        ellipse = Ellipse(width = 3.5, height = 2.5, color = BLUE_D, fill_opacity=1).set_fill(BLUE_D).shift(2.4*RIGHT).shift(0.25 * DOWN)
        self.play(FadeIn(shape_anno))
        shape_anno.generate_target() 
        shape_anno.target.shift(2.2 * UP)
        self.add(poly)
        self.add(ellipse)
        self.play(
            LaggedStart(
                *[
                    MoveToTarget(shape_anno), 
                    LaggedStart(
                        *[
                            DrawBorderThenFill(ellipse), 
                            DrawBorderThenFill(poly)
                        ], lag_ratio = 0
                    )
                ], lag_ratio = 0.8
            )
        )

        self.wait(0.5)

        shape_group = VGroup(ellipse, poly)
        shape_group.generate_target() 
        shape_group.target.shift(0.25 * UP)
        ellipse_anno = Tex("Ellipses", font_size = 32).shift(2.45 * RIGHT).shift(1.6*DOWN)
        polygon_anno = VGroup(Tex("Convex Polygons", font_size = 32)).arrange(DOWN).shift(2.2*LEFT).shift(1.6*DOWN)
        self.play(
            LaggedStart(
                *[
                    MoveToTarget(shape_group), 
                    LaggedStart(
                        *[
                            FadeIn(ellipse_anno), 
                            FadeIn(polygon_anno),
                        ], lag_ratio = 0
                    ), 
                ], lag_ratio = 0.4
            )
        )

        self.wait(1)

        square = Rectangle(width = 3.5, height = 2.5, color = BLUE_D, fill_opacity = 1.0).shift(2.2 * LEFT)
        circle = Circle(radius = 1.25, color = BLUE_D, fill_opacity = 1.0).shift(2.45 * RIGHT)
        self.play(Transform(poly, square), Transform(ellipse, circle)) 

        self.wait(2)

class ConservationOfMomentum(Scene):
    def construct(self):
        title = Tex("Conservation of Momentum", font_size = 48).shift(UP)
        ul = Underline(title, stroke_width=1)
        definition = Tex("In an isolated system, ", "the total momentum remains constant", ".", font_size = 34)
        definition.set_color_by_tex("total momentum remains constant", RED).shift(0.44 * UP)
        definition_collision = Tex("Thus, in a collision between two objects, momentum is always conserved.", font_size = 34)
        definition_group = VGroup(title, ul, definition)
        self.play(Write(definition_group[0]), run_time = 1.2)
        self.play(FadeIn(definition_group[1]), FadeIn(definition_group[2]))

        self.wait(0.2)

        definition_group.generate_target() 
        definition_group.target.shift(1.75*UP)
        self.play(MoveToTarget(definition_group))


        # Circle 1 

        circle_1 = Circle(radius = 1.0).set_fill(BLUE, opacity=0.8).set_stroke(BLUE_E, width = 3)
        circle_1_anno = Tex("15 kg", font_size = 34, color = BLUE_E).shift(UP * 1.2)
        circle_1_arrow = Arrow(start=ORIGIN, end=3*RIGHT, color=RED).shift(LEFT/4)
        circle_1_velocity = Tex("6 m/s", font_size = 24, color = RED).shift(UP * 0.185).shift(1.53 * RIGHT)
        circle_1_group = VGroup(circle_1, circle_1_anno, circle_1_arrow, circle_1_velocity)
        circle_1_brace = Brace(circle_1_group)
        circle_1_group.add(circle_1_brace)
        circle_1_brace_text = MathTex(r"\vec{p} = ", "15 kg"," \cdot ", "6 m/s", font_size = 28).shift(RIGHT * 0.78).shift(1.75 * DOWN)
        # print(circle_1_brace_text[1])
        circle_1_brace_text.set_color_by_tex_to_color_map({
            "15 kg" : BLUE_E, 
            "6 m/s" : RED, 
        })
        circle_1_group.add(circle_1_brace_text)
        circle_1_group.shift(LEFT * 4)

        # Circle 2 
        circle_2 = Circle(radius = 1.0).set_fill(PURPLE, opacity=0.8).set_stroke(PURPLE_E, width = 3)
        circle_2_anno = Tex("8 kg", font_size = 34, color = PURPLE_E).shift(UP * 1.2)
        circle_2_arrow = Arrow(start=ORIGIN, end=3*LEFT, color=RED).shift(RIGHT/4)
        circle_2_velocity = Tex("-10 m/s", font_size = 24, color = RED).shift(UP * 0.185).shift(1.53 * LEFT)
        circle_2_group = VGroup(circle_2, circle_2_anno, circle_2_arrow, circle_2_velocity)
        circle_2_brace = Brace(circle_2_group)
        circle_2_group.add(circle_2_brace)
        circle_2_brace_text = MathTex(r"\vec{p} = ", "8 kg"," \cdot ", "-10 m/s", font_size = 28).shift(LEFT * 0.78).shift(1.75 * DOWN)
        # print(circle_1_brace_text[1])
        circle_2_brace_text.set_color_by_tex_to_color_map({
            "8 kg" : PURPLE_E, 
            "-10 m/s" : RED, 
        })
        circle_2_group.add(circle_2_brace_text)
        circle_2_group.shift(RIGHT * 4)

        self.play(DrawBorderThenFill(circle_1_group[0]), DrawBorderThenFill(circle_2_group[0]), run_time = 1)
        self.play(FadeIn(circle_1_group[1]), FadeIn(circle_1_group[2]), FadeIn(circle_1_group[3]), FadeIn(circle_2_group[1]), FadeIn(circle_2_group[2]), FadeIn(circle_2_group[3])) 
        self.wait(0.25)
        self.play(FadeIn(circle_1_group[4]), FadeIn(circle_2_group[4]), run_time = 0.5)
        self.play(FadeIn(circle_1_group[5][0]), FadeIn(circle_1_group[5][2]), TransformMatchingShapes(circle_1_anno.copy(), circle_1_group[5][1]), TransformMatchingShapes(circle_1_velocity.copy(), circle_1_group[5][3]), 
                  FadeIn(circle_2_group[5][0]), FadeIn(circle_2_group[5][2]), TransformMatchingShapes(circle_2_anno.copy(), circle_2_group[5][1]), TransformMatchingShapes(circle_2_velocity.copy(), circle_2_group[5][3])
        )
        self.wait(0.8)
        circle_1_group_new_brace_text = MathTex(r"\vec{p} = ", "90 kg \cdot m/s", font_size = 28).shift(LEFT * 4).shift(RIGHT * 0.78).shift(1.75 * DOWN)
        circle_1_group_new_brace_text.set_color_by_tex("90 kg \cdot m/s", MAROON)
        circle_2_group_new_brace_text = MathTex(r"\vec{p} = ", "-80 kg \cdot m/s", font_size = 28).shift(RIGHT * 4).shift(LEFT * 0.78).shift(1.75 * DOWN)
        circle_2_group_new_brace_text.set_color_by_tex("-80 kg \cdot m/s", MAROON)

        self.play(ReplacementTransform(circle_1_group[5], circle_1_group_new_brace_text), ReplacementTransform(circle_2_group[5], circle_2_group_new_brace_text))

        self.wait(0.8)

        total_momentum = MathTex(r"\vec{p}_{total} = ", "90 kg \cdot m/s", " + ", "(-80 kg \cdot m/s)", font_size = 32).shift(2.5 * DOWN)
        total_momentum.set_color_by_tex_to_color_map({
            "90 kg \cdot m/s" : MAROON, 
            "(-80 kg \cdot m/s)" : MAROON, 
        })
        self.play(FadeIn(total_momentum[0]), FadeIn(total_momentum[2]), TransformMatchingShapes(circle_1_group_new_brace_text[1].copy(), total_momentum[1]), TransformMatchingShapes(circle_2_group_new_brace_text[1].copy(), total_momentum[3]))
        self.wait(0.8)
        total_momentum_new = MathTex(r"\vec{p}_{total} = ", "10 kg \cdot m/s", font_size = 32).shift(2.5 * DOWN).set_color_by_tex("10 kg \cdot m/s", MAROON)
        self.play(ReplacementTransform(total_momentum, total_momentum_new))
        self.wait(0.2)
        self.play(
            LaggedStart(
                *[
                    LaggedStart(*[FadeOut(circle_1_group[4]), FadeOut(circle_2_group[4]), FadeOut(circle_1_group_new_brace_text), FadeOut(circle_2_group_new_brace_text), FadeOut(circle_1_group[2]), FadeOut(circle_1_group[3]), FadeOut(circle_2_group[2]), FadeOut(circle_2_group[3])], lag_ratio=0),
                    total_momentum_new.animate.shift(UP * 0.65)
                ], lag_ratio = 0.5
            )
        )
        circle_1_group[0].generate_target()
        circle_2_group[0].generate_target()
        circle_1_group[1].generate_target()
        circle_2_group[1].generate_target()
        circle_2_group[0].target.shift(3*LEFT)
        circle_1_group[0].target.shift(3*RIGHT)
        circle_2_group[1].target.shift(3*LEFT)
        circle_1_group[1].target.shift(3*RIGHT)
        self.play(MoveToTarget(circle_1_group[0]), MoveToTarget(circle_2_group[0]), MoveToTarget(circle_1_group[1]), MoveToTarget(circle_2_group[1]), run_time = 0.6, rate_func = linear)
        circle_1_arrow = Arrow(start=ORIGIN, end=3*LEFT, color=RED).shift(0.75 * LEFT)
        circle_1_anno = MathTex(r"\vec{v_{1}}", font_size = 34, color = RED).shift(UP * 0.3).shift(2.6 * LEFT)

        circle_2_arrow = Arrow(start=ORIGIN, end=3*RIGHT, color=RED).shift(0.75 * RIGHT)
        circle_2_anno = MathTex(r"\vec{v_{2}}", font_size = 34, color = RED).shift(UP * 0.3).shift(2.6 * RIGHT)
        self.play(FadeIn(circle_1_arrow), FadeIn(circle_2_arrow), FadeIn(circle_1_anno), FadeIn(circle_2_anno), run_time = 0.6)
        left_side = MathTex("15 kg", r"\cdot", r"\vec{v_{1}}", "+", "8 kg", r"\cdot", r"\vec{v_{2}}", " = ", r"10 kg \cdot m/s", font_size = 32).shift(1.85 * DOWN)
        left_side.set_color_by_tex_to_color_map({
            "15 kg" : BLUE_E, 
            "8 kg" : PURPLE_E, 
            r"\vec{v_{1}}" : RED, 
            r"\vec{v_{2}}" : RED
        })
        self.wait(0.2)
        self.play(ReplacementTransform(total_momentum_new[0], left_side[:8]), TransformMatchingShapes(total_momentum_new[1], left_side[8]))
        self.wait(4)

class Intro(Scene):
    def construct(self):
        anno = Tex(r"\text{Physics Engines}", font_size = 80)
        anno_2 = Tex(r"\text{An exploration of how computers simulate physical phenomena}", font_size = 36).shift(DOWN * 0.6)
        self.wait(1)
        self.play(Write(anno), run_time = 2)
        self.play(FadeIn(anno_2), run_time = 1.2)
        self.wait(2)

class Updater7Ball_dt(Circle):
    def __init__(self, ** kwargs):
        Circle.__init__(self, ** kwargs)
        self.radius = 0.4
        self.fill_color = BLUE
        self.fill_opacity = 1
        self.color = BLUE
        self.velocity = np.array((0.0, 0.0, 0.0))

    def get_top(self):
        return self.get_center()[1] + self.radius

    def get_bottom(self):
        return self.get_center()[1] - self.radius

    def get_right_edge(self):
        return self.get_center()[0] + self.radius

    def get_left_edge(self):
        return self.get_center()[0] - self.radius

class BouncingBall(Scene):
    def construct(self):
        types_of_collisions = Tex("Types of Collisions", font_size = 48)
        marble_text = Tex("Marble", font_size = 40, color = BLUE_E).shift(3.75 * LEFT).shift(2.3 * UP)
        rubber_ball_text = Tex("Rubber Ball", font_size = 40, color = MAROON_C).shift(3.75 * RIGHT).shift(2.3 * UP)
        self.play(Write(types_of_collisions))
        self.play(types_of_collisions.animate.shift(3 * UP))
        self.wait(0.50)

        floor = Line((-10, -3.5, 0), (10, -3.5, 0))
        top = Line((-10, 2, 0), (10, 2, 0))
        mid = Line((0, 2.6, 0), (0, -3.5, 0))
        marble = Updater7Ball_dt(radius = 0.4, fill_color = BLUE_E, fill_opacity = 1).set_stroke(BLUE_E).shift(3.75*LEFT).shift(1.25*UP)
        rubber_ball = Updater7Ball_dt(radius = 0.4, fill_color = MAROON_C, fill_opacity = 1).set_stroke(MAROON_C).shift(3.75*RIGHT).shift(1.25*UP)
        self.play(FadeIn(floor), FadeIn(top), FadeIn(mid), FadeIn(marble_text), FadeIn(rubber_ball_text))
        self.play(DrawBorderThenFill(marble), DrawBorderThenFill(rubber_ball))
        global finished_marble, finished_rubber_ball
        finished_marble = 0 
        finished_rubber_ball = 0 
        def update_marble(ball, dt):
            global finished_marble 
            if(finished_marble): return 
            ball.acceleration = np.array((0.0, -6.0, 0.0))
            before = ball.velocity[1] > 0 
            ball.velocity = ball.velocity + ball.acceleration * dt
            if before and ball.velocity[1] < 0: 
                ball.shift(2*ball.velocity * dt) 
                finished_marble = 1
                return 
            ball.shift(ball.velocity * dt)  
            if ball.get_bottom() <= -3.5: 
                ball.velocity[1] = -ball.velocity[1]
                ball.velocity *= 0.7

        def update_rubber_ball(ball, dt):
            global finished_rubber_ball 
            if(finished_rubber_ball): return 
            ball.acceleration = np.array((0.0, -6.0, 0.0))
            before = ball.velocity[1] > 0 
            ball.velocity = ball.velocity + ball.acceleration * dt
            if before and ball.velocity[1] < 0: 
                finished_rubber_ball = 1
                ball.shift(2*ball.velocity * dt)  
                return 
            ball.shift(ball.velocity * dt)  
            if ball.get_bottom() <= -3.5: 
                ball.velocity[1] = -ball.velocity[1]
                ball.velocity *= 0.85

        marble.add_updater(update_marble)
        rubber_ball.add_updater(update_rubber_ball)
        self.wait(3.01)

        marble_text = Tex("Retained LESS velocity", font_size = 40, color = RED).shift(3.75 * LEFT).shift(0.75*DOWN)
        rubber_ball_text = Tex("Retained MORE velocity", font_size = 40, color = GREEN).shift(3.75 * RIGHT).shift(0.75*DOWN)
        rect = Rectangle(width = 10, height = 5.5, fill_color = WHITE, fill_opacity = 0.35).shift(5*LEFT).shift(0.76 * DOWN)
        rect2 = Rectangle(width = 10, height = 5.5, fill_color = WHITE, fill_opacity = 0.35).shift(5*RIGHT).shift(0.76 * DOWN)
        self.play(FadeIn(rect), FadeIn(rect2), FadeIn(marble_text), FadeIn(rubber_ball_text))
        self.wait(4)

class COR(Scene):
    def construct(self):
        title = Tex("Coefficient of Restitution", font_size = 48).shift(UP)
        ul = Underline(title, stroke_width=1)
        definition = Tex("\\text{The ratio between of the final to initial relative velocity between two objects after they collide.}", font_size = 28, color = BLUE_C).shift(0.5 * UP)
        definition_group = VGroup(title, ul, definition)
        self.play(Write(definition_group[0]), run_time = 1.2)
        self.play(FadeIn(definition_group[1]), FadeIn(definition_group[2]))
        definition_group.generate_target()
        definition_group.target.shift(1.5*UP)
        self.wait(3.5)
        math_definition = MathTex(r"e=\frac{\abs{\overrightarrow{RV_{f}}}}{\abs{\overrightarrow{RV_{i}}}}", font_size = 42)
        e_definition = Tex(r"$e =$ \text{Coefficient of Restitution}", font_size=26)
        rvf_definition = Tex(r"$\overrightarrow{RV_{f}} =$ \text{Final Relative Velocity}", font_size=26)
        rvi_definition = Tex(r"$\overrightarrow{RV_{i}} =$ \text{Initial Relative Velocity}", font_size=26)
        group = VGroup(math_definition, e_definition, rvf_definition, rvi_definition)
        group.arrange(DOWN, center=True)
        group.shift(0.2*DOWN)
        self.play(MoveToTarget(definition_group)) 
        self.play(Write(group[0]))
        self.play(FadeIn(group[1:]), run_time=0.5)
        self.wait(3)

class CORRange(Scene):
    def construct(self):
        l0 = NumberLine(
            x_range = [0, 1, 0.1],
            color = BLUE_C, 
            font_size = 24,  
            length = 12, 
            tick_size = 0.2,  
            include_numbers=True,
            decimal_number_config={"num_decimal_places": 2},
        ).shift(3*DOWN)
        slider = Circle(radius = 0.12).set_fill(ORANGE, opacity=1).set_stroke(ORANGE).shift(3*DOWN)
        floor = Line((-10, -2, 0), (10, -2, 0))
        def update_ball(ball, dt):
            ball.acceleration = np.array((0.0, -5.0, 0.0))
            before = ball.velocity[1] > 0 
            ball.velocity = ball.velocity + ball.acceleration * dt
            if(ball.get_bottom() + ball.velocity[1] * dt <= -2.0):
                ball.shift((0, -2 - ball.get_bottom(), 0))
            else: ball.shift(ball.velocity * dt)  
            if ball.get_bottom() <= -2.0: 
                ball.velocity[1] = -ball.velocity[1]
            
        self.add(floor)
        # self.add(l0, slider)
        self.play(FadeIn(l0), FadeIn(slider))
        self.wait(1)
        self.play(slider.animate.shift(6*RIGHT), run_time = 0.8)
        self.wait(0.25)
        ball = Updater7Ball_dt(radius = 0.4, fill_color = RED, fill_opacity = 1).set_stroke(RED).shift(2*UP)
        ball.add_updater(update_ball)
        self.add(ball)
        self.wait(3.69)
        self.play(FadeOut(ball), slider.animate.shift(12*LEFT), run_time = 0.8)
        self.wait(0.25)
        def update_ball(ball, dt):
            if ball.get_bottom() <= -2: 
                return 
            ball.acceleration = np.array((0.0, -5.0, 0.0))
            ball.velocity = ball.velocity + ball.acceleration * dt
            if(ball.get_bottom() + ball.velocity[1] * dt <= -2.0):
                ball.shift((0, -2 - ball.get_bottom(), 0))
                return 
            ball.shift(ball.velocity * dt)  
            if ball.get_bottom() <= -2.0: 
                return 
        ball = Updater7Ball_dt(radius = 0.4, fill_color = RED, fill_opacity = 1).set_stroke(RED).shift(2*UP)
        ball.add_updater(update_ball)
        self.add(ball)
        self.wait(4.48)
        self.play(FadeOut(ball), slider.animate.shift(6*RIGHT), run_time = 0.8)
        def update_ball(ball, dt):
            ball.acceleration = np.array((0.0, -5.0, 0.0))
            before = ball.velocity[1] > 0 
            ball.velocity = ball.velocity + ball.acceleration * dt
            ball.shift(ball.velocity * dt)  
            if ball.get_bottom() <= -2.0: 
                ball.velocity[1] = -ball.velocity[1]
                ball.velocity[1] *= 0.8
        ball = Updater7Ball_dt(radius = 0.4, fill_color = RED, fill_opacity = 1).set_stroke(RED).shift(2*UP)
        ball.add_updater(update_ball)
        self.add(ball)
        self.wait(5)
        self.play(FadeOut(ball), run_time = 0.8)

class RepresentingObjects(Scene):
    def construct(self):
        title = Tex(r"\text{\underline{Representing Objects}}", font_size = 54)
        self.play(Write(title), run_time = 1.25)
        self.wait(2)
        self.play(title.animate.shift(2.75 * UP))
        parameters = Tex(r"\text{Parameters}", font_size = 42, color = RED_D).shift(2.1 * UP)
        self.play(FadeIn(parameters))
        plane = NumberPlane(
            x_range = (0, 10),
            y_range = (0, 10),
            x_length = 4.2,
            y_length = 4.2,
        )
        plane.center().shift((-3.25, -0.5, 0))
        l1 = Line((-1.15, 1.6, 0), (-1.15, -2.6, 0), stroke_width=2)
        l2 = Line((-5.35, 1.6, 0), (-1.15, 1.6, 0), stroke_width=2)
        anno = Tex("Two-Dimensional",font_size=32).shift((-3.25, -2.9, 0))
        plane_group = VGroup(plane, l1, l2, anno).shift((0.5, 0, 0))
        self.play(FadeIn(plane_group[0]), FadeIn(plane_group[1]), FadeIn(plane_group[2]), FadeIn(plane_group[3]))
        circle = Circle(radius = 2, color = BLUE, fill_opacity = 1.0).set_stroke(BLUE_E, width = 5).shift((2.75, 0, 0)).shift(DOWN * 0.5)
        anno_2 = Tex("Rigid Body", font_size=32).shift((2.75, -2.9, 0)) 
        anno_3 = Tex("(No Deformation)", font_size=22, color = RED).shift((2.75, -3.2, 0)) 
        self.wait(0.25)
        self.play(DrawBorderThenFill(circle), run_time = 1.5)
        self.play(FadeIn(anno_2))
        self.play(FadeIn(anno_3))
        self.wait(2)
        self.play(FadeOut(plane_group), FadeOut(circle), FadeOut(anno_2), FadeOut(anno_3), FadeOut(parameters))
        shape_text = (Tex(r"\text{Shapes}", font_size = 42, color = RED_D).shift(2.1 * UP))
        self.play(FadeIn(shape_text))



        Hexagon = [(0,0,0),(1,1,0),(2,1,0),(3,0,0),(2,-1,0),(1,-1,0)]
        poly = Polygon(*Hexagon, color = BLUE, fill_opacity = 1).center().set_stroke(BLUE_E, width = 5).scale(1.6).shift((-2.75, 0, 0))
        ellipse = Ellipse(width = 3.5, height = 2.5, color = BLUE, fill_opacity=1).scale(1.2).center().set_stroke(BLUE_E, width = 5).shift((2.75, 0, 0))
        anno_2 = Tex("Polygons", font_size=32).shift((-2.75, -2, 0)) 
        anno_3 = Tex("Ellipses", font_size=32).shift((2.75, -2, 0)) 
        self.play(FadeIn(poly), FadeIn(ellipse))
        self.play(Write(anno_2), Write(anno_3))
        self.wait(1)
        rectangle = Rectangle(width = 3, height = 2, color = BLUE, fill_opacity = 1.0).set_stroke(BLUE_E, width = 5).scale(1.6).shift((-2.75, 0, 0))
        circle = Circle(radius = 1.25, color = BLUE, fill_opacity=1).scale(1.2).center().set_stroke(BLUE_E, width = 5).shift((2.75, 0, 0))
        self.play(Transform(poly, rectangle), Transform(ellipse, circle))
        self.wait(0.25)
        # big_group = VGroup(anno_2, anno_3, rectangle, circle)
        self.play(anno_2.animate.shift(RIGHT/2), anno_3.animate.shift(RIGHT/2), poly.animate.shift(RIGHT/2), ellipse.animate.shift(RIGHT/2))
        self.wait(6.5)
        self.play(FadeOut(anno_2), FadeOut(anno_3), FadeOut(poly), FadeOut(ellipse), FadeOut(title), FadeOut(shape_text))

class BasicProperties(Scene):
    def construct(self):
        square = Square(side_length = 2.5, color = BLUE, fill_opacity = 0.3)
        l0 = Line((-8, -1.275, 0), (8, -1.275, 0), color = BLUE_A)
        rect1 = Rectangle(width = 16, height = 6.72500, color = BLUE_A, fill_opacity = 0.5).shift(4.65 * DOWN)
        self.play(FadeIn(rect1), FadeIn(l0))
        self.play(DrawBorderThenFill(square))
        dimensions = Brace(square, direction = [-1, 0, 0])
        dim_text = Tex(r"\text{Dimensions}", font_size = 36, color = RED_E).shift(2.8*LEFT)
        self.play(FadeIn(dimensions), FadeIn(dim_text))
        position = Dot(point = ORIGIN)
        position_text = MathTex(r"(x,y)", font_size = 36, color = RED_E).shift(0.35*DOWN)
        self.play(FadeIn(position), FadeIn(position_text))
        l1 = Line((0, 0, 0), (-1.25, 0, 0))
        l2 = Line((0, 0, 0), (0, 1.25, 0))
        angle = Angle(l2, l1)
        theta = MathTex(r"\theta", color = RED_E,font_size = 36).shift((-0.4, 0.4, 0))
        self.play(FadeIn(l1), FadeIn(l2), FadeIn(angle), FadeIn(theta))
        mass = Tex(r"\text{Mass}", color = RED_E, font_size = 36).shift((0, 1.5, 0))
        self.play(FadeIn(mass))
        arrow = Arrow(start=ORIGIN, end=3.5*RIGHT).shift(LEFT/4)
        vel = Tex(r"\text{Velocity}", font_size = 24, color = RED_E).shift(UP * 0.185).shift(1.9 * RIGHT)
        self.play(FadeIn(arrow), FadeIn(vel))
        self.wait(8)

class Procedure(Scene):
    def construct(self):
        procedure_text = Tex(r"\text{\underline{Physics Engine Procedure}}", font_size = 60)
        first = Tex(r"1. Contact Detection", font_size=42)
        square1 = Square(side_length = 1, color = BLUE_E, fill_opacity = 0.5).shift(1.2*UP).shift(4*LEFT)
        square2 = Square(side_length = 1, color = BLUE_E, fill_opacity = 0.5).shift(1.2*UP).shift(4*RIGHT)



        second = Tex(r"2. Contact Resolution", font_size=42)
        third = Tex(r"3. State Integration", font_size=42)
        group = VGroup(procedure_text, first, second, third)
        group.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(group[0]))
        self.play(group[0].animate.shift(3*UP))
        group[1:].shift(3*LEFT)
        group[1].shift(3*UP)
        group[2].shift(1.5*UP)
        self.wait(1.1)

        self.play(FadeIn(group[1]), FadeIn(square1), FadeIn(square2))
        square1.generate_target()
        square2.generate_target() 
        square1.target.shift(3.5*RIGHT)
        square2.target.shift(3.5*LEFT)
        self.play(MoveToTarget(square1), MoveToTarget(square2), rate_func = linear)
        self.play(square1.animate.set_color(RED_E), square2.animate.set_color(RED_E), run_time=0.01)

       
        square3 = Square(side_length = 1, color = BLUE_E, fill_opacity = 0.5).shift(0.9*DOWN).shift(4*LEFT)
        square4 = Square(side_length = 1, color = BLUE_E, fill_opacity = 0.5).shift(0.9*DOWN).shift(4*RIGHT)
        square3.generate_target()
        square4.generate_target() 
        square3.target.shift(3.5*RIGHT)
        square4.target.shift(3.5*LEFT)

        self.play(FadeIn(group[2]), FadeIn(square3), FadeIn(square4))
        self.play(MoveToTarget(square3), MoveToTarget(square4), rate_func = linear)
        square3.target.shift(-3.5*RIGHT)
        square4.target.shift(-3.5*LEFT)
        self.play(MoveToTarget(square3), MoveToTarget(square4), rate_func = linear)

        square5 = Square(side_length = 1, color = BLUE_E, fill_opacity = 0.5).shift(2.9*DOWN).shift(5.5*LEFT)
        arrow = Arrow(start = (-5.5, -2.9, 0), end = (-4.0, -2.9, 0), color = RED, buff = 0, stroke_width = 5, max_tip_length_to_length_ratio = 0.1)
        S = VGroup(square5, arrow)
        S.generate_target()
        S.target.shift(9.52*RIGHT)


        self.play(FadeIn(group[3]), FadeIn(square5), FadeIn(arrow))
        self.play(MoveToTarget(S), rate_func = linear, run_time = 2.8)
        self.wait(1.15)
        website_link = Tex(r"https://jeffreykaili.github.io/SPH4UEA-Website/", font_size = 26, color = WHITE).shift(3.8*DOWN)
        self.play(FadeIn(website_link))
        self.wait(2.5)
        self.play(FadeOut(website_link), FadeOut(second), FadeOut(third), FadeOut(procedure_text), FadeOut(S), FadeOut(square1), FadeOut(square2), FadeOut(square3), FadeOut(square4))
        first.generate_target() 
        first.target.center()
        first.target.shift(3.2*UP)
        self.play(MoveToTarget(first))
        box = Rectangle(width = 13, height = 6.2).shift(0.3 * DOWN)
        self.play(FadeIn(box))
        square1 = Square(color = BLUE, fill_opacity = 1).set_stroke(WHITE, width = 3).rotate(PI / 4)
        square2 = Square(color = BLUE, fill_opacity = 1).set_stroke(WHITE, width = 3).rotate(-PI / 3.234234).shift(1.45*RIGHT).shift(0.65*UP)
        square3 = Square(color = BLUE, fill_opacity = 1).set_stroke(WHITE, width = 3).rotate(2*PI/3).shift(3.2*LEFT).shift(1.3*DOWN)
        square4 = Square(color = BLUE, fill_opacity = 1).set_stroke(WHITE, width = 3).rotate(2*PI/2.234234).shift(4*RIGHT).shift(1.8*DOWN)
        square5 = Square(color = BLUE, fill_opacity = 1).set_stroke(WHITE, width = 3).rotate(-PI/8).shift(4.3*LEFT).shift(1.32*UP)
        square6 = Square(color = BLUE, fill_opacity = 1).set_stroke(WHITE, width = 3).rotate(-PI/1.123123).shift(4.2*RIGHT).shift(1.2*UP)
        self.play(FadeIn(square1), FadeIn(square2), FadeIn(square3), FadeIn(square4), FadeIn(square5), FadeIn(square6))
        self.wait(3)
        self.play(square2.animate.set_color(RED).set_stroke(WHITE, width = 3), square1.animate.set_color(RED).set_stroke(WHITE, width = 3))
        self.wait(2)
        self.play(FadeOut(square1), FadeOut(square2), FadeOut(square3), FadeOut(square4), FadeOut(square5), FadeOut(square6), FadeOut(first), FadeOut(box))

class SAT(Scene):
    def construct(self):
        title = Tex(r"\text{Separating Axis Theorem (SAT)}", font_size = 48)
        ul = Underline(title, stroke_width = 1)
        definition = Tex("Two objects", " do not overlap", " if there exists a line onto which both the object's projections do not intersect", ".", font_size = 34).shift(0.8 * DOWN)
        definition.set_color_by_tex("do not overlap", RED)
        definition_group = VGroup(title, ul, definition)
        self.play(Write(definition_group[0]), run_time = 2)
        self.play(FadeIn(definition_group[1]), FadeIn(definition_group[2]))
        self.play(definition_group.animate.shift(3.1*UP))
        square1 = Square(side_length = 1.8,color = BLUE, fill_opacity = 1).set_stroke(BLUE_E, width = 3)
        dotted_A1 = DashedLine((0, 0.9, 0), (0, -1.7, 0), color = RED).shift(0.9*RIGHT)
        dotted_A2 = DashedLine((0, 0.9, 0), (0, -1.7, 0), color = RED).shift(0.9*LEFT)
        square1_group = VGroup(square1, dotted_A1, dotted_A2)
        square1_group.rotate(PI / 9).shift(0.72*DOWN).shift(1.5*LEFT)
        square2 = Square(side_length = 1.8, color = BLUE, fill_opacity = 1).set_stroke(BLUE_E, width = 3)
        dotted_B1 = DashedLine((0, 0.9, 0), (0, -1.7, 0), color = RED).shift(0.9*RIGHT)
        dotted_B2 = DashedLine((0, 0.9, 0), (0, -1.7, 0), color = RED).shift(0.9*LEFT)
        square2_group = VGroup(square2, dotted_B1, dotted_B2)
        square2_group.rotate(PI / 9).shift(RIGHT).shift(0.5*LEFT)
        l1 = Line((0, 0, 0), (1.8, 0, 0), color = WHITE).scale(10).rotate(PI / 9).shift(1.3*DOWN).shift(RIGHT)
        self.play(FadeIn(square1_group[0]), FadeIn(square2_group[0]), FadeIn(l1))
        self.play(FadeIn(square1_group[1]), FadeIn(square1_group[2]), FadeIn(square2_group[1]), FadeIn(square2_group[2]))
        self.wait(1)
        result = Tex(r"A line exists, so these shapes are ", "not colliding*", ".", font_size=28).shift(1.55 * UP)
        result.set_color_by_tex("not colliding*", RED)
        extra_info = Tex("*This concept is mostly math, so it is further explained on my website.", color = RED,font_size = 20).shift(3.65*RIGHT).shift(3.8*DOWN)
        self.play(FadeIn(result), FadeIn(extra_info))
        self.wait(2)
        self.play(FadeOut(extra_info), FadeOut(square2_group), FadeOut(square1_group), FadeOut(title), FadeOut(ul), FadeOut(definition), FadeOut(result), FadeOut(l1))

class CollidingBodies(Scene):
    def construct(self):
        CircleA = Circle(radius = 2.5, color = BLUE, fill_opacity = 0.3).set_stroke(width = 3).shift(0.5*RIGHT)
        CircleB = Circle(radius = 2, color = BLUE, fill_opacity = 0.3).set_stroke(width = 3).shift(1.25*UP).shift(2.3*LEFT)
        depth = DoubleArrow((-1.783, 1.019, 0), (-0.474, 0.435, 0), buff = 0, tip_length = 0.1, stroke_width = 3, color = RED)
        normal = Arrow(start = (0.5, 0, 0), end = (-2.3, 1.25, 0), buff = 3.06635, color = MAROON, stroke_width = 3, max_tip_length_to_length_ratio = 0.05)
        dot = Dot((0.5, 0, 0), radius = 0.04, color = BLUE)
        dot2 = Dot((-2.3, 1.25, 0), radius = 0.04, color = BLUE)
        normalized_normal = Arrow(start = (0.5, 0, 0), end = (-2.3, 1.25, 0), buff = 1.0, color = MAROON, stroke_width = 3, max_tip_length_to_length_ratio = 0.1)
        circle_group = VGroup(CircleA, CircleB, depth, dot, dot2, normal, normalized_normal)
        circle_group.center() 
        circle_group.shift(0.6*UP) 
        circle_group[6].shift(0.415 * DOWN).shift(0.93*RIGHT)
        text = Tex(r"\text{Collision Normal}", font_size = 12, color = MAROON).rotate(-0.42).shift(0.78*RIGHT).shift(0.525*UP)
        text2 = Tex(r"\text{Collision Depth}", font_size = 14, color = RED).rotate(-0.42).shift(0.41 * LEFT).shift(1.06*UP)

        self.play(FadeIn(circle_group[0]), FadeIn(circle_group[1]), FadeIn(circle_group[3]), FadeIn(circle_group[4]))
        self.play(FadeIn(circle_group[5]))
        self.play(Transform(circle_group[5], circle_group[6]))
        self.play(FadeIn(text))
        self.play(FadeIn(circle_group[2]), FadeIn(text2))
        # self.play(FadeIn(circle_group[0]), FadeIn(circle_group[1]), FadeIn(circle_group[2]), FadeIn(circle_group[3]), FadeIn(circle_group[4]), FadeIn(circle_group[6]))
        self.wait(0.8)
        normal_definition = Tex("Collision Normal: ", "A ", "normalized", " vector of the", " collision direction", ".", font_size = 25).shift(DOWN*2.8)
        normal_definition.set_color_by_tex_to_color_map({
            "Collision Normal:" : MAROON, 
            "normalized" : MAROON_B, 
            "collision direction" : MAROON_B, 
        }) 
        collision_dep_definition = Tex("Collision Depth: ", "A ", "scalar", " value of how far the objects have", " already overlapped", ".", font_size = 25).shift(DOWN*3.2)
        collision_dep_definition.set_color_by_tex_to_color_map({
            "Collision Depth: " : RED, 
            "scalar" : RED_B, 
            " already overlapped" : RED_B, 
        })
        self.play(Write(normal_definition[0]), run_time = 0.7)
        self.play(FadeIn(normal_definition[1:]))
        self.wait(2.7)
        self.play(Write(collision_dep_definition[0]), run_time = 0.7)
        self.play(FadeIn(collision_dep_definition[1:]))
        self.wait(5.9)
        self.play(FadeOut(collision_dep_definition), FadeOut(normal_definition), FadeOut(circle_group), FadeOut(text), FadeOut(text2))

class SeparatingObjects(Scene):
    def construct(self):
        square1 = Square(side_length = 2, color = BLUE_E, fill_opacity = 0.5).shift(4*LEFT).shift(0.25*DOWN)
        square2 = Square(side_length = 2, color = RED_E, fill_opacity = 0.5).shift(4*RIGHT).shift(0.25*DOWN)
        A = Tex("A", font_size = 70).shift(4*LEFT).shift(0.25*DOWN)
        B = Tex("B", font_size = 70).shift(4*RIGHT).shift(0.25*DOWN)
        square1_group = VGroup(square1, A)
        square2_group = VGroup(square2, B)
        rect1 = Rectangle(width = 16, height = 6.72500, color = BLUE_A, fill_opacity = 0.5).shift(4.65 * DOWN)
        self.play(FadeIn(square1_group), FadeIn(square2_group), FadeIn(rect1))
        square1_group.generate_target() 
        square2_group.generate_target() 
        square1_group.target.shift(3*RIGHT)
        square2_group.target.shift(3*LEFT)
        self.play(MoveToTarget(square1_group), MoveToTarget(square2_group), rate_func = linear, run_time = 1)
        self.wait(1.8)
        A_pos = MathTex(r"p_{A}=(-1, 0)", font_size = 38)
        A_orientation = MathTex(r"\theta_{A}=0^\circ", font_size = 38)
        A_vel = MathTex(r"\overrightarrow{v_{A}}=3m/s", font_size = 38)
        A_mass = MathTex(r"m_{A}=10kg", font_size = 38)
        A_info = VGroup(A_pos, A_orientation, A_vel, A_mass) 
        A_info.arrange(DOWN).shift(4.4 * LEFT).shift(UP * 1.75)
        B_pos = MathTex(r"p_{B}=(1, 0)", font_size = 38)
        B_orientation = MathTex(r"\theta_{B}=0^\circ", font_size = 38)
        B_vel = MathTex(r"\overrightarrow{v_{B}}=-3m/s", font_size = 38)
        B_mass = MathTex(r"m_{B}=8kg", font_size = 38)
        B_info = VGroup(B_pos, B_orientation, B_vel, B_mass) 
        B_info.arrange(DOWN).shift(4.4 * RIGHT).shift(UP * 1.75)
        for i in range(4):
            self.play(FadeIn(A_info[i]), FadeIn(B_info[i]), run_time = 0.65) 
        self.wait(1)
        self.play(FadeOut(B_info), FadeOut(A_info), FadeOut(square1_group[1]), FadeOut(square2_group[1]))
        title = Tex("Newton's Third Law", font_size = 48).shift(0.8*UP)
        ul = Underline(title, stroke_width=1)
        definition = Tex("When two bodies interact, they apply forces to one another that are", " equal in magnitude", " and ", "opposite in direction", ".", font_size = 34)
        definition.set_color_by_tex_to_color_map({
            "equal in magnitude" : RED,
            "opposite in direction" : RED, 
        })
        definition_group = VGroup(title, ul, definition).shift(2.1*UP)
        arrow_1 = Arrow(start = ORIGIN, end = 1.6 * RIGHT, buff = 0, stroke_width = 5, max_tip_length_to_length_ratio = 0.1, color = BLUE_D).shift(0.25*DOWN)
        arrow_2 = Arrow(start = ORIGIN, end = 1.6 * LEFT, buff = 0, stroke_width = 5, max_tip_length_to_length_ratio = 0.1, color = RED_D).shift(0.25*DOWN)
        fab = MathTex(r"F_{AB}", font_size = 28, color = BLUE_D).shift(0.01*DOWN).shift(0.8*RIGHT)
        fba = MathTex(r"F_{BA}", font_size = 28, color = RED_D).shift(0.01*DOWN).shift(0.8*LEFT)
        self.play(Write(definition_group[0]), run_time = 1.2)
        self.play(FadeIn(definition_group[1]), FadeIn(definition_group[2]))
        self.play(FadeIn(arrow_2), FadeIn(arrow_1), FadeIn(fab), FadeIn(fba))
        self.wait(4)
        self.play(FadeOut(arrow_2), FadeOut(arrow_1), FadeOut(fab), FadeOut(fba), FadeOut(rect1), FadeOut(square1_group[0]), FadeOut(square2_group[0]), FadeOut(definition_group))

class Impulse(Scene):
    def construct(self):
        impulse_text = Tex("Impulse: ", "A vector quantity describing the effect of ", "force acting over time", ".", font_size = 36)
        impulse_text.set_color_by_tex_to_color_map({
            "force acting over time" : RED, 
        })
        self.play(Write(impulse_text[0]))
        self.play(FadeIn(impulse_text[1:]))
        self.play(impulse_text.animate.shift(2.2*UP))
        impulse_def = Tex("For a constant force,", font_size = 32)
        impulse_definition = MathTex(r"\vec{J}=\vec{F}\Delta t", font_size=64)
        j_definition = MathTex(r"\vec{J}=\text{Impulse}", font_size=32)
        f_definition = MathTex(r"\vec{F}=\text{Force}", font_size=32)
        t_definition = MathTex(r"\Delta t=\text{Elapsed Time}", font_size=32)
        group = VGroup(impulse_def, impulse_definition, j_definition, f_definition, t_definition)
        group.arrange(DOWN, center=True)
        self.play(FadeIn(group[0]))
        self.play(Write(group[1]))
        group[2:].shift(0.3*DOWN)
        self.play(FadeIn(group[2:]), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(group[0]), FadeOut(group[2:]), FadeOut(impulse_text))
        group[1].generate_target()
        group[1].target.center().shift(3*UP)
        self.play(MoveToTarget(group[1]))
        floor = Line((-10, -2.5, 0), (10, -2.5, 0))
        mid = Line((0, 2.3, 0), (0, -2.5, 0))
        self.play(FadeIn(floor), FadeIn(mid))

        square1 = Square(side_length = 1, color = BLUE_E, fill_opacity = 0.5).shift((-6, -1.96, 0))
        square2 = Square(side_length = 1, color = RED_E, fill_opacity = 0.5).shift((-1.25, -1.96, 0))
        self.play(FadeIn(square1), FadeIn(square2))
        square1.generate_target()
        square2.generate_target() 
        square1.target.shift((2, 0, 0))
        square2.target.shift((-2, 0, 0))
        self.play(MoveToTarget(square1), MoveToTarget(square2), rate_func = linear)
        square1.target.shift((-2, 0, 0))
        square2.target.shift((2, 0, 0))
        self.play(MoveToTarget(square1), MoveToTarget(square2), rate_func = linear)
        first_text = Tex(r"Collision Resolved Late\\", "UNREALISTIC", font_size = 40).shift(3.75 * LEFT).shift(0.1*DOWN)
        first_text.set_color_by_tex("UNREALISTIC", RED)
        rect = Rectangle(width = 10, height = 4.8, fill_color = WHITE, fill_opacity = 0.35).shift(5*LEFT).shift(0.1 * DOWN)
        self.play(FadeIn(rect))
        self.play(FadeIn(first_text))
        self.wait(1)

        square3 = Square(side_length = 1, color = BLUE_E, fill_opacity = 0.5).shift((6, -1.96, 0))
        square4 = Square(side_length = 1, color = RED_E, fill_opacity = 0.5).shift((1.25, -1.96, 0))
        self.play(FadeIn(square3), FadeIn(square4))
        square3.generate_target()
        square4.generate_target() 
        square3.target.shift((-1.875, 0, 0))
        square4.target.shift((1.875, 0, 0))
        self.play(MoveToTarget(square3), MoveToTarget(square4), rate_func = linear)
        square3.target.shift((1.875, 0, 0))
        square4.target.shift((-1.875, 0, 0))
        self.play(MoveToTarget(square3), MoveToTarget(square4), rate_func = linear)
        second_text = Tex(r"Collision Resolved On Time\\", "REALISTIC", font_size = 40).shift(3.75 * RIGHT).shift(0.1*DOWN)
        second_text.set_color_by_tex("REALISTIC", GREEN)
        rect2 = Rectangle(width = 10, height = 4.8, fill_color = WHITE, fill_opacity = 0.35).shift(5*RIGHT).shift(0.1 * DOWN)
        self.play(FadeIn(rect2))
        self.play(FadeIn(second_text))
        self.wait(1)

        resolve_text = Tex(r"So, when the engine detects a collision, it will apply an", " impulse", " to resolve it.", font_size = 38)
        resolve_text.set_color_by_tex(" impulse", RED)
        resolve_text.shift(3.2*DOWN)
        self.play(FadeIn(resolve_text))
        self.wait(3) 

class ImpulseScalar(Scene):
    def construct(self):
        impulse_scalar = MathTex(r"J=\text{Impulse Scalar}", font_size = 48).shift(2.5*UP)
        self.play(FadeIn(impulse_scalar))
        square1 = Square(side_length = 2, color = BLUE_E, fill_opacity = 0.5).shift(4*LEFT)
        square2 = Square(side_length = 2, color = RED_E, fill_opacity = 0.5).shift(4*RIGHT)
        A = Tex("A", font_size = 70).shift(4*LEFT)
        B = Tex("B", font_size = 70).shift(4*RIGHT)
        square1_group = VGroup(square1, A).shift(0.7*UP)
        square2_group = VGroup(square2, B).shift(0.7*UP)
        self.play(FadeIn(square1_group), FadeIn(square2_group))
        square1_group.generate_target()
        square2_group.generate_target() 
        square1_group.target.shift(3*RIGHT)
        square2_group.target.shift(3*LEFT)
        self.play(MoveToTarget(square1_group), MoveToTarget(square2_group), rate_func = linear, run_time = 0.6)
        delta_A = MathTex(r"\Delta v_{A}=\mathord{?}", font_size = 42, color = BLUE).shift(3.4*LEFT).shift(0.7*UP)
        delta_B = MathTex(r"\Delta v_{B}=\mathord{?}", font_size = 42, color = RED).shift(3.4*RIGHT).shift(0.7*UP)
        self.play(FadeIn(delta_A), FadeIn(delta_B))
        impulse_vec = MathTex(r"\vec{J}=J\vec{n}", font_size = 38)
        n_definition = MathTex(r"\vec{n}=\text{Collision Normal}", font_size = 32)
        impulse_2_def = MathTex(r"\vec{J}", "=","m", r"\Delta v", font_size = 38)
        impulse_rearrange = MathTex(r"\Delta v", "=", "{", r"\vec{J}", r"\over", "m", "}", font_size = 38, color = MAROON_E)
        m_definition = MathTex(r"m = \text{mass}", font_size = 28)
        impulse_group = VGroup(impulse_vec, n_definition, impulse_2_def, impulse_rearrange, m_definition).arrange(DOWN).shift(2.1*DOWN)
        self.wait(3)
        self.play(FadeIn(impulse_group[0]))
        self.play(FadeIn(impulse_group[1]))
        self.wait(2)
        self.play(FadeIn(impulse_group[2]))
        self.wait(1)
        self.play(TransformMatchingTex(
            impulse_group[2].copy(), impulse_group[3],
            path_arc=90 * DEGREES,
        ))
        self.play(FadeIn(m_definition))
        self.wait(4)

class RelativeMotion(Scene):
    def construct(self):
        relative_motion = Tex("Relative Motion: ", "The velocity of one body with respect to another body.", font_size = 36)
        relative_motion.set_color_by_tex("Relative Motion: ", RED)
        self.play(Write(relative_motion[0]))
        self.play(FadeIn(relative_motion[1]))
        self.wait(2)
        self.play(relative_motion.animate.shift(3*UP))
        mid = Line((0, 2.5, 0), (0, -3.5, 0))
        self.play(FadeIn(mid))
        self.wait(30)

class RelativeMotion2(Scene):
    def construct(self):
        relative_motion = Tex("Relative Motion: ", "The velocity of one body with respect to another body.", font_size = 36).shift(3*UP)
        relative_motion.set_color_by_tex("Relative Motion: ", RED)
        self.add(relative_motion[0], relative_motion[1])
        mid = Line((0, 2.5, 0), (0, -3.5, 0))
        self.add((mid))
        self.wait(1)
        self.play(FadeOut(mid))
        square1 = Square(side_length = 2, color = BLUE_E, fill_opacity = 0.5).shift(4*LEFT)
        square_1_arrow = Arrow(start=ORIGIN, end=2.5*RIGHT, buff=0.0).shift(4*LEFT)
        square_1_velocity = MathTex(r"\overrightarrow{v_{A}}", font_size = 38, color = BLUE).shift(UP * 0.3).shift(2.45*LEFT)
        square1_group = VGroup(square1, square_1_arrow, square_1_velocity)

        square2 = Square(side_length = 2, color = RED_E, fill_opacity = 0.5).shift(RIGHT)
        square_2_arrow = Arrow(start=ORIGIN, end=2.5*RIGHT, buff=0.0).shift(RIGHT)
        square_2_velocity = MathTex(r"\overrightarrow{v_{B}}", font_size = 38, color = RED).shift(UP * 0.3).shift(2.6*RIGHT)
        square2_group = VGroup(square2, square_2_arrow, square_2_velocity)
        relative_motion.generate_target()
        relative_motion.target.shift(0.6 * DOWN)
        self.play(MoveToTarget(relative_motion), FadeIn(square1_group), FadeIn(square2_group))
        square1_group.generate_target()
        square1_group.target.shift(5*RIGHT)
        square2_group.generate_target()
        square2_group.target.shift(3.5*RIGHT)
       # self.play(MoveToTarget(square1_group), MoveToTarget(square2_group), rate_func = linear, run_time = 5)
       # self.wait(2)
        relative = MathTex(r"\vec{v}_{BA} = \vec{v}_{B} - \vec{v}_{A}", font_size = 36)
        relative_def = MathTex(r"\vec{v}_{BA} = \text{Relative Velocity}", font_size = 32)
        dot_product = MathTex(r"J = \vec{v}_{BA} \cdot \vec{n}", font_size = 36)
        lines = VGroup(relative, relative_def, dot_product)
        lines.arrange(DOWN).shift(2.4*DOWN)

        self.play(
            LaggedStart(
                *[
                    LaggedStart(
                        *[
                           MoveToTarget(square1_group, run_time = 6, rate_func = linear), 
                           MoveToTarget(square2_group, run_time = 6, rate_func = linear), 
                        ], lag_ratio = 0
                    ), 
                    LaggedStart(
                        *[
                            LaggedStart(
                                *[
                                    FadeIn(lines[0]), 
                                    FadeIn(lines[1]),
                                ], lag_ratio = 1
                            ), 
                            FadeIn(lines[2]),
                        ], lag_ratio = 2
                    )
                ], lag_ratio = 0.2 
            )
        )
        self.wait(3)

class CombiningCOR(Scene):
    def construct(self):
        from_before = MathTex(r"\text{From before,}", font_size=46, color = BLUE)
        dot_product = MathTex(r"J = ", r"\vec{v}_{BA} \cdot \vec{n}", font_size = 60)
        with_COR = MathTex(r"J = ", r"(1 + e)(", r"\vec{v}_{BA} \cdot \vec{n}", ")", font_size = 60)
        add_neg = MathTex(r"J = ", "-", r"(1 + e)(", r"\vec{v}_{BA} \cdot \vec{n}", ")", font_size = 60)
        lines = VGroup(from_before, dot_product, with_COR, add_neg)
        lines.arrange(DOWN)
        lines.center()
        self.play(Write(lines[0]))
        self.play(Write(lines[1]))
        self.wait(3)
        self.play(TransformMatchingTex(lines[1].copy(), lines[2]))
        self.wait(8)
        self.play(TransformMatchingTex(lines[2].copy(), lines[3]))
        self.wait(3)

class CombiningMomentum(Scene):
    def construct(self):
        square1 = Square(side_length = 2, color = BLUE_E, fill_opacity = 0.5).shift(LEFT)
        square2 = Square(side_length = 2, color = RED_E, fill_opacity = 0.5).shift(RIGHT)
        A = Tex("A", font_size = 70).shift(LEFT)
        A_mass = MathTex(r"m_{A}", font_size = 48, color = BLUE).shift(LEFT).shift(1.3*UP)
        B = Tex("B", font_size = 70).shift(RIGHT)
        B_mass = MathTex(r"m_{B}", font_size = 48, color = RED).shift(RIGHT).shift(1.3*UP)

        square1_group = VGroup(square1, A, A_mass).shift(1.4*UP)
        square2_group = VGroup(square2, B, B_mass).shift(1.4*UP)
        self.play(FadeIn(square1_group), FadeIn(square2_group))
        current = MathTex(r"J = ", "-", r"(1 + e)(", r"\vec{v}_{BA} \cdot \vec{n}", ")", font_size = 36)
        impulse_rearrange = MathTex(r"\Delta v", "=", "{", r"\vec{J}", r"\over", "m", "}", font_size = 36)
        new_definition = MathTex(r"J = ", "{", "-", r"(1 + e)(", r"\vec{v}_{BA} \cdot \vec{n}", ")", r"\over", r"m_{A}^{-1}", " + ", r"m_{B}^{-1}", "}", font_size = 36)
        new_definition.set_color_by_tex_to_color_map({r"m_{A}^{-1}" : BLUE, r"m_{B}^{-1}" : RED})
        lines = VGroup(impulse_rearrange, current, new_definition)
        lines.arrange(DOWN).center().shift(1.5*DOWN)
        self.play(FadeIn(lines[0]))
        self.play(FadeIn(lines[1]))
        self.wait(4.5)
        self.play(TransformMatchingTex(lines[1].copy(), lines[2]))
        self.wait(10)
        self.play(FadeOut(current), FadeOut(impulse_rearrange))
        self.play(lines[2].animate.shift(1.7*UP))
        self.wait(1)
        final_definition = MathTex(r"\vec{J} = ", "{", "-", r"(1 + e)(", r"\vec{v}_{BA} \cdot \vec{n}", ")", r"\over", r"m_{A}^{-1}", " + ", r"m_{B}^{-1}", r"}\cdot \vec{n}", font_size = 28)
        final_definition.shift(1.85*DOWN)
        self.play(TransformMatchingTex(lines[2].copy(), final_definition))
        delta_v = MathTex(r"\Delta v = ", "{", "{", "-", r"(1 + e)(", r"\vec{v}_{BA} \cdot \vec{n}", ")", r"\over", r"m_{A}^{-1}", " + ", r"m_{B}^{-1}", r"}\cdot \vec{n}", r"\over m}", font_size = 28)
        delta_v = delta_v.shift(3*DOWN)
        self.wait(1.5)
        self.play(TransformMatchingTex(final_definition.copy(), delta_v))
        self.wait(9)

class SemiImplicitEuler(Scene):
    def construct(self):
        title = Tex("Semi-implicit Euler Method", font_size = 48).shift(UP)
        ul = Underline(title, stroke_width=1)
        definition_group = VGroup(title, ul, )
        self.play(Write(definition_group[0]), run_time = 1.2)
        self.play(FadeIn(definition_group[1]))

        self.wait(0.2)

        definition_group.generate_target() 
        definition_group.target.shift(1.75*UP)
        self.play(MoveToTarget(definition_group))
        self.wait(4.5)
        equation_1 = MathTex(r"\vec{a} = \frac{\vec{F}}{m}")
        equation_2 = MathTex(r"\vec{v} = \vec{v}_{i} + \vec{a} \Delta t")
        equation_3 = MathTex(r"\vec{p} = \vec{p}_{i} + \vec{v} \Delta t")
        equation_group = VGroup(equation_1, equation_2, equation_3)
        equation_group.center().arrange(RIGHT).shift(1.5*UP)
        equation_group[0].shift(1.6*LEFT)
        equation_group[1].shift(0.4*RIGHT)
        equation_group[2].shift(1.9*RIGHT)
        frame_definition = MathTex(r"\text{Let } n \text{ be our current frame: }", font_size = 32, color = BLUE).shift(0.45 * UP)
        eq_1 = MathTex(r"1.\text{ } \vec{a}_{n} = \frac{\vec{F}}{m}", font_size = 36, color = RED)
        eq_2 = MathTex(r"2. \text{ } \vec{v}_{n+1} = \vec{v}_{n} + \vec{a}_{n}" ,r"\Delta t", font_size = 36, color = RED)
        eq_3 = MathTex(r"3. \text{ } \vec{p}_{n+1} = \vec{p}_{n} + \vec{v}_{n+1}", r"\Delta t", font_size = 36, color = RED)
        lines = VGroup(eq_1, eq_2, eq_3)
        lines.arrange(DOWN, center = False, aligned_edge = LEFT).shift(0.4 * DOWN).shift(1.1*LEFT)
        self.play(FadeIn(equation_group))
        self.wait(3)
        self.play(FadeIn(frame_definition))
        # self.play(FadeIn(lines))
        self.play(
            LaggedStart(
                *[
                    equation_group[0].animate.set_color(RED), 
                    FadeIn(lines[0])
                ], lag_ratio = 0.1
            )

        )
        self.wait(1.25)
        self.play(
            LaggedStart(
                *[
                    LaggedStart(
                        *[equation_group[0].animate.set_color(WHITE), equation_group[1].animate.set_color(RED), lines[0].animate.set_color(WHITE)], 
                        lag_ratio = 0
                    ), FadeIn(lines[1])
                ], lag_ratio = 0.1
            )
        )
        self.wait(3)
        self.play(
            LaggedStart(
                *[
                    LaggedStart(
                        *[equation_group[1].animate.set_color(WHITE), equation_group[2].animate.set_color(RED), lines[1].animate.set_color(WHITE)], 
                        lag_ratio = 0
                    ), FadeIn(lines[2])
                ], lag_ratio = 0.1
            )
        )
        self.wait(3)
        self.play(equation_group[2].animate.set_color(WHITE), lines[2].animate.set_color(WHITE))
        self.wait(8)
        delta_t = MathTex(r"\Delta t = \frac{1}{60} \text{s}", color = RED).shift(3*DOWN)
        eq_1 = MathTex(r"1.\text{ } \vec{a}_{n} = \frac{\vec{F}}{m}", font_size = 36)
        eq_2 = MathTex(r"2. \text{ } \vec{v}_{n+1} = \vec{v}_{n} + \vec{a}_{n}" ,r"\Delta t", font_size = 36)
        eq_2.set_color_by_tex(r"\Delta t", RED)
        eq_3 = MathTex(r"3. \text{ } \vec{p}_{n+1} = \vec{p}_{n} + \vec{v}_{n+1}", r"\Delta t", font_size = 36)
        eq_3.set_color_by_tex(r"\Delta t", RED)
        lines_2 = VGroup(eq_1, eq_2, eq_3)
        lines_2.arrange(DOWN, center = False, aligned_edge = LEFT).shift(0.4 * DOWN).shift(1.1*LEFT)

        self.play(FadeIn(delta_t), TransformMatchingTex(lines[1], lines_2[1]), TransformMatchingTex(lines[2], lines_2[2]))
        self.wait(8)

class AngularComponents(Scene):
    def construct(self):
        square = Square(side_length = 4, color = BLUE, fill_opacity = 0.3)
        dot = Dot(point = ORIGIN, radius = 0.05, color = BLUE)
        curvedArrow = CurvedArrow(start_point = (2,  0, 0), end_point = (0, 2, 0), color = RED, stroke_width = 5)
        arc = ArcBetweenPoints(start = (0, -2, 0), end = (2, 0, 0), stroke_color=RED)
        arc2 = ArcBetweenPoints(start = (-2, 0, 0), end = (0, -2, 0), stroke_color=RED)
        arc3 = ArcBetweenPoints(start = (-0.2, 1.9, 0), end = (-2, 0, 0), stroke_color=RED)
        arc_group = VGroup(curvedArrow, arc, arc2, arc3).scale(0.6)
        definition = MathTex(r"\omega = \text{Angular Velocity}", font_size = 28, color = RED).shift(3.2*DOWN)
        definition2 = MathTex(r"\alpha = \text{Angular Acceleration}", font_size = 28, color = BLUE).shift(3.6*DOWN)
       
        square_group = VGroup(square, dot, arc_group)
        self.play(FadeIn(square_group))
        self.play(
            LaggedStart(
                *[
                    Rotating(square_group, radians = 2 * PI, run_time=3, rate_func = rush_into), 
                    LaggedStart(
                        *[  
                            FadeIn(definition2), 
                            FadeIn(definition),
                        ], lag_ratio = 0, 
                    )
                ], lag_ratio = 0.4, 
            )
        )
        self.wait(0.25)
        self.play(square_group.animate.shift(1.5 * UP), definition.animate.shift(2.15*UP), definition2.animate.shift(2.15*UP))
        self.wait(1)
        self.play(FadeOut(definition), FadeOut(definition2), FadeOut(square_group[2]))
        arrow = Arrow(start = ORIGIN, end = 4 * RIGHT, buff = 0, color = RED).shift(1.5 * UP)
        F = MathTex(r"\vec{F}", color = RED, font_size = 58).shift(2*UP).shift(2.8*RIGHT)
        self.play(FadeIn(arrow), FadeIn(F))
        F_eq = MathTex(r"\vec{F}=m\vec{a}").shift(1.05 * DOWN)
        torque = MathTex(r"\vec{\tau} = \vec{F} \cross \vec{r}").shift(3.25 * DOWN)
        t_def = MathTex(r"\vec{\tau} = \text{Torque}", font_size = 26)
        f_def = MathTex(r"\vec{F} = \text{Force}", font_size = 26)
        r_def = MathTex(r"\vec{r} = \text{A position vector from centre of mass to the point where the force is applied}", font_size = 26)
        def_group = VGroup(torque, t_def, f_def, r_def).arrange(DOWN).shift(2.5 *DOWN)
        self.play(Write(F_eq))
        self.wait(2.5)
        self.play(FadeIn(def_group[0]))
        self.wait(0.25)
        self.play(FadeIn(def_group[1:]))
        self.wait(11)

class LinearVSRotational(Scene):
    def construct(self):
        square = Square(side_length = 3, color = BLUE, fill_opacity = 0.3)
        dots = []
        for i in range(13):
            for j in range(13):
                dot = Dot(point = (-1.5 + 0.25 * i, 1.5 - 0.25 * j, 0), radius = 0.05, color = RED)
                dots.append(dot)
        square_group = VGroup(square, *dots).shift(4 * LEFT)
        self.play(FadeIn(square_group))
        square_group.generate_target()
        square_group.target.shift(4 * RIGHT)
        self.wait(0.25)
        self.play(MoveToTarget(square_group), rate_func = linear, run_time = 4)
        self.wait(0.5)
        self.play(Rotating(square_group, radians = 2 * PI, run_time=5.5))
        self.wait(1)
        self.play(square_group.animate.shift(1.65*UP))        
        MOI = Tex("Moment of Inertia: ", "A quantity based on a body's distribution of mass that determines the amount of torque required for a certain angular acceleration on a chosen axis of rotation.", font_size = 36).shift(DOWN)
        MOI.set_color_by_tex("Moment of Inertia: ", RED)
        self.play(Write(MOI[0]))
        self.play(FadeIn(MOI[1]))
        self.wait(7) 
        fma = MathTex(r"\vec{a}=\frac{F}{", r"m}", font_size = 48)
        fma.set_color_by_tex(r"m}", RED)
        re = MathTex(r"\alpha = \frac{\tau}{", r"I}", font_size = 48)
        re.set_color_by_tex(r"I}", RED)
        arrow = Arrow(start = (-1, 0, 0), end = (1, 0, 0), buff = 0, stroke_width = 2.6, max_tip_length_to_length_ratio = 0.06)
        group = VGroup(fma, arrow, re)
        group.arrange(RIGHT).shift(2.5*DOWN)
        group[0].shift(0.08*LEFT)
        group[2].shift(0.08*RIGHT)
        a_def = MathTex(r"\alpha = \text{Angular Acceleration}", font_size = 26)
        t_def = MathTex(r"\tau = \text{Torque}", font_size = 26)
        i_def = MathTex(r"I = \text{Moment of Inertia}", font_size = 26)
        def_group = VGroup(a_def, t_def, i_def).arrange(DOWN, center = False, aligned_edge = LEFT).shift(5*RIGHT).shift(2*DOWN)
        self.play(FadeIn(group[0]))
        self.wait(3)
        self.play(FadeIn(group[1]), FadeIn(group[2]))
        self.wait(0.25)
        self.play(FadeIn(def_group))
        self.wait(6)

class LastScene(Scene):
    def construct(self):
        final_impulse = MathTex(r"\vec{J}=\frac{-(1+e)(\vec{v}_{BA}\cdot\vec{n})}{", r"m_{A}^{-1}", "+", r"m_{B}^{-1}", r"+(", r"I_{A}^{-1}", r"(\vec{r}_A\cross\vec{n})\cross \vec{r}_{A}+", r"I_{B}^{-1}", r"(\vec{r}_B\cross\vec{n})\cross \vec{r}_{B})\cdot\vec{n}}", font_size = 42)
        note = MathTex(r"\text{Note that this equation \emph{looks} confusing because it is all presented at the same time, but it makes more sense if you build up to it.}", font_size = 20)
        note.shift(3.6*DOWN)
        self.play(FadeIn(final_impulse), FadeIn(note))
        self.wait(4.5)
        final_impulse_anim = MathTex(r"\vec{J}=\frac{-(1+e)(\vec{v}_{BA}\cdot\vec{n})}{", r"m_{A}^{-1}", "+", r"m_{B}^{-1}", r"+(", r"I_{A}^{-1}", r"(\vec{r}_A\cross\vec{n})\cross \vec{r}_{A}+", r"I_{B}^{-1}", r"(\vec{r}_B\cross\vec{n})\cross \vec{r}_{B})\cdot\vec{n}}", font_size = 42)
        final_impulse_anim.set_color_by_tex_to_color_map({r"m_{A}^{-1}" : RED, r"m_{B}^{-1}" : RED})
        self.play(TransformMatchingTex(final_impulse, final_impulse_anim))
        self.wait(1)
        final_impulse_anim2 = final_impulse_anim.copy()
        final_impulse_anim2.set_color_by_tex_to_color_map({r"I_{A}^{-1}" : BLUE, r"I_{B}^{-1}" : BLUE})
        self.play(TransformMatchingTex(final_impulse_anim, final_impulse_anim2))
        self.wait(2.5)
        integrate = MathTex(r"\Delta \omega=\frac{(\vec{r}\cross\vec{J}\vec{n})}{I^{-1}}").shift(1.5*DOWN)
        self.play(Write(integrate))
        self.wait(3)