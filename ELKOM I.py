print("###################################################### ")
print(" ###	                                              ")
print(" ###  ##   #######   #########   #########   ###   ### ")
print(" #######  ###   ###   ###   ###   ###   ###  ###   ### ")
print(" ###  ##  ########    ###         ###         ######## ")
print(" ###      ###         ###         ###              ### ")
print("#####      #######    ###         ###        ########\n")

def faktorial(n):
    hasil = 1
    for x in range(2,n+1):
        hasil *= x
    return hasil

print("PROGRAM MENCARI NILAI FAKTORIAL DARI SEBUAH ANGKA")
angka = int(input("Masukkan angka : "))
faktorial(angka)
print("Nilai faktorial dari",angka,"adalah",faktorial(angka))
