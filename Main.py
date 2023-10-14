a = 20
b = 10
ENTER = '\n'

def Perimetro(a, b):
    perimetro = 2* (a + b)
    print(f'Perimetro = {perimetro}')
    
def Area(a, b): 
    area = a * b
    print(f'Area = {area}')

P= Perimetro(a, b)
A= Area(a, b)

print(f'{P} {ENTER} {A}')