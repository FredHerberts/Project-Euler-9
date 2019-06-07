import time
start = time.time()

def Pythagoras(x,y):
    for a in range(294, x):
        for b in range(2, a):
            c = (a**2 + b**2)**(1/2)
            if a + b + c == y:
                print(a*b*c)
                break
        if a + b + c == y:
            return a

Pythagoras(500,1000)
end = time.time()
print(end - start)
