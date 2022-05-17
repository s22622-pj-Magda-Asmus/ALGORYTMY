import datetime as dt

def mergeSort(A):
    if len(A)>1 :
        m=len(A)//2 #dzielenie przez // to tak jakby zrobic int() czyli zaokragla wartość w dół
        L=A[:m]     #tablica lewa z elementami d 0 do środka
        R=A[m:]     #tablica prawa z elementami od srodka do końca

        mergeSort(L)
        mergeSort(R)

        i = j= k =0
        while i<len(L) and j<len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i=i+1
            else:
                A[k] = R[j]
                j=j+1
            k=k+1

        while i<len(L):
            A[k] = L[i]
            i=i+1
            k=k+1

        while j<len(R):
            A[k]=R[j]
            j=j+1
            k=k+1



# Tutaj tworze tablice z randomowmi wartościami na podstawie pliku wyniki.txt (wygenerowany za pomocą skryptu "randomTable.py")
file = open('999_odwrotnie_posortowana.txt', 'r').read()
lines=file.split('\n')
A=[]

for line in lines :
    liczba = int(line)
    A.append(liczba)

#Tutaj wywołanie funkcji i zmierzenie czasu działania
n1 = dt.datetime.now()
mergeSort(A)
n2 = dt.datetime.now()

#Tutaj wszelkie zeczy które chce sobie wyświetlić po sortowaniu
print("Sorted array is: ")
print(A, "\n")

print("***Sortowanie mergesort*** ", "\n")

print("Długość tablicy wejściowej: ")
print(len(A), "\n")
print("Czas obliczeń [s]:  ")

g=((n2.hour-n1.hour)*3600)*1000000
m= (((n2.minute-n1.minute)*60))*1000000
s= ((n2.second-n1.second))*1000000
us=(n2.microsecond-n1.microsecond)

print((g+m+s+us)/1000000)

