class Animal():
    
    def mover(self):
        pass
    
    
    def comer(self):
        print('Animal come')
        
class Gato(Animal):
    def mover(self):
        print('Mover gato')
        
        
    def comer(self):
        super().comer()
        print('Gato come')
        
g = Gato()
g.mover()
g.comer()