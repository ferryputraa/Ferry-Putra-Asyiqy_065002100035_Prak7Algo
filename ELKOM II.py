print("###################################################### ")
print(" ###	                                              ")
print(" ###  ##   #######   #########   #########   ###   ### ")
print(" #######  ###   ###   ###   ###   ###   ###  ###   ### ")
print(" ###  ##  ########    ###         ###         ######## ")
print(" ###      ###         ###         ###              ### ")
print("#####      #######    ###         ###        ########\n")

def vokal(x):
    karakter=['a','i','u','e','o','A','I','U','E','O']
    hasil=0
    for i in x:
        if i in karakter:
            hasil+=1
    return hasil

def konsonan(x):
    karakter=['a','i','u','e','o','A','I','U','E','O']
    hasil=0
    for i in x:
        if i not in karakter:
            hasil+=1
    return hasil

print("PROGRAM MENGHITUNG HURUF VOKAL DAN KONSONAN DARI KALIMAT")
kalimat=str(input("Masukkan kalimat : "))
vokal(kalimat)
konsonan(kalimat)
print("Jumlah huruf vokal    : ",vokal(kalimat))
print("Jumlah huruf konsonan : ",konsonan(kalimat))
