import cv2 as cv
import numpy as np
from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import ImageTk
from PIL import Image
def showimage():
    flm=filedialog.askopenfilename(initialdir=os.getcwd(),title="Selec Image File",
                                filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("All Files","*.*")))
    img=Image.open(flm)
    img.thumbnail((800,800))
    img= ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image=img
    return flm

class Color(object):
    def __init__(self, red=0, green=0, blue=0,alpha=None):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def imprimir(self):
        print(self.red)
        print(self.green)
        print(self.blue)


def convertir(num):
    if(num[0] == '1'):
        if (num[1] == '1'):
            if (num[2]=='1'):
                return 7
            else:
                return 6
        else:
            if (num[2]=='1'):
                return 5
            else:
                return 4
    else:
        if (num[1] == '1'):
            if (num[2]=='1'):
                return 3
            else:
                return 2
        else:
            if (num[2]=='1'):
                return 1
            else:
                return 0

class OctreeNode(object):
    def __init__(self,level,parent):
        self.color = Color(0, 0, 0)
        self.contadorpixel = 0
        self.indicePaleta=0
        self.children = [None for _ in range(8)]
        
        if level < OctreeQuantizer.MAX_PROFUNDIDAD - 1:
            parent.add_level_node(level, self)

    def add_color(self,color,level,parent):
        
        if level >= OctreeQuantizer.MAX_PROFUNDIDAD:
            self.color.red += color.red
            self.color.green += color.green
            self.color.blue += color.blue
            self.contadorpixel += 1
            return

        indice = self.get_indiceColorByLevel(color,level)
        if not self.children[indice]:
            self.children[indice] = OctreeNode(level, parent)
        self.children[indice].add_color(color, level + 1, parent)

    def esHoja(self):
        return self.contadorpixel>0

    def get_NodosHoja(self):
        nodosHoja=[]
        for i in range(8):
            nodo=self.children[i]
            if nodo:
                if nodo.esHoja():
                    nodosHoja.append(nodo)
                else:
                    nodosHoja.extend(nodo.get_NodosHoja())
        return nodosHoja

    def get_ContadorPixel(self):
        suma = self.contadorpixel
        for i in range(8):
            nodo=self.children[i]
            if nodo:
                suma+=nodo.contadorpixel
        return suma
    
    def reduce(self):
        result=0
        for i in range(8):
            nodo=self.children[i]
            if nodo:
                self.color.red+=nodo.color.red
                self.color.green+=nodo.color.green
                self.color.blue+=nodo.color.blue
                self.contadorpixel+=nodo.contadorpixel
                result+=1
        self.children=[]
        return result - 1


    def get_indiceColorByLevel(self, color, level):

        index = 0
        mask = 0x80 >> level
        if color.red & mask:
            index |= 4
        if color.green & mask:
            index |= 2
        if color.blue & mask:
            index |= 1
        return index
    
    def get_Color(self):
        return(Color(self.color.red / self.contadorpixel,
            self.color.green / self.contadorpixel,
            self.color.blue / self.contadorpixel))

    def get_IndicePaleta(self,color,level):

        if self.esHoja():
            return self.indicePaleta
        indice = self.get_indiceColorByLevel(color,level)
        if self.children[indice]:
            return self.children[indice].get_IndicePaleta(color,level+1)
        else:

            for i in range(8):
                if self.children[i]:
                    return self.children[i].get_IndicePaleta(color,level+1)


class OctreeQuantizer(object):
    MAX_PROFUNDIDAD = 8

    def __init__(self):
       
        self.levels = {i: [] for i in range(OctreeQuantizer.MAX_PROFUNDIDAD)}
        self.root = OctreeNode(0, self)
    def add_level_node(self, level, nodo):
        
        self.levels[level].append(nodo)
    
    def add_color(self, color):
        
        self.root.add_color(color, 0, self)

    def get_Hojas(self):
        return [nodo for nodo in self.root.get_NodosHoja()]

    def add_levelNodo(self):
        self.levels[level].append(nodo)

    def hacerPaleta(self,contadorColor):
        paleta=[]
        indicePaleta=0
        contadorHoja=len(self.get_Hojas())

        for level in range(OctreeQuantizer.MAX_PROFUNDIDAD -1,-1,-1):
            if self.levels[level]:
                for nodo in self.levels[level]:
                    contadorHoja-=nodo.reduce()
                    if contadorHoja <= contadorColor:
                        break
                if contadorHoja <= contadorColor:
                    break
                self.levels[level]=[]

        for nodo in self.get_Hojas():
            if indicePaleta >=contadorColor:
                break
            if nodo.esHoja():
                paleta.append(nodo.get_Color())
            nodo.indicePaleta=indicePaleta
            indicePaleta+=1
        return paleta

    def get_IndicePaleta(self,color):
        return self.root.get_IndicePaleta(color,0)

def cargarimagen(img,h,w):
    for i in range(h):
            for j in range(w):
                octr.add_color(Color(img[j,i,0],img[j,i,1],img[j,i,2]))
    print(" imagen cargada al arbol")
def mostrarpaleta():
    paleta = octr.hacerPaleta(256)
    print(paleta)
    pixelsPaleta=np.zeros(shape=[16,16,3],dtype=np.uint8)

    for i,color in enumerate(paleta):
        pixelsPaleta[i%16][i//16] = (color.red,color.green,color.blue)
    
    img2 = cv.imwrite('Salida.jpg',pixelsPaleta)
    cv.imshow('Ejemplo',pixelsPaleta)
    cv.waitKey(10000)
    cv.destroyAllWindows()
    imagenResul=np.zeros(shape=[h,w,3],dtype=np.uint8)

    for j in range(h):
        for i in range(w):
            indice=octr.get_IndicePaleta(Color(img[i][j][0],img[i][j][1],img[i][j][2]))
            color=paleta[indice]
            imagenResul[i][j]=(color.red,color.green,color.blue)

    cv.imwrite("Salida2.png",imagenResul)
    cv.imshow('Ejemplo',imagenResul)
    cv.waitKey(10000)
    cv.destroyAllWindows()



root=Tk()
frm=Frame(root)
frm.pack(side=BOTTOM, padx=15,pady=15)
lbl=Label(root)
lbl.pack()
octr = OctreeQuantizer()
imagen = showimage()
img = cv.imread(imagen)
w,h,z=img.shape 
cargarimagen(img,h,w)
btn3 = Button(frm, text= "Cuantizar",command=mostrarpaleta)
btn3.pack(side=tk.LEFT)
btn2= Button(frm, text="Salir",command=lambda: exit())
btn2.pack(side=tk.LEFT,padx=10)
root.title("Laboratorio 4")
root.geometry("600x600")
root.mainloop()
