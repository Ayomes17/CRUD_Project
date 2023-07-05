from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "pk":"xxxxxx",
    "date_add":"yyyy-mm-dd",
    "judul":255*" ",
    "penulis":255*" ",
    "tahun":"yyyy"
}

def init_console():
    try:
        with open(DB_NAME,"r") as file:
            print("DB tersedia")
    except:
        print("DB tidak ada")
        Operasi.create_first_data()
       