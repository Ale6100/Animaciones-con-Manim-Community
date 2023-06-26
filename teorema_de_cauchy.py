from manim import *

class cauchy(Scene):
    def construct(self):
        tiempo_entre_videos = 5
#        grid = NumberPlane()
#        self.add(grid)
        titulo = Tex('Demostración del Teorema de Cauchy').scale(1.5)
        self.play(Write(titulo), run_time = 1)
        self.wait(tiempo_entre_videos-1)

        ##########? Agrega el enunciado

        enunciado = Tex('Si $f$ y $g$ son funciones continuas en $[a, b]$ y derivables en $(a, b)$, entonces $\\exists~c \\in (a, b)$ tal que $f\'(c)(g(b) - g(a)) = g\'(c)(f(b) - f(a))$').scale(0.8)
        colores1, colores2 = [2, 74, 97, 102], [4, 80, 85, 91]
        for i in range(4):
            enunciado[0][colores1[i]].set_color(BLUE)
            enunciado[0][colores2[i]].set_color(RED)
        self.play(Transform(titulo, enunciado), run_time = 1)
        self.wait(tiempo_entre_videos+1)

        ##########? Agrega el inicio de la demostración y un gráfico

        demostracion = Tex('Iniciemos definiendo la función auxiliar $h(x) = (f(x) - f(a))(g(b) - g(a)) - (g(x) - g(a))(f(b) - f(a))$').move_to(np.array([0, 0.01, 0]))
        nota = Tex('Nota: observar que $h(x)$ tiene una estructura muy similar a la expresión que queremos hallar').scale(0.4).move_to(np.array([-2.9, -2, 0]))
        colores3, colores4 = [42, 47, 76, 81], [53, 58, 65, 70]
        for i in range(4):
            demostracion[0][colores3[i]].set_color(BLUE)
            demostracion[0][colores4[i]].set_color(RED)
        self.play(Transform(titulo, demostracion), Write(nota), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########?
        index_desplazado = 36
        
        demo_recortada = demostracion[0][index_desplazado:].copy()
        observacion1 = Tex('Observemos que').move_to(np.array([0, 2, 0]))
        observacion2 = Tex('$h(a) = (f(a) - f(a))(g(b) - g(a)) - (g(a) - g(a))(f(b) - f(a)) = 0$').move_to(np.array([0, 1, 0])).scale(0.9)
        observacion3 = Tex('$h(b) = (f(b) - f(a))(g(b) - g(a)) - (g(b) - g(a))(f(b) - f(a)) = 0$').move_to(np.array([0, 0.01, 0])).scale(0.9)
        for i in range(4):
            observacion2[0][colores3[i]-index_desplazado].set_color(BLUE)
            observacion3[0][colores3[i]-index_desplazado].set_color(BLUE)
            observacion2[0][colores4[i]-index_desplazado].set_color(RED)
            observacion3[0][colores4[i]-index_desplazado].set_color(RED)
        observaciones = VGroup(observacion1, observacion2, observacion3)
        self.play(demo_recortada.animate.move_to(np.array([0, 3, 0])), Write(observaciones), FadeOut(titulo, nota))
        self.wait(tiempo_entre_videos)

        ##########?

        h_a_b = Tex('$\\Rightarrow h(a) = h(b)$').move_to(np.array([0, -1, 0]))
        self.play(Write(h_a_b))
        self.wait(tiempo_entre_videos-3)

        ##########?

        cumple_rolle = Tex('considerando esto último y que por álgebra de funciones continuas y derivables, $h$ es continua en $[a, b]$ y derivable en $(a, b)$, podemos afirmar que se cumplen las hipótesis del teorema de Rolle').scale(0.8).move_to(np.array([0, -2, 0]))
        self.play(Write(cumple_rolle))
        self.wait(tiempo_entre_videos)

        ##########?

        es_decir = Tex('Es decir, $\\exists~c \\in (a, b)$ tal que $h\'(c) = 0$. Sabiendo esto:').move_to(np.array([0, 3, 0]))
        self.play(Transform(cumple_rolle, es_decir), FadeOut(observaciones, h_a_b), demo_recortada.animate.move_to(np.array([0, 2, 0])))
        self.wait(tiempo_entre_videos-3)

        ##########?

        demo_recortada2 = demo_recortada[0].copy()
        h_derivada = Tex('$h\'(x) = f\'(x)(g(b) - g(a)) - g\'(x)(f(b) - f(a))$').move_to(np.array([0, 1, 0]))
        for i in range(3):
            h_derivada[0][colores1[1:][i]-68].set_color(BLUE)
            h_derivada[0][colores2[1:][i]-68].set_color(RED)
        self.play(Transform(demo_recortada2, h_derivada))
        self.wait(tiempo_entre_videos-3)

        ##########?

        h_derivada_copia = h_derivada[0].copy()
        h_derivada_evaluada = Tex('$h\'(c) = f\'(c)(g(b) - g(a)) - g\'(c)(f(b) - f(a)) = 0$').move_to(np.array([0, 0.1, 0]))
        for i in range(3):
            h_derivada_evaluada[0][colores1[1:][i]-68].set_color(BLUE)
            h_derivada_evaluada[0][colores2[1:][i]-68].set_color(RED)
        self.play(Transform(h_derivada_copia, h_derivada_evaluada))
        self.wait(tiempo_entre_videos-3)

        ##########?

        finalmente = Tex('reorganizando la expresión se llega a').move_to(np.array([0, -1, 0]))
        self.play(Write(finalmente))
        self.wait(tiempo_entre_videos-4)

        ##########?

        demostrado = Tex('$f\'(c)(g(b) - g(a)) = g\'(c)(f(b) - f(a))$').move_to(np.array([0, -2, 0]))

        for i in range(3):
            demostrado[0][colores1[1:][i]-74].set_color(BLUE)
            demostrado[0][colores2[1:][i]-74].set_color(RED)
        framebox = SurroundingRectangle(demostrado[0], buff = 0.1)
        self.play(Write(demostrado), Create(framebox), run_time = 3)
        self.wait(tiempo_entre_videos-4)

        ##########?

        listo = Tex('finalizando así la demostración del teorema').move_to(np.array([0, -3, 0]))
        self.play(Write(listo))
        self.wait(tiempo_entre_videos)
