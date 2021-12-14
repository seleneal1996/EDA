## **Antes de empezar**
Este laboratorio se realizo escuchando el siguiente [remix](https://www.youtube.com/watch?v=Vq_OlYypkN8&ab_channel=AlexGarcia%27-Per%C3%BA) para calmar la sed 🍺 

👁️ Debes instalar *Graphviz* para generar los graficos.

👨‍💻 El codigo tiene los comandos para generar el .dot y la imagen en formato .png

## **Laboratorio 5: M-TREE** **🌳**

En el siguiente trabajo se implementó el *M-Tree en C++*.  En lugar de tener que crear una subclase para definir nuevas funciones de soporte (distance, split, promotion, partition), se uso argumentos de plantilla:

1. El tipo de datos que indexará el M-Tree debe ser un tipo asignable y se debe definir un orden débil estricto std :: less <Data>.
2. El metodo DistanceFunction se utilizará para calcular la distancia entre dos objetos de datos, por defecto, es *euclidean_distance*.
3. SplitFunction se utilizará para dividir un nodo cuando está en su capacidad máxima y un nuevo hijo debe ser adicional. Por defecto, es una composición de *random_promotion* y *balanced_partition*.

Considerar que el directorio mtree fue una base para entender el funcionamiento 😅 , se agradece a [tburette](https://github.com/tburette/mtree) 🥰. 
Los dataset usados se encuentran en este [link](https://www.worldometers.info/coronavirus) fueron usandos para el experimento 🤩.

## **Autores ✒️**

1. Barrios Cornejo Selene [seleneal1996](https://github.com/seleneal1996) 
2. Ccalluchi Lopez Luis Alberto [cheems-dev](https://github.com/cheems-dev) 
3. Bustinza Cornejo Alejandra [Al3p4](https://github.com/Al3p4)

## **Licencia 📄**

Este proyecto está bajo la LICENCIA MIT

## **Expresiones de Gratitud 🎁**

-   Comenta a otros sobre este proyecto 📢
-   Invita una cerveza 🍺 o un café ☕ a alguien del equipo.
-   Da las gracias públicamente 🤓.
