
# Program Evaluasi Mahasiswa

# Input nilai mahasiswa
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))
kehadiran = float(input("Masukkan persentase kehadiran: "))

# Menghitung nilai akhir
nilai_akhir = (0.20 * tugas) + (0.30 * uts) + (0.50 * uas)

# Menentukan status kelulusan
if nilai_akhir >= 75 and kehadiran >= 80:
    if nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 == 0:
        status = "LULUS DENGAN PREDIKAT"
    else:
        status = "LULUS"
else:
    status = "BELUM LULUS"

# Menampilkan hasil
print("\n=== HASIL EVALUASI MAHASISWA ===")
print(f"Nilai akhir: {nilai_akhir:.2f}")
print(f"Status: {status}")