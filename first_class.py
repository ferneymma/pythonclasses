# print("This is the first class")
#
# #  simples variable string, int, char, float, boolean, double
#
# blood_type = 'a'  # char
# nombre = "Lina"  # string
# edad = 12  #  int
#
# print(nombre, edad, type(edad))
# edad = "123"
#
# print(nombre, edad, type(edad))
#
# is_in_the_country = True
# live_in_bogota = False
#
# print(is_in_the_country, live_in_bogota)
# print(blood_type, chr(65))
#
# edad_str = str(edad)
# print(edad_str)
# # nombre_int = int(nombre)
# # print(nombre_int)
#
# numero_a = 10
# numero_b = 20
# numero_c = "30"
# numero_d = "10"
#
# ### sumas
#
# sumas = numero_a + numero_b + int(numero_c)
# print(sumas)
#
# concatenation = numero_c + numero_d
# print(concatenation)


# tipos de datos compuestos: dict, list, tuplas, set

# dict
# MUTABLES
# car = {
#     "asientos": 5,
#     "volante": 1,
#     "color": "Azul",
#     "id_cliente": 123,
#     "numero_seguro": "abc123",
#     "propietarios": ["lina", "Jairo", "Ferney"]
# }
# propietarios = car.get("propietarios")
# print(propietarios[1])
# print(car)
# eliminados = {}

# print(car.get("llantas"), car["color"])
#
# car["color"] = "Negro"
#
# # car["chasis"]
#
# print(car.get("chasis"))
# del car["color"]
# print(car)
#
# volante = car.pop("volante")
# print(volante)
# print(car)

# eliminados["id_cliente"] = car.pop("id_cliente")
# eliminados["numero_seguro"] = car.pop("numero_seguro")
#
# print(car, eliminados)

# list
# MUTABLES
# mercado = ["manzanas", "peras", "bananos", 123, "mora", "peras"]
#
# vegetales = ["lechuga", "pepino"]
#
# # print(mercado[0])
# # print(len(mercado))
# # print(mercado[2:])
# print(mercado)
# print(mercado.pop(0))
# print(mercado.remove("peras"))
# print(mercado)
#
# mercado.append("maracuya")
# print(mercado)
#
# mercado.extend(vegetales)
#
# print (len(mercado))

# tuplas
# INMUTABLES
# codigos_estudiantes = ("123", "456", "543")
#
# print(codigos_estudiantes[0])
#
# # codigos_estudiantes[0] = "6666" NO ES POSIBLE HACER
#
# variables_entorno = ("DB", "PASS", "USER")
#
#
# print(variables_entorno.index("PASS"))
#

#### CREAR DICT ATRIBUTOS USUARIO, DICT ATRIBUTOS PRODUCTO, DICT VENTA