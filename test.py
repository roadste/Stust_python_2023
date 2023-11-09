print('test')
def function(name,age):
    print(name,age)

function("violet",23)

def func1(*args):
    for i in args:
        print(i)

func1(20,40,60)
func1(80,100)

def calculate(a,b):
    add = a+b
    red = a-b
    return add,red
res = calculate(40,10)
print(res)


