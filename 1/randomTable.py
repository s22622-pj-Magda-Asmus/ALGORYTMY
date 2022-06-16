import random

def createaTable(xxx):
    arr=[]
    for i in range(xxx):
        a=str(random.randint(0,999))
        arr.append(a)
    print(arr)

    linia = "\n".join(arr)
    f = open("999_random.txt", mode='w')
    f.write(linia)
    f.close()

    print(len(arr))


createaTable(999)