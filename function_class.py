from usuario_class import compradores
from product_class import articulos

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
    print('Bienvenid@', compradores[id_user-1].get('nombre'), compradores[id_user-1].get('apellidos'))
    exist_id = True
    return exist_id

def exist_user():
    exist_id = False
    id_user = int(input('Enter your ID: '))
    for comprador in compradores:
        if id_user == comprador.get('id_usuario'):
            exist_id = True

            print('Bienvenid@',comprador.get('nombre'),comprador.get('apellidos'))
            return exist_id
    return exist_id

def buy_products(cant_product, id_product, product_buy):
    for product in articulos:
        if product.get('id_articulo') == id_product:
            val_total_product = product.get('valor') * cant_product
            product_buy.append({
                "id_articulo": product.get('id_articulo'),
                "valor_unidad": product.get('valor'),
                "cantidad": cant_product,
                "valor_articulos": val_total_product
            })
    return product_buy