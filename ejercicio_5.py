def main():

    palabra = input("ingresa una palabra: ")
    
    letra = input("ingresa una letra: ")

    cont = 0

    for l in palabra:
        if l == letra:
            cont += 1

    print(f"la letra {letra} aparece {cont} ")

if __name__ == "__main__":
    main()