# Abstract
Permite producir **familias de productos** que se encuentras relacionadas, sin necesidad de especificar sus clases concretas.


## Ejemplo de problema
Se tiene una fábrica de muebles dnde se hacen kits de sillas, sofa y mesa de centro. Además, estos kits pueden tener distintos estilos visuales, de modo que pueden ser de estilo Art Deco, Victorianos o Modernos.

## Implementación

### Diseño de la solución
Se debe tener claro qué elementos componen la familia y cuantas tipas de familias existen:


|Factory| Chair| Coffee Table| Sofa|
| -- | -- | -- | -- |
| Victorian | VictorianChair | VictorianCoffeeTable | VictorianSofa |
| Modern | ModernChair | ModernCoffeeTable | ModernSofa |
| ArtDeco | ArtDecoChair | ArtDecoCoffeeTable | ArtDecoSofa |


### Declaración de interfaces
1. Declaración de interfaces generícas de los productos, para el caso serían las de:
    
    + Chair
    + Sofa
    + CoffeeTable

2. Declarar interfaz para la fábrica Abstracta, la cual debe incluir los comandos de creación de cada uno de los productos que son parte de la familia.

    + create_chair()
    + create_coffee_table()
    + crate_sofa()


### Creación de las fábricas específicas

1. Para este ejercicio, hay 3 tipos de fábricas:

    + VictorianFactory
    + ModernFactory
    + ArtDecoFactory