import datetime as dt

def Quicksort(A, p, r):

    if p<r:
        q=Partition(A,p,r)
        Quicksort(A,p,q-1)
        Quicksort(A,q+1,r)



def Partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p, r):
        if A[j] <=x:
            i=i+1
            A[i], A[j] = A[j] ,A[i]
    A[i+1], A[r] = A[r], A[i+1]

    return i+1


# Tutaj tworze tablice z  wartościami na podstawie pliku .txt (wygenerowany za pomocą skryptu "randomTable.py")
file = open('999_random.txt', 'r').read()
lines=file.split('\n')
A=[]

for line in lines :
    liczba = int(line)
    A.append(liczba)



#Tutaj wywołanie funkcji i zmierzenie czasu działania
n1 = dt.datetime.now()
Quicksort(A,0,len(A)-1)
n2 = dt.datetime.now()

#Tutaj wszelkie zeczy które chce sobie wyświetlić po sortowaniu

print("Sorted array is: ")
print(A, "\n")

print("***Sortowanie quicksort*** ", "\n")

print("Długość tablicy wejsciowej: ")
print(len(A))

print("Czas obliczeń [s]:  ")

g=((n2.hour-n1.hour)*3600)*1000000
m= (((n2.minute-n1.minute)*60))*1000000
s= ((n2.second-n1.second))*1000000
us=(n2.microsecond-n1.microsecond)

print((g+m+s+us)/1000000)
