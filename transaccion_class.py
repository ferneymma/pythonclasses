from usuario_class import compradores
from function_class import crea_usuario, exist_user
from compra_class import facturas_venta
from product_class import articulos

exist_id = False
n_intentos = 'Y'
while(n_intentos == 'Y'):
    flag_exist_id = input('Are you registered? Y/N ')
    #id_usuario = int(input('Enter your ID: '))
    if flag_exist_id.upper() == 'N':
        crea_usuario()
    elif flag_exist_id.upper() == 'Y':
        exist_id = exist_user()
        print("fuera ",exist_id)
    else:
        print("you've entered an invalid option.")
        continue
    if exist_id is False:
        print('Your id no exists, try again.')
    print()


#print(compradores)


#for comprador in compradores:
#    if comprador.get("id_usuario") == id_usuario and flag_exist_id == False:
#        print("User already exist.")
#print("Productos en venta: ", articulos)
