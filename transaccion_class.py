from usuario_class import compradores
from function_class import crea_usuario, exist_user, buy_products
from compra_class import facturas_venta
from product_class import articulos

exist_id = False
n_intentos = 'Y'
while(n_intentos == 'Y'):
    flag_exist_id = input('Are you registered? Y/N ')
    #id_usuario = int(input('Enter your ID: '))
    if flag_exist_id.upper() == 'N':
        exist_id = crea_usuario()
    elif flag_exist_id.upper() == 'Y':
        exist_id = exist_user()
        if exist_id is False:
            print('Your id no exists, try again.')
            continue
    else:
        print("you've entered an invalid option.")
        continue
    n_intentos = 'N'

if exist_id is True:
    print('These are products than exist: ')
    for articulo in articulos:
        print('Articulo: ',articulo.get('tipo'), 'id producto: ',articulo.get('id_articulo'), 'Valor: ', articulo.get('valor'))
    elige_arti = input('would you like select any item? Y/N ')
    product_buy = list()
    while elige_arti.upper() == 'Y':
        id_product = int(input('Enter the product code: '))
        cant_product = int(input('Enter the quantity of products: '))
        if cant_product > 0:
           product_buy = buy_products(cant_product, id_product, product_buy)
        else:
            print('Enter correct quantity')
            continue
        elige_arti = input('Do you want to select other product: Y/N ')

if len(product_buy) > 0:
    max_id_fact = None
    for factura in facturas_venta:

        if max_id_fact is None or factura.get('id_factura') > max_id_fact:
            max_id_fact = factura.get('id_factura')
            print(max_id_fact, factura.get('id_factura'))
    facturas_venta.append({
        "id_factura": max_id_fact+1,
        "fecha_factura": '2019-12-10',
        "articulos": product_buy
    })
    print(facturas_venta)

