def statusLulus(nilai: int, presentaseKehadiran: int) -> bool:
    KKM: int = 70
    MIN_KEHADIRAN: int = 75
    lulus: bool = True
    
    if ((nilai >= KKM) and presentaseKehadiran >= MIN_KEHADIRAN):
        return lulus
    elif ((nilai >= KKM) and presentaseKehadiran < MIN_KEHADIRAN):
        return not lulus
    else: return not lulus    
    
def main():
    detailKelulusan: dict = {
        True : "Lulus",
        False : "Tidak Lulus"
    }
    
    inputNilaiAkhir: int = int(input("Masukkan nilai akhir: "))
    inputPresentaseKehadiran: int = int(input("Masukkan presentase kehadiran: "))
    
    statusAkhirKelulusan: bool = statusLulus(inputNilaiAkhir, inputPresentaseKehadiran)
    
    if statusAkhirKelulusan:
        print(detailKelulusan[True])
    else:
        print(detailKelulusan[False])

main()
    
    