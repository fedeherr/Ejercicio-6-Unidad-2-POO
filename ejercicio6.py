from Menu import Menu
if __name__ == '__main__':
    menu=Menu()
    salir = False
    while not salir:
        print("""
              0 Salir
              1 Sumar horas
              2 Restar horas
              3 Comparar horas""")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op)
        salir = op == 0