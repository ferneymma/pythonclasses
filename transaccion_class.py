from usuario_class import compradores
from function_class import existe_usuario
from compra_class import facturas_venta
from product_class import articulos

flag_exist_id = input('Are you registered? Y/N ')

#id_usuario = int(input('Enter your ID: '))
existe_usuario(flag_exist_id)

print(compradores)


#for comprador in compradores:
#    if comprador.get("id_usuario") == id_usuario and flag_exist_id == False:
#        print("User already exist.")
#print("Productos en venta: ", articulos)
