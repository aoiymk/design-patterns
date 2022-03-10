# Factory method

Proporciona una interfaz para la creación de objetos en una superclase, mientras que permite a las subclases alterar el tipo de objetos que se crearán

## Ejemplo de problema
Se crea una aplicación de gestión logística, cuya primera versión es capaz de manejar el transporte en camión, por lo que la mayor parte del código se encuentra dentro de la clase Camión.

Al cabo de un tiempo, la aplicación se vuelve bastante popular y se deben integrar otros medios de transporte, pero todo el código está acoplado.



## Implementación

### Para los productos
1. Declaración de la interfaz de **producto** la cual es común a todos los tipos de productos que se puedan crear. En dicha interfaz se deben declarar todas las operaciones que los productos deben implementar.
2. Crear las distintas implementaciones de productos concretos.

### Interfaz Creadora
1. Añadir el patrón Factory Method vacío dentro de la clase creadora, el tipo de retorno debe ser la interfaz de producto

### Sustitución de constructores de producto
Por cada una de las llamadas a constructores de producto se debe:

1. Sustituir por la invocación del Factory method

### Clases Creadoras
1. Escribir cada subclase creadora para cada producto existente
