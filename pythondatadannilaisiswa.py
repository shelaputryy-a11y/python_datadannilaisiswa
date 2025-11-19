import json
import os

FILE = "data_siswa.json"

# -----------------------------
# Fungsi untuk load data
# -----------------------------
def load_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# -----------------------------
# Fungsi untuk simpan data
# -----------------------------
def save_data(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# -----------------------------
# Fungsi tambah data siswa
# -----------------------------
def tambah_data():
    print("\n=== TAMBAH IDENTITAS SISWA ===")
    nama = input("NAMA PESERTA DIDIK       : ")
    sekolah = input("ASAL SEKOLAH             : ")
    kelas = input("KELAS                    : ")
    orang_tua = input("NAMA ORANG TUA           : ")
    ttl = input("TTL                      : ")

    siswa = {
        "nama": nama,
        "sekolah": sekolah,
        "kelas": kelas,
        "orang_tua": orang_tua,
        "ttl": ttl,
        "nilai": None
    }

    data = load_data()
    data.append(siswa)
    save_data(data)

    print("\n✓ DATA SISWA BERHASIL DITAMBAHKAN!")

# -----------------------------
# Fungsi input nilai
# -----------------------------
def input_nilai():
    print("\n=== Input Nilai Siswa ===")

    def input_angka(pesan):
        while True:
            try:
                return float(input(pesan))
            except ValueError:
                print("Input harus berupa angka!")

    AGAMA = input_angka("AGAMA          : ")
    JAWA = input_angka("B. JAWA        : ")
    INDO = input_angka("B. INDO        : ")
    INGGRIS = input_angka("B. Inggris     : ")
    KIMIA = input_angka("KIMIA          : ")
    FISIKA = input_angka("FISIKA         : ")
    BIOLOGI = input_angka("BIOLOGI        : ")
    SOSIOLOGI = input_angka("SOSIOLOGI      : ")
    EKONOMI = input_angka("EKONOMI        : ")
    GEOGRAFI = input_angka("GEOGRAFI       : ")
    SEJARAH = input_angka("SEJARAH        : ")
    MATEMATIKA = input_angka("MATEMATIKA     : ")
    INFORMATIKA = input_angka("INFORMATIKA    : ")
    SENIBUDAYA = input_angka("SENIBUDAYA     : ")
    OLAHRAGA = input_angka("OLAHRAGA       : ")
    PKN = input_angka("PKN            : ")

    rata = (AGAMA + JAWA + INDO + INGGRIS + KIMIA + FISIKA + BIOLOGI + SOSIOLOGI +
            EKONOMI + GEOGRAFI + SEJARAH + MATEMATIKA + INFORMATIKA +
            SENIBUDAYA + OLAHRAGA + PKN) / 16

    status = "LULUS" if rata >= 75 else "TIDAK LULUS"

    return {
        "AGAMA": AGAMA,
        "JAWA": JAWA,
        "INDO": INDO,
        "INGGRIS": INGGRIS,
        "KIMIA": KIMIA,
        "FISIKA": FISIKA,
        "BIOLOGI": BIOLOGI,
        "SOSIOLOGI": SOSIOLOGI,
        "EKONOMI": EKONOMI,
        "GEOGRAFI": GEOGRAFI,
        "SEJARAH": SEJARAH,
        "MATEMATIKA": MATEMATIKA,
        "INFORMATIKA": INFORMATIKA,
        "SENIBUDAYA": SENIBUDAYA,
        "OLAHRAGA": OLAHRAGA,
        "PKN": PKN,
        "rata": rata,
        "status": status
    }

# -----------------------------
# Fungsi simpan nilai ke siswa
# -----------------------------
def tambah_nilai():
    data = load_data()
    if len(data) == 0:
        print("\nTambahkan data siswa terlebih dahulu!")
        return

    print("\nPilih siswa untuk menambahkan nilai:")
    for i, siswa in enumerate(data, start=1):
        print(f"{i}. {siswa['nama']}")

    try:
        pilih = int(input("Masukkan nomor siswa: "))
    except ValueError:
        print("Input harus angka!")
        return

    if pilih < 1 or pilih > len(data):
        print("Pilihan tidak valid!")
        return

    nilai = input_nilai()
    data[pilih - 1]["nilai"] = nilai
    save_data(data)

    print("\n✓ DATA NILAI SISWA BERHASIL DITAMBAHKAN!\n")

# -----------------------------
# Fungsi tampilkan semua data
# -----------------------------
def tampilkan_data():
    print("\n=== Data Semua Siswa ===")
    data = load_data()

    if not data:
        print("Belum ada data siswa.")
        return

    for i, siswa in enumerate(data, start=1):
        print("\n----------------------------------------")
        print(f"Siswa ke-{i}")
        print("----------------------------------------")
        print(f"NAMA PESERTA DIDIK : {siswa['nama']}")
        print(f"ASAL SEKOLAH       : {siswa['sekolah']}")
        print(f"KELAS              : {siswa['kelas']}")
        print(f"NAMA ORANG TUA     : {siswa['orang_tua']}")
        print(f"TTL                : {siswa['ttl']}")

        # 🔥 Cek apakah siswa sudah punya nilai
        if "nilai" not in siswa or siswa["nilai"] is None:
            print("Belum ada nilai.")
        else:
            print("\n--- NILAI ---")
            for mapel, nilai in siswa["nilai"].items():
                print(f"{mapel.upper():15} : {nilai}")

# -----------------------------
# Menu Utama
# -----------------------------
def main():
    while True:
        print("\n=== Aplikasi Data Siswa ===")
        print("1. Tambah Data Siswa")
        print("2. Tambah Data Nilai")
        print("3. Tampilkan Semua Data")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tambah_nilai()
        elif pilihan == "3":
            tampilkan_data()
        elif pilihan == "4":
            print("Keluar dari aplikasi. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan program
main()

