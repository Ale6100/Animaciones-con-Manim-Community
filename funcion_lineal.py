from manim import Scene, NumberPlane, Tex, Write, Axes, Create, Transform, Uncreate, Unwrite, ReplacementTransform, ShowPassingFlash, Underline, Dot, ValueTracker, always_redraw, Arc, SurroundingRectangle
import numpy as np

class funcion_lineal(Scene):
    def construct(self):
        tiempo_entre_videos = 5

        # grid = NumberPlane().set_opacity(0.33)
        # self.add(grid)

        titulo = Tex('La expresión más famosa de la función lineal $f(x) : \mathbb{R} \\rightarrow \mathbb{R}$ tiene la forma $y=mx+b$, donde $m$ y $b$ son constantes reales llamadas pendiente y ordenada al origen respecitvamente').scale(0.8).move_to([0, 3, 0])

        titulo[0][60:66].set_color('YELLOW')

        self.play(Write(titulo), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? #Agrega un gráfico de una función lineal que se va transformando en otras

        ax = Axes(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            x_length = 6,
            y_length = 6,
        ).move_to([0, -0.75, 0])
        # .move_to([-1, -0.75, 0])

        labels = ax.get_axis_labels(Tex("$x$"), Tex("$y$"))

        recta = ax.plot(lambda x: 2*x, color='blue', x_range=ax.x_range)

        label_recta = Tex('$y = 2x$').move_to([-5, 1, 0]).set_color('blue')

        self.play(Create(ax), Write(labels), Create(recta), Write(label_recta), run_time = 1)
        self.wait(tiempo_entre_videos-2)

        ms = [-1, 2, -3, 0, 1/2]
        bs = [0, -3, 5, 2, -1]
        colors = ['red', 'green', 'purple', 'orange', 'yellow']

        for i in range(len(ms)):
            nueva_recta = ax.plot(lambda x, i=i: ms[i]*x + bs[i], color=f'{colors[i]}', x_range=ax.x_range)
            nuevo_label_recta = Tex(f'$y={ms[i]}x + {bs[i]}$').move_to(label_recta.get_center()).set_color(f'{colors[i]}')

            self.play(Transform(recta, nueva_recta), Transform(label_recta, nuevo_label_recta), run_time = 0.33)
            self.wait(0.67)

        self.wait(tiempo_entre_videos-2)

        ##########? Cuestionarnos sobre la forma del gráfico

        pero = Tex('Pero... cómo sabemos que el gráfico tiene esta forma? La información está dentro de $m$ y $b$').move_to([0, 1, 0]).scale(0.8)

        self.play(ReplacementTransform(titulo, pero), Uncreate(recta), Uncreate(label_recta), Uncreate(ax), Unwrite(labels), run_time = 1)
        self.wait(tiempo_entre_videos-2)

        idea = Tex('Tratemos de obtener nosotros mismos la fórmula de la función lineal, para entender mejor el significado de estas dos constantes').move_to([0, -1, 0]).scale(0.8)

        self.play(Write(idea), run_time = 1)
        self.wait(tiempo_entre_videos-2)

        ##########? Resaltamos brevemente la idea

        self.play(ShowPassingFlash(Underline(idea).set_color('YELLOW')), run_time = 1)
        self.wait(2)

        ##########? Empezamos despacio agregando dos puntos

        empecemos = Tex('Consideremos dos puntos cualesquiera en el plano, los llamaremos $P_1 = (x_1, y_1)$ y $P_2 = (x_2, y_2)$').move_to([0, 3, 0]).scale(0.8)

        p1_text = Tex('$P_1 = (x_1, y_1)$').move_to([3.5/2, -3, 0]).set_color('BLUE').scale(0.8)
        p2_text = Tex('$P_2 = (x_2, y_2)$').move_to([3.5 + 3.5/2, -3, 0]).set_color('RED').scale(0.8)

        empecemos[0][56:66].set_color('BLUE')
        empecemos[0][67:77].set_color('RED')

        ax = Axes(
            x_range=[-3, 10, 1],
            y_range=[-3, 10, 1],
            x_length = 6,
            y_length = 6,
        ).move_to([-3.8, -0.75, 0])

        labels = ax.get_axis_labels(Tex("$x$"), Tex("$y$"))

        x1 = ValueTracker(2)
        x2 = ValueTracker(7)

        P1 = always_redraw(lambda: Dot(ax.coords_to_point(x1.get_value(), x1.get_value()-1), color='BLUE'))
        P2 = always_redraw(lambda: Dot(ax.coords_to_point(x2.get_value(), x2.get_value()-1), color='RED'))

        self.play(ReplacementTransform(pero, empecemos), Create(ax), Write(labels), Create(P1), Create(P2), Write(p1_text), Write(p2_text), Unwrite(idea), run_time = 1)
        self.wait(tiempo_entre_videos-1)

        ##########? Aparición de theta

        observacion_theta = Tex('Podemos observar la existencia de un ángulo que llamaremos $\\theta$, donde $tan (\\theta) = \\frac{y_2 - y_1}{x_2 - x_1}$').move_to([0, 3, 0]).scale(0.8)

        recta = ax.plot(lambda x: x-1, color='green', x_range=ax.x_range).set_opacity(0)

        secante = ax.get_secant_slope_group(
            x=x1.get_value(),
            graph=recta,
            dx=x2.get_value()-x1.get_value(),
            dx_label=Tex('$x_2 - x_1$'),
            dy_label=Tex('$y_2 - y_1$'),
            dx_line_color='YELLOW',
            dy_line_color='PURPLE',
            include_secant_line=False
        )

        secante.add_updater(lambda m: m.become(ax.get_secant_slope_group(
            x=x1.get_value(),
            graph=recta,
            dx=x2.get_value()-x1.get_value(),
            dx_label=Tex('$x_2 - x_1$').scale(0.8),
            dy_label=Tex('$y_2 - y_1$').scale(0.8),
            dx_line_color='GREEN',
            dy_line_color='PURPLE',
            include_secant_line=False
        )))

        theta = always_redraw(lambda: Arc(1, start_angle=0, angle=np.arctan(1), arc_center=P1.get_center()).set_color('YELLOW'))

        theta_text = always_redraw(lambda: Tex('$\\theta$').scale(0.8).move_to(theta.get_center() + np.array([0.33, 0.2, 0])))

        formula = Tex('$tan(\\theta) = \\frac{y_2 - y_1}{x_2 - x_1}$').move_to([3.5, 1.5, 0])

        self.play(ReplacementTransform(empecemos, observacion_theta), Create(recta), Create(secante), Create(theta), Write(theta_text), Write(formula), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? Movemos el segundo punto

        movemos_segundo_punto = Tex('¿Qué sucede si movemos el segundo punto de manera tal que el ángulo no cambie? Si hacemos eso, podremos notar que todas las posibles ubicaciones de $(x_2, y_2)$ formarán una recta, es justamente el gráfico de una función lineal').move_to([0, 3.25, 0]).scale(0.7)

        self.play(ReplacementTransform(observacion_theta, movemos_segundo_punto), run_time = 1)
        self.wait(tiempo_entre_videos)

        self.play(x2.animate.set_value(9), recta.animate.set_opacity(1), run_time = 0.33)
        self.wait(0.67)

        self.play(x2.animate.set_value(7), run_time = 0.33)
        self.wait(0.67)

        self.play(x2.animate.set_value(3), run_time = 0.33)
        self.wait(0.67)

        self.play(x2.animate.set_value(8), run_time = 0.33)
        self.wait(0.67)

        self.play(x2.animate.set_value(4), run_time = 0.33)
        self.wait(0.67)

        self.play(x2.animate.set_value(6), run_time = 0.33)
        self.wait(0.67)

        self.play(x2.animate.set_value(10), run_time = 0.33)
        self.wait(0.67)

        self.play(x2.animate.set_value(7), run_time = 0.33)
        self.wait(0.67)

        self.wait(tiempo_entre_videos)

        ##########? Definimos m

        definimos_m = Tex('Como el ángulo $\\theta$ es constante, la igualdad se mantiene sin importar cuáles dos puntos elijamos, lo que nos anima a definir este valor constante especial como $m$').move_to([0, 3, 0]).scale(0.75)

        m = Tex('$m = \\frac{y_2 - y_1}{x_2 - x_1}$').move_to([3.5, 0, 0])

        self.play(ReplacementTransform(movemos_segundo_punto, definimos_m), Write(m), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? Reemplazar el segundo punto por uno genérico y obtener la fórmula

        self.play(Unwrite(formula), m.animate.move_to(np.array([3.5, 1.5, 0])), Uncreate(theta), Unwrite(theta_text), run_time = 1)
        self.wait(tiempo_entre_videos-3)

        obtenemos_formula = Tex('Esto quiere decir que poderíamos simplemente reescribir al punto $(x_2, y_2)$ como $(x, y)$, ya que vale para cualquier punto de la recta').move_to([0, 3, 0]).scale(0.8)

        m2 = Tex('$m = \\frac{y - y_1}{x - x_1}$').move_to([3.5, 0, 0])

        self.play(ReplacementTransform(definimos_m, obtenemos_formula), ReplacementTransform(m.copy(), m2), run_time = 1)
        self.wait(tiempo_entre_videos)

        obtenemos = Tex('Acabamos de hallar la fórmula de una función lineal que pasa por el punto $(x_1, y_1)$ y tiene pendiente $m$.').move_to([0, 3, 0]).scale(0.8)

        formula = Tex('$y = m (x-x_1) + y_1$').move_to([3.5, -1.5, 0])

        box_formula = SurroundingRectangle(formula, color='YELLOW', buff = 0.1)

        self.play(ReplacementTransform(obtenemos_formula, obtenemos), ReplacementTransform(m2.copy(), formula), Create(box_formula), run_time = 1)
        self.wait(tiempo_entre_videos)

        self.play(Unwrite(m), Unwrite(m2), Uncreate(box_formula), formula.animate.move_to(np.array([3.5, 1.5, 0])), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? Obtener el caso particular donde y = mx + b

        obs = Tex('En particular, si $x_1 = 0$, entonces el punto estará posicionado sobre el eje vertical, lo que implica que su segunda coordenada $y_1$ será el valor donde la función se cruza con el eje vertical (valor conocido como ordenada al origen)').move_to([0, 3.25, 0]).scale(0.7)

        formulax1_0 = Tex('$y = m (x-0) + y_1$').move_to([3.5, 0.5, 0])

        self.play(ReplacementTransform(obtenemos, obs), x1.animate.set_value(0), ReplacementTransform(formula.copy(), formulax1_0), run_time = 1)
        self.wait(tiempo_entre_videos-1)

        formulax1_02 = Tex('$y = mx + y_1$').move_to([3.5, -0.5, 0])

        self.play(ReplacementTransform(formulax1_0.copy(), formulax1_02), run_time = 1)
        self.wait(tiempo_entre_videos-1)

        definir_b = Tex('Este valor especial de $y_1$ nos incita a renombrarlo de otra manera, como por ejemplo $b$, obteniendo así la fórmula que queríamos obtener').move_to([0, 3, 0]).scale(0.8)

        formula_final = Tex('$y = mx + b$').move_to([3.5, -1.5, 0])

        box_formula_final = SurroundingRectangle(formula_final, color='YELLOW', buff = 0.1)

        self.play(ReplacementTransform(obs, definir_b), ReplacementTransform(formulax1_02.copy(), formula_final), Create(box_formula_final), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? Ejemplo

        ejemplo = Tex('Hagamos un ejemplo para que quede claro. Grafiquemos $y = -\\frac{3}{4}x + 5$. Sabemos que la ordenada al origen $b$ es $5$, por lo tanto el punto $(0, 5)$ pertenece a la recta.').scale(0.8).move_to([0, 3, 0])

        ejercicio_formula = Tex('$y = -\\frac{3}{4}x + 5$').move_to([3.5, 0, 0])

        P3 = Dot(ax.coords_to_point(0, 5), color='BLUE')

        self.play(ReplacementTransform(definir_b, ejemplo), ReplacementTransform(formula_final, ejercicio_formula), Create(P3), Uncreate(recta), Uncreate(secante), Uncreate(P1), Uncreate(P2), Unwrite(formula), Unwrite(formulax1_0), Unwrite(formulax1_02), Uncreate(box_formula_final), Unwrite(p1_text), Unwrite(p2_text), run_time = 1)
        self.wait(tiempo_entre_videos)

        obs_m = Tex('Por otro lado, la pendiente $m$ es $-\\frac{3}{4}$. Recordemos que $m = \\frac{y_2 - y_1}{x_2 - x_1}$ donde $(x_1, y_1)$ y $(x_2, y_2)$ son dos puntos de la recta. Esto nos quiere decir que si nos posicionamos en el primer punto y nos desplazamos 4 unidades a la derecha y descendemos 3, encontraremos otro punto').scale(0.8).move_to([0, 3, 0])

        P4 = Dot(ax.coords_to_point(4, 2), color='RED')

        recta = ax.plot(lambda x: (-3/4)*x+5, color='green', x_range=ax.x_range).set_opacity(0)

        secante = ax.get_secant_slope_group(
            x=0,
            graph=recta,
            dx=4,
            dx_label=Tex('$4$'),
            dy_label=Tex('$-3$'),
            dx_line_color='YELLOW',
            dy_line_color='PURPLE',
            include_secant_line=False
        )

        self.play(ReplacementTransform(ejemplo, obs_m), Create(P4), Create(secante), run_time = 1)
        self.wait(tiempo_entre_videos+2)

        terminamos = Tex('Ya con estos dos únicos puntos podemos trazar el gráfico, finalizando así este simple ejercicio').scale(0.8).move_to([0, 3, 0])

        self.play(ReplacementTransform(obs_m, terminamos), Create(recta), recta.animate.set_opacity(1), run_time = 1)
        self.wait(tiempo_entre_videos)
