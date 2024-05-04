from manim import Scene, NumberPlane, Tex, Write, Transform, Unwrite, Circle, Create, Dot, FadeIn, FadeOut, Ellipse, SurroundingRectangle
import numpy as np

class conjuntos_numericos(Scene):
    def construct(self):
        tiempo_entre_videos = 3

        grid = NumberPlane().set_opacity(0.33)
        self.add(grid)

        titulo = Tex('Conjuntos numéricos').scale(1.33)
        self.play(Write(titulo), run_time = 1)
        self.wait(tiempo_entre_videos-1)

        ##########? #Agrega el enunciado

        enunciado = Tex('Definición informal: Un conjunto es una coleccion de objetos, llamados elementos, que tiene la propiedad que dado un objeto cualquiera, se puede decidir si ese objeto es un elemento del conjunto o no.').move_to(np.array([0, 2.01, 0])).scale(0.8)
        self.play(Transform(titulo, enunciado), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? #Agrega los conjuntos A, B, C y D como ejemplo

        A = Tex('$A = \{3, 4, 5, 8, 34\}$').move_to(np.array([0, 0, 0]))

        B = Tex('$B = \{1, \{1\}, \{2, 64\}\}$').move_to(np.array([0, -1, 0]))

        C = Tex('$C = \{x \in \mathbb{R} \mid x > 0\}$').move_to(np.array([0, -2, 0]))

        D = Tex('$D = \{Arroz, Canela, Leche, Azucar, 500\}$').move_to(np.array([0, -3, 0]))

        self.play(Write(A), Write(B), Write(C), Write(D), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? Decir que el orden no importa

        orden_no_importa = Tex('El orden de los elementos no importa en un conjunto, y en un conjunto no se tiene en cuenta repeticiones de elementos').move_to(np.array([0, 2.01, 0])).scale(0.8)

        A2 = Tex('$A2 = \{8, 34, 4, 3, 5\}$').move_to(np.array([0, -1, 0]))

        A3 = Tex('$A2 = \{3, 4, 5, 8, 34, 5, 3\}$').move_to(np.array([0, -2, 0]))

        a_iguales = Tex('$A = A2 = A3$').move_to(np.array([0, -3, 0]))

        self.play(Transform(titulo, orden_no_importa), Transform(B, A2), Transform(C, A3), Transform(D, a_iguales), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? Mostrar que el orden no importa

        texto_pertenencia = Tex('Se dice que cada elemento $a$ de un conjunto $A$ pertenece a $A$ y se nota $a \in A$. Si un elemento $b$ no pertenece al conjunto $A$, se nota $b \\notin A$').move_to(np.array([0, 2.01, 0])).scale(0.8)

        ocho_pertenece = Tex('$8 \in A$').move_to(np.array([0, -1, 0]))

        uno_no_pertenece = Tex('$1 \\notin A$').move_to(np.array([0, -2, 0]))

        self.play(Transform(titulo, texto_pertenencia), Transform(B, ocho_pertenece), Transform(C, uno_no_pertenece), Unwrite(D), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? Diagramas de Venn

        diagrama_venn = Tex('Los conjuntos se suelen representar gráficamente por los llamados diagramas de Venn: simplemente se utiliza una circunferencia para representar el conjunto, y eventualmente en el interior sus elementos.').move_to(np.array([0, 2.5, 0])).scale(0.8)

        diagrama = Circle(2, 'BLUE').move_to(np.array([-0, -0.55, 0]))

        nuevo_a = Tex('$A = \{3, 4, 5\}$').move_to(np.array([-0, -3.5, 0])).set_color('BLUE')

        a_diagrama = Tex('$A$').set_color('BLUE').add_updater(lambda v: v.move_to(diagrama.get_center() + np.array([-2.1, 1, 0])))

        punto_tres = Dot().set_color('RED').add_updater(lambda v: v.move_to(diagrama.get_center() + np.array([-0.75, 0.75, 0])))
        tres = Tex('$3$').set_color('RED').add_updater(lambda v: v.move_to(punto_tres.get_center() + np.array([-0.33, 0, 0])))

        punto_cuatro = Dot().set_color('ORANGE').add_updater(lambda v: v.move_to(diagrama.get_center() + np.array([0.75, 0.75, 0])))
        cuatro = Tex('$4$').set_color('ORANGE').add_updater(lambda v: v.move_to(punto_cuatro.get_center() + np.array([0.33, 0, 0])))

        punto_cinco = Dot().set_color('GREEN').add_updater(lambda v: v.move_to(diagrama.get_center() + np.array([0, -0.75, 0])))
        cinco = Tex('$5$').set_color('GREEN').add_updater(lambda v: v.move_to(punto_cinco.get_center() + np.array([0, -0.33, 0])))

        self.play(Transform(titulo, diagrama_venn), Write(nuevo_a), Write(a_diagrama), Create(diagrama), Write(tres), Write(cuatro), Write(cinco), Create(punto_tres), Create(punto_cuatro), Create(punto_cinco), Unwrite(A), Unwrite(B), Unwrite(C), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? Subconjuntos e inclusión

        inclusion = Tex('Sean $A$ y $B$ conjuntos, se dice que $B$ está incluído en $A$ si para todo $x$, se tiene que si $x$ pertenece a $B$ entonces $x$ pertenece a $A$, y $B$ no está incluído en $A$ si existe $x$ perteneciendo a $B$ tal que no pertenece a $A$. Esto se escribe:').move_to(np.array([0, 2.1, 0])).scale(0.8)

        inclusion_formal = Tex('$B \subseteq A$ si $\\forall x$, $x \\in B \\Rightarrow x \in A$, $B \\nsubseteq A$ si $\\exists x \in B : x \\notin A$').move_to(np.array([0, -1, 0]))

        self.play(Transform(titulo, inclusion), Write(inclusion_formal), nuevo_a.animate.set_opacity(0), a_diagrama.animate.set_opacity(0), FadeOut(diagrama), tres.animate.set_opacity(0), cuatro.animate.set_opacity(0), cinco.animate.set_opacity(0), punto_tres.animate.set_opacity(0), punto_cuatro.animate.set_opacity(0), punto_cinco.animate.set_opacity(0), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########? Mostrar ejemplo B incluído en A

        diagrama.move_to(np.array([-3.25, -0.55, 0]))

        nuevo_a.move_to(np.array([0, 1, 0]))

        B = Tex('$B = \{3, 4\}$').move_to(np.array([0, -1, 0])).set_color('YELLOW')

        diagrama_b = Ellipse(width = 2.75, height = 1.33).set_color('YELLOW')
        diagrama_b.add_updater(lambda v: v.move_to((punto_tres.get_center() + punto_cuatro.get_center())/2))

        self.play(inclusion_formal.animate.move_to(np.array([0, 3, 0])), Create(diagrama_b), Write(B), Unwrite(titulo), nuevo_a.animate.set_opacity(1), a_diagrama.animate.set_opacity(1), FadeIn(diagrama), tres.animate.set_opacity(1), cuatro.animate.set_opacity(1), cinco.animate.set_opacity(1), punto_tres.animate.set_opacity(1), punto_cuatro.animate.set_opacity(1), punto_cinco.animate.set_opacity(1), run_time = 1)
        self.wait(tiempo_entre_videos)

        ##########?

        # Hacer que se coloree en rojo la parte del texto inclusion_formal que se corresponde con la primera afirmación

        recorte = inclusion_formal[0][0:15]

        remarcar = recorte.copy().set_color('RED')

        b_incluido_en_a = Tex('$\\Rightarrow B \subseteq A$').move_to(np.array([3.5, 0, 0]))
        box_b_incluido_en_a = SurroundingRectangle(b_incluido_en_a, buff = 0.1)

        self.play(Write(b_incluido_en_a), Create(box_b_incluido_en_a), Transform(recorte, remarcar), run_time = 1)
        self.wait(tiempo_entre_videos)

