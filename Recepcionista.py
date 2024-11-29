

from Empleado import Empleado



class Recepcionista(Empleado):
    def __init__(self,nick,correo):
        super().__init__(nick,correo)
        num_consultas=0