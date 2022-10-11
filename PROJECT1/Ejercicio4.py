from PIL import Image
import sys
import subprocess
#
import os
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'Pillow'])
#
# def funcion4ProcessPixelsInPlace():
# def funcion4FlipImage():
# def funcion4Border():
# def funcion4ProcessPixels():
# def funcion4Fade():
# def funcion4MakeImages():
# def funcion4final():
# # brightness_image

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
    rojo_fuera = fijador (int(rojo * x))
    verde_fuera = fijador (int(verde * x))
    azul_fuera = fijador (int(azul * x))
    return (rojo_fuera, verde_fuera, azul_fuera)
# brillo_imagen
def brillo_imagen(i, x):
        def b(p): return brillo(p, x)
        return procesado_pixels(b, i)
# contrast_image
def contraste_imagen(i, x):
    def c(p): return contraste(p, x)
    return procesado_pixels(c, i)

def gris(p):
    rojo, verde, azul = p
    gr = int((rojo + verde + azul) / 3)
    return (gr, gr, gr)

def proceso_pixels_lugar(f, i):
    p = i.load()
    sx, sy = i.size
    for x in range(sx):
        for y in range(sy):
            p[x, y] = f(p[x, y])
            
def difuminado(i):
    p = i.load()
    i2 = i.copy()
    p2 = i2.load()
    sx, sy = i.size
    for x in range(1, sx - 1):
        for y in range(1, sy - 1):
            sumrojo, sumverde, sumazul = 0, 0, 0, 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    recursorojo, recursoverde,recursoazul = p[x + dx, y + dy]
                    sumrojo += recursorojo
                    sumverde += recursoverde
                    sumazul += recursoazul
            p2[x, y] = (int(sumrojo / 9), int(sumverde / 9), int(sumazul / 9))
    return i2   
                 
def descolorear(f, p):
    rojo, verde, azul = p
    rojo_fuera = int((f * rojo + (100 - f) * 255 / 100))
    verde_fuera = int((f * verde + (100 - f) * 255 / 100))
    azul_fuera = int((f * rojo + (100 - f) * 255 / 100))
    return (rojo_fuera, verde_fuera, azul_fuera)

def borde(i, ancho, color):
    sx, sy = i.size
    p = i.load()
    i2 = Image.new('RGB', (sx + ancho * 2, sy + ancho * 2), color)
    p2 = i2.load()
    for x in range(sx):
        for y in range(sy):
            p2[x + ancho, y + ancho] = p[x, y]
    return i2

def procesado_pixels(f, i):
    p = i.load()
    i2 = i.copy()
    p2 = i2.load()
    sx, sy = i.size
    for x in range(sx):
        for y in range(sy):
            p2[x, y] = f(p[x, y])
    return i2






#hflip
def vueltahorizontal(i):
    p = i.load()
    sx, sy = i.size
    for x in range(sx // 2):
        for y in range(sy):
            r = p[x, y]
            p[x, y]
            p[x, y] = p[sx -x -1, y]
            p[sx - x - 1, y] = r
#vflip
def vueltavertical(i):
    p = i.load()
    sx, sy = i.size
    for y in range(sy // 2):
        for x in range(sy):
            r = p[x, y]
            p[x, y]
            p[x, y] = p[x -sy -y -1]
            p[x -sy -y -1] = r
            
def rotar180(i):
    vueltahorizontal(i)
    vueltavertical(i)
# blur_in_place
def difuminar(i):
    p = i.load()
    sx, sy = i.size
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
# blur_auto   
def difuminar_auto(i, n):
    i = borde(i, n, (255, 255, 255))
    for x in range(n):
        i = difuminar(i)
    return i
def crear_imagen(i):
    images = []
    for x in range(100, -1, -5):
        def descolor(p): return descolorear(x, p)
        descoloro = procesado_pixels(descolor, i)
        images.append(descoloro)
    return images

try:
    i = Image.open('..\\imagen.png')
    p = i.load()
    sx, sy = i.size
    for x in range(sx):
        for y in range(sy):
            rojo, verde, azul = p[x, y]
            gr = int((rojo + verde + azul) / 3)
            p[x, y] = (gr, gr, gr)
    #
    menosbrillo = brillo_imagen(i, 0.5)
    masbrillo = brillo_imagen (i, -0.5)
    menosconstrastes = contraste_imagen (i, 0.25)
    masconstrastes = contraste_imagen (i, 1.5)
    #
    brillo.save('menosbrillo.png')
    masbrillo.save('masbrillo.png')
    menosconstrastes.save('menosconstrastes.png')
    masconstrastes.save('masconstrastes.png')
    #
    i = Image.open('imagen.png')
    images = [i]

    for x in range(99):
        i = difuminar(i)
        images.append(i)

    images[0].save('difuminado.gif', save_all=True, append_images=images[1:], duration=100, loop=0)
except:
    print("NO IMAGE FOUND!!")
finally:
    print("GOOD BYE!!")
