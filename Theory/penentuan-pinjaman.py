def pinjamanValid(penghasilan: int, punyaJaminan: bool) -> bool | str:
    BATAS_PENGHASILAN: int = 5000000
    
    if penghasilan >= BATAS_PENGHASILAN and punyaJaminan:
        return True
    elif penghasilan < BATAS_PENGHASILAN and not punyaJaminan:
        return "Pinjaman Dipertimbangkan"
    else:
        return False

def main():
    inputPenghasilan: int = int(input("Masukkan penghasilan: "))
    inputJaminan: bool | str = input("Punya jaminan? (T/F): ")
    
    if inputJaminan == "T": inputJaminan = True
    else: inputJaminan = False
    
    statusPinjaman: bool | str = pinjamanValid(inputPenghasilan, inputJaminan)
    
    if statusPinjaman == True:
        print("Pinjaman disetujui!")
    elif statusPinjaman == "Pinjaman Dipertimbangkan":
        print("Pinjaman akan dipertimbangkan lebih lanjut")
    else:
        print("Pinjaman ditolak")

main()