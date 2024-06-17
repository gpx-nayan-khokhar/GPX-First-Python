def perimeter_rectangle(length, breadth):
    p = 2 * (length + breadth)
    return p

def area_rectangle(length, breadth):
    a =  length * breadth
    return a

l = int(input('enter the length: '))
b = int(input('enter the breadth: '))

l = print(perimeter_rectangle(l,b))
l = print(area_rectangle(l,b))