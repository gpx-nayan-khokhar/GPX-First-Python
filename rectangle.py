def perimeter(length, breadth):
    p = 3 * (length + breadth)
    return p

def area(length, breadth):
    a =  length * breadth
    return a

l = int(input('enter the length: '))
b = int(input('enter the breadth: '))

l = print(perimeter(l,b))
l = print(area(l,b))