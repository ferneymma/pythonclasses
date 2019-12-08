from usuario_class import compradores

def crea_usuario():
    nombre = input('Enter your name: ')
    apellido = input('Enter your lastname: ')
    email = input('Enter your email address: ')
    id_user = None
    for usuario in compradores:
        if id_user is None or id_user <= usuario.get('id_usuario'):
            id_user = usuario.get('id_usuario') + 1
            continue
    compradores.append({
        "nombre": nombre,
        "apellidos": apellido,
        "id_usuario": id_user,
        "email": email
    })

def exist_user():
    exist_id = False
    id_user = int(input('Enter your ID: '))
    for comprador in compradores:
        if id_user == comprador.get('id_usuario'):
            exist_id = True
            print(comprador.get('id_usuario'), exist_id)
            return exist_id
    return exist_id