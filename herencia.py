class Perona:
    def __init__(self,nombre, edad):
        self.nombre= nombre
        self.edad= edad
    def mostInfo(self):
        return f"Nombre: {self.nombre} \nEdad: {self.edad}"
            
class Empleado(Perona):
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad)
        self.sueldo = sueldo
    def info(self):
        print(f"{super().mostInfo()}\nSueldo: {self.sueldo}")    
emp= Empleado(input("ingrese su nombre: "),int(input("ingrese su edad: ")),int(input("Ingreses sueldo: ")))                    
emp.info()