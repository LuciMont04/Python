class Ret:
    def __init__(self, altura, base):
        self.altura= altura
        self.base= base
        
    def area(self):
        rest= self.base * self.altura
        print(rest)
    def peri(self):
        con= self.base*2 + self.altura*2
        print(con)    
recta= Ret(12,5)
recta.area()
recta.peri()

class Circulo:
    def __init__(self,radio):
        self.radio = radio
        
    def diametro(self):
        d =self.radio * 2
        print(d)
    def per(self):
        d =self.radio * 2
        p = d * 3.14   
        print(p) 
cir= Circulo(8)
cir.diametro()
cir.per()         