from PIL import Image
import os
import sys
import subprocess
    #
    # -------------------------------------------------------------
    #
    # COMPROBAR SI PILLOW ESTA INSTALADO EN EL PC
    #
    # -------------------------------------------------------------
    #
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'Pillow'])

def funcion4BlackandWhite_1():
    #
    # -------------------------------------------------------------
    #
    # EJERCICIO 0.1 : IMAGEN EN COLOR A BLANCO Y NEGRO -> 1ra manera
    #
    # -------------------------------------------------------------
    #
    def buscar_imagen():
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'mister_rabbit.png')
        mister_rabbit = Image.open(filename)
        mister_rabbit.show()
        def color_a_blanco_y_negro():
            p = mister_rabbit.load()
            sx, sy = mister_rabbit.size
            for x in range(sx):
                for y in range(sy):
                    rojo, verde, azul = p[x, y]
                    gr = int((rojo + verde + azul) / 3)
                    p[x, y] = (gr, gr, gr)
            mister_rabbit.save('black_and_white_rabbit1.png')
            mister_rabbit.show()
        color_a_blanco_y_negro()
    buscar_imagen()
funcion4BlackandWhite_1()
    #
    # -------------------------------------------------------------
    #
    # EJERCICIO 0.2 : IMAGEN EN COLOR A BLANCO Y NEGRO -> 2na manera
    #
    # -------------------------------------------------------------
    #
def funcion4BlackandWhite_2():
    def buscar_imagen():
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'mister_rabbit.png')
        mister_rabbit = Image.open(filename)
        def gris(p):
            rojo, verde, azul = p
            gr = int((rojo + verde + azul) / 3)
            return (gr, gr, gr)
        # process_pixels_in_place
        def proceso_pixels_lugar(f, mister_rabbit):
            p = mister_rabbit.load()
            sx, sy = mister_rabbit.size
            for x in range(sx):
                for y in range(sy):
                    p[x, y] = f(p[x, y])
        proceso_pixels_lugar(gris,mister_rabbit)
        mister_rabbit.save('black_and_white_rabbit2.png')
        mister_rabbit.show()
    buscar_imagen()
funcion4BlackandWhite_2()
    #
    # -------------------------------------------------------------
    #
    # EJERCICIO 1 : CAMBIAR CONTRASTE Y BRILLO
    #
    # -------------------------------------------------------------
    #
def funcion4ProcessPixelsInPlace():
    # -- clamp --
    def fijador(x):
        if x < 0: return 0
        elif x > 255: return 255
        else: return x
    # -- brightness --
    def brillo(p,x):
        rojo, verde, azul = p
        rojo_fuera = fijador (int(rojo + x * 128))
        verde_fuera = fijador (int(verde + x * 128))
        azul_fuera = fijador (int(azul + x * 128))
        return (rojo_fuera, verde_fuera, azul_fuera)
    # -- contrast --
    def contraste(p, x):
        rojo, verde, azul = p
        rojo_fuera = fijador(int(rojo * x))
        verde_fuera = fijador(int(verde * x))
        azul_fuera = fijador(int(azul * x))
        return (rojo_fuera, verde_fuera, azul_fuera)
    # -- process_pixels --
    def procesado_pixels(f, i):
        p = i.load()
        i2 = i.copy()
        p2 = i2.load()
        sx, sy = i.size
        for x in range(sx):
            for y in range(sy):
                p2[x, y] = f(p[x, y])
        return i2
    # -- brillo_imagen --
    def brillo_imagen(i, x):
        def b(p): return brillo(p, x)
        return procesado_pixels(b, i)
    # -- contrast_image --
    def contraste_imagen(i, x):
        def c(p): return contraste(p, x)
        return procesado_pixels(c, i)
    #
    # -- SEARCH IMAGE --
    #
    def buscar_imagen():
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'mister_rabbit.png')
        mister_rabbit = Image.open(filename)
        def cambiar_contraste_brillo():
            p = mister_rabbit.load()
            sx, sy = mister_rabbit.size
            for x in range(sx):
                for y in range(sy):
                    rojo, verde, azul = p[x, y]
                    gr = int((rojo + verde + azul) / 3)
                    p[x, y] = (gr, gr, gr)
            menosbrillo = brillo_imagen(mister_rabbit, 0.5)
            masbrillo = brillo_imagen (mister_rabbit, -0.5)
            menosconstrastes = contraste_imagen(mister_rabbit, 0.25)
            masconstrastes = contraste_imagen(mister_rabbit, 1.5)
                        #
            menosbrillo.save('lessbright_rabbit.png')
            menosbrillo.show()
            masbrillo.save('morebright_rabbit.png')
            masbrillo.show()
            menosconstrastes.save('lesscontrast_rabbit.png')
            menosconstrastes.show()
            masconstrastes.save('morecontrast_rabbit.png')
            masconstrastes.show()
        cambiar_contraste_brillo()
    buscar_imagen()
