from usuario_class import compradores

def existe_usuario(flag_exist_id):
    if flag_exist_id.upper() == 'N':
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