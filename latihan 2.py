print ('========== latihan 2 ============')
print ('menampilkan bilangan terbesar dan berhenti ketika input angka 0')

a = 1
b = 1
c = 1
d = 1
e = 1
f = 1
g = 1
while g != 0:
        a = int(input("masukkan angka: "))
        b = int(input("masukkan angka: "))
        c = int(input("masukkan angka: "))
        d = int(input("masukkan angka: "))
        e = int(input("masukkan angka: "))
        f = int(input("masukkan angka: "))
        g = int(input("masukkan angka: "))

        if a>b and a>c and a>d and a>e and a>f and a>g:
               print("bilangan terbesar adalah: ",a)
        elif b>a and b>c and b>d and b>e and b>f and b>g:
               print("bilangan terbesar adalah: ",b)
        elif c>b and c>a and c>d and c>e and c>f and c>g:
               print("bilangan terbesar adalah: ",c)
        elif d>b and d>c and d>a and d>e and d>f and d>g:
               print("bilangan terbesar adalah: ",d)
        elif e>b and e>c and e>d and e>a and e>f and e>g:
               print("bilangan terbesar adalah: ",e)
        elif f>b and f>c and f>d and f>e and f>a and f>g:
               print("bilangan terbesar adalah: ",f)
        else:
               print("bilangan terbesar adalah: ",g)
               
