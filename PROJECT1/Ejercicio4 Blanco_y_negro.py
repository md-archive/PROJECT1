from PIL import Image
import os
#
# -------------------------------------------------------------
#
# EJERCICIO 0.1 : IMAGEN EN COLOR A BLANCO Y NEGRO -> 1ra manera
#
# -------------------------------------------------------------
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
    color_a_blanco_y_negro()
buscar_imagen()
# -------------------------------------------------------------
#
# EJERCICIO 0.2 : IMAGEN EN COLOR A BLANCO Y NEGRO -> 2na manera
#
# -------------------------------------------------------------
# def buscar_imagen():
#     dirname = os.path.dirname(__file__)
#     filename = os.path.join(dirname, 'mister_rabbit.png')
#     mister_rabbit = Image.open(filename)
#     mister_rabbit.show()
#     def gris(p):
#         rojo, verde, azul = p
#         gr = int((rojo + verde + azul) / 3)
#         return (gr, gr, gr)
# # process_pixels_in_place
#     def proceso_pixels_lugar(f, mister_rabbit):
#         p = mister_rabbit.load()
#         sx, sy = mister_rabbit.size
#         for x in range(sx):
#             for y in range(sy):
#                 p[x, y] = f(p[x, y])
#     proceso_pixels_lugar(gris,mister_rabbit)
#     mister_rabbit.save('black_and_white_rabbit2.png')
# buscar_imagen()

