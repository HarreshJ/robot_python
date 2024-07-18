def fun1():
    if 5 == 5:
        return True
    else:
        return False
    
res1 = fun1()

def fun2():
    if res1 == True:
        print('5 = 5')
    else:
        print('5 != 5')

fun2()