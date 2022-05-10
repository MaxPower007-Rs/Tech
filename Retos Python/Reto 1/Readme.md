
# RETO 1 - FUNDAMENTOS DE PROGRAMACIÓN
Usted ha sido contratado por la tienda de su barrio para hacer una calculadora
que le facilitará llevar al tendero la cuenta de una compra.
Su calculadora le permitirá hacer las siguientes operaciones al tendero:

- El programa le solicita al tendero cuál es el valor unitario de un producto que lleva el cliente (Sin IVA incluído).
- El programa le pregunta al tendero si el producto tiene IVA.
- El programa le solicita al tendero cuál es la cantidad que lleva el cliente de ese producto.
- Si el producto tiene IVA, el sistema debe sumarlo e imprimir en consola EXACTAMENTE las siguientes palabras: “IVA incluído”, si no tiene IVA imprimir en consola: “PRODUCTO SIN IVA”, el IVA se asume del 19%.
- A continuación el programa imprime el subtotal EXACTAMENTE como sigue: “SUBTOTAL: 𝑥” donde 𝑥 es el subtotal (Cantidad de dinero a cobrarse hasta ese instante).
- El programa le pregunta al tendero si faltan productos por cobrar en esta compra
- Cuando el tendero termine de realizar el cobro, el programa debe imprimir la cuenta total a cobrarle al cliente en esta compra EXACTAMENTE como sigue: “TOTAL A COBRAR: 𝑦” donde 𝑦 es el valor total a cobrarle al cliente.

## TAREAS
Realizar un programa en Python que le permita al tendero realizar la cuenta de una compra, teniendo en cuenta las siguientes instrucciones:
1. Debe usar la función 𝑝𝑟𝑖𝑛𝑡 haciendo uso de UN SOLO argumento (Solo limítese a imprimir los mensajes solicitados con mayúsculas, espacios y tildes), limítese a SOLO imprimir los mensajes tal y como se le especifica a lo largo del documento.
2. NO usar la función 𝑝𝑟𝑖𝑛𝑡 para solicitar la información, es decir, usted usará la función 𝑖𝑛𝑝𝑢𝑡 con UN argumento para solicitar la información al cliente:
  - Incorrecto: 𝑝𝑟𝑖𝑛𝑡("𝐼𝑛𝑔𝑟𝑒𝑠𝑒 𝑒𝑙 𝑣𝑎𝑙𝑜𝑟 𝑢𝑛𝑖𝑡𝑎𝑟𝑖𝑜 𝑑𝑒𝑙 𝑝𝑟𝑜𝑑𝑢𝑐𝑡𝑜: ")
  - Correcto: 𝑖𝑛𝑝𝑢𝑡("𝐼𝑛𝑔𝑟𝑒𝑠𝑒 𝑒𝑙 𝑣𝑎𝑙𝑜𝑟 𝑢𝑛𝑖𝑡𝑎𝑟𝑖𝑜 𝑑𝑒𝑙 𝑝𝑟𝑜𝑑𝑢𝑐𝑡𝑜: ")
3. Cuando el sistema le solicite al tendero ingresar si un producto tiene o no IVA, el tendero ingresará “N” para decir que el producto NO tiene IVA, e ingresará “S” para decir que el producto tiene IVA.
4. Cuando el sistema le solicite al tendero ingresar si faltan productos por cobrar, el tendero ingresará “N” para decir que terminó de registrar toda la compra, e ingresará “S” para decir que faltan productos por registrar en la compra.
5. Sugerencia: Para imprimir el subtotal y el total a cobrar usar la función 𝑝𝑟𝑖𝑛𝑡 de la siguiente manera (Siempre usando UN SOLO argumento):
  - print(f"SUBTOTAL: {subtotal}")
  - print(f"TOTAL A COBRAR: {subtotal}")

## EJEMPLOS
### Ejemplo 1
El tendero ingresa la siguiente tabla a medida de que el programa le va
solicitando datos (En la figura 1 puede ver la secuencia):
![image](https://user-images.githubusercontent.com/56212392/167720444-93e15321-6742-4870-88aa-0d0e8c8dcae3.png)
![image](https://user-images.githubusercontent.com/56212392/167720554-d4e5d2da-859b-4e7f-9f69-968073641330.png)
### Nota: 
No se preocupe por el manejo de los decimales, el calificador tendrá en cuenta un 1% de error por cuestión de aproximación de los decimales



![image](https://user-images.githubusercontent.com/56212392/167722028-c50d23ff-4067-4694-9ccc-d0f39204a215.png)


Los 𝑖𝑛𝑝𝑢𝑡 pueden tener cualquier texto como argumento, pero las funciones 𝑝𝑟𝑖𝑛𝑡 deben imprimir exactamente los datos como se pide SIN decorar información (No dejar renglón, ni usar los argumentos 𝑠𝑒𝑝 ni 𝑒𝑛𝑑).

¡MUCHOS ÉXITOS EN EL DESARROLLO DEL RETO 1 TRIPULANTE!

