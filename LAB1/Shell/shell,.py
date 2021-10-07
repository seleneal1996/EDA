import random
import sys
from time import time
def ShellSort(array, n):
  interval = n // 2
  while interval > 0:
    for i in range(interval, n):
      temp = array[i]
      j = i
      while j >= interval and array[j - interval] > temp:
        array[j] = array[j - interval]
        j -= interval
        array[j] = temp
      interval //= 2

archivo = sys.stdin.readlines()
n = int(archivo[0])
arr = []
dato = archivo[1].split()
for i in range (n):
  arr.append(int(dato[i]))
start = time()
ShellSort(arr,len(arr))
finish = time()
print(finish-start,end = '')