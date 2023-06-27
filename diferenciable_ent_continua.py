from manim import *

class dif_cont(Scene):
    def construct(self):
        tiempo_entre_videos = 5
        # grid = NumberPlane() #La grilla es muy útil cuando estás editando el video
        # self.add(grid)
        titulo = Tex('Demostración: Si $f$ es diferenciable, entonces es continua')
        self.play(Write(titulo), run_time = 1)
        self.wait(tiempo_entre_videos-1)

        ##########?  #Agrega el enunciado

        enunciado = Tex('Enunciado: Sea $f: A \\subset \\mathbb{R}^n \\rightarrow \mathbb{R}$, $P \in A^o$. Si $f$ es diferenciable en $P$, entonces es continua en $P$').move_to(np.array([0, 0.1, 0])).scale(0.8)
        self.play(Transform(titulo, enunciado), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########?

        demostracion = Tex('Queremos probar que $f$ es continua en $P$. Es decir, que $f(x) \\rightarrow f(P)$ cuando $x \\rightarrow P ~\\forall~ x \\in A$').move_to(np.array([0, 1, 0])).scale(0.8)
        self.play(Transform(titulo, demostracion), run_time = 1)
        self.wait(tiempo_entre_videos-1)

        ##########?

        demostracion2 = Tex('Sabemos que $f$ es diferenciable en $P$, por lo tanto $\\lim\\limits_{x \\to P}  \\frac{ || f(x) - f(P) - Df(P)(x-P) || }{ || x-P || } = 0$').move_to(np.array([0, -1, 0])).scale(0.8)
        self.play(Write(demostracion2), run_time = 1)
        self.wait(tiempo_entre_videos-2)

        ##########?

        inicio = Tex('Partamos de la siguiente afirmación:').move_to(np.array([0, 3.5, 0])).scale(0.8)
        diferenciable = demostracion2[0][-40:].copy()
        self.play(diferenciable.animate.move_to(np.array([5.25, 3.5, 0])).scale(0.6), Transform(titulo, inicio), Unwrite(demostracion2))
        self.wait(tiempo_entre_videos-3)

        ##########?

        inicio2 = Tex('$0 \\leqslant || f(x) - f(P) ||$').move_to(np.array([0, 2.5, 0])).scale(0.8)
        self.play(Write(inicio2))
        self.wait(tiempo_entre_videos-3)

        ##########?

        inicio3 = Tex('Queremos llegar a una expresión que contenga el límite mencionado').move_to(np.array([0, 1.5, 0])).scale(0.8)
        self.play(Write(inicio3))
        self.wait(tiempo_entre_videos-3)

        ##########?

        self.play(Indicate(diferenciable))

        ##########?

        i4 = Tex('sumemos y restemos por $Df(P)(x-P)$ (la igualdad se mantiene)').move_to(np.array([0, 0.5, 0])).scale(0.8)
        self.play(Write(i4))
        self.wait(tiempo_entre_videos-3)

        ##########?

        i2_copia = inicio2[0][2:].copy()
        i5 = Tex('$|| f(x) - f(P) || = || f(x) - f(P) - Df(P)(x-P) + Df(P)(x-P)|| $').move_to(np.array([0, -0.5, 0])).scale(0.8)
        self.play(Transform(i2_copia, i5))
        self.wait(tiempo_entre_videos-3)

        ##########?

        i6 = Tex('aplicando desigualdad triangular $(||B + C|| \\leqslant ||B|| + ||C||)$ queda').move_to(np.array([0, -1.49, 0])).scale(0.8)
        self.play(Write(i6))
        self.wait(tiempo_entre_videos-3)

        ##########?

        i5_copia = i5[0][14:].copy()
        i7 = Tex('$\\leqslant ||f(x) - f(P) - Df(P)(x-P)|| + ||Df(P)(x-P)||$').move_to(np.array([0, -2.5, 0])).scale(0.8)
        i7[0][1:25].set_color(BLUE)
        i7[0][26:].set_color(RED)
        self.play(Transform(i5_copia, i7))
        self.wait(tiempo_entre_videos-1)

        ##########?

        i8 = Tex('Multipliquemos y dividamos el primer término por $|| x-P ||$').move_to(np.array([0, 1.49, 0])).scale(0.8)
        self.play(Write(i8), FadeOut(titulo, inicio3, i4, i2_copia, i6), i5_copia.animate.move_to(np.array([0, 2.55, 0])), inicio2.animate.move_to(np.array([-5.25, 3.49, 0])).scale(0.6))
        self.wait(tiempo_entre_videos-3)

        ##########?

        i5_copia_copia = i5_copia[0][1:25].copy()
        i9 = Tex('$||f(x) - f(P) - Df(P)(x-P)|| = \\frac{||f(x) - f(P) - Df(P)(x-P)||}{|| x-P ||} || x-P ||$ ').move_to(np.array([0, 0.5, 0])).scale(0.8)
        i9[0][:24].set_color(BLUE)
        i9[0][25:].set_color(BLUE)
        self.play(Transform(i5_copia_copia, i9))
        self.wait(tiempo_entre_videos-3)

        ##########?

        i10 = Tex('luego, por la desigualdad de $Cauchy-Schwarz$ sabemos que:').move_to(np.array([0, -0.5, 0])).scale(0.8)
        self.play(Write(i10))
        self.wait(tiempo_entre_videos-3)

        ##########?

        i5_copia_copia2 = i5_copia[0][26:].copy()
        i11 = Tex('$||Df(P)(x-P)|| \\leqslant ||\\nabla f(P)||~||x-P||$').move_to(np.array([0, -1.5, 0])).scale(0.8)
        i11[0][:14].set_color(RED)
        i11[0][15:].set_color(RED)
        self.play(Transform(i5_copia_copia2, i11))
        self.wait(tiempo_entre_videos-3)

        ##########?

        self.play(FadeOut(i8, i10), i5_copia_copia.animate.move_to(np.array([0, 1.5, 0])), i5_copia_copia2.animate.move_to(np.array([0, 0.5, 0])))
        self.wait(tiempo_entre_videos-3)

        ##########?

        luego = Tex('la desigualdad nos queda').move_to(np.array([0, -0.5, 0])).scale(0.8)
        self.play(Write(luego))
        self.wait(tiempo_entre_videos-3)

        ##########?

        queda = Tex('$\\leqslant \\frac{||f(x) - f(P) - Df(P)(x-P)||}{|| x-P ||} || x-P || + ||\\nabla f(P)||~||x-P||$').move_to(np.array([0, -1.5, 0])).scale(0.8)
        queda[0][1:40].set_color(BLUE)
        queda[0][41:].set_color(RED)
        self.play(Write(queda))
        self.wait(tiempo_entre_videos-3)

        ##########?

        obs = Tex('observemos que cuando $x \\rightarrow P$ ambos términos tienden a cero').move_to(np.array([0, 1.4, 0])).scale(0.8)
        self.play(queda.animate.move_to(np.array([0, 2.5, 0])).set_color(WHITE), Write(obs), FadeOut(luego, i5_copia_copia, i5_copia_copia2, i5_copia))
        self.wait(tiempo_entre_videos-3)

        ##########?

        self.play(diferenciable.animate.move_to(np.array([0, 0.01, 0])).scale(5/3))
        self.wait(tiempo_entre_videos-3)

        ##########?

        obs2 = Tex('$\\lim\\limits_{x \\to P}  || x-P || = 0$').move_to(np.array([0, -1, 0])).scale(0.8)
        self.play(Write(obs2))
        self.wait(tiempo_entre_videos-3)

        ##########?

        decir = Tex('por lo tanto').move_to(np.array([0, -2, 0])).scale(0.8)
        self.play(Write(decir))
        self.wait(tiempo_entre_videos-3)

        ##########?

        ya_casi = Tex('$\\leqslant 0$').move_to(np.array([1.65, -3, 0])).scale(0.8)
        self.play(inicio2.animate.move_to(np.array([-0.4, -3, 0])).scale(5/3), Write(ya_casi))
        self.wait(tiempo_entre_videos-3)

        ##########?

        quiere = Tex('finalmente, como $ \\lim\\limits_{x \\to P} || f(x) - f(P) || = 0$, podemos afirmar que').move_to(np.array([0, 1, 0])).scale(0.8)
        quiere2 = Tex('$f(x) \\rightarrow f(P)$ cuando $x \\rightarrow P$').move_to(np.array([0, 0.01, 0])).scale(0.8)
        framebox = SurroundingRectangle(quiere2[0], buff = 0.1)
        self.play(Write(quiere), Write(quiere2), FadeOut(queda, obs, diferenciable, obs2, decir), inicio2.animate.move_to(np.array([-0.4, 2, 0])), ya_casi.animate.move_to(np.array([1.65, 2, 0])), Create(framebox))
        self.wait(tiempo_entre_videos-3)

        ##########?

        listo = Tex('que es justo lo que queríamos probar, pues esto implica que $f$ es continua en $P$, finalizando así la demostración del teorema').move_to(np.array([0, -1.25, 0])).scale(0.8)
        self.play(Write(listo))
        self.wait(tiempo_entre_videos)
