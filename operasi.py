#operasi penugasan
a = int(input('masukkan angka 1 :'));
b = int(input('masukkan angka 2 :'));

# operasi aritmatika
def aritmetika(a, b):
    def multiply(a, b):
        hasil = a * b
        return hasil
    def addition(a, b):
        hasil = a + b
        return hasil
    def division(a, b):
        hasil = a / b
        return hasil
    def subtraction(a, b):
        hasil = a - b
        return hasil
    print("hasil pengurangan : " ,subtraction(a, b), '\n',
        "hasil penambahan : ", addition(a, b), "\n",
        "hasil perkalian : ", multiply(a, b), "\n",
        "hasil pembagian : ", division(a, b), "\n")
#penugasan
def penugasan(a):
    a +=3
    return f"hasil penugasan a + 3 : {a}"

#perbandingan 
def perbandingan(a, b):
    if a == b :
        return f"{a} sama dengan  {b}"
    elif a < b :
        return f"a kurang dari b"
    else :
        return f"a lebih dari b"
#logika
def logika(a,b):
    if a or b < 10:
        return f"angka pertama atau angka kedua adalah angka di bawah 10"
    else : 
        return f"angka pertama dan angka kedua adalah angka di atas 10"

def menu():
    print("Pilih jenis operasi:")
    print("1. Aritmetika")
    print("2. Penugasan")
    print("3. Perbandingan")
    print("4. Logika")
    pilih = input("Masukkan pilihan (1-4): ")
    return pilih

pilih = menu()

match pilih:
    case "1":
        aritmetika(a,b)
    case "2":
        print(penugasan(a))
    case "3":
        print(perbandingan(a, b))
    case "4":
        print(logika(a, b))
    case _:
        print("Pilihan tidak valid.")