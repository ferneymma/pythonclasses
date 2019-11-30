
## Parametros de entrada
def sumar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

# res = sumar(12, 20)
# print(res)


## Sin parametros de entrada, pero si de salida

def print_hola():
    return "Hola"


# Sin parametros de salida
def guardar_variable_nombre(nombre):
    name = nombre + "Maria"
    apellido = "Toquica"
    name = "{} Maria".format(nombre)
    name = "{0} Maria {1}".format(nombre, apellido)
    name = "%s Maria " % nombre
    name = "%s Maria %s" % (nombre, apellido)
    name = f"{nombre} Maria {apellido}"

    print(name)
    return name


def bienvenida(nombre):
    nombre_completo = guardar_variable_nombre(nombre)
    valor_hola = print_hola()
    return valor_hola + nombre_completo


def bienvenida_2(nombre):
    return f"{print_hola()} {guardar_variable_nombre(nombre)}"


def bienvenida_3(nombre="Luisa"):
    return f"{print_hola()} {guardar_variable_nombre(nombre)}"


def sumar_restar(numero1, numero2):
    resultad_suma = 0
    resultad_resta = 0

    def sumar(numero1, numero2):
        return numero1 + numero2

    def restar(numero1, numero2):
        return numero1 - numero2

    resultad_suma = sumar(numero1, numero2)
    resultad_resta = restar(numero1, numero2)
    return f" el resultado de la suma es: {resultad_suma}, el resultado de la resta es: {resultad_resta}"


def main():
    print(sumar_restar(20, 50))

if __name__ == "__main__":
    print("estoy en el main")
    main()
