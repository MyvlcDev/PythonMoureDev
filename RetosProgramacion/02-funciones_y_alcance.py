""" /*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */ """


### Ejemplos de funciones  dddd

## funcion sin parametros ni retorno

def inicioFuncion():
    print()


## funcion conParametros

def funcionParametro(par1, par2):
    print()

## funcion con retorno

def funcionSaluda(nombre):
    
    return "Hola " + nombre

## funcion dentro de funcion

def funcion_suma_total(x):
    def funcion_suma_parcial(y):
        return x + y
    return funcion_suma_parcial

# Uso de la función
resultado = funcion_suma_total(10)
print(resultado(5))

## ejemplos de funciones ya creadas en el sistema

print("Funicones del sistema    ")

texto="Ejemplo de texto"
print()
print(texto)
longitud =len(texto)
print("Longitud del texto: " + str(longitud) )
print(texto.upper())

## variable locales y global

var_global = "El coche"

def colorea(objeto):
    var_local= "azul"
    print(f"{objeto} es {var_local}")


print(colorea(var_global))
    
### DIFICULTAD EXTRA.

def imprimeNumeros(text_1, text_2) -> int:
    
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    return count

        
imprimeNumeros("Lucas","Grejander")