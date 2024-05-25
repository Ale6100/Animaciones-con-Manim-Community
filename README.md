# Animaciones con Manim Community

Bienvenido! En este repositorio dejaré el código base de varias animaciones matemáticas hechas con [Manim Community](https://docs.manim.community/en/stable/index.html). La mayoría de estos videos los subo a [mi canal de YouTube](https://www.youtube.com/channel/UCfgt4--XgLnHxYNDPOvYioA)

Me falta aprender mucho de esta librería pero poco a poco voy a ir guardando acá algunas animaciones que se me vayan ocurriendo.

Es importante aclarar que es un módulo en desarrollo, la versión actual es la 0.18.1

## Comenzando 🚀

Lee atentamente las siguientes instrucciones si deseas obtener una copia funcional del proyecto en tu computadora.

Descarga el archivo comprimido _zip_ desde el botón "code" o hacer click [aquí](https://github.com/Ale6100/animaciones-con-manim-community/archive/refs/heads/main.zip).

### Pre-requisitos 📋

Necesitas tener previamente descargado e instalado [Manim Community](https://docs.manim.community/en/stable/installation/windows.html). Tal como se especifica en su documentación, se recomienda hacer la instalación completa con [chocolatey](https://chocolatey.org/) ya que para ejecutar estos códigos se necesitan otras dependencias como [ffmpeg](https://ffmpeg.org/) y [LaTeX](https://es.wikipedia.org/wiki/LaTeX), que son más fáciles de instalar de este modo.

## Desarrollo 👷

Ejecuta el código que desees con el comando

```bash
manim -pql X.py Y
```

Donde:

* `p` el video se abre cuando termina de renderizarse

* `ql` indica la calidad del video. `ql`, `qm`, `qh` y `qk` es calidad baja, media, HD y HD 4k respectivamente

* `X.py` es el nombre del archivo Python donde tenemos el código

* `Y` es el nombre de la escena que va a renderizarse (es decir, clase principal que creará la animación)

Por ejemplo en la carpeta de este proyecto puedes ejecutar:

```bash
manim -pql teorema_de_lagrange_en_r.py lagrange_en_r
```

otros comandos son:

* `f` se abrirá la carpeta contenedora del video generado

* `--format=[png|gif|mp4|webm|mov]` formato del archivo generado

Click [aquí](https://docs.manim.community/en/stable/guides/configuration.html) para más información.

## Construido con 🛠️

* Python
* [Manim Community](https://docs.manim.community/)

## Autor ✒️

| ![Alejandro Portaluppi](https://avatars.githubusercontent.com/u/107259761?size=50)
|:-:
| **Alejandro Portaluppi**
|[![GitHub](https://img.shields.io/badge/github-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ale6100) [![LinkedIn](https://img.shields.io/badge/linkedin%20-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alejandro-portaluppi)
