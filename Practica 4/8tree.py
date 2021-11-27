import numpy as np
import cv2 as cv
class Color(object):
    def __init__(self, red=0, green=0, blue=0, alpha=None):

        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def mostrarColor(self):
    	print("Red ",self.red)
    	print("Green ",self.green)
    	print("Blue ",self.blue)

class NodoOctree:
    def __init__(self,level,parent):
        self.flag=False
        self.color=Color(0,0,0)
        self.contador_pixel=0
        self.paleta_indice=0
        self.children= [None for _ in range(8)]
        
        if level < Octree.MAX_PROFUNDIDAD - 1:
            parent.add_nivel(level,self)
    def es_hoja(self):
     return self.contador_pixel>0
    def get_Nodohojas(self):
        nodos_hoja=[]
        for i in range(8):
            nodo=self.children[i]
            if nodo:
                if nodo.es_hoja():
                    nodos_hoja.append(nodo)
                else:
                    nodos_hoja.extend(nodo.get_Nodohojas())
        return nodos_hoja
    
    def get_contador(self):
        suma=self.contador_pixel
        for i in range(8):
            nodo=self.children[i]
            if nodo:
                suma = suma + nodo.contador_pixel
        return suma
    
    def addColor(self,color,level,parent):
        if(level>= Octree.MAX_PROFUNDIDAD):
            self.color.red+=color.red
            self.color.green+=color.green
            self.color.blue+=color.blue
            self.contador_pixel +=1
            return
        print("level ",level)
        if not self.children[level]:
            self.children[level]=NodoOctree(level,parent)
        self.children[level].addColor(color,level+1,parent)
    def get_color(self):
        return Color(self.color.red / self.pixel_count,self.color.green / self.pixel_count,self.color.blue / self.pixel_count)
    def Mostrarroot(self):
        nodo=self.root
        print("Contador Pixel")
        print(nodo.contador_pixel)
        print("Colores")
        print(nodo.color.mostrarColor)

class Octree(object):
    MAX_PROFUNDIDAD=8
    def __init__(self):
        self.levels= {i:[] for i in range(Octree.MAX_PROFUNDIDAD)}
        self.root=NodoOctree(0,self)
    
    def get_leaves(self):
        return [nodo for nodo in self.root.get_Nodohojas()]
    
    def mostrar(self):
        Mostrarroot()
    def add_nivel(self,level,nodo):
        self.levels[level].append(nodo)
    def addColor(self,color):
        self.root.addColor(color,0,self)

def main():
    pixels=cv.imread('input1.png')
    cv.imshow('Ejemplo',pixels)
    cv.waitKey(1000)
    cv.destroyAllWindows()
    w,h,z=pixels.shape
    octree=Octree()
    for i in range(h):
        for j in range(w):
            octree.addColor(Color(pixels[i][j][0],pixels[i][j][1],pixels[i][j][2]))

if __name__ == '__main__':
    main()