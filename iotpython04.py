#Function 3 : Have Parameter/Have Reture ***
def funcA( n1, n2) :
    print(f'N1 is {n1}')
    print(f'N2 is {n2}')
    return n1 + n2

def funcB( name, year ) :
    return f'สวัสดี {name}', 2023 -year

print('Sum is {funcA(10, 20)}')

x , y = funcB('สมชาย', 2000)
print(f'{x} อายุ {y} ปี')