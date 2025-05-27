# Stack sebagai list
stack = []

# Operasi Stack
def push(item):
    stack.append(item)
    print(f"{item} telah ditambahkan ke stack.")

def pop():
    if not stack:
        print("Stack kosong. Tidak bisa melakukan pop.")
    else:
        removed = stack.pop()
        print(f"{removed} telah dihapus dari stack.")

def peek():
    if not stack:
        print("Stack kosong. Tidak ada item untuk dilihat.")
    else:
        print(f"Item paling atas di stack adalah: {stack[-1]}")

def tampilkan_stack():
    if not stack:
        print("Stack kosong.")
    else:
        print("Isi stack saat ini:", stack)

# Menu Interaktif
while True:
    print("\nMenu Stack:")
    print("1. Push (Tambah data)")
    print("2. Pop (Ambil data)")
    print("3. Peek (Lihat paling atas)")
    print("4. Tampilkan Stack")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        data = input("Masukkan data yang ingin ditambahkan: ")
        push(data)
    elif pilihan == "2":
        pop()
    elif pilihan == "3":
        peek()
    elif pilihan == "4":
        tampilkan_stack()
    elif pilihan == "5":
        print("Terima kasih. Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")