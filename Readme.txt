1. Implementar la función de medios (promedio)
El código ya implementa una función media que cubre los casos solicitados.

 1.1. Caso sin elementos en la lista (excepción `NoSePuedeCalcular`):
   - Explicación: Si la lista está vacía, lanza una excepción `NoSePuedeCalcular`. Esto está cubierto en la prueba `test_media` del caso vacío.

1.2. Caso con un solo elemento en la lista:
  - Explicación: Si la lista tiene un solo elemento, la función simplemente retorna ese valor, lo cual es correcto.

1.3. Caso con dos elementos en la lista:
   - Explicación: Para dos o más elementos, la función calcula la media sumando los elementos y dividiendo por la cantidad. Esto está probado con dos elementos en las pruebas.

1.4. Caso con n elementos positivos:
   - Explicación: La media se calcula sumando todos los elementos y dividiendo por el número de elementos. El caso de n elementos positivos se cubre con la prueba de `[4, 6, 8, 12.5]`.

1.5. Caso con n elementos donde todos son ceros:
   - Explicación: La media de una lista con todos ceros es 0, y esto está cubierto en la prueba correspondiente.

1.6. Caso con n elementos positivos y negativos:
   - Explicación: Se aplica la misma lógica que con los elementos positivos. Está cubierto en el caso con `[3.5, 8, -4.2]`.

1.7. Caso con n elementos no numéricos (excepción `ExcepcionDatos`):
   - Explicación: Se verifica si algún elemento no es un número, y se lanza una excepción personalizada `ExcepcionDatos` si se encuentra uno. El código trata adecuadamente con este caso y está probado con la lista `[5, "4.5"]` y `[8, "a"]`.

2. Implementar la función de desviación estándar

La función de `desviacion_estandar` también cubre los casos solicitados.

2.1. Caso sin elementos en la lista (excepción `NoSePuedeCalcular`):
   - Explicación: Igual que en el caso de la media, se lanza la excepción `NoSePuedeCalcular` si la lista está vacía.

2.2. Caso con un solo elemento:
   - Explicación: Si solo hay un elemento, la desviación estándar es 0, porque no hay variación.

2.3. Caso con dos elementos:
   - Explicación: La desviación estándar se calcula como la raíz cuadrada de la suma de las diferencias al cuadrado, dividida entre el número de elementos. Esto funciona para dos o más elementos y está probado en la función `test_desviacion_estandar`.

2.4. Caso con n elementos positivos:
   - Explicación: Calcula la desviación estándar de n elementos positivos. Esto está probado en el caso con `[4, 6, 8, 12.5]`.

2.5. Caso con n elementos donde todos son ceros:
   - Explicación: La desviación estándar de una lista con todos ceros es 0. Esto se prueba con `[0, 0, 0, 0]`.

2.6. Caso con n elementos positivos y negativos:
   - Explicación: El código es el mismo y está probado con el caso de `[3.5, 8, -4.2]`.

2.7. Caso con n elementos no numéricos (excepción `ExcepcionDatos`):
   -Explicación: Como con la función de media, se verifica si los elementos son numéricos, y si no lo son, se lanza la excepción `ExcepcionDatos`.
