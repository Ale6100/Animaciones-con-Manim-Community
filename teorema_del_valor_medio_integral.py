from manim import *

class tvmi(Scene):
    def construct(self):
        tiempo_entre_videos = 5
        # grid = NumberPlane() # La grilla es muy útil cuando estás editando el video
        # self.add(grid)
        titulo = Tex('Demostración del teorema del valor medio integral')
        self.play(Write(titulo), run_time = 1)
        self.wait(tiempo_entre_videos-1)

        ##########?

        enunciado = Tex('Si $f:[a, b] \\rightarrow \mathbb{R}$ es una función continua en $[a, b]$, entonces $\\exists~c \\in (a, b)$ tal que $\\int_a^bf = f(c)(b - a)$').move_to(np.array([0, 0.01, 0])).scale(0.8)
        self.play(Transform(titulo, enunciado), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########?

        demostracion = Tex('Iniciemos observando que por ser $f$ continua en $[a, b]$, es integrable en $[a, b]$').move_to(np.array([0, 3.5, 0])).scale(0.8)
        F = Tex('Es decir: $F(x) = \\int_a^xf \\Rightarrow \\int_a^bf = F(b) - F(a)$').move_to(np.array([0, 2.5, 0])).scale(0.8)
        donde = Tex('donde $F$ es la primitiva de $f$').move_to(np.array([0, 1.5, 0])).scale(0.8)

        axes = Axes(x_range=[-3.5, 3.5, 1], y_range=[-1, 10, 1]).scale(0.6).move_to(np.array([0, -2, 0]))
        def f(x):
            return -(x-3)*(x+3)
        f_grafico = axes.plot(f, color=YELLOW)
        area1 = axes.get_area(
                    f_grafico,
                    x_range=(-3, 3),
                    color=BLUE,
                    opacity=0.4,
                )

        plot1 = VGroup(axes, f_grafico, area1)
        label_f = axes.get_graph_label(f_grafico, 'f(x)').scale(0.6)
        label_area1 = Tex('$\\int_a^bf$').move_to(np.array([3.5, -2.5, 0])).scale(0.6).set_color(BLUE)
        a = Tex('$a$').move_to(np.array([-3, -3.7, 0])).scale(0.6)
        b = Tex('$b$').move_to(np.array([3, -3.7, 0])).scale(0.6)
        self.play(Transform(titulo, demostracion), Write(F), Write(donde), Write(a), Write(b), Create(label_f), Create(label_area1), Create(plot1), run_time = 2)
        self.wait(tiempo_entre_videos+2)

        ##########?

        F_copia = F[0][-14:].copy()

        entonces = Tex('podemos afirmar que $F: [a,b] ~\\rightarrow~ \mathbb{R}$ es continua en $[a, b]$ y derivable en $(a, b)$, con lo cual cumple con las hipótesis del teorema de Lagrange, es decir').move_to(np.array([0, 2.49, 0])).scale(0.8)
        entonces2 = Tex('$\\exists~c \\in (a, b)$ tal que $F\'(c) = \\frac{F(b) - F(a)}{b - a}$').move_to(np.array([-2.75, 1.49, 0])).scale(0.8)

        self.play(F_copia.animate.move_to(np.array([-5, 3.5, 0])), FadeOut(titulo, F, donde), Write(entonces), Write(entonces2))
        self.wait(tiempo_entre_videos+1)

        ##########?

        flecha = Tex('$\\Rightarrow F\'(c)(b - a) = F(b) - F(a)$').move_to(entonces2.get_right() + RIGHT*2.75).scale(0.8)
        self.play(Write(flecha))
        self.wait(tiempo_entre_videos-3)

        ##########?

        self.play(F_copia.animate.move_to(flecha.get_center() + DOWN + RIGHT + np.array([-0.05, 0.01, 0])), FadeOut(entonces, reverse=False))
        self.wait(tiempo_entre_videos-3)

        ##########?

        copia1 = flecha[0][-20:].copy()
        copia2 = F[0][-14:].copy().move_to(F_copia)

        igualdad = Tex('$\\int_a^bf = F\'(c)(b - a)$').move_to(np.array([-3.5, 3, 0])).scale(0.8)

        self.play(Transform(copia1, igualdad), Transform(copia2, igualdad), FadeOut(F_copia, entonces2, flecha))
        self.wait(tiempo_entre_videos-3)

        ##########?

        pero2 = Tex('pero $F\'(c) = f(c)$ por ser $F$ primitiva de $f$').move_to(np.array([2.09, 3, 0])).scale(0.8)
        self.play(Write(pero2), FadeOut(copia2))
        self.wait(tiempo_entre_videos-2)

        ##########?

        listo = Tex('$\\int_a^bf = f(c)(b - a)$').move_to(np.array([0, 1.5, 0])).scale(0.8)
        framebox = SurroundingRectangle(listo[0], buff = 0.1)

        def l(x):
            return 6
        l_grafico = axes.plot(l, color=ORANGE)
        area2 = axes.get_area(
                    l_grafico,
                    x_range=(-3, 3),
                    color=PINK,
                    opacity=0.4,
                )
        linea_vertical_izquierda = axes.get_vertical_line(axes.i2gp(-1.7327327327327327, l_grafico))
        linea_vertical_derecha = axes.get_vertical_line(axes.i2gp(1.726726726726727, l_grafico))
        c1 = Tex('$c$').move_to(np.array([-1.775, -3.7, 0])).scale(0.6)
        c2 = Tex('$c$').move_to(np.array([1.775, -3.7, 0])).scale(0.6)
        label_l = axes.get_graph_label(l_grafico, 'f(c)').scale(0.6)
        label_area2 = Tex('$f(c)(b - a)$').move_to(np.array([-4, -2.5, 0])).scale(0.6).set_color(PINK)
        plot2 = VGroup(l_grafico, area2, linea_vertical_izquierda, linea_vertical_derecha, c1, c2, label_l, label_area2)

        nota1 = Tex('Nota: Observar que nada impide que exista más de un').move_to(np.array([-4, -0.25, 0])).scale(0.35)
        nota2 = Tex('valor $c$ que cumpla con la condición planteada').move_to(np.array([-4, -0.5, 0])).scale(0.35)

        self.play(Write(nota1), Write(nota2), Write(listo), Create(framebox), Create(plot2), run_time = 3)
        self.wait(tiempo_entre_videos-2)

        ##########?

        igual = Tex('=').move_to(np.array([0, 0.5, 0]))
        area1_copia = area1.copy()
        area2_copia = area2.copy()

        self.play(area1_copia.animate.move_to([-1, 0.5, 0]).scale(0.175), area2_copia.animate.move_to([1, 0.5, 0]).scale(0.175), Write(igual), run_time = 2)
        self.wait(tiempo_entre_videos-2)

        ##########?

        demostrado = Tex('podemos dar por demostrado el teorema').move_to(listo.get_center() + np.array([4.45, 0, 0])).scale(0.6)
        self.play(Write(demostrado))
        self.wait(tiempo_entre_videos)
