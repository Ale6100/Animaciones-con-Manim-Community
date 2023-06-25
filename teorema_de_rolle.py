from manim import *

class rolle(Scene):
    def construct(self):
        tiempo_entre_videos = 5
#        grid = NumberPlane()
#        self.add(grid)
        titulo = Tex('Demostración del Teorema de Rolle').move_to(np.array([0, 0.1, 0])).scale(1.5)

        self.play(Write(titulo), run_time = 1)
        self.wait(tiempo_entre_videos-1)

        ######################################################################? Agrega el enunciado

        enunciado = Tex('Si $f:[a, b] \\rightarrow \mathbb{R}$ es continua en $[a, b]$, derivable en $(a, b)$, y además $f(a) = f(b)$, entonces $\\exists~c \\in (a, b)$ tal que $f\'(c) = 0$').scale(0.75)
        self.play(Transform(titulo, enunciado), run_time = 1)
        self.wait(tiempo_entre_videos)

        ######################################################################? Agrega el inicio de la demostración y un gráfico

        demostracion = Tex('Si $f$ es constante, entonces $f\'(x) = 0 ~\\forall~ x \\in (a, b)$, por lo tanto $c$ puede ser cualquier valor en $(a, b)$').scale(0.75).move_to(np.array([0, 2, 0]))

        axes = Axes(x_range=[0, 8, 1], y_range=[0, 8, 1])
        f_grafico = axes.plot(lambda x: 5, color=BLUE)
        plot = VGroup(axes, f_grafico).scale(0.75).move_to(np.array([0, -1, 0]))
        def f(x):
            return 5

        linea_vertical_izquierda = axes.get_vertical_line(axes.i2gp(1, f_grafico))
        linea_vertical_derecha = axes.get_vertical_line(axes.i2gp(7, f_grafico))
        linea_vertical_c = axes.get_vertical_line(axes.i2gp(5, f_grafico))

        coordenadas_punto_izquierda = [axes.coords_to_point(1, f(1))]
        punto_izquierda = Dot(point=coordenadas_punto_izquierda).set_color(RED)

        coordenadas_punto_derecha = [axes.coords_to_point(7, f(7))]
        punto_derecha = Dot(point=coordenadas_punto_derecha).set_color(RED)

        coordenadas_punto_c = [axes.coords_to_point(5, f(5))]
        punto_c = Dot(point=coordenadas_punto_c).set_color(GREEN)

        label_f = axes.get_graph_label(f_grafico, 'f(x)').scale(0.75)
        label_punto_izquierda = axes.get_graph_label(f_grafico, 'f(a)').move_to(np.array([-3.3, 0, 0])).set_color(RED).scale(0.75)
        label_punto_derecha = axes.get_graph_label(f_grafico, 'f(b)').move_to(np.array([3.4, 0, 0])).set_color(RED).scale(0.75)
        label_punto_c = axes.get_graph_label(f_grafico, 'f(c)').move_to(np.array([1.2, 0, 0])).set_color(GREEN).scale(0.75)

        lineas = VGroup(linea_vertical_izquierda, linea_vertical_derecha, linea_vertical_c)
        puntos = VGroup(punto_izquierda, punto_derecha, punto_c)
        labels = VGroup(label_f, label_punto_izquierda, label_punto_derecha, label_punto_c)

        self.play(Transform(titulo, demostracion), Create(plot), Create(lineas), Create(puntos), Create(labels), run_time = 2)
        self.wait(tiempo_entre_videos-1)

        ######################################################################? Reemplaza el inicio de la demostración por otro texto, transforma un gráfico en otro y crea uno nuevo

        demostracion2 = Tex('Si $f$ no es constante, entonces como $f$ es continua en un compacto $[a, b]$, por el teorema de Weierstrass sabemos que $f$ tiene máximo y mínimo en dicho compacto, y como $f(a) = f(b)$, por lo menos un extremo está en $(a, b)$. Observamos que se cumplen las hipótesis del Teorema de Fermat, por lo tanto $\\exists~c \\in (a, b)$ tal que $f\'(c) = 0$').move_to(np.array([0, 2.25, 0])).scale(0.8)

        axes2 = Axes(x_range=[0, 8, 1], y_range=[0, 10, 1])
        f_grafico2 = axes2.plot(lambda x: -(x-4)**2 + 10, color=BLUE)
        plot2 = VGroup(axes2, f_grafico2).scale(0.55).move_to(np.array([-3.5, -2.5, 0]))
        def f2(x):
            return -(x-4)**2 + 10

        linea_vertical_izquierda2 = axes2.get_vertical_line(axes2.i2gp(1, f_grafico2))
        linea_vertical_derecha2 = axes2.get_vertical_line(axes2.i2gp(7, f_grafico2))
        linea_vertical_c2 = axes2.get_vertical_line(axes2.i2gp(4, f_grafico2))

        coordenadas_punto_izquierda2 = [axes2.coords_to_point(1, f2(1))]
        punto_izquierda2 = Dot(point=coordenadas_punto_izquierda2).set_color(RED)

        coordenadas_punto_derecha2 = [axes2.coords_to_point(7, f2(7))]
        punto_derecha2 = Dot(point=coordenadas_punto_derecha2).set_color(RED)

        coordenadas_punto_c2 = [axes2.coords_to_point(4, f2(4))]
        punto_c2 = Dot(point=coordenadas_punto_c2).set_color(GREEN)

        label_f2 = axes2.get_graph_label(f_grafico2, 'f(x)').move_to(np.array([-1.5, -0.9, 0])).scale(0.75)
        label_punto_izquierda2 = axes2.get_graph_label(f_grafico2, 'f(a)').move_to(np.array([-6.25, -2.5, 0])).set_color(RED).scale(0.75)
        label_punto_derecha2 = axes2.get_graph_label(f_grafico2, 'f(b)').move_to(np.array([-0.7, -2.5, 0])).set_color(RED).scale(0.75)
        label_punto_c2 = axes2.get_graph_label(f_grafico2, 'f(c)').move_to(np.array([-3.5, 0.5, 0])).set_color(GREEN).scale(0.75)

        lineas2 = VGroup(linea_vertical_izquierda2, linea_vertical_derecha2, linea_vertical_c2)
        puntos2 = VGroup(punto_izquierda2, punto_derecha2, punto_c2)
        labels2 = VGroup(label_f2, label_punto_izquierda2, label_punto_derecha2, label_punto_c2)

        axes3 = Axes(x_range=[0, 8, 1], y_range=[0, 10, 1])
        f_grafico3 = axes3.plot(lambda x: (x-4)**2 + 1, color=BLUE)
        plot3 = VGroup(axes3, f_grafico3).scale(0.55).move_to(np.array([3.5, -0.4225, 0]))
        def f3(x):
            return (x-4)**2 + 1

        linea_vertical_izquierda3 = axes3.get_vertical_line(axes3.i2gp(1, f_grafico3))
        linea_vertical_derecha3 = axes3.get_vertical_line(axes3.i2gp(7, f_grafico3))
        linea_vertical_c3 = axes3.get_vertical_line(axes3.i2gp(4, f_grafico3))

        coordenadas_punto_izquierda3 = [axes3.coords_to_point(1, f3(1))]
        punto_izquierda3 = Dot(point=coordenadas_punto_izquierda3).set_color(RED)

        coordenadas_punto_derecha3 = [axes3.coords_to_point(7, f3(7))]
        punto_derecha3 = Dot(point=coordenadas_punto_derecha3).set_color(RED)

        coordenadas_punto_c3 = [axes3.coords_to_point(4, f3(4))]
        punto_c3 = Dot(point=coordenadas_punto_c3).set_color(GREEN)

        label_f3 = axes3.get_graph_label(f_grafico3, 'f(x)').move_to(np.array([5, -2.5, 0])).scale(0.75)
        label_punto_izquierda3 = axes3.get_graph_label(f_grafico3, 'f(a)').move_to(np.array([1.55, 0.3, 0])).set_color(RED).scale(0.75)
        label_punto_derecha3 = axes3.get_graph_label(f_grafico3, 'f(b)').move_to(np.array([5.6, 0.3, 0])).set_color(RED).scale(0.75)
        label_punto_c3 = axes3.get_graph_label(f_grafico3, 'f(c)').move_to(np.array([3.55, -2.5, 0])).set_color(GREEN).scale(0.75)

        lineas3 = VGroup(linea_vertical_izquierda3, linea_vertical_derecha3, linea_vertical_c3)
        puntos3 = VGroup(punto_izquierda3, punto_derecha3, punto_c3)
        labels3 = VGroup(label_f3, label_punto_izquierda3, label_punto_derecha3, label_punto_c3)

        self.play(Transform(titulo, demostracion2), Transform(plot, plot2), Transform(lineas, lineas2), Transform(puntos, puntos2), Transform(labels, labels2), Create(plot3), Create(lineas3), Create(puntos3), Create(labels3), run_time = 2)
        self.wait(11)

        ######################################################################? Borra todo y pone un texto final

        self.clear()
        nuevo_texto = Tex('Acabamos de probar que $\\exists~c \\in (a, b)$ tal que $f\'(c) = 0$ para $f=cte$ como para $f \\ne cte$, por lo tanto damos por demostrado el teorema').move_to(np.array([0, 0.1, 0])).scale(0.75)
        self.play(Write(nuevo_texto), run_time = 1)
        self.wait(tiempo_entre_videos)
