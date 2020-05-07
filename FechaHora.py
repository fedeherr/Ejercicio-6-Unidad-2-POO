class FechaHora:
    __dia = 0
    __mes = 0
    __anio = 0
    __hora = 0
    __minutos = 0
    __segundos = 0
    def __init__(self, dia = 1, mes = 1, anio = 2020, hora = 0, minutos = 0, segundos = 0):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
        self.__hora = hora
        self.__minutos = minutos
        self.__segundos = segundos
    def Mostrar(self):
        print (f"La fecha es {self.__dia} del {self.__mes} del año {self.__anio}, hora {self.__hora}:{self.__minutos}:{self.__segundos}")
    def __str__(self):
        return "%d:%d:%d" % (self.__hora, self.__minutos, self.__segundos)
    def AdelantarHora(self,adelantohora=0,adelantominuto=0,adelantosegundo=0):
        diventera = 0 
        self.__hora = self.__hora + adelantohora
        self.__minutos = self.__minutos + adelantominuto
        self.__segundos = self.__segundos + adelantosegundo
        if (self.__segundos >= 60):
            diventera = self.__segundos // 60
            resto = self.__segundos - 60
            while (resto >= 60): resto = resto - 60
            self.__segundo = resto
            self.__minutos = self.__minutos + diventera
        if (self.__minutos >= 60):
            diventera = self.__minutos // 60
            resto = self.__minutos - 60
            while (resto >= 60): resto = resto - 60
            self.__minutos = resto
            self.__hora = self.__hora + diventera
        if (self.__hora >= 24):
            diventera = self.__hora // 24
            resto = self.__hora - 24
            while (resto >= 24): resto = resto - 24
            self.__hora = resto
            self.__dia = self.__dia + diventera
        if (self.__segundos < 0):
            diventera = self.__segundos // 60
            resto = self.__segundos + 60
            while (resto < 0): resto = resto + 60
            self.__segundos = resto
            self.__minutos = self.__minutos + diventera
        if (self.__minutos < 0):
            diventera = self.__minutos // 60
            resto = self.__minutos + 60
            while (resto < 0): resto = resto + 60
            self.__minutos = resto
            self.__hora = self.__hora + diventera
        if (self.__hora < 0):
            diventera = self.__hora // 24
            resto = self.__hora + 24
            while (resto < 0): resto = resto + 24
            self.__hora = resto


    def PonerEnHora(self, nuevahora, nuevosminutos = 0, nuevossegundos = 0):
        if (nuevosminutos < 60): self.__minutos = nuevosminutos
        else: self.__AdelantarHora()
        if (nuevossegundos < 60): self.__segundos = nuevossegundos
        else: self.__AdelantarHora()
        if (nuevahora < 25): self.__hora = nuevahora
        else: self.__AdelantarHora()
    def gethora(self):
        return self.__hora
    def getminutos(self):
        return self.__minutos
    def getsegundos(self):
        return self.__segundos
    def __add__(self, otrahora):
        return FechaHora(self.__dia, self.__mes, self.__anio, self.__hora+otrahora.gethora(),self.__minutos+otrahora.getminutos(), self.__segundos+otrahora.getsegundos())
    def __sub__(self, otrahora):
        return FechaHora(self.__dia, self.__mes, self.__anio, self.__hora-otrahora.gethora(),self.__minutos-otrahora.getminutos(), self.__segundos-otrahora.getsegundos())
    def __gt__(self, otrahora):
        if(self.__hora==otrahora.gethora()):
            if(self.__minutos==otrahora.getminutos()):
                if (self.__segundos > otrahora.getsegundos()): return(True)
                else: return(False)
            else:
                if(self.__minutos>otrahora.getminutos()): return(True)
        else:
            if(self.__hora>otrahora.gethora()): return(True)
        return(False)