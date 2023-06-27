from manim import *
import numpy as np

class coord_cilindricas(Scene):
    def construct(self):  
        ##########? Introducción, ejes tradicionales, partícula, vector posición y labels
                
        intro = Tex('Sabemos que en los ejes tradicionales podemos escribir a la posición, velocidad y aceleración de una partícula puntual como').move_to(np.array([0, 2.5, 0])).scale(0.75)
        r_trad = Tex('$\\vec{r} = x(t) \hat{i} + y(t) \hat{j} + z(t) \hat{k}$').move_to(intro.get_center() + np.array([-3, -2.25, 0]))
        v_trad = Tex('$\\vec{v} = \dot{x}(t) \hat{i} + \dot{y}(t) \hat{j} + \dot{z}(t) \hat{k}$').add_updater(lambda p:  p.next_to(r_trad, np.array([0, -1, 0])))
        a_trad = Tex('$\\vec{a} = \ddot{x}(t) \hat{i} + \ddot{y}(t) \hat{j} + \ddot{z}(t) \hat{k}$').add_updater(lambda p:  p.next_to(v_trad, np.array([0, -1, 0])))
               
        axes = Axes(x_range=[-10, 10, 2], y_range=[-10, 10, 2], x_length=10, y_length=10).scale(0.5).move_to(intro.get_center() + np.array([3, -3.5, 0])).set_color(RED)
        
        labels = axes.get_axis_labels(Tex('$\hat{i}$').scale(0.75), Tex('$\hat{j}$').scale(0.75))
        
        particula = Dot(point=axes.get_center() + np.array([2, 1.5, 0]), radius=0.05, color=PURPLE_A)        
        
        vector = Arrow(start=axes.get_center(), end=particula.get_center(), buff=0, color=WHITE, max_stroke_width_to_length_ratio=1.5, tip_length=0.15)
        vector_label = Tex('$\\vec{r}$').move_to(particula.get_center() + np.array([0, -0.4, 0])).scale(0.75)
        
        xy = axes.get_lines_to_point(particula.get_center(), color=RED)
        p_relativo_al_grafico = particula.get_center() - axes.get_center()
        x_label = Tex("$x$").move_to(particula.get_center() + np.array([0, -p_relativo_al_grafico[1]-0.3, 0])).scale(0.75)
        y_label = Tex("$y$").move_to(particula.get_center() + np.array([-p_relativo_al_grafico[0]-0.3, 0, 0])).scale(0.75)
        
        nota = Tex('La coordenada correspondiente a $\hat{k}$ apunta hacia ti. Para simplificar el gráfico vamos a suponer que $z=0$').scale(0.4).move_to(np.array([3, -2.5, 0]))
        
        self.play(Write(intro), Write(r_trad), Write(v_trad), Write(a_trad), Create(axes), Create(labels), Create(particula), Create(vector), Write(vector_label), Create(xy), Create(x_label), Create(y_label), Write(nota), run_time = 2)
        self.wait(5)

        ##########? Hacemos que varios objetos se mantengan al tanto del movimiento de la partícula. Hacemos que la partícula rote
        
        # Hay mejores maneras de usar el add_updater, pero esta es la que aprendí por ahora
        vector.add_updater(lambda v: v.become(Arrow(start=axes.get_center(), end=particula.get_center(), buff=0, color=WHITE, max_stroke_width_to_length_ratio=1.5, tip_length=0.15)))
        vector_label.add_updater(lambda v: v.become(Tex('$\\vec{r}$').move_to(particula.get_center() + np.array([0, -0.4, 0])).scale(0.75)))
        xy.add_updater(lambda v: v.become(axes.get_lines_to_point(particula.get_center(), color=RED)))
        x_label.add_updater(lambda v: v.become(Tex("$x$").move_to(particula.get_center() + np.array([0, -(particula.get_center() - axes.get_center())[1]-0.3, 0])).scale(0.75)))
        y_label.add_updater(lambda v: v.become(Tex("$y$").move_to(particula.get_center() + np.array([-(particula.get_center() - axes.get_center())[0]-0.3, 0, 0])).scale(0.75)))
        
        self.add(vector, vector_label, xy, x_label, y_label)
        
        self.play(Rotate(particula, about_point=axes.get_center(), angle = 360 * DEGREES), run_time = 3)        
        self.wait(4)
        
        ##########? Explicamos nuestro objetivo, colocamos el nuevo gráfico y las nuevas coordenadas
        
        intro2 = Tex('Nuestra tarea actual será obtener las coordenadas cilíndricas').move_to(intro.get_center()).scale(0.75)
        r_cil = Tex('$\\vec{r} = r \hat{r} + z \hat{k}$').move_to(np.array([-3, 1.5, 0])).scale(0.75)
        v_cil = Tex('$\\vec{v} = \dot{r} \hat{r} + r \dot{\\theta} \hat{\\theta} + \dot{z} \hat{k}$').add_updater(lambda p:  p.next_to(r_cil, np.array([0, -1, 0]))).scale(0.75)
        a_cil = Tex('$\\vec{a} = (\ddot{r} - r \dot{\\theta}^2) \hat{r} + (2 \dot{r} \dot{\\theta} + r \ddot{\\theta}) \hat{\\theta} + \ddot{z} \hat{k}$').add_updater(lambda p:  p.next_to(v_cil, np.array([0, -1, 0]))).scale(0.75)
        
        aclaracion = Tex('Donde:').add_updater(lambda p:  p.next_to(a_cil, np.array([0, -2, 0]))).scale(0.4)
        aclaracion2 = Tex('$r$: Magnitud de la proyección de $\\vec{r}$ en el plano generado por $\hat{i}$ y $\hat{j}$, apuntando siempre en la dirección de $\hat{r}$').add_updater(lambda p:  p.next_to(aclaracion, np.array([0, -1, 0]))).scale(0.4)
        aclaracion3 = Tex('$\\theta$: Ángulo entre en el eje $\hat{i}$ y la proyección de $\\vec{r}$ en el plano mencionado').add_updater(lambda p:  p.next_to(aclaracion2, np.array([0, -1, 0]))).scale(0.4)
        aclaracion4 = Tex('$\hat{\\theta}$: Versor que apunta en la dirección donde crece $\\theta$').add_updater(lambda p:  p.next_to(aclaracion3, np.array([0, -1, 0]))).scale(0.4)
        aclaracion5 = Tex('$r$ y $\\theta$ dependen del tiempo, por lo tanto $r=r(t)$ y $\\theta = \\theta(t)$, pero no escribo los $(t)$ para simplificar la notación').add_updater(lambda p:  p.next_to(aclaracion4, np.array([0, -1, 0]))).scale(0.4)
        aclaracion6 = Tex('Obviamente todos los versores tienen módulo 1, pero hice los gráficos con distinto tamaño para que sea más fácil diferenciarlos').add_updater(lambda p:  p.next_to(aclaracion5, np.array([0, -1, 0]))).scale(0.4)
        
        p_relativo_al_grafico = particula.get_center() - axes.get_center()
        axes_polares = Axes(x_range=[-10, 10, 2], y_range=[-10, 10, 2], x_length=10, y_length=10).scale(0.25).move_to(axes.get_center()).rotate(angle = np.arctan(p_relativo_al_grafico[1]/p_relativo_al_grafico[0]), about_point=axes.get_center()).set_color(BLUE)
        
        r_versor_label = Tex('$\hat{r}$').scale(0.5).move_to(axes_polares.get_center() + np.array([axes_polares.x_length*0.125, -0.25, 0]))
        theta_versor_label = Tex('$\hat{\\theta}$').scale(0.5).move_to(axes_polares.get_center() + np.array([-0.25, axes_polares.y_length*0.125, 0]))
        
        r = axes_polares.get_lines_to_point(particula.get_center(), color=BLUE)
        r_label = Tex('$r$').move_to(particula.get_center() + np.array([0, 0.2, 0])).scale(0.5)
        
        arc = Arc(vector.get_length(), start_angle=0, angle=np.arctan(p_relativo_al_grafico[1]/p_relativo_al_grafico[0]), arc_center=axes_polares.get_center()).set_color(BLUE)
    
        theta = Tex('$\\theta$').scale(0.5).move_to(axes_polares.get_center() + np.array([vector.get_length()*1.1, 0, 0]))
        
        self.play(Transform(intro, intro2), Transform(r_trad, r_cil), Transform(v_trad,  v_cil), Transform(a_trad, a_cil), Create(axes_polares), Write(aclaracion), Write(aclaracion2), Write(aclaracion3), Write(aclaracion4), Write(aclaracion5), Write(aclaracion6), Rotate(r_versor_label, about_point=axes_polares.get_center(), angle =np.arctan(p_relativo_al_grafico[1]/p_relativo_al_grafico[0])), Rotate(theta_versor_label, about_point=axes_polares.get_center(), angle =np.arctan(p_relativo_al_grafico[1]/p_relativo_al_grafico[0])), Create(r), Write(r_label), Create(arc), Rotate(theta, about_point=axes_polares.get_center(), angle =np.arctan(p_relativo_al_grafico[1]/(2*p_relativo_al_grafico[0]))), run_time = 1)        
        self.wait(6)
        
        ##########? Hacemos que los nuevos objetos se mantengan al tanto del movimiento de la partícula. Hacemos que la partícula rote
        
        axes_polares.add_updater(lambda v: v.become(Axes(x_range=[-10, 10, 2], y_range=[-10, 10, 2], x_length=10, y_length=10).scale(0.25).move_to(axes.get_center()).rotate(angle = np.arctan((particula.get_center() - axes.get_center())[1]/(particula.get_center() - axes.get_center())[0]), about_point=axes.get_center()).set_color(BLUE)))
        
        r_versor_label.add_updater(lambda v: v.become(Tex('$\hat{r}$').scale(0.5).move_to(axes_polares.get_center() + np.array([axes_polares.x_length*0.125, -0.25, 0])).rotate(angle = np.arctan((particula.get_center() - axes.get_center())[1]/(particula.get_center() - axes.get_center())[0]), about_point=axes.get_center())))
        theta_versor_label.add_updater(lambda v: v.become(Tex('$\hat{\\theta}$').scale(0.5).move_to(axes_polares.get_center() + np.array([-0.25, axes_polares.y_length*0.125, 0])).rotate(angle = np.arctan((particula.get_center() - axes.get_center())[1]/(particula.get_center() - axes.get_center())[0]), about_point=axes.get_center())))
        
        r.add_updater(lambda v: v.become(axes_polares.get_lines_to_point(particula.get_center(), color=BLUE)))
        r_label.add_updater(lambda v: v.become(Tex('$r$').move_to(particula.get_center() + np.array([0, 0.2, 0])).scale(0.5)))
        
        arc.add_updater(lambda v: v.become(Arc(vector.get_length(), start_angle=0, angle=np.arctan((particula.get_center() - axes.get_center())[1]/(particula.get_center() - axes.get_center())[0]), arc_center=axes_polares.get_center()).set_color(BLUE)))
        
        theta.add_updater(lambda v: v.become(Tex('$\\theta$').scale(0.5).move_to(axes_polares.get_center() + np.array([vector.get_length()*1.1, 0, 0])).rotate(angle=np.arctan((particula.get_center() - axes.get_center())[1]/(2*(particula.get_center() - axes.get_center()))[0]), about_point=axes_polares.get_center())))
        
        self.add(axes_polares, r_versor_label, theta_versor_label, r, r_label, arc, theta)
        
        self.play(Rotate(particula, about_point=axes.get_center(), angle = 45 * DEGREES), run_time = 2)   
        self.play(Rotate(particula, about_point=axes.get_center(), angle = -45 * DEGREES), run_time = 2)
        self.wait(6)
        
        ##########? Empezamos a deducir a partir de lo que sabemos
        
        empezemos = Tex('Empecemos a deducir las fórmulas:').move_to(np.array([0, 3, 0])).scale(0.75)
        
        ya_sabemos = Tex('Ya sabemos que $\\vec{r} = r \hat{r} + z \hat{k}$, pues así es como decidimos definirlo').move_to(np.array([-3.5, 2.5, 0])).scale(0.5)
        
        self.play(Transform(intro, empezemos), Transform(r_trad, ya_sabemos), Unwrite(nota), Unwrite(a_trad), Unwrite(v_trad), Unwrite(aclaracion), Unwrite(aclaracion2), Unwrite(aclaracion3), Unwrite(aclaracion4), Unwrite(aclaracion5), Unwrite(aclaracion6), run_time = 1)
        self.wait(5)
        
        ##########?
        
        quienes = Tex('Cómo podemos encontrar la conversión entre $\hat{i}$ $\hat{j}$ y $\hat{r}$ $\hat{\\theta}$?').add_updater(lambda p:  p.next_to(r_trad, np.array([0, -1, 0]))).scale(0.5)
        
        self.play(Write(quienes), run_time = 1)
        self.wait(4)
        
        ##########?
        
        podemos = Tex('Podemos simplemente mirar el gráfico y observar que:').add_updater(lambda p:  p.next_to(quienes, np.array([0, -1, 0]))).scale(0.5)
        
        r_versor_formula = Tex('$\hat{r} = \hat{r}_i \hat{i} + \hat{r}_j \hat{j}$').add_updater(lambda p: p.move_to(podemos.get_center() + np.array([-1.75, -1, 0]))).scale(0.66)
        theta_versor_formula = Tex('$\hat{\\theta} = \hat{\\theta}_i \hat{i} + \hat{\\theta}_j \hat{j}$').add_updater(lambda p:  p.next_to(r_versor_formula, np.array([0, -1, 0]))).scale(0.66)
        
        podemos2 = Tex('$cos(\\theta) = \\frac{\hat{r}_i}{|\hat{r}|}$').add_updater(lambda p:  p.move_to(podemos.get_center() + np.array([1.75, -1, 0]))).scale(0.66)
        podemos3 = Tex('$sen(\\theta) = \\frac{\hat{r}_j}{|\hat{r}|}$').add_updater(lambda p:  p.next_to(podemos2, np.array([0, -1, 0]))).scale(0.66)
        podemos4 = Tex('$sen(\\theta) = \\frac{-\hat{\\theta}_i}{|\hat{\\theta}|}$').add_updater(lambda p:  p.next_to(podemos3, np.array([0, -1, 0]))).scale(0.66)
        podemos5 = Tex('$cos(\\theta) = \\frac{\hat{\\theta}_j}{|\hat{\\theta}|}$').add_updater(lambda p:  p.next_to(podemos4, np.array([0, -1, 0]))).scale(0.66)
        
        arc_auxiliar = Arc(0.33, start_angle=90*DEGREES, angle=arc.angle, arc_center=axes_polares.get_center()).set_color(BLUE)
        
        r_proyecciones = axes.get_lines_to_point(axes_polares.get_center() + np.array([1, 0.75, 0]), color=YELLOW)
        theta_proyecciones = axes.get_lines_to_point(axes_polares.get_center() + np.array([-0.71, 1, 0]), color=YELLOW)
        
        ri_label = Tex('$\hat{r}_i$').move_to(axes_polares.get_center() + np.array([1, -0.25, 0])).scale(0.5)
        rj_label = Tex('$\hat{r}_j$').move_to(axes_polares.get_center() + np.array([-0.2, 0.75, 0])).scale(0.5)
        
        thetai_label = Tex('$\hat{\\theta}_i$').move_to(axes_polares.get_center() + np.array([-0.71, -0.25, 0])).scale(0.5)
        thetaj_label = Tex('$\hat{\\theta}_j$').move_to(axes_polares.get_center() + np.array([0.2, 1, 0])).scale(0.5)
        
        self.play(Write(podemos), Write(r_versor_formula), Write(theta_versor_formula), Write(podemos2), Write(podemos3), Write(podemos4), Write(podemos5), Create(arc_auxiliar), Create(r_proyecciones), Create(theta_proyecciones), Write(ri_label), Write(rj_label), Write(thetai_label), Write(thetaj_label), run_time = 2)
        self.wait(7)
        
        ##########?
        
        por_lo = Tex('Por lo tanto:').move_to(np.array([-5.5, -2, 0])).scale(0.5)
        r_versor_form_obtenida = Tex('$\hat{r} = |\hat{r}| cos(\\theta) \hat{i} + |\hat{r}| sen(\\theta) \hat{j} = cos(\\theta) \hat{i} + sen(\\theta) \hat{j}$').move_to(np.array([-3.5, -2.75, 0])).scale(0.5)
        theta_versor_form_obtenida = Tex('$\hat{\\theta} = -|\hat{\\theta}| sen(\\theta) \hat{i} + |\hat{\\theta}| cos(\\theta) \hat{j} = - sen(\\theta) \hat{i} + cos(\\theta) \hat{j}$').move_to(np.array([-3.5, -3.25, 0])).scale(0.5)
        
        self.play(Write(por_lo), Write(r_versor_form_obtenida), Write(theta_versor_form_obtenida), run_time = 1)
        self.wait(6)
        
        ##########?
        
        r_definido = r_trad[0][12:22].copy().scale(2).scale(0.6)
        
        r_versor_form_obtenida2 = Tex('$\hat{r} = cos(\\theta) \hat{i} + sen(\\theta) \hat{j}$').move_to(np.array([0, 3.5, 0])).scale(0.6)
        theta_versor_form_obtenida2 = Tex('$\hat{\\theta} = - sen(\\theta) \hat{i} + cos(\\theta) \hat{j}$').move_to(np.array([0, 2, 0])).scale(0.6)
        
        buscar_v_cil = Tex('Busquemos $\\vec{v}$ derivando $\\vec{r} = r \hat{r} + z \hat{k}$ con respecto al tiempo:').move_to(np.array([-3.3, 1.25, 0])).scale(0.55)
        
        self.play(r_definido.animate.move_to(np.array([-3.5, 3.5, 0])), Transform(r_versor_form_obtenida, r_versor_form_obtenida2), Transform(theta_versor_form_obtenida, theta_versor_form_obtenida2), Write(buscar_v_cil), Unwrite(intro), Unwrite(r_trad), Unwrite(quienes), Unwrite(podemos), Unwrite(podemos2), Unwrite(podemos3), Unwrite(podemos4), Unwrite(podemos5), Unwrite(r_versor_formula), Unwrite(theta_versor_formula), Uncreate(arc_auxiliar), Uncreate(r_proyecciones), Uncreate(theta_proyecciones), Unwrite(ri_label), Unwrite(rj_label), Unwrite(thetai_label), Unwrite(thetaj_label), Unwrite(por_lo), run_time = 1)
        self.wait(5)
        
        ##########?
        
        r_derivada = Tex('$\\vec{v} = \\frac{d \\vec{r}}{dt} = \dot{\\vec{r}} = \dot{r} \hat{r} + r \dot{\hat{r}} + \dot{z} \hat{k} + z \dot{\hat{k}}$').move_to(np.array([-3.5, 0.25, 0])).scale(0.75)
        
        self.play(Write(r_derivada), run_time = 1)
        self.wait(8)
        
        ##########?
        
        aclaracion = Tex('Sin embargo podemos deducir que:').move_to(np.array([-3.5, -0.5, 0])).scale(0.6)
        
        derivada_versor = Tex('$\dot{\hat{r}} = \\frac{d \hat{r}}{dt} = - sen(\\theta) \dot{\\theta} \hat{i} + cos(\\theta) \dot{\\theta} \hat{j}$').move_to(np.array([-3.5, -1.25, 0])).scale(0.75)
        
        self.play(Write(aclaracion), Write(derivada_versor), run_time = 1)
        self.wait(5)
        
        ##########?
        
        derivada_versor2 = Tex('$= \dot{\\theta} (- sen(\\theta) \hat{i} + cos(\\theta) \hat{j}) $').move_to(np.array([-2.85, -2, 0])).scale(0.75)
            
        self.play(Write(derivada_versor2), run_time = 1)
        self.wait(3)
        
        ##########?
        
        derivada_versor3 = Tex('$= \dot{\\theta} \hat{\\theta} $').move_to(np.array([-4.425, -2.75, 0])).scale(0.75)
        
        self.play(Write(derivada_versor3), Indicate(theta_versor_form_obtenida), run_time = 1)
        self.wait(4)
        
        ##########?
        
        tambien = Tex('También sabemos que $\dot{\hat{k}} = 0$, ya que $\hat{k}$ se mantiene en una posición constante').move_to(np.array([-2.25, -3.5, 0])).scale(0.55)
        
        self.play(Write(tambien), run_time = 1)
        self.wait(5)
        
        ##########?
        
        r_versor_derivado_encontrado = derivada_versor3[0].copy().scale(1.333).scale(0.6)
        r_versor_derivado_encontrado2 = Tex('$\dot{\hat{r}} = \dot{\\theta} \hat{\\theta} $').move_to(np.array([3.5, 3.5, 0])).scale(0.75)
        
        k_versor_derivado_encontrado = tambien[0][18:23].copy().scale(1.818).scale(0.6)
        
        reorganizando = Tex('Reorganizando un poco llegamos a que:').move_to(np.array([0, 1, 0])).scale(0.7)
        v_cil_encontrado = Tex('$\\vec{v} = \dot{r} \hat{r} + r \dot{\\theta} \hat{\\theta} + \dot{z} \hat{k}$').move_to(np.array([0, 0, 0])).scale(0.7)
        
        self.play(r_versor_derivado_encontrado.animate.move_to(np.array([3.5, 3.5, 0])), Transform(r_versor_derivado_encontrado, r_versor_derivado_encontrado2), k_versor_derivado_encontrado.animate.move_to(np.array([3.5, 2.75, 0])), Transform(buscar_v_cil, reorganizando), Transform(r_derivada, v_cil_encontrado), Unwrite(aclaracion), Unwrite(derivada_versor), Unwrite(derivada_versor2), Unwrite(derivada_versor3), Unwrite(tambien), Uncreate(axes), Uncreate(labels), Uncreate(particula), Uncreate(vector), Unwrite(vector_label), Uncreate(xy), Unwrite(x_label), Unwrite(y_label), Uncreate(axes_polares), Uncreate(r_versor_label), Uncreate(theta_versor_label), Uncreate(r), Unwrite(r_label), Uncreate(arc), Uncreate(theta), run_time = 1)
        self.wait(4)
        
        ##########?
        
        nombres_v = Tex('En consecuencia, $\dot{r}$ se llama velocidad radial, mientras que $r \dot{\\theta}$ velocidad tangencial').move_to(np.array([0, -1.25, 0])).scale(0.7)
        
        self.play(Write(nombres_v), run_time = 1)
        self.wait(6)
        
        ##########?
        
        v_derivada_planteo = Tex('Derivemos nuevamente para obtener la aceleración').move_to(np.array([0, 1, 0])).scale(0.7)
        
        self.play(Transform(buscar_v_cil, v_derivada_planteo), Unwrite(nombres_v), run_time = 1)
        self.wait(2)
        
        ##########?
        
        v_derivada = Tex('$\\vec{a} = \\frac{d \\vec{v}}{dt} = \dot{\\vec{v}} = \ddot{r} \hat{r} + \dot{r} \dot{\hat{r}} + \dot{r} \dot{\\theta} \hat{\\theta} + r \ddot{\\theta} \hat{\\theta} + r \dot{\\theta} \dot{\hat{\\theta}} + \ddot{z} \hat{k} + \dot{z} \dot{\hat{k}}$').move_to(np.array([0, -1.25, 0])).scale(0.7)
        
        self.play(Write(v_derivada), run_time = 1)
        self.wait(7)
        
        ##########?
        
        sin_emb = Tex('Sin embargo').move_to(np.array([0, -2.25, 0])).scale(0.7)
        
        theta_versor_derivada = Tex('$\dot{\hat{\\theta}} = \\frac{d \hat{\\theta}}{dt} = - cos(\\theta) \dot{\\theta} \hat{i} - sen(\\theta) \dot{\\theta} \hat{j} = - \dot{\\theta} (cos(\\theta) \hat{i} + sen(\\theta) \hat{j})$').move_to(np.array([-1, -3.25, 0])).scale(0.7)
        
        self.play(Write(sin_emb), Write(theta_versor_derivada), run_time = 1)
        self.wait(7)
        
        ##########?
        
        theta_versor_derivada2 = Tex('$= - \dot{\\theta} \hat{r}$').move_to(np.array([3.85, -3.25, 0])).scale(0.7)
        
        self.play(Write(theta_versor_derivada2), Indicate(r_versor_form_obtenida), run_time = 1)
        self.wait(5)
        
        ##########?
        
        theta_versor_derivada_encontrada = theta_versor_derivada2[0][1:].copy().scale(1.4285).scale(0.6)
        theta_versor_derivada_encontrada2 = Tex('$\dot{\hat{\\theta}} = - \dot{\\theta} \hat{r}$').move_to(np.array([3.5, 2, 0])).scale(0.6)
        
        si_reemp = Tex('Si reemplazamos $\dot{\hat{r}}$, $\dot{\hat{\\theta}}$ y $\dot{\hat{k}}$ en $\\vec{a}$, se obtiene:').move_to(np.array([0, 1, 0])).scale(0.7)
        
        self.play(Transform(buscar_v_cil, si_reemp), r_derivada.animate.move_to(np.array([-3.5, 2, 0])), v_derivada.animate.move_to(np.array([0, 0, 0])), theta_versor_derivada_encontrada.animate.move_to(np.array([3.5, 2, 0])), Transform(theta_versor_derivada_encontrada, theta_versor_derivada_encontrada2), Unwrite(sin_emb), Unwrite(theta_versor_derivada), Unwrite(theta_versor_derivada2), run_time = 1)
        self.wait(3)
        
        ##########?
        
        self.play(Indicate(r_versor_derivado_encontrado), Indicate(k_versor_derivado_encontrado), Indicate(theta_versor_derivada_encontrada), run_time = 1)
        self.wait(1)   
        
        ##########?
        
        v_derivada_reemp = Tex('$= \ddot{r} \hat{r} + \dot{r} (\dot{\\theta} \hat{\\theta}) + \dot{r} \dot{\\theta} \hat{\\theta} + r \ddot{\\theta} \hat{\\theta} + r \dot{\\theta} (- \dot{\\theta} \hat{r}) + \ddot{z} \hat{k}$').move_to(np.array([1.075, -1, 0])).scale(0.7)
        
        self.play(Write(v_derivada_reemp), run_time = 1)
        self.wait(7)
        
        ##########?
        
        a_cil_encontrado = Tex('$\\vec{a} = ( \ddot{r} - r \dot{\\theta}^2) \hat{r} + (2 \dot{r} \dot{\\theta} + r \ddot{\\theta} )  \hat{\\theta} + \ddot{z} \hat{k}$').move_to(np.array([0.225, -2, 0])).scale(0.7)
        
        self.play(Write(a_cil_encontrado), run_time = 1)
        self.wait(7)
        
        ##########?
        
        consecuencia = Tex('En consecuencia, $\ddot{r} - r \dot{\\theta}^2$ se llama aceleración radial, mientras que $2 \dot{r} \dot{\\theta} + r \ddot{\\theta}$ aceleración tangencial').move_to(np.array([0, 0, 0])).scale(0.7)
        
        self.play(a_cil_encontrado.animate.move_to(np.array([0, 1, 0])), Write(consecuencia), Unwrite(buscar_v_cil), Unwrite(v_derivada), Unwrite(v_derivada_reemp), run_time = 1)
        self.wait(8)
        
        ##########?
        
        listo = Tex('Ya encontramos las fórmulas de la posición, velocidad y aceleración utilizando coordenadas cilíndricas').move_to(np.array([0, 3.5, 0])).scale(0.6)
        
        self.play(Write(listo), r_definido.animate.move_to(np.array([0, 2.5, 0])), r_derivada.animate.move_to(np.array([0, 1.5, 0])), a_cil_encontrado.animate.scale(1.4285).scale(0.6), a_cil_encontrado.animate.move_to(np.array([0, 0.5, 0])), Unwrite(r_versor_form_obtenida), Unwrite(theta_versor_form_obtenida), Unwrite(r_versor_derivado_encontrado), Unwrite(k_versor_derivado_encontrado), Unwrite(theta_versor_derivada_encontrada), Unwrite(consecuencia), run_time = 1)
        self.wait(2)
        
        ##########?
        
        box_r = SurroundingRectangle(r_definido)
        box_v = SurroundingRectangle(r_derivada)
        box_a = SurroundingRectangle(a_cil_encontrado)                

        self.play(Create(box_r), Create(box_v), Create(box_a), run_time = 1)
        self.wait(5)
        
        ##########?
        
        yahora = Tex('En particular, si el movimiento es en el plano $\hat{x} \hat{y}$, entonces $z = z(t) = 0 \\Rightarrow \dot{z} = \ddot{z} = 0$, y las coordenadas cilíndricas se convierten en polares:').move_to(np.array([0, -0.5, 0])).scale(0.6)

        self.play(Write(yahora), run_time = 1)
        self.wait(6)                

        ##########?
        
        r_polar = Tex('$\\vec{r} = r \hat{r}$').move_to(np.array([0, -1.5, 0])).scale(0.6)
        v_polar = Tex('$\\vec{v} = \dot{r} \hat{r} + r \dot{\\theta} \hat{\\theta}$').move_to(np.array([0, -2.5, 0])).scale(0.6)
        a_polar = Tex('$\\vec{a} = ( \ddot{r} - r \dot{\\theta}^2) \hat{r} + (2 \dot{r} \dot{\\theta} + r \ddot{\\theta} )  \hat{\\theta}$').move_to(np.array([0, -3.5, 0])).scale(0.6)

        self.play(Write(r_polar), Write(v_polar), Write(a_polar), run_time = 1)
        self.wait(3)                
        
        ##########?
        
        box_r_polar = SurroundingRectangle(r_polar)
        box_v_polar = SurroundingRectangle(v_polar)
        box_a_polar = SurroundingRectangle(a_polar)                

        self.play(Create(box_r_polar), Create(box_v_polar), Create(box_a_polar), run_time = 1)
        self.wait(5)
