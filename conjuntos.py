from manim import Scene, NumberPlane, Tex, Write, Transform, Unwrite, Circle, Create, Dot, FadeIn, FadeOut, Ellipse, SurroundingRectangle, Uncreate, Rectangle, Intersection, Union, Underline
import numpy as np

class conjuntos(Scene):
    def construct(self):
        tiempo_entre_videos = 5

        # grid = NumberPlane().set_opacity(0.33)
        # self.add(grid)

        titulo = Tex('Conjuntos y operaciones entre ellos').scale(1.33)
        self.play(Write(titulo), run_time = 1)
        self.wait(tiempo_entre_videos-1)

        ##########? #Agrega el enunciado

        enunciado = Tex('Definición informal: Un conjunto es una agrupación de objetos, llamados elementos, donde cada objeto se puede determinar fácilmente si pertenece o no al conjunto.').move_to(np.array([0, 2.01, 0])).scale(0.8)

        relleno_para_despues = Rectangle(width=5, height=5).move_to(np.array([-3.5, -0.53, 0])).set_color('WHITE').set_fill('WHITE', opacity=0).set_opacity(0)

        self.play(Transform(titulo, enunciado), Create(relleno_para_despues), run_time = 1)
        self.wait(tiempo_entre_videos+3)


        ##########? #Agrega los conjuntos A, B, C y D como ejemplo

        A = Tex('$A = \{3, 4, 5, 8, 34\}$').move_to(np.array([0, 0, 0]))

        B = Tex('$B = \{1, \{1\}, \{2, 64\}\}$').move_to(np.array([0, -1, 0]))

        C = Tex('$C = \{x \in \mathbb{R} \mid x > 0\}$').move_to(np.array([0, -2, 0]))

        D = Tex('$D = \{Arroz, Canela, Leche, Tomates, 500\}$').move_to(np.array([0, -3, 0]))

        self.play(Write(A), Write(B), Write(C), Write(D), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? Decir que el orden no importa

        orden_no_importa = Tex('Considerar que el orden de los elementos no importa en un conjunto, y que en un conjunto no se tiene en cuenta repeticiones de elementos').move_to(np.array([0, 2.01, 0])).scale(0.8)

        A2 = Tex('$A_2 = \{8, 34, 4, 3, 5\}$').move_to(np.array([0, -1, 0]))

        A3 = Tex('$A_3 = \{3, 4, 5, 8, 34, 5, 3\}$').move_to(np.array([0, -2, 0]))

        a_iguales = Tex('$A = A_2 = A_3$').move_to(np.array([0, -3, 0]))

        self.play(Transform(titulo, orden_no_importa), Transform(B, A2), Transform(C, A3), Transform(D, a_iguales), run_time = 1)
        self.wait(tiempo_entre_videos+4)

        ##########? Mostrar que el orden no importa

        texto_pertenencia = Tex('Se dice que si $a$ pertenece al conjunto $A$ se nota $a \in A$. En cambio, si $a$ no pertenece a $A$ se nota $a \\notin A$').move_to(np.array([0, 2.01, 0])).scale(0.8)

        ocho_pertenece = Tex('$8 \in A$').move_to(np.array([0, -1, 0]))

        uno_no_pertenece = Tex('$1 \\notin A$').move_to(np.array([0, -2, 0]))

        self.play(Transform(titulo, texto_pertenencia), Transform(B, ocho_pertenece), Transform(C, uno_no_pertenece), Unwrite(D), run_time = 1)
        self.wait(tiempo_entre_videos+4)

        ##########? Diagramas de Venn

        diagrama_venn = Tex('Los conjuntos se suelen representar gráficamente por los llamados diagramas de Venn: simplemente se utiliza una circunferencia para representar el conjunto y eventualmente en el interior sus elementos.').move_to(np.array([0, 2.5, 0])).scale(0.8)

        diagrama_venn[0][57:72].set_color('RED')

        diagrama = Circle(2, 'BLUE').move_to(np.array([-0, -0.55, 0]))

        nuevo_a = Tex('$A = \{3, 4, 5\}$').move_to(np.array([-0, -3.5, 0]))

        nuevo_a[0][0].set_color('BLUE')
        nuevo_a[0][3].set_color('RED')
        nuevo_a[0][5].set_color('GOLD')
        nuevo_a[0][7].set_color('GREEN')

        a_diagrama = Tex('$A$').set_color('BLUE').add_updater(lambda v: v.move_to(diagrama.get_center() + np.array([-2.1, 1, 0])))

        punto_tres = Dot().set_color('RED').add_updater(lambda v: v.move_to(diagrama.get_center() + np.array([-0.75, 0.75, 0])))

        punto_cuatro = Dot().set_color('GOLD').add_updater(lambda v: v.move_to(diagrama.get_center() + np.array([0.75, 0.75, 0])))

        punto_cinco = Dot().set_color('GREEN').add_updater(lambda v: v.move_to(diagrama.get_center() + np.array([0, -0.75, 0])))

        self.play(Transform(titulo, diagrama_venn), Write(nuevo_a), Write(a_diagrama), Create(diagrama), Create(punto_tres), Create(punto_cuatro), Create(punto_cinco), Unwrite(A), Unwrite(B), Unwrite(C), run_time = 1)
        self.wait(1)

        ##########?

        tres = Tex('$3$').set_color('RED').move_to(punto_tres.get_center() + np.array([-0.33, 0, 0]))
        cuatro = Tex('$4$').set_color('GOLD').move_to(punto_cuatro.get_center() + np.array([0.33, 0, 0]))
        cinco = Tex('$5$').set_color('GREEN').move_to(punto_cinco.get_center() + np.array([-0.33, 0, 0]))

        self.play(Write(tres), Write(cuatro), Write(cinco), run_time = 1)
        self.wait(tiempo_entre_videos+10)

        ##########? Subconjuntos e inclusión

        inclusion = Tex('Sean $A$ y $B$ conjuntos, se dice que $B$ está incluído en $A$ si para todo $x$, se tiene que si $x$ pertenece a $B$ entonces $x$ pertenece a $A$. Por otro lado $B$ no está incluído en $A$ si existe $x$ perteneciente a $B$ tal que no pertenece a $A$. Esto se escribe:').move_to(np.array([0, 2.1, 0])).scale(0.8)

        inclusion_formal = Tex('$B \subseteq A$ si $\\forall x$, $x \\in B \\Rightarrow x \in A$, $B \\nsubseteq A$ si $\\exists x \in B \mid x \\notin A$').move_to(np.array([0, -1, 0]))

        inclusion[0][26:100].set_color('RED')
        inclusion[0][112:175].set_color('BLUE')

        inclusion_formal[0][:15].set_color('RED')
        inclusion_formal[0][16:30].set_color('BLUE')

        self.play(Transform(titulo, inclusion), Write(inclusion_formal), nuevo_a.animate.set_opacity(0), a_diagrama.animate.set_opacity(0), FadeOut(diagrama), tres.animate.set_opacity(0), cuatro.animate.set_opacity(0), cinco.animate.set_opacity(0), punto_tres.animate.set_opacity(0), punto_cuatro.animate.set_opacity(0), punto_cinco.animate.set_opacity(0), run_time = 1)
        self.wait(tiempo_entre_videos+10)

        ##########? Mostrar ejemplo B incluído en A

        diagrama.move_to(np.array([-3.25, -0.55, 0]))

        nuevo_a.move_to(np.array([0, 1, 0]))

        B = Tex('$B = \{3, 4\}$').move_to(np.array([0, -1, 0]))

        B[0][0].set_color('YELLOW')
        B[0][3].set_color('RED')
        B[0][5].set_color('GOLD')

        def move_to_center(v):
            center = (punto_tres.get_center() + punto_cuatro.get_center()) / 2
            v.move_to(center)

        diagrama_b = Ellipse(width = 2.75, height = 1.33).set_color('YELLOW')
        diagrama_b.add_updater(move_to_center)

        texto_b = Tex('$B$').set_color('YELLOW').add_updater(lambda v: v.move_to(diagrama_b.get_center() + np.array([-1.5, -0.66, 0])))

        self.play(inclusion_formal.animate.move_to(np.array([0, 3, 0])).set_color('WHITE'), Create(diagrama_b), Write(B), Unwrite(titulo), nuevo_a.animate.set_opacity(1), a_diagrama.animate.set_opacity(1), FadeIn(diagrama), tres.animate.set_opacity(1), cuatro.animate.set_opacity(1), cinco.animate.set_opacity(1), punto_tres.animate.set_opacity(1), punto_cuatro.animate.set_opacity(1), punto_cinco.animate.set_opacity(1), Write(texto_b), run_time = 1)
        self.wait(1)

        ##########?

        self.play(tres.animate.move_to(punto_tres.get_center() + np.array([-0.33, 0, 0])), cuatro.animate.move_to(punto_cuatro.get_center() + np.array([0.33, 0, 0])), cinco.animate.move_to(punto_cinco.get_center() + np.array([-0.33, 0, 0])), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? Remarcamos la conclusión

        indice_a_recortar = 15
        recorte = inclusion_formal[0][0:indice_a_recortar]

        remarcar = recorte.copy().set_color('GREEN')

        b_incluido_en_a = Tex('$\\Rightarrow B \subseteq A$').move_to(np.array([3.5, 0, 0]))
        box_b_incluido_en_a = SurroundingRectangle(b_incluido_en_a, color='GREEN', buff = 0.1)

        diagrama_b.remove_updater(move_to_center)

        self.play(Write(b_incluido_en_a), Create(box_b_incluido_en_a), Transform(recorte, remarcar), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? Mostrar ejemplo B no incluído en A

        nuevo_b = Tex('$B = \{6, 5\}$').move_to(np.array([0, -1, 0]))

        nuevo_b[0][0].set_color('YELLOW')
        nuevo_b[0][3].set_color('PURPLE')
        nuevo_b[0][5].set_color('GREEN')

        punto_seis = Dot().set_color('PURPLE').move_to(diagrama.get_center() + np.array([-2, -0.75, 0]))
        seis = Tex('$6$').set_color('PURPLE').add_updater(lambda v: v.move_to(punto_seis.get_center() + np.array([-0.33, 0, 0])))

        diagrama_b2 = Ellipse(width = 3.25, height = 1.30).set_color('YELLOW').move_to((punto_seis.get_center() + punto_cinco.get_center())/2)

        print('ubicacion del diagrama:', diagrama_b2.get_center())

        self.play(recorte.animate.set_color('WHITE'), Transform(B, nuevo_b), Transform(diagrama_b, diagrama_b2), Create(punto_seis), Write(seis), Uncreate(box_b_incluido_en_a), Unwrite(b_incluido_en_a), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? Remarcamos la conclusión 2

        recorte2 = inclusion_formal[0][indice_a_recortar+1:]

        remarcar2 = recorte2.copy().set_color('GREEN')

        b_no_incluido_en_a = Tex('$\\Rightarrow B \\nsubseteq A$').move_to(np.array([3.5, 0, 0]))
        box_b_no_incluido_en_a = SurroundingRectangle(b_no_incluido_en_a, color='GREEN', buff = 0.1)

        self.play(Write(b_no_incluido_en_a), Create(box_b_no_incluido_en_a), Transform(recorte2, remarcar2), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? Igualdad de conjuntos y ejemplo

        en_cambio = Tex('Por otro lado, $A = B \\iff A \subseteq B$ y $B \subseteq A$').move_to(np.array([0, 2.1, 0]))

        diagrama_b_futura = diagrama.copy().set_color('YELLOW')

        nuevo_b2 = Tex('$B = \{3, 4, 5\}$').move_to(np.array([0.1, -1, 0]))

        nuevo_b2[0][0].set_color('YELLOW')
        nuevo_b2[0][3].set_color('RED')
        nuevo_b2[0][5].set_color('GOLD')
        nuevo_b2[0][7].set_color('GREEN')

        self.play(Write(en_cambio), Transform(diagrama_b, diagrama_b_futura), Transform(B, nuevo_b2), Uncreate(punto_seis), Unwrite(seis), Unwrite(recorte2), Unwrite(inclusion_formal), Unwrite(b_no_incluido_en_a), Uncreate(box_b_no_incluido_en_a), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? Remarcamos la conclusión 3

        recorte3 = en_cambio[0][12:]

        remarcar3 = recorte3.copy().set_color('GREEN')

        b_igual_a_a = Tex('$\\Rightarrow B = A$').move_to(np.array([3.5, 0, 0]))
        box_b_igual_a_a = SurroundingRectangle(b_igual_a_a, color='GREEN', buff = 0.1)

        self.play(Transform(recorte3, remarcar3), Create(box_b_igual_a_a), Write(b_igual_a_a), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? Definir Conjunto referencial U

        conjunto_referencial = Tex('En lo que sigue vamos a definir al conjunto $U$ como un conjunto referencial (o de referencia), es decir, contendrá a todos los elementos de los conjuntos que vamos a considerar.').move_to(np.array([0, 3.1, 0])).scale(0.8)

        diagrama_u = Rectangle(width=5, height=5).move_to(np.array([-3.5, -0.53, 0])).set_color('WHITE')

        u = Tex('$U$').move_to(diagrama_u.get_center() + np.array([-3, -0.01, 0])).set_color('WHITE')
        u_igual_a = Tex('$U = \{3, 4, 5, 7\}$').move_to(np.array([3.5, 0.01, 0]))

        u_igual_a[0][3].set_color('RED')
        u_igual_a[0][5].set_color('GOLD')
        u_igual_a[0][7].set_color('GREEN')
        u_igual_a[0][9].set_color('PURPLE')

        punto_siete = Dot().set_color('PURPLE').move_to(diagrama_u.get_center() + np.array([-2, -1.02, 0]))
        siete = Tex('$7$').set_color('PURPLE').add_updater(lambda v: v.move_to(punto_siete.get_center() + np.array([0, -0.33, 0])))

        self.play(Write(conjunto_referencial), nuevo_a.animate.move_to(np.array([2, -1, 0])), B.animate.set_opacity(0), Create(diagrama_u), Write(u), Create(punto_siete), Write(siete), Write(u_igual_a), diagrama.animate.move_to(np.array([-3.5, -0.5, 0])), Uncreate(diagrama_b), Unwrite(en_cambio), Unwrite(recorte3), Uncreate(box_b_igual_a_a), Unwrite(b_igual_a_a), Unwrite(texto_b), run_time = 1)
        self.wait(1)

        ##########?

        self.play(tres.animate.move_to(punto_tres.get_center() + np.array([-0.33, 0, 0])), cuatro.animate.move_to(punto_cuatro.get_center() + np.array([0.33, 0, 0])), cinco.animate.move_to(punto_cinco.get_center() + np.array([-0.33, 0, 0])), run_time = 1)
        self.wait(tiempo_entre_videos+10)

        ##########? Complemento de A

        complemento_a = Tex('Complemento de A').move_to(np.array([0, 3, 0]))

        ul = Underline(complemento_a, color='RED')

        definicion_c = Tex('$A^c = \{x \in U \mid x \\notin A\}$').move_to(np.array([3.5, 1, 0]))

        ac = Tex('$A^c = \{7\}$').move_to(np.array([5, -1, 0])).set_color('YELLOW')

        diagrama_copia = diagrama.copy().set_fill('BLUE', opacity=1)

        self.play(relleno_para_despues.animate.set_fill('PURPLE', opacity=1).set_opacity(1), Transform(conjunto_referencial, complemento_a), Write(definicion_c), Write(ac), diagrama_u.animate.set_fill('YELLOW', opacity=1).set_stroke(color='PURPLE', width=10), Create(diagrama_copia), Create(ul), nuevo_a.animate.set_color('BLUE'), u_igual_a.animate.set_color('PURPLE'), u.animate.set_color('PURPLE'), Uncreate(diagrama), Uncreate(punto_tres), Uncreate(punto_cuatro), Uncreate(punto_cinco), Uncreate(punto_siete), Unwrite(a_diagrama), Unwrite(tres), Unwrite(cuatro), Unwrite(cinco), Unwrite(siete), run_time = 1)
        self.wait(tiempo_entre_videos+5)

        ##########? Unión

        union = Tex('Unión').move_to(np.array([0, 3, 0])).scale(1.1)

        ul_u = Underline(union, color='RED')

        definicion_u = Tex('$A \\cup B = \{x \in U \mid x \\in A \\text{ o } x \\in B\}$').move_to(np.array([3.5, 1, 0]))

        otro_b = Tex('$B = \{7, 5\}$').move_to(np.array([5, -1, 0])).set_color('GREEN')

        union_texto = Tex('$A \\cup B = \{3, 4, 5, 7\}$').move_to(np.array([3.5, -2, 0])).set_color('RED')

        u_igual_a2 = Tex('$U = \{3, 4, 5, 7, 10\}$').move_to(np.array([3.5, 0, 0])).set_color('PURPLE')

        circulo_a = Circle(1.33, 'BLUE').move_to(np.array([-4.33, -0.5, 0])).set_fill('RED', opacity=1).set_stroke(color='BLUE', width=10)

        circulo_b = Circle(1.33, 'GREEN').move_to(np.array([-2.66, -0.5, 0])).set_fill('RED', opacity=1).set_stroke(color='GREEN', width=10)

        borde_a = Circle(1.33, 'BLUE').move_to(circulo_a.get_center()).set_stroke(color='BLUE', width=10)

        self.play(Transform(conjunto_referencial, union), Transform(definicion_c, definicion_u), Write(otro_b), Transform(ac, union_texto), Transform(u_igual_a, u_igual_a2), Transform(diagrama_copia, circulo_a), Transform(ul, ul_u), Create(circulo_b), diagrama_u.animate.set_fill('YELLOW', opacity=0), Create(borde_a), run_time = 1)
        self.wait(tiempo_entre_videos+5)

        ##########? Intersección

        interseccion = Tex('Intersección').move_to(np.array([0, 3, 0])).scale(1.1)

        ul_i = Underline(interseccion, color='RED')

        definicion_i = Tex('$A \\cap B = \{x \in U \mid x \\in A \\text{ y } x \\in B\}$').move_to(np.array([3.5, 1, 0]))

        interseccion_texto = Tex('$A \\cap B = \{5\}$').move_to(np.array([3.5, -2, 0])).set_color('RED')

        diagrama_i = Intersection(diagrama_copia, circulo_b).set_fill('RED', opacity=1).set_stroke(color='BLACK', width=0)

        borde_b = Circle(1.33, 'GREEN').move_to(np.array([-2.66, -0.5, 0])).set_stroke(color='GREEN', width=10)

        self.play(Transform(conjunto_referencial, interseccion), Transform(definicion_c, definicion_i), Transform(ac, interseccion_texto), Transform(ul, ul_i), circulo_b.animate.set_fill('GREEN', opacity=1), diagrama_copia.animate.set_fill('BLUE', opacity=1), Create(diagrama_i), Create(borde_b), run_time = 1)
        self.wait(tiempo_entre_videos+5)

        ##########? Diferencia

        diferencia = Tex('Diferencia').move_to(np.array([0, 3, 0])).scale(1.1)

        ul_d = Underline(diferencia, color='RED')

        definicion_d = Tex('$A - B = \{x \in A \mid x \\notin B\}$').move_to(np.array([3.5, 1, 0]))

        diferencia_texto = Tex('$A - B = \{3, 4\}$').move_to(np.array([3.5, -2, 0])).set_color('RED')

        borde_a2 = Circle(1.33, 'BLUE').move_to(circulo_a.get_center()).set_stroke(color='BLUE', width=10)

        self.play(Transform(conjunto_referencial, diferencia), Transform(definicion_c, definicion_d), Transform(ac, diferencia_texto), Transform(ul, ul_d), diagrama_copia.animate.set_fill('RED', opacity=1), Transform(borde_a, borde_a2), Uncreate(diagrama_i), run_time = 1)
        self.wait(tiempo_entre_videos+5)

        ##########? Diferencia simétrica

        diferencia_simetrica = Tex('Diferencia simétrica').move_to(np.array([0, 3, 0])).scale(1.1)

        ul_ds = Underline(diferencia_simetrica, color='RED')

        definicion_ds = Tex('$A \\triangle B = \{ x \in U \mid (x \in A$ y $x \\notin B$) o $(x \in B$ y $x \\notin A) \}$').move_to(np.array([3.1, 1, 0])).scale(0.66)

        diferencia_simetrica_texto = Tex('$A \\triangle B = \{3, 4, 7\}$').move_to(np.array([3.5, -2, 0])).set_color('RED')

        diagrama_union = Union(diagrama_copia, circulo_b).set_fill('RED', opacity=1).set_stroke(color='BLACK', width=0)

        diagrama_i2 = Intersection(diagrama_copia, circulo_b).set_fill('BLACK', opacity=1).set_stroke(color='BLACK', width=0)

        borde_a3 = Circle(1.33, 'BLUE').move_to(circulo_a.get_center()).set_stroke(color='BLUE', width=10)

        borde_b2 = Circle(1.33, 'GREEN').move_to(np.array([-2.66, -0.5, 0])).set_stroke(color='GREEN', width=10)

        self.play(Transform(conjunto_referencial, diferencia_simetrica), Transform(definicion_c, definicion_ds), Transform(ac, diferencia_simetrica_texto), Transform(ul, ul_ds), diagrama_copia.animate.set_fill('RED', opacity=0), Create(diagrama_union), circulo_b.animate.set_fill('BLACK', opacity=0), Create(diagrama_i2), Uncreate(borde_a), Create(borde_a3), Uncreate(borde_b), Create(borde_b2), run_time = 1)
        self.wait(tiempo_entre_videos+5)

        ##########? Quitamos todo

        self.play(Uncreate(conjunto_referencial), Uncreate(definicion_c), Uncreate(ac), Uncreate(ul), Uncreate(diagrama_copia), Uncreate(diagrama_union), Uncreate(circulo_b), Uncreate(diagrama_i2), Uncreate(borde_a3), Uncreate(borde_b2), Uncreate(diagrama_u), Uncreate(u), Uncreate(u_igual_a), Uncreate(nuevo_a), Uncreate(otro_b), Uncreate(relleno_para_despues), run_time = 1)
        self.wait(3)
