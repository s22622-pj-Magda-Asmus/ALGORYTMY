import datetime as dt

def MaxHeapify(A, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l < n and A[l] > A[i]:
        largest = l

    if r < n and A[largest] < A[r]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MaxHeapify(A, n, largest)


def Heapsort(A):

    n = len(A)
    for i in range(int(n/2), -1, -1):
        MaxHeapify(A, n, i)

    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        MaxHeapify(A, i, 0)

# Tutaj tworze tablice z randomowmi wartościami na podstawie pliku .txt (wygenerowany za pomocą skryptu "randomTable.py")
file = open('999_odwrotnie_posortowana.txt', 'r').read()
lines=file.split('\n')
A=[]

for line in lines :
    liczba = int(line)
    A.append(liczba)

#Tutaj wywołanie funkcji i zmierzenie czasu działania
n1 = dt.datetime.now()
Heapsort(A)
n2 = dt.datetime.now()

#Tutaj wszelkie zeczy które chce sobie wyświetlić po sortowaniu
print("Sorted array is: ")
print(A, "\n")

print("Długość tablicy wejściowej: ")
print(len(A), "\n")

print("***Sortowanie heapsort*** ", "\n")

print("Czas obliczeń [s]:  ")

g=((n2.hour-n1.hour)*3600)*1000000
m= (((n2.minute-n1.minute)*60))*1000000
s= ((n2.second-n1.second))*1000000
us=(n2.microsecond-n1.microsecond)

print((g+m+s+us)/1000000)
