from . import Operasi

def update_console():
    read_console()
    while (True):
        print("Silahkan Pilih Nomor Buku Yang Diupdate")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)
        if data_buku:
            break
        else:
            print("Nomor Tidak Valid. Masukan Lagi No!")
    
    data_break = data_buku.split(",")
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while (True):
        print("\n"+"="*100)
        print("Silahkan Pilih Data Yang Ingin Diubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        user_option = input("Pilih Data [1,2,3]: ")
        print("\n"+"="*100)
        match user_option:
            case "1" : judul = input("Judul\t :")
            case "2" : penulis = input("Penulis\t :")
            case "3" : 
                 while (True):
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun harus 4 angka!")
                    except:
                        print("Tahun harus angka!")
            case _: print("Index Salah!")

        print("Data Baru Anda")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        is_done = input("Apakah sudah selesai update (y/n)?")
        if (is_done == "y") or (is_done == "Y"):
            break   

    Operasi.update(no_buku,pk,data_add,judul,penulis,tahun)

def create_console():
    print("\n\n"+"="*100)
    print("Silahkan Tambahkan Buku\n")
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while (True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus 4 angka!")
        except:
            print("Tahun harus angka!")

    Operasi.create(penulis,judul,tahun)
    print("\nData Baru Anda")
    read_console()


def read_console():
    data_file = Operasi.read()
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    #Header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)
    
    #Data
    for index, data in enumerate(data_file):
        data_break = data.split(",")

        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}")

    #Footer
    print("="*100+"\n")