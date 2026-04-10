def biayaPengiriman(tipePengiriman: str, jarakPengiriman: int, harga: int = 0) -> int:
    BATAS_JARAK: int = 10
    hargaPengali: int = 5000
    
    daftarTipePengiriman: list[str] = [
        "Ekspres",
        "Reguler"
    ]        
        
    if ((tipePengiriman in daftarTipePengiriman[0].lower()) and jarakPengiriman < BATAS_JARAK ): 
        return hargaPengali * 4
    elif ((tipePengiriman in daftarTipePengiriman[0].lower()) and jarakPengiriman >= BATAS_JARAK):
        return hargaPengali * 6
    elif ((tipePengiriman in daftarTipePengiriman[1].lower()) and jarakPengiriman < BATAS_JARAK):
        return hargaPengali * 2
    else:
        return hargaPengali * 3  
    

def main():
    inpuTipePengiriman: str = input("Pilih tipe pengiriman (Ekspres/Reguler): ").lower()
    inputJarakPengiriman: int = int(input("Masukkan jarak pengiriman barang: "))
    
    biayaAkhirPengiriman: int = biayaPengiriman(inpuTipePengiriman, inputJarakPengiriman)
    print(f"Harga akhir pengiriman barang adalah Rp{biayaAkhirPengiriman:.2f}")

main()