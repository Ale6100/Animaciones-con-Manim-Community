from manim import *
import numpy as np

class unicidad(Scene):
    def construct(self):
        tiempo_entre_videos = 5
        # grid = NumberPlane() #La grilla es muy útil cuando estás editando el video
        # self.add(grid)
        titulo = Tex('Demostración del Teorema de Unicidad').scale(1.5)
        self.play(Write(titulo), run_time = 1)
        self.wait(tiempo_entre_videos-1)

        ##########? Agrega el enunciado

        e1 = Tex('Enunciado: Sea $f: A \\subset \\mathbb{R}^n \\rightarrow \mathbb{R}$, $P \in A^o$. Si existe una transformación lineal $T_p : \\mathbb{R}^n \\rightarrow \mathbb{R}$ tal que $\\lim\\limits_{x \\to P}  \\frac{ | f(x) - f(P) - T_P(x-P) | }{ || x-P || } = 0$, entonces').move_to(np.array([0, 3, 0])).scale(0.8)
        e2 = Tex('$-~ T_p(V) = \\frac{\\partial f}{\\partial V}(P) ~\\forall~ V \in \\mathbb{R}^n$, $||V|| = 1$').move_to(np.array([0, 1.5, 0])).scale(0.8)
        e3 = Tex('$-$ Existen todas las derivadas direccionales de $f$ en $P$').move_to(np.array([0, 0.5, 0])).scale(0.8)
        e4 = Tex('$-~ T_p(x) =~ < \\nabla f(P),~ x >$').move_to(np.array([0, -0.5, 0])).scale(0.8)
        e5 = Tex('$-~ f$ es diferenciable en $P$').move_to(np.array([0, -1.5, 0])).scale(0.8)
        e6 = Tex('$-$ La transformación lineal $T_P$ es única').move_to(np.array([0, -2.5, 0])).scale(0.8)
        e = VGroup(e2, e3, e4, e5, e6)
        self.play(Transform(titulo, e1), Write(e), run_time = 1)
        self.wait(tiempo_entre_videos+8)

        ##########?

        self.play(e.animate.move_to(np.array([-5, 3, 0])).scale(0.4), Unwrite(titulo))
        self.wait(tiempo_entre_videos-4)

        ##########?

        framebox1 = SurroundingRectangle(e, buff = 0.05)
        self.play(Create(framebox1))
        self.wait(tiempo_entre_videos-4)

        ##########?

        demostracion = Tex('Iniciemos observando que si $\\lim\\limits_{x \\to P}  \\frac{ | f(x) - f(P) - T_P(x-P) | }{ || x-P || } = 0$, entonces lo hace por cualquier curva por la cual $x$ tienda a $P$. En particular, si tomamos $x = P+tV$ donde $V \in \\mathbb{R}^n$, $||V|| = 1$, se observa que $t \\rightarrow 0$ cuando $x \\rightarrow P$. Con lo cual:').move_to(np.array([0, 0.51, 0])).scale(0.8)
        self.play(Write(demostracion))
        self.wait(tiempo_entre_videos+2)

        ##########?

        demo_copia = demostracion[0][24:59].copy()
        limite1 = Tex('$\\lim\\limits_{t \\to 0}  \\frac{ | f(P+tV) - f(P) - T_P(tV) | }{ || tV || } = 0$').move_to(np.array([0, -1.495, 0])).scale(0.8)
        self.play(Transform(demo_copia, limite1))
        self.wait(tiempo_entre_videos)

        ##########?

        ademas = Tex('observando que $T_P(tV) = tT_P(V)$ por ser $T_P$ una transformación lineal, y que $||tV|| = |t|~||V|| = |t|$, se tiene:').move_to(np.array([0, 1.005, 0])).scale(0.8)
        self.play(demo_copia.animate.move_to(np.array([0, 2.505, 0])), Transform(demostracion, ademas))
        self.wait(tiempo_entre_videos+1)

        ##########?

        limite2 = Tex('$\\lim\\limits_{t \\to 0} \\left| \\frac{  f(P+tV) - f(P) - tT_P(V)  }{ t } \\right| = \\lim\\limits_{t \\to 0} \\left| \\frac{  f(P+tV) - f(P) }{ t } - T_P(V) \\right| = 0$').move_to(np.array([0, -0.02, 0])).scale(0.8)
        self.play(Write(limite2))
        self.wait(tiempo_entre_videos)

        ##########?

        locual = Tex('por lo tanto').move_to(np.array([0, -1, 0])).scale(0.8)
        self.play(Write(locual))
        self.wait(tiempo_entre_videos-4)

        ##########?

        locual2 = Tex('$\\lim\\limits_{t \\to 0} \\frac{  f(P+tV) - f(P) }{ t } = T_P(V) $').move_to(np.array([0, -2, 0])).scale(0.8)
        self.play(Write(locual2))
        self.wait(tiempo_entre_videos-2)

        ##########?

        self.play(locual2.animate.move_to(np.array([0, 2.51, 0])), FadeOut(demo_copia, demostracion, limite2, locual))
        self.wait(tiempo_entre_videos-4)

        ##########?

        pero = Tex('pero sabemos que $\\lim\\limits_{t \\to 0} \\frac{  f(P+tV) - f(P) }{ t } = \\frac{\\partial f}{\\partial V}(P)$, por lo tanto').move_to(np.array([0, 1.01, 0])).scale(0.8)
        self.play(Write(pero))
        self.wait(tiempo_entre_videos-2)

        ##########?

        locual2_copia = locual2[0].copy()
        pero_copia = pero[0][14:43].copy()
        e2_listo = Tex('$T_p(V) = \\frac{\\partial f}{\\partial V}(P)$').move_to(np.array([0, -0.02, 0])).scale(0.8)
        framebox2 = SurroundingRectangle(e2_listo[0], buff = 0.1)
        self.play(Transform(locual2_copia, e2_listo), Transform(pero_copia, e2_listo), Create(framebox2), Indicate(e2))
        self.remove(pero_copia)
        self.wait(tiempo_entre_videos-2)

        ##########?

        como = Tex('como $V$ puede ser cualquier versor en $\\mathbb{R}^n$ (no le consideramos ninguna restricción), se cumple que existen todas las derivadas direccionales de $f$ en $P$').move_to(np.array([0, -1.01, 0])).scale(0.8)
        framebox3 = SurroundingRectangle(como[0][-43:], buff = 0.1)
        self.play(Write(como), Create(framebox3), Indicate(e3), e2.animate.set_color(GREEN))
        self.wait(tiempo_entre_videos)

        ##########?

        en_p = Tex('En particular, se cumple que $T_p(e_i) = \\frac{\\partial f}{\\partial e_i}(P)$, donde $e_i$ es el $i-\\acute{e}simo$ vector de la base canónica').move_to(np.array([0, -2.5, 0])).scale(0.8)
        self.play(Write(en_p), e3.animate.set_color(GREEN))
        self.wait(tiempo_entre_videos-1)

        ##########?

        T = en_p[0][24: 40].copy()
        recordando = Tex('Sabiendo esto último y recordando que una transformación lineal está determinada por sus valores en la base canónica de la forma').move_to(np.array([0, 1.5, 0])).scale(0.8)
        self.play(Uncreate(framebox2), Uncreate(framebox3), FadeOut(en_p, como, locual2_copia, pero, locual2), Write(recordando), T.animate.move_to([0, 2.5, 0]))
        self.wait(tiempo_entre_videos-1)

        ##########?

        forma = Tex('''$
        T_P(x) =
        \\left( \\begin{smallmatrix} | & ~ & | \\\\ T_P(e_1) & \\dotsb & T_P(e_n) \\\\ | & ~ & | \\end{smallmatrix} \\right)
        \\left( \\begin{smallmatrix} x_1 \\\\ |  \\\\ x_n \\end{smallmatrix} \\right)
            $''').move_to(np.array([0, 0.5, 0])).scale(0.8)

        self.play(Write(forma))
        self.wait(tiempo_entre_videos)

        ##########?

        se_tiene = Tex('se tiene').move_to(np.array([0, -0.5, 0])).scale(0.8)
        self.play(Write(se_tiene))
        self.wait(tiempo_entre_videos-3)

        ##########?

        forma2 = Tex('''$
        T_P(x) =
        \\left( \\begin{smallmatrix} | & ~ & | \\\\ \\frac{\\partial f}{\\partial e_1}(P) & \\dotsb & \\frac{\\partial f}{\\partial e_n}(P) \\\\ | & ~ & | \\end{smallmatrix} \\right)
        \\left( \\begin{smallmatrix} x_1 \\\\ |  \\\\ x_n \\end{smallmatrix} \\right)
            $''').move_to(np.array([0, -1.5, 0])).scale(0.8)
        self.play(Write(forma2))
        self.wait(tiempo_entre_videos-2)

        ##########?

        esto = Tex('y esto último es equivalente a decir que ').move_to(np.array([-3, -2.5, 0])).scale(0.8)
        t = Tex('$T_p(x) =~ < \\nabla f(P),~ x >$').move_to(np.array([2.75, -2.5, 0])).scale(0.8)
        framebox4 = SurroundingRectangle(t[0], buff = 0.1)
        self.play(Write(esto), Write(t), Create(framebox4), Indicate(e4), Unwrite(T))
        self.wait(tiempo_entre_videos-1)

        ##########?

        rec = Tex('Recordemos que $\\lim\\limits_{x \\to P}  \\frac{ | f(x) - f(P) - T_P(x-P) | }{ || x-P || } = 0$. Considerando este límite y la última fórmula encontrada, podemos afirmar que $T_P(x-P) =~ < \\nabla f(P),~ x-P >$, por lo tanto').move_to(np.array([0, 1, 0])).scale(0.8)
        self.play(FadeOut(recordando, forma, forma2, se_tiene, esto), Uncreate(framebox4), Write(rec), e4.animate.set_color(GREEN), t.animate.move_to([0, 2.5, 0]))
        self.wait(tiempo_entre_videos+1)

        ##########?

        dif = Tex('$\\lim\\limits_{x \\to P}  \\frac{ | f(x) - f(P) - < \\nabla f(P),~ x-P > | }{ || x-P || } = 0$').move_to(np.array([0, -0.5, 0])).scale(0.8)
        self.play(Write(dif))
        self.wait(tiempo_entre_videos-2)

        ##########?

        que = Tex('esto último nos indica que $f$ es diferenciable en $P$').move_to(np.array([0, -1.5, 0])).scale(0.8)
        framebox5 = SurroundingRectangle(que[0][-19:], buff = 0.1)
        self.play(Write(que), Create(framebox5), Indicate(e5))

        ##########?

        self.play(e5.animate.set_color(GREEN))
        self.wait(tiempo_entre_videos-2)

        ##########?

        por = Tex('Por otro lado, si existe otra transformación lineal $S_P$ que verifique la condición del límite original, entonces también cumple que $S_p(x) =~ < \\nabla f(P),~ x >$, por lo tanto $S_P(x) = T_P(x)$').move_to(np.array([0, 1.01, 0])).scale(0.8)
        por2 = Tex('Esto nos indica que la transformación lineal $T_P$ es única').move_to(np.array([0, -0.05, 0])).scale(0.8)
        framebox6 = SurroundingRectangle(por2[0][-31:], buff = 0.1)
        self.play(Write(por), Write(por2), FadeOut(rec, dif, que, t), Create(framebox6), Indicate(e6), Uncreate(framebox5))

        ##########?

        self.play(e6.animate.set_color(GREEN))
        self.wait(tiempo_entre_videos+3)

        ##########?

        listo = Tex('Ya podemos dar por demostrado el teorema').move_to(np.array([0, -1.01, 0])).scale(0.8)
        self.play(Uncreate(framebox6), FadeOut(por, por2), e.animate.move_to([0, 1.01, 0]).scale(5/3), Uncreate(framebox1), Write(listo))
        self.wait(tiempo_entre_videos)
