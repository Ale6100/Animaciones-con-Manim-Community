from manim import *

class fermat_en_r(Scene):
    def construct(self):
        tiempo_entre_videos = 5
#        grid = NumberPlane() # La grilla es muy útil cuando estás editando el video
#        self.add(grid)
        titulo = Tex('Demostración del Teorema de Fermat en $\mathbb{R}$').move_to(np.array([0, 0, 0]))
        self.play(Write(titulo), run_time = 1)
        self.wait(tiempo_entre_videos-1)

        ##########? Agrega el enunciado

        enunciado = Tex('Si $f:[a, b] \\rightarrow \mathbb{R}$ es derivable en $(a, b)$ y $P\in(a, b)$ es un extremo local de $f$, entonces $f\'(P) = 0$').scale(0.8)
        self.play(Transform(titulo, enunciado), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? Agrega el inicio de la demostración

        demostracion = Tex('Queremos probar que  $f\'(P) = 0$. Iniciemos suponiendo que $P$ es un máximo local. En dicho caso existe un entorno $A = (P - \\varepsilon, P + \\varepsilon)$ de $P$ tal que $f(x) \\leqslant f(P) ~ \\forall ~ x \\in A$. Busquemos $f\'(P)$ mediante límites laterales').scale(0.75)
        self.play(Transform(titulo, demostracion), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? Aparecen los límites, se mueve la observación para arriba y aparece el gráfico con la función

        axes = Axes(x_range=[0, 7, 1], y_range=[0, 11, 1])
        f_grafico = axes.plot(lambda x: -(x-4)**2 + 10, color=BLUE)
        plot = VGroup(axes, f_grafico).move_to(np.array([3.5, -2.75, 0])).scale(0.5)
        limite_por_izquierda = Tex('$\\lim\\limits_{t \\to 0^-} \\frac{f(P+t) - f(P)}{t} = $ ?').move_to(np.array([-4.5, -0.5, 0]))
        limite_por_derecha = Tex('$\\lim\\limits_{t \\to 0^+} \\frac{f(P+t) - f(P)}{t} = $ ?').move_to(np.array([-4.5, -2.5, 0]))
        self.play(Write(limite_por_izquierda), Write(limite_por_derecha), titulo.animate.move_to(np.array([0, 2.75, 0])), Create(plot), run_time = 2)
        self.wait(tiempo_entre_videos-2)

        ##########? Agrega rectángulos en los símbolos "e"

        index_epsilon1 = 96
        index_epsilon2 = 100

        framebox1 = SurroundingRectangle(titulo[0][index_epsilon1], buff = 0.1)
        framebox2 = SurroundingRectangle(titulo[0][index_epsilon2], buff = 0.1)
        self.play(Create(framebox1), Create(framebox2), run_time = 1)
        self.wait(tiempo_entre_videos-4)

        ##########? Mueve los "e", hace aparecer dos observaciones, colorea cosas, y borra los rectángulos

        e1 = titulo[0][index_epsilon1].copy()
        e2 = titulo[0][index_epsilon2].copy()
        pos_aclaracion = np.array([2.5, 1, 0])
        aclaracion1 = Tex('$\\approx 0$ y positivo, por lo tanto $P-\\varepsilon$ es análogo a $P+t$ cuando $t \\rightarrow 0^-$').move_to(pos_aclaracion).scale(0.5)
        aclaracion2 = Tex('$\\approx 0$ y positivo, por lo tanto $P+\\varepsilon$ es análogo a $P+t$ cuando $t \\rightarrow 0^+$').next_to(aclaracion1, np.array([0, -0.5, 0])).scale(0.5)
        aclaracion1[0][22:25].set_color(YELLOW)
        aclaracion1[0][36:39].set_color(GREEN)
        aclaracion2[0][22:25].set_color(RED)
        aclaracion2[0][36:39].set_color(BLUE)
        self.play(Uncreate(framebox1), Uncreate(framebox2), e1.animate.next_to(aclaracion1, np.array([-0.35, 0, 0])).scale(2/3), e2.animate.next_to(aclaracion2, np.array([-0.35, 0, 0])).scale(2/3), Write(aclaracion1), Write(aclaracion2), limite_por_derecha[0][9:12].animate.set_color(BLUE), limite_por_izquierda[0][9:12].animate.set_color(GREEN), titulo[0][index_epsilon1-2:index_epsilon1+1].animate.set_color(YELLOW), titulo[0][index_epsilon2-2:index_epsilon2+1].animate.set_color(RED), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? Agrega los puntos, líneas, y texto en el gráfico

        def f(x): #Uso una función igual a la escrita en la línea 28
            return -(x-4)**2 + 10

        linea_vertical_P = axes.get_vertical_line(axes.i2gp(4, f_grafico))
        coordenadas_punto_P = [axes.coords_to_point(4, f(4))]
        punto_P = Dot(point=coordenadas_punto_P)
        label_P = axes.get_graph_label(f_grafico, 'f(P)').set_color(WHITE).move_to(np.array([4, -0.4, 0])).scale(0.5)

        linea_vertical_P_menos_e = axes.get_vertical_line(axes.i2gp(3, f_grafico))
        coordenadas_punto_P_menos_e = [axes.coords_to_point(3, f(3))]
        punto_P_menos_e = Dot(point=coordenadas_punto_P_menos_e)
        label_P_menos_e = axes.get_graph_label(f_grafico, 'f(P - \\varepsilon)').set_color(WHITE).move_to(np.array([2.9, -0.7, 0])).scale(0.5)
        label_P_menos_e[0][2:-1].set_color(YELLOW)

        linea_vertical_P_mas_e = axes.get_vertical_line(axes.i2gp(5, f_grafico))
        coordenadas_punto_P_mas_e = [axes.coords_to_point(5, f(5))]
        punto_P_mas_e = Dot(point=coordenadas_punto_P_mas_e)
        label_P_mas_e = axes.get_graph_label(f_grafico, 'f(P + \\varepsilon)').set_color(WHITE).move_to(np.array([5.1, -0.7, 0])).scale(0.5)
        label_P_mas_e[0][2:-1].set_color(RED)

        lineas = VGroup(linea_vertical_P, linea_vertical_P_menos_e, linea_vertical_P_mas_e)
        puntos = VGroup(punto_P, punto_P_menos_e, punto_P_mas_e)
        labels = VGroup(label_P, label_P_menos_e, label_P_mas_e)
        self.play(Create(lineas), Create(puntos), Create(labels), run_time = 2)
        self.wait(tiempo_entre_videos-3)

        ##########? Agrega un óvalo y la letra A rosa

        index_a = 91
        A = titulo[0][index_a].copy()
        ovalo = Ellipse(width=2.0, height=1, color=PINK).move_to(np.array([4, -3.4, 0]))
        self.play(Create(ovalo), titulo[0][index_a].animate.set_color(PINK), A.animate.next_to(ovalo, np.array([0.6, 0.05, 0])).set_color(PINK))
        self.wait(tiempo_entre_videos)

        ##########? Transforma las observaciones en otras

        aclaracion3 = Tex('Como $f(P+\\varepsilon) \\leqslant f(P)$, y $f(P-\\varepsilon) \\leqslant f(P)$, se debe cumplir que').move_to(aclaracion1).scale(0.5)
        aclaracion4 = Tex('$f(P+t) \\leqslant f(P)$ cuando $t \\to 0^+$ y $t \\to 0^-$').move_to(aclaracion2).scale(0.5)
        self.play(FadeOut(e1, e2), Transform(aclaracion1, aclaracion3), Transform(aclaracion2, aclaracion4), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? Transforma las observaciones en otras

        aclaracion5 = Tex('por lo tanto, $f(P+t) - f(P) \\leqslant 0$').move_to(aclaracion2).scale(0.5)
        self.play(Transform(aclaracion1, aclaracion5), aclaracion2.animate.move_to(pos_aclaracion), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? Agrega una igualdad más a los límites, cambia las observaciones, borra el gráfico y quita los colores

        menor_a_cero1 = aclaracion1[0][-3:].copy()
        menor_a_cero2 = aclaracion1[0][-3:].copy()
        aclaracion6 = Tex('$= \\frac{"algo~menor~o~igual~a~cero"}{?}$').move_to(np.array([0.9, -2.42, 0]))
        aclaracion7 = Tex('$= \\frac{"algo~menor~o~igual~a~cero"}{?}$').move_to(np.array([0.9, -0.42, 0]))
        self.play(FadeOut(puntos, labels, plot, ovalo, A, lineas), Transform(menor_a_cero1, aclaracion6), Transform(menor_a_cero2, aclaracion7), limite_por_derecha[0][9:12].animate.set_color(WHITE), limite_por_izquierda[0][9:12].animate.set_color(WHITE), titulo[0][:].animate.set_color(WHITE))
        self.wait(tiempo_entre_videos)

        ##########? Cambia observaciones

        aclaracion8 = Tex('Por otro lado, $ t > 0$ cuando $t \\to 0^+$').move_to(aclaracion2).scale(0.5)
        aclaracion9 = Tex('mientras que $ t < 0$ cuando $t \\to 0^-$').move_to(aclaracion1).scale(0.5)
        self.play(Transform(aclaracion2, aclaracion8), Transform(aclaracion1, aclaracion9))
        self.wait(tiempo_entre_videos)

        ##########? Intercambia un denominador por otro en el primer límite

        mayor_a_cero1 = aclaracion2[0][23:29].copy()
        nuevo_denominador1 = Tex('$"algo~mayor~a~cero"$').move_to(menor_a_cero1[0][-1]).scale(0.725)
        self.remove(menor_a_cero1[0][-1])
        self.play(Transform(mayor_a_cero1, nuevo_denominador1))
        self.wait(tiempo_entre_videos-4)

        ##########? Intercambia un denominador por otro en el segundo límite

        menor_a_cero3 = aclaracion1[0][22:28].copy()
        nuevo_denominador2 = Tex('$"algo~menor~a~cero"$').move_to(menor_a_cero2[0][-1]).scale(0.725)
        self.remove(menor_a_cero2[0][-1])
        self.play(Transform(menor_a_cero3, nuevo_denominador2))
        self.wait(tiempo_entre_videos)

        ##########?

        desigualdad_limite_derecha = Tex('$\\leqslant 0$').move_to(np.array([-1.62, -2.42, 0]))
        for i in range(len(menor_a_cero1[0])):
            self.remove(menor_a_cero1[0][i])
        self.remove(mayor_a_cero1)
        aclaracion6_modificado = Tex('$= \\frac{"algo~menor~o~igual~a~cero"}{"algo~mayor~a~cero"}$').move_to(np.array([0.9, -2.42, 0]))
        self.play(Transform(aclaracion6_modificado, desigualdad_limite_derecha))
        self.wait(tiempo_entre_videos-4)

        ##########?

        desigualdad_limite_izquierda = Tex('$\\geqslant 0$').move_to(np.array([-1.62, -0.42, 0]))
        for i in range(len(menor_a_cero2[0])):
            self.remove(menor_a_cero2[0][i])
        self.remove(menor_a_cero3)
        aclaracion7_modificado = Tex('$= \\frac{"algo~menor~o~igual~a~cero"}{"algo~menor~a~cero"}$').move_to(np.array([0.9, -0.42, 0]))
        self.play(Transform(aclaracion7_modificado, desigualdad_limite_izquierda))
        self.wait(tiempo_entre_videos-2)

        ##########? Hace aparecer un límite

        copia1 = aclaracion6_modificado.copy()
        copia2 = aclaracion7_modificado.copy()
        derivada = Tex('$\\Rightarrow \\lim\\limits_{t \\to 0} \\frac{f(P+t) - f(P)}{t} = 0$').move_to(np.array([2, -1.5, 0]))
        self.play(Transform(copia1, derivada), Transform(copia2, derivada))
        self.wait(tiempo_entre_videos)

        ##########? Cambia las observaciones

        recordatorio1 = Tex('Pero recordemos que $\\lim\\limits_{t \\to 0} \\frac{f(P+t) - f(P)}{t} = f\'(P)$').move_to(pos_aclaracion).scale(0.75)
        recordatorio2 = Tex('por lo tanto:').next_to(recordatorio1, np.array([0, -0.1, 0])).scale(0.75)
        self.play(FadeOut(copia2), Transform(aclaracion2, recordatorio1), Transform(aclaracion1, recordatorio2))
        self.wait(tiempo_entre_videos-4)

        ##########? Agrega una igualdad al lado del último límite creado

        derivada_agregado = Tex('$= f\'(P)$').move_to(np.array([5.5, -1.47, 0]))    
        self.play(Write(derivada_agregado), run_time = 4)
        self.wait(tiempo_entre_videos)

        ##########? Borra todo y escribe algo nuevo

        self.clear()
        nuevo_texto = Tex('Acabamos de probar que si $P$ es un máximo local, entonces $f\'(P) = 0$').move_to(np.array([0, 1, 0])).scale(0.75)
        self.play(Write(nuevo_texto), run_time = 2)
        self.wait(tiempo_entre_videos-2)

        ##########?

        nuevo_texto2 = Tex('Análogamente se puede probar que si $P$ es un mínimo local, entonces también $f\'(P) = 0$, considerando que en dicho caso existe un entorno $B = (P - \\varepsilon, P + \\varepsilon)$ de $P$ tal que $f(x) \\geqslant f(P) ~ \\forall ~ x \\in B$').move_to(np.array([0, -1, 0])).scale(0.75)
        self.play(Write(nuevo_texto2), run_time = 3)
        self.wait(tiempo_entre_videos-1)

        ##########?

        self.clear()
        nuevo_texto4 = Tex('Ya se probó que si $P$ es un extremo local de $f$, entonces $f\'(P) = 0$, por lo tanto se puede dar por demostrado el teorema').scale(0.8)
        self.play(Write(nuevo_texto4), run_time = 2)
        self.wait(tiempo_entre_videos)
