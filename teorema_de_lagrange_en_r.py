from manim import *

class lagrange_en_r(Scene):
    def construct(self):
        tiempo_entre_videos = 5
        #grid = NumberPlane()
        #self.add(grid)
        titulo = Tex('Demostración del Teorema de Lagrange en $\mathbb{R}$').scale(1.25)
        self.play(Write(titulo), run_time = 1)
        self.wait(tiempo_entre_videos-1)

        ##########? #Agrega el enunciado

        enunciado = Tex('Si $f:[a, b] \\rightarrow \mathbb{R}$ es continua en $[a, b]$ y derivable en $(a, b)$, entonces $\\exists~c \\in (a, b)$ tal que $f\'(c) = \\frac{f(b) - f(a)}{b - a}$').scale(0.8)
        self.play(Transform(titulo, enunciado), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? #Agrega el inicio de la demostración y un gráfico

        demostracion = Tex('Iniciamos definiendo una función auxiliar $L: [a, b] \\rightarrow \mathbb{R}$ rectilínea que une $(a, f(a))$ con $(b, f(b))$: $L(x) = mx + p$. Observemos que la pendiente (la inclinación de la recta) $m$ debe ser $m = \\frac{f(b) - f(a)}{b - a}$').move_to(np.array([0, 2, 0])).scale(0.8)

        axes = Axes(x_range=[-1.5, 1.6, 0.5], y_range=[-1.5, 1.5, 0.5])
        f_grafico = axes.plot(lambda x: -x**4 + 2*(x**2), color=BLUE)
        L_grafico = axes.plot(lambda x: -0.281*x - 0.984, color=YELLOW)

        def f(x):
            return -x**4 + 2*(x**2)

        plot = VGroup(axes, f_grafico, L_grafico).move_to(np.array([0, -1.9, 0])).scale(0.6)

        coordenadas_punto_izquierda = [axes.coords_to_point(-1.5, f(-1.5))]
        punto_izquierda = Dot(point=coordenadas_punto_izquierda).set_color(RED)

        coordenadas_punto_derecha = [axes.coords_to_point(1.6, f(1.6))]
        punto_derecha = Dot(point=coordenadas_punto_derecha).set_color(RED)

        label_f = axes.get_graph_label(f_grafico, 'f(x)').move_to(np.array([3, -3, 0])).scale(0.8)
        label_L = axes.get_graph_label(L_grafico, 'L(x)').scale(0.8).move_to(np.array([-1.7, -3.2, 0])).set_color(YELLOW)
        label_punto_izquierda = axes.get_graph_label(f_grafico, 'f(a)').move_to(np.array([-3.6, -3, 0])).set_color(RED).scale(0.8)
        label_punto_derecha = axes.get_graph_label(f_grafico, 'f(b)').move_to(np.array([4.1, -3.5, 0])).set_color(RED).scale(0.8)

        puntos = VGroup(punto_izquierda, punto_derecha)
        labels = VGroup(label_punto_izquierda, label_punto_derecha, label_f, label_L)
        self.play(Transform(titulo, demostracion), Create(plot), Create(puntos), Create(labels), run_time = 2)
        self.wait(8)

        ##########?
        
        demostracion2 = Tex('Asociamos ambas funciones mediante $h(x) = f(x) - L(x)$').move_to(demostracion).scale(0.8)

        h_grafico = axes.plot(lambda x: (-x**4 + 2*(x**2)) - (-0.281*x - 0.984), color=GREEN)
        label_h = axes.get_graph_label(h_grafico, 'h(x)').scale(0.8)
        self.play(Transform(titulo, demostracion2), Create(h_grafico), Create(label_h), run_time = 2)
        self.wait(tiempo_entre_videos)

        ##########?
        
        h = demostracion2[0][-14:].copy()
        self.play(h.animate.move_to(np.array([-5.25, 3, 0])))
        self.wait(tiempo_entre_videos-3)

        ##########?
        
        h_copia1 = h.copy()
        h_a = Tex('$h(a) = f(a) - L(a) = 0$, ya que $f(a) = L(a)$').move_to(np.array([-4.06, 2, 0])).scale(0.6)

        h_copia2 = h.copy()
        h_b = Tex('$h(b) = f(b) - L(b) = 0$, ya que $f(b) = L(b)$').move_to(np.array([-4.09, 1, 0])).scale(0.6)

        observacion = Tex('Observamos que $h(a) = h(b)$').move_to(np.array([3.195, 3.25, 0])).scale(0.8)

        self.play(Transform(h_copia1, h_a), Transform(h_copia2, h_b), Transform(titulo, observacion))
        self.wait(tiempo_entre_videos)

        ##########?
        
        observacion2 = Tex('pero además $h$ es continua en $[a, b]$ y derivable en $(a, b)$').next_to(titulo, np.array([0, -0.5, 0])).scale(0.65)
        observacion3 = Tex('ya que $f$ y $L$ también, por lo tanto cumple con las').next_to(observacion2, np.array([0, -0.5, 0])).scale(0.65)
        observacion4 = Tex('hipótesis del teorema de Rolle').next_to(observacion3, np.array([0, -0.5, 0])).scale(0.65)
        self.play(Write(observacion2), Write(observacion3), Write(observacion4), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########?
        
        observacion5 = Tex('Es decir, $\\exists~c \\in (a, b)$ tal que $h\'(c) = 0$').move_to(np.array([0, 3, 0]))

        tangente1 = axes.plot(lambda x: 1.70812144299680, color=PINK)
        tangente2 = axes.plot(lambda x: 0.974112924733156, color=PINK)
        tangente3 = axes.plot(lambda x: 2.26976546511223, color=PINK)

        coordenadas_punto_c1 = [axes.coords_to_point(-0.9631631631631632, 1.70812144299680)]
        punto_c1 = Dot(point=coordenadas_punto_c1).set_color(TEAL)

        coordenadas_punto_c2 = [axes.coords_to_point(-0.07257257257257255, 0.974112924733156)]
        punto_c2 = Dot(point=coordenadas_punto_c2).set_color(TEAL)

        coordenadas_punto_c3 = [axes.coords_to_point(1.0321321321321322, 2.26976546511223)]
        punto_c3 = Dot(point=coordenadas_punto_c3).set_color(TEAL)

        label_tangente = axes.get_graph_label(f_grafico, 'Rectas~tangentes~en~h(c)').move_to(np.array([-5, 0, 0])).set_color(PINK).scale(0.5)
        label_punto_c = axes.get_graph_label(f_grafico, 'Puntos~h(c)').move_to(np.array([-5, -0.5, 0])).set_color(TEAL).scale(0.5)

        nota1 = Tex('Nota: Observar que nada impide que exista más de un').move_to(np.array([5, -0.12, 0])).scale(0.35)
        nota2 = Tex('punto $c$ que cumpla con la condición planteada').move_to(np.array([5, -0.25, 0])).scale(0.35)

        nuevos_puntos = VGroup(punto_c1, punto_c2, punto_c3)
        tangentes = VGroup(tangente1, tangente2, tangente3)
        nuevos_labels = VGroup(label_tangente, label_punto_c)

        self.play(Create(nuevos_puntos), Create(tangentes), Create(nuevos_labels), Transform(titulo, observacion5), FadeOut(h, h_copia1, h_copia2, observacion2, observacion3, observacion4), Write(nota1), Write(nota2), run_time = 2)
        self.wait(tiempo_entre_videos)

        ##########?
        
        h_derivada_busco = Tex('Sabiendo que $h\'(c) = 0$:').move_to(np.array([0, 3.5, 0])).scale(0.9)
        self.play(Transform(titulo, h_derivada_busco))
        self.wait(tiempo_entre_videos-2)

        ##########?
        
        h_derivada = Tex('$h(x) = f(x) - L(x)$').move_to(np.array([-5.5, 3, 0])).scale(0.7)
        self.play(Write(h_derivada))
        self.wait(tiempo_entre_videos-3)

        ##########?
        
        h_derivada_copia = h_derivada[0].copy()
        h_derivada2 = Tex('$h\'(x) = f\'(x) - L\'(x) = f\'(x) - m$').move_to(np.array([-4.38, 2, 0])).scale(0.7)
        self.play(Transform(h_derivada_copia, h_derivada2))
        self.wait(tiempo_entre_videos-3)

        ##########?
        
        h_derivada2_copia = h_derivada2[0].copy()
        h_derivada3 = Tex('$h\'(c) = f\'(c) - m = 0$').move_to(np.array([0, 3, 0])).scale(0.7)
        self.play(Transform(h_derivada2_copia, h_derivada3))
        self.wait(tiempo_entre_videos-3)

        ##########?
        
        h_derivada3_copia = h_derivada3[0][6:].copy()
        h_derivada4 = Tex('$f\'(c) = m$').move_to(np.array([0, 2, 0])).scale(0.7)
        self.play(Transform(h_derivada3_copia, h_derivada4))
        self.wait(tiempo_entre_videos-3)

        ##########?
        
        pero = Tex('Pero $m = \\frac{f(b) - f(a)}{b - a}$, por lo tanto').move_to(np.array([4.625, 2.9, 0])).scale(0.7)
        self.play(Write(pero))
        self.wait(tiempo_entre_videos-3)

        ##########?
        
        conclusion = Tex('$f\'(c) = \\frac{f(b) - f(a)}{b - a}$').move_to(np.array([3.75, 2, 0])).scale(0.8)
        framebox = SurroundingRectangle(conclusion[0], buff = 0.1)

        tangente1_2 = axes.plot(lambda x: 0.726422240322581 - 0.278611206451613*x, color=PINK)
        tangente2_2 = axes.plot(lambda x: -0.288761393548387*x - 0.0104503403225806, color=PINK)
        tangente3_2 = axes.plot(lambda x: 1.27397794225806 - 0.26957944516129*x, color=PINK)

        coordenadas_punto_c1_2 = [axes.coords_to_point(-0.9631631631631632, f(-0.9631631631631632))]
        punto_c1_2 = Dot(point=coordenadas_punto_c1_2).set_color(TEAL)

        coordenadas_punto_c2_2 = [axes.coords_to_point(-0.07257257257257255, f(-0.07257257257257255))]
        punto_c2_2 = Dot(point=coordenadas_punto_c2_2).set_color(TEAL)

        coordenadas_punto_c3_2 = [axes.coords_to_point(1.0321321321321322, f(1.0321321321321322))]
        punto_c3_2 = Dot(point=coordenadas_punto_c3_2).set_color(TEAL)

        label_tangente_2 = axes.get_graph_label(f_grafico, 'Rectas~tangentes~en~f(c)').move_to(label_tangente).set_color(PINK).scale(0.5)
        label_punto_c_2 = axes.get_graph_label(f_grafico, 'Puntos~f(c)').move_to(label_punto_c).set_color(TEAL).scale(0.5)

        nota3 = Tex('Nota: recordar que $f\'(c)$ es la pendiente de').move_to(nota1).scale(0.35)
        nota4 = Tex('la recta tangente al gráfico de $f$ en $c$').move_to(nota2).scale(0.35)

        nuevos_puntos_2 = VGroup(punto_c1_2, punto_c2_2, punto_c3_2)
        tangentes_2 = VGroup(tangente1_2, tangente2_2, tangente3_2)
        nuevos_labels_2 = VGroup(label_tangente_2, label_punto_c_2)

        self.play(Write(conclusion), Transform(nuevos_puntos, nuevos_puntos_2), Transform(tangentes, tangentes_2), Transform(nuevos_labels, nuevos_labels_2), Create(framebox), Transform(nota1, nota3), Transform(nota2, nota4), run_time = 5)
        self.wait(tiempo_entre_videos-3)

        ##########?
        
        demostrado = Tex('dicho esto, podemos dar por demostrado el teorema').move_to(np.array([3.6, 1.2, 0])).scale(0.6)
        self.play(Write(demostrado))
        self.wait(tiempo_entre_videos)