funcion4ProcessPixelsInPlace()
    #
    # -------------------------------------------------------------
    #
    # EJERCICIO 2.1 : ROTAR IMAGEN
    #
    # -------------------------------------------------------------
    #

def funcion4FlipImage():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'mister_rabbit.png')
    mister_rabbit = Image.open(filename)
    #hflip
    def vueltahorizontal(mister_rabbit):
        p = mister_rabbit.load()
        sx, sy = mister_rabbit.size
        for x in range(sx // 2):
            for y in range(sy):
                r = p[x, y]
                p[x, y]
                p[x, y] = p[sx -x -1, y]
                p[sx - x - 1, y] = r
        
    #vflip
    def vueltavertical(mister_rabbit):
        p = mister_rabbit.load()
        sx, sy = mister_rabbit.size
        for y in range(sy // 2):
            for x in range(sx):
                r = p[x, y]
                p[x, y] = p[x, sy -y -1]
                p[x, sy -y -1] = r
       
    vueltahorizontal(mister_rabbit)
    vueltavertical(mister_rabbit)
    mister_rabbit.save('rotated_rabbit.png')
    mister_rabbit.show()
funcion4FlipImage()
    #
    # -------------------------------------------------------------
    #
    # EJERCICIO 2.2 : AÑADIR BORDE EN LA IMAGEN
    #
    # -------------------------------------------------------------
    #
def funcion4Border():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'mister_rabbit.png')
    mister_rabbit = Image.open(filename)
    # -- border --
    def borde(i, ancho, color):
        sx, sy = i.size
        p = i.load()
        i2 = Image.new('RGB', (sx + ancho * 2, sy + ancho * 2), color)
        p2 = i2.load()
        for x in range(sx):
            for y in range(sy):
                p2[x + ancho, y + ancho] = p[x, y]
        return i2
    bordered = borde(mister_rabbit, 20, (150,150,150))
    bordered.save("bordered_rabbit.png")
    bordered.show()
funcion4Border()
    #
    # -------------------------------------------------------------
    #
    # EJERCICIO 2.3 : DIFUMINAR LA IMAGEN (1ra manera)
    #
    # -------------------------------------------------------------
    #
def funcion4Fade_1():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'mister_rabbit.png')
    mister_rabbit = Image.open(filename)
    # -- border --
    def borde(mister_rabbit, ancho, color):
        sx, sy = mister_rabbit.size
        p = mister_rabbit.load()
        i2 = Image.new('RGB', (sx + ancho * 2, sy + ancho * 2), color)
        p2 = i2.load()
        for x in range(sx):
            for y in range(sy):
                p2[x + ancho, y + ancho] = p[x, y]
            return i2
    # -- blur --
        def difuminar(mister_rabbit):
            p = mister_rabbit.load()
            i2 = mister_rabbit.copy()
            p2 = i2.load()
            sx, sy = mister_rabbit.size
            for x in range (1, sx - 1):
                for y in range (1, sy - 1):
                    sumrojo, sumverde, sumazul = 0, 0, 0
                    for dx in range (-1, 2):
                        for dy in range(-1, 2):
                            recursorojo, recursoverde, recursoazul = p[x + dx, y + dy]
                            sumrojo = sumrojo + recursorojo
                            sumverde = sumverde + recursoverde
                            sumazul = sumazul + recursoazul
                    p2[x, y] = (int(sumrojo / 9), int(sumverde / 9), int(sumazul / 9))
            return i2
    #
        white_bordered = borde(mister_rabbit, 20, (255, 255, 255))
        blurred = difuminar(difuminar(difuminar(white_bordered)))
        blurred.save("blurred_rabbit_1.png")
        blurred.show()
funcion4Fade_1()
    #
    # -------------------------------------------------------------
    #
    # EJERCICIO 3 : DIFUMINAR LA IMAGEN (2na manera)
    #
    # -------------------------------------------------------------
    #
