# Patrones de diseño

## Creacionales
Proporcionan mecanismos de creación de objetos que incrementan la flexibilidad y reutilización de código.

+ [Factory](desing-patterns/creacionales/factory/factory.md)
+ [Abstract Factory](desing-patterns/creacionales/abstract/abstract.md)
+ [Builder](desing-patterns/creacionales/builder/builder.md)
+ [Prototype](desing-patterns/creacionales/prototype/prototype.md)
+ [Singleton](desing-patterns/creacionales/singleton/singleton.md)

### Principales relaciones entre ellos:

+ Es usual que Factory termine evolucionando a Abstract Factory o Builder
+ Abstract Factory se especializa en devolver familias de productos, en cambio Builder se enfoca en construir objetos complejos
+ Las clases de Abstract Factory se pueden basar tanto en Factory como en Prototype
+ Abstract Factory puede servir como alternativa a Facade cuando se quiere esconder la forma en que se crean los objetos del subsistema a partir del código cliente.
+ Se puede utilizar Abstract Factory junto a Bridge. Este emparejamiento resulta útil cuando algunas abstracciones definidas por Bridge sólo pueden funcionar con implementaciones específicas.
+ Los patrones Abstract Factory, Builder y Prototype pueden todos ellos implementarse como Singletons.

## Estructurales
Explican cómo ensamblar objetos y clases en estructuras más grandes a la vez que se mantiene la flexibilidad y eficiencia de la estructura

## Comportamiento
Se encargan de comunicación efectiva y la asignación de responsabilidad entre objetos

