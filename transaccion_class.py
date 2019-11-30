from usuario_class import compradores
from compra_class import facturas_venta
from product_class import articulos

flag_exist_id = input('Are you registered? Y/N ')

#id_usuario = int(input('Enter your ID: '))
if flag_exist_id.upper() == 'N':
    nombre = input('Enter your name: ')
    apellido = input('Enter your lastname: ')
    email= input('Enter your email address: ')
    id_user = None
    for usuario in compradores:
        if id_user is None or id_user <= usuario.get('id_usuario'):
            id_user = usuario.get('id_usuario')+1
            continue
    compradores.append({
            "nombre": nombre,
            "apellidos": apellido,
            "id_usuario": id_user,
            "email": email
    })

print(compradores)


#for comprador in compradores:
#    if comprador.get("id_usuario") == id_usuario and flag_exist_id == False:
#        print("User already exist.")
#print("Productos en venta: ", articulos)
