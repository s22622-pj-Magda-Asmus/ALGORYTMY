import numpy
B=[" ",'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','W','X','Y','Z',"a","b","c","d","e","f","g",'h','i','j','k','l','m','n','o','p','r','s','t','u','w','x','y','z'];
Z=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
i=0;

def main(B,A,Z):
    # tutaj zliczam ilosc wystapien liter w tekscie
    for n in range(len(B)):
        for m in range(len(A)):
            if B[n] == A[m]:
                Z[n]= Z[n]+1
    print("tablica z literami:")
    print(B)
    print("tablica zawierajaca ilości wystapień poszczególnych literek: ")
    print(Z);

    S= createTabeOfLettersThatAppears(Z,B)
    dictionary= createEmptyDictionary(Z)

    # kopcowanie tablicy wejsciowej S
    for i in range(int(n / 2),-1,-1):
        n = len(S)
        minHeap(S, n, i);

    print("Przekopcowana tablica wyjsciowa: ")
    print(S)

    ti = []
    for d in range(len(S)-1):
        print("-----------------------------------------------------------------------------------")
        minHeap(S,len(S), d)

        # WSZYSTKO DO X:
        x = S[0]
        xi=[x,0]
        ti.append(xi)
        S[0],S[len(S)-1] = S[len(S)-1], S[0];
        print("x= ", x)
        S.pop(len(S)-1)
        print(S)
        minHeap(S,len(S),0)
        print("kopiec: " , S)

        # WSZYSTKO DO Y:
        y = S[0]
        yi=[y,1]
        ti.append(yi)
        S[0], S[len(S) - 1] = S[len(S) - 1], S[0];
        print("y= ", y)
        S.pop(len(S) - 1)
        print(S)
        minHeap(S, len(S), 0)
        print("kopiec: ", S)

        # WEZEŁ
        print("--------------------")
        print("WEZEŁ:")
        z=[x[0]+y[0], x[1]+y[1]]
        print(z)
        insert(S, z)

    print("Tablica ti reprezentująca drzewo: ")
    print(ti)
    dictionary = createBitsDictionary(ti,dictionary)

    # tworze ciag "0" "1" reprezentujacych znaki w tekscie
    wynik=""
    for i in range(len(A)):
        # print(A[i])
        for j in range(len(dictionary)):
            if A[i] == dictionary[j][0]:
                # print(A[i],"=",dictionary[j][1])
                wynik=wynik+dictionary[j][1]

    print("wynik", wynik)


    # mój "wynik"  to tablica stringów ale ja chce to zapisac bitowo więć:
    w = [wynik[i:i + 8] for i in range(0, len(wynik), 8)]
    # print(w)
    for x in range(len(w)):
        value = int((w[x]), 2).to_bytes(1, "little")
        # print(value)
        f = open("wyjsciowy.txt", "ab")
        f.write(value)
        f.close()

def createEmptyDictionary(Z):
    k = 0;
    # ten for wylicza ile literek wystapiło w stringu
    for c in range(len(Z)):
        if Z[c] != 0:
            k = k + 1;
    m = 2;
    # tu tworze pusta tablice dwuwymiarowa
    dictionary=[[0]*m]*k;
    return dictionary

def createTabeOfLettersThatAppears(Z,B):
    k=0;
    # ten for wylicza ile literek wystapiło w stringu
    for c in range(len(Z)):
        if Z[c]!=0:
            k=k+1;
    m=2;
    # tu tworze pusta tablice dwuwymiarowa która bedzie zawierac literke i liczbe jej powtorzeń w stringu
    S=[[0]*m]*k;
    # dictionary=[[0]*m]*k;

    # tu chce wypełnic tablice dwuwymiarowa danymi
    j = 0;
    for v in range(len(Z)):
        if Z[v]!=0:
            S[[j][0]]=[B[v],Z[v]];
            j=j+1;
    print("utworzona tablica: ")
    print(S);
    return S

def minHeap(S,n,i):
    l = 2 * i + 1
    r = 2 * i + 2
    smallest = i
    if l < n and S[l][1] < S[i][1]:
        smallest = l

    if r < n and S[smallest][1] > S[r][1]:
        smallest = r

    if smallest != i:
        S[i], S[smallest] = S[smallest], S[i]
        minHeap(S, n, smallest)


def insert(S,x):
    print("--------------------")
    print("INSERT: ")
    S.append(x);
    print("przed kopcowaniem: ")
    print(S);
    print("-----------------------------------------------------------------------------------")

    return S

def createBitsDictionary(ti,dictionary):
    j = 0
    stringDictionary= ""
    for x in range(len(ti)):
        if len(ti[x][0][0])==1:
            print("---------------------------------")
            print("Do sprawdzenia", ti[x])
            l=ti[x][0][0]
            print(l)
            kod=""
            for y in range(len(ti)):
                # print(ti[y][0][0])
                if ti[y][0][0].find(ti[x][0][0])!=-1:
                    # print(ti[y][0][0])
                    kod=kod+str(ti[y][1])

            kodd=list(reversed(kod))
            print(kodd)

            # tworzenie stringa
            kodString = ""
            for x in range(len(kodd)):
                kodString = kodString + kodd[x]
            print(kodString)


            dictionary[[j][0]] = [l, kodString];
            stringDictionary= stringDictionary + l + "= " + kodString +",  "

            j = j + 1

    print("-----------------------------------------------------------------------------------")
    print("słownik:  ", dictionary);

    f = open("wyjsciowy.txt", "w")
    f.write(stringDictionary)
    f.close()
    return dictionary

file = open('wejsciowe.txt', 'r').read()
print(file)
A=file

main(B, A, Z);


