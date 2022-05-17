import datetime as dt


def sortowanieBabelkowe(arr):

    n=len(arr)
    j=n-1
    while j>0:
        for  i in range(0,j):
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1]= arr[i+1], arr[i]
        j=j-1


# Tutaj tworze tablice z randomowmi wartościami na podstawie pliku wyniki.txt (wygenerowany za pomocą skryptu "randomTable.py")
file = open('999_random.txt', 'r').read()
lines = file.split('\n')
arr = []

for line in lines:
    liczba = int(line)
    arr.append(liczba)


#Tutaj wywołanie funkcji i zmierzenie czasu działania
n1 = dt.datetime.now()
sortowanieBabelkowe(arr)
n2 = dt.datetime.now()


#Tutaj wszelkie zeczy które chce sobie wyświetlić po sortowaniu
print("Sorted array is: ")
print(arr, "\n")

print("***Sortowanie bąbelkowe*** ", "\n")

print("Czas obliczeń [s]:  ")

g=((n2.hour-n1.hour)*3600)*1000000
m= (((n2.minute-n1.minute)*60))*1000000
s= ((n2.second-n1.second))*1000000
us=(n2.microsecond-n1.microsecond)

print((g+m+s+us)/1000000)

