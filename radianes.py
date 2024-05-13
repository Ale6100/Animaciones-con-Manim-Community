from manim import Scene, NumberPlane, Tex, Write, ParametricFunction, Create, Line, PI, ValueTracker, always_redraw, ReplacementTransform, Dot, ArcBetweenPoints, Arc, SurroundingRectangle, Uncreate, Unwrite, Transform
import numpy as np

class radianes(Scene):
    def construct(self):
        tiempo_entre_videos = 5

        # grid = NumberPlane().set_opacity(0.33)
        # self.add(grid)

        inicio = Tex('Consideremos un círculo de radio $r$').move_to([0, 3, 0])

        self.play(Write(inicio), run_time = 1)
        self.wait(tiempo_entre_videos-3)

        circulo = ParametricFunction(lambda t: [2.5*np.cos(t)-3.5, 2.5*np.sin(t)-0.5, 0], t_range=[-PI, PI, 0.01]).set_color('WHITE').set_stroke(width=10)

        radian_radio = ValueTracker(1)

        radio = always_redraw(lambda: Line(circulo.get_center(), circulo.get_point_from_function(radian_radio.get_value())).set_color('RED').set_stroke(width=10))

        radio_label = always_redraw(lambda: Tex('$r$').move_to(radio.get_center()+[-0.66, -0.5, 0]).set_color('RED'))

        self.play(Create(radio), Create(circulo), Write(radio_label), run_time=1)
        self.wait(1)

        self.play(radian_radio.animate.set_value(2*PI + 1), run_time=2)
        self.wait(tiempo_entre_videos-3)

        ##########? Creamos un arco de un radián
        radian_radio.set_value(1)

        tomemos = Tex('Dibujemos un arco cuya la longitud sea exactamente igual al radio').move_to([0, 3, 0]).scale(0.8)

        P1 = Dot().move_to(circulo.get_point_from_function(0))
        P2 = Dot().move_to(circulo.get_point_from_function(1))

        arco_1 = ArcBetweenPoints(start=P1.get_center(), end=P2.get_center(), radius=2.5, color='BLUE').set_stroke(width=10)

        theta = always_redraw(lambda: Arc(1, start_angle=0, angle=radian_radio.get_value(), arc_center=circulo.get_center()).set_color('YELLOW'))

        theta_label = Tex('$\\theta$').move_to(theta.get_center()+np.array([-0.5, 0.5, 0])).set_color('YELLOW')

        self.play(ReplacementTransform(inicio, tomemos), ReplacementTransform(radio.copy(), arco_1), Create(theta), Write(theta_label), run_time=1)
        self.wait(tiempo_entre_videos)

        ##########? Definimos el radián

        radian = Tex('A este ángulo especial lo denominamos radián, cuyo valor es aproximadamente $57.29^\circ$').move_to([0, 3, 0]).scale(0.8)

        primera_igualdad = Tex('$1$ radián $\\approx 57.29^\circ$').move_to([3.5, 2, 0])

        self.play(ReplacementTransform(tomemos, radian), Write(primera_igualdad), run_time=1)
        self.wait(tiempo_entre_videos)

        ##########? Creamos un arco de dos radiánes

        dos_radianes = Tex('Dupliquemos y el ángulo...').move_to([0, 3, 0])

        P3 = Dot().move_to(circulo.get_point_from_function(2))

        arco_2 = ArcBetweenPoints(start=P2.get_center(), end=P3.get_center(), radius=2.5, color='GREEN').set_stroke(width=10)

        segunda_igualdad = Tex('$2$ radianes $\\approx 114.59^\circ$').move_to([3.5, 1, 0])

        self.play(ReplacementTransform(radian, dos_radianes), radian_radio.animate.set_value(2), theta_label.animate.move_to(theta.get_center()+np.array([-0.33, 0.75, 0])), Create(arco_2), ReplacementTransform(primera_igualdad.copy(), segunda_igualdad), run_time=1)
        self.wait(tiempo_entre_videos-1)

        ##########? Creamos un arco de tres radiánes

        tres_radianes = Tex('Tripliquemos el ángulo...').move_to([0, 3, 0])

        P4 = Dot().move_to(circulo.get_point_from_function(3))

        arco_3 = ArcBetweenPoints(start=P3.get_center(), end=P4.get_center(), radius=2.5, color='PURPLE').set_stroke(width=10)

        tercera_igualdad = Tex('$3$ radianes $\\approx 171.88^\circ$').move_to([3.5, 0, 0])

        self.play(ReplacementTransform(dos_radianes, tres_radianes), radian_radio.animate.set_value(3), theta_label.animate.move_to(theta.get_center()+np.array([-0.33, 0.75, 0])), Create(arco_3), ReplacementTransform(segunda_igualdad.copy(), tercera_igualdad), run_time=1)
        self.wait(tiempo_entre_videos-1)

        ##########? Agregamos un cachito más para llegar a $\pi$

        un_poco_mas = Tex('Observemos que para llegar a un ángulo de $180^\circ$ necesitamos sumar un poquito más, ese valor agregado es aproximadamente $0.1416$ radianes').move_to([0, 3, 0]).scale(0.8)

        P5 = Dot().move_to(circulo.get_point_from_function(PI))

        arco_4 = ArcBetweenPoints(start=P4.get_center(), end=P5.get_center(), radius=2.5, color='GOLD').set_stroke(width=10)

        self.play(ReplacementTransform(tres_radianes, un_poco_mas), radian_radio.animate.set_value(PI), Create(arco_4), run_time=1)
        self.wait(tiempo_entre_videos+1)

        ##########? Definimos pi radianes

        obtencion_pi = Tex('En particular, si le sumamos ese valor a los 3 radianes que ya teníamos, obtenemos el valor de $\\pi$ radianes, lo que implica que $180^\circ = \pi$ radianes').move_to([0, 3, 0]).scale(0.8)

        pi_radianes = Tex('$\pi$ radianes $= 180^\circ$').move_to([3.5, -1, 0])

        box_formula = SurroundingRectangle(pi_radianes, color='YELLOW', buff = 0.1)

        nota = Tex('Nota: Recordar que el número $\pi$ es aproximadamente $3.1416$').move_to([3.5, -3, 0]).scale(0.5)

        self.play(ReplacementTransform(un_poco_mas, obtencion_pi), ReplacementTransform(tercera_igualdad.copy(), pi_radianes), Create(box_formula), Write(nota), run_time=1)
        self.wait(tiempo_entre_videos+1)

        ##########?

        finalmente = Tex('Ya somos capaces de entender el concepto del radián y escribirlo en términos de $\pi$. Veamos ejemplos').move_to([0, 3, 0]).scale(0.8)

        self.play(ReplacementTransform(obtencion_pi, finalmente), pi_radianes.animate.move_to(np.array([3.5, -3, 0])), Uncreate(arco_1), Uncreate(arco_2), Uncreate(arco_3), Uncreate(arco_4), Unwrite(primera_igualdad), Unwrite(segunda_igualdad), Unwrite(tercera_igualdad), Uncreate(box_formula), Unwrite(nota), run_time=1)
        self.wait(tiempo_entre_videos)

        ##########? Ejemplo 1

        theta_label.add_updater(lambda v: v.move_to(theta.get_center()+np.array([-0.33, 0.75, 0])))

        ejemplo_1 = Tex('$\\theta = 0$ radianes').move_to([3.5, 0, 0])

        self.play(Write(ejemplo_1), radian_radio.animate.set_value(0), run_time=1)
        self.wait(1)

        angulos = [PI/4, PI/2, 3*PI/4, PI, 3*PI/2, 2*PI]
        textos = ['\\frac{\pi}{4}', '\\frac{\pi}{2}', '\\frac{3\pi}{4}', '\pi', '\\frac{3\pi}{2}', '2\pi']

        for i in range(len(angulos)):
            self.play(Transform(ejemplo_1, Tex(f'$\\theta = {textos[i]}$ radianes').move_to([3.5, 0, 0])), radian_radio.animate.set_value(angulos[i]), run_time=1)
            self.wait(1)

        self.wait(tiempo_entre_videos)