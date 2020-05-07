from FechaHora import FechaHora



class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 0:self.opcion0,
                            1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()
    def opcion0(self):
        print('Chao')
    def opcion1(self):
        h=int(input("Ingrese Hora: "))
        m=int(input("Ingrese Minutos: "))
        s=int(input("Ingrese Segundos: "))
        r = FechaHora(0,0,0,h, m, s) 
        h=int(input("Ingrese Hora a agregar: "))
        m=int(input("Ingrese Minutos a agregar: "))
        s=int(input("Ingrese Segundos a agregar: "))
        r2 = FechaHora(0,0,0,h, m, s)
        suma = r + r2
        suma.AdelantarHora()
        print('Hora después de la suma: ', suma)
    def opcion2(self):
        h=int(input("Ingrese Hora: "))
        m=int(input("Ingrese Minutos: "))
        s=int(input("Ingrese Segundos: "))
        r = FechaHora(0,0,0,h, m, s) 
        h=int(input("Ingrese Hora a restar: "))
        m=int(input("Ingrese Minutos a restar: "))
        s=int(input("Ingrese Segundos a restar: "))
        r2 = FechaHora(0,0,0,h, m, s)
        resta = r - r2
        resta.AdelantarHora()
        print('Hora después de la resta: ', resta)
    def opcion3(self):
        h=int(input("Ingrese Hora: "))
        m=int(input("Ingrese Minutos: "))
        s=int(input("Ingrese Segundos: "))
        r = FechaHora(0,0,0,h, m, s) 
        h=int(input("Ingrese Hora para comparar: "))
        m=int(input("Ingrese Minutos para comparar: "))
        s=int(input("Ingrese Segundos para comparar: "))
        r2 = FechaHora(0,0,0,h, m, s)
        r.AdelantarHora()
        if(r > r2): print ("La primera hora es mayor")
        else: print ("La segunda hora es mayor o igual")