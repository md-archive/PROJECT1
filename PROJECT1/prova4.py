from PIL import Image
import os
#
def funcion4ProcessPixelsInPlace():
    # clamp
    def fijador(x):
        if x < 0: return 0
        elif x > 255: return 255
        else: return x
    # brightness
    def brillo(p,x):
        rojo, verde, azul = p
        rojo_fuera = fijador (int(rojo + x * 128))
        verde_fuera = fijador (int(verde + x * 128))
        azul_fuera = fijador (int(azul + x * 128))
        return (rojo_fuera, verde_fuera, azul_fuera)
    # contrast
    def contraste(p, x):
        rojo, verde, azul = p
        rojo_fuera = fijador(int(rojo * x))
        verde_fuera = fijador(int(verde * x))
        azul_fuera = fijador(int(azul * x))
        return (rojo_fuera, verde_fuera, azul_fuera)
    def procesado_pixels(f, i):
        p = i.load()
        i2 = i.copy()
        p2 = i2.load()
        sx, sy = i.size
        for x in range(sx):
            for y in range(sy):
                p2[x, y] = f(p[x, y])
        return i2
    # brillo_imagen
    def brillo_imagen(i, x):
        def b(p): return brillo(p, x)
        return procesado_pixels(b, i)
    # contrast_image
    def contraste_imagen(i, x):
        def c(p): return contraste(p, x)
        return procesado_pixels(c, i)
    def buscar_imagen():
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'mister_rabbit.png')
        mister_rabbit = Image.open(filename)
        mister_rabbit.show()
    #
        def color_a_blanco_y_negro():
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
            menosbrillo.save('menosbrillo.png')
            masbrillo.save('masbrillo.png')
            menosconstrastes.save('menosconstrastes.png')
            masconstrastes.save('masconstrastes.png')
        mister_rabbit.save(filename)
        color_a_blanco_y_negro()
    buscar_imagen()
funcion4ProcessPixelsInPlace()


# # grey
# def gris(p):
#     rojo, verde, azul = p
#     gr = int((rojo + verde + azul) / 3)
#     return (gr, gr, gr)
# # process_pixels_in_place
# def proceso_pixels_lugar(f, i):
#     p = i.load()
#     sx, sy = i.size
#     for x in range(sx):
#         for y in range(sy):
#             p[x, y] = f(p[x, y])
#     proceso_pixels_lugar(gris, i)
