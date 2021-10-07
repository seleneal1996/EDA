import random
import sys
from time import time

def burbuja(arr, tam):
    for i in range (tam):
       for j in range (tam-1):
           if(arr[j] < arr [j+1]):
               tem = arr[j]
               arr[j] = arr[j+1]
               arr[j+1] = tem

archivo = sys.stdin.readlines()
n = int(archivo[0])
arr = []
dato = archivo[1].split()
for i in range (n):
    arr.append(int(dato[i]))
start = time()
burbuja(arr, len(arr))
finish = time()
print(finish-start,end = '')