def funcion4Fade_2():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'mister_rabbit.png')
    mister_rabbit = Image.open(filename)
    # blur_in_place
    def difuminar_sitio(mister_rabbit):
         p = mister_rabbit.load()
         sx, sy = mister_rabbit.size
         for x in range (3, sx - 3):
             for y in range (3, sy - 3):
                sumrojo, sumverde, sumazul = 0, 0, 0
                for dx in range (-1, 2):
                    for dy in range(-1, 2):
                        recursorojo, recursoverde, recursoazul = p[x + dx, y +dy]
                        sumrojo = sumrojo + recursorojo
                        sumverde = sumverde + recursoverde
                        sumazul = sumazul + recursoazul
                p[x, y] = (int(sumrojo / 9), int(sumverde / 9), int(sumazul / 9))
    difuminar_sitio(mister_rabbit)
    mister_rabbit.save('blurred_rabbit_2.png')
    mister_rabbit.show()
funcion4Fade_2()
    #
    # -------------------------------------------------------------
    #
    # EJERCICIO 4 : AMPLIAR BORDE
    #
    # -------------------------------------------------------------
    #
def funcion4MakeImages():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'mister_rabbit.png')
    mister_rabbit = Image.open(filename)
    # -- boder --
    def borde(mister_rabbit, ancho, color):
            sx, sy = mister_rabbit.size
            p = mister_rabbit.load()
            i2 = Image.new('RGB', (sx + ancho * 2, sy + ancho * 2), color)
            p2 = i2.load()
            for x in range(sx):
                for y in range(sy):
                    p2[x + ancho, y + ancho] = p[x, y]
                return i2
    def difuminar_auto(mister_rabbit, n):
        mister_rabbit = borde(mister_rabbit, n, (255, 255, 255))
        for _ in range(n):
            mister_rabbit = difuminar_auto(mister_rabbit)
        return mister_rabbit
    # -- process_pixels --
    def procesado_pixels(f, mister_rabbit):
        p = mister_rabbit.load()
        i2 = mister_rabbit.copy()
        p2 = i2.load()
        sx, sy = mister_rabbit.size
        for x in range(sx):
            for y in range(sy):
                p2[x, y] = f(p[x, y])
        return i2
    # -- fade_by --
    def descolorear(f, p):
        rojo, verde, azul = p
        rojo_fuera = int((f * rojo + (100 - f) * 255 / 100))
        verde_fuera = int((f * verde + (100 - f) * 255 / 100))
        azul_fuera = int((f * azul + (100 - f) * 255 / 100))
        return (rojo_fuera, verde_fuera, azul_fuera)
    # -- make_images --
    def crear_imagen(mister_rabbit):
        images = []
        for x in range(100, -1, -5):
            def descolor(p): return descolorear(x, p)
            descoloro = procesado_pixels(descolor, mister_rabbit)
            images.append(descoloro)
        return images
    images = crear_imagen(mister_rabbit)
    images[0].save('difuminado_1.gif', save_all=True, append_images=images[1:], duration=100, loop=0)
    mister_rabbit.show()
funcion4MakeImages()
    #
    # -------------------------------------------------------------
    #
    # EJERCICIO 5 : CREAR GIF
    #
    # -------------------------------------------------------------
    #
def funcion4final():
    # -- blur_auto -- 
    def difuminar(mister_rabbit):
        p = mister_rabbit.load()
        i2 = mister_rabbit.copy()
        p2 = i2.load()
        sx, sy = mister_rabbit.size
        for x in range (1, sx - 1):
            for y in range (1, sy - 1):
                sumrojo, sumverde, sumazul = 0, 0, 0
                for dx in range (-1, 2):
                    for dy in range(-1, 2):
                        recursorojo, recursoverde, recursoazul = p[x + dx, y + dy]
                        sumrojo = sumrojo + recursorojo
                        sumverde = sumverde + recursoverde
                        sumazul = sumazul + recursoazul
                p2[x, y] = (int(sumrojo / 9), int(sumverde / 9), int(sumazul / 9))
        return i2
    def create_gif():
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'mister_rabbit.png')
        mister_rabbit = Image.open(filename)
        #
        images = [mister_rabbit]
        #
        print("Creating GIF, please wait.")
        #
        for _ in range(99):
            mister_rabbit = difuminar(mister_rabbit)
            images.append(mister_rabbit)
        #
        images[0].save('difuminado.gif', save_all=True, append_images=images[1:],
        duration=100, loop=0)
        print("GIF created succesfully")
        mister_rabbit.show()
    create_gif()
funcion4final()
