from Empleado import Empleado
class Administrador(Empleado):
    def __init__(self,nick,correo):
        super().__init__(nick,correo)
        num_actulizaciones=0