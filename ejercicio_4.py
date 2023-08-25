def lista_compra(carrito):

    print("\n lista de la compra ")

    total = 0

    for articulo, precio in carrito.items():

        print(f"{articulo}  {precio}")

        total += precio

    print(f"coste total  {total}")

carrito = {}
def main():
    while True:
        articulo = input("ingresa el  artículo ( escriba 'salir' para terminar tarea): ")
        
        if articulo.lower() == 'salir':
            break
        
        precio = int(input(f"ingresa el precio del {articulo}: "))
        
        carrito[articulo] = precio

    lista_compra(carrito)

if __name__ == "__main__":
    main()    

