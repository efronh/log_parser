# Basit log dosyasi okuyucu ve ozet raporlayici
# Sadece Python'un yerlesik kutuphaneleri kullanilir

import sys


def oku_log_dosyasi(dosya_yolu):
  
    satirlar = []
    dosya = open(dosya_yolu, "r", encoding="utf-8")
    for satir in dosya:
        satirlar.append(satir)
    dosya.close()
    return satirlar


def seviye_bul(satir):
  
    temiz = satir.strip()
    if temiz == "":
        return None

    parcalar = temiz.split()
    if len(parcalar) < 3:
        return None

    seviye = parcalar[2]
    if seviye in ("INFO", "WARNING", "HIGH", "CRITICAL"):
        return seviye

    return None


def sayim_yap(satirlar):
  
    sayilar = {
        "INFO": 0,
        "WARNING": 0,
        "HIGH": 0,
        "CRITICAL": 0,
    }

    for satir in satirlar:
        seviye = seviye_bul(satir)
        if seviye is not None:
            sayilar[seviye] = sayilar[seviye] + 1

    return sayilar


def uyari_satirlarini_kaydet(satirlar, cikti_dosyasi):
 
    #HIGH ve CRITICAL seviyeli satirlari alerts.txt dosyasina yazar.

    dosya = open(cikti_dosyasi, "w", encoding="utf-8")
    for satir in satirlar:
        seviye = seviye_bul(satir)
        if seviye == "HIGH" or seviye == "CRITICAL":
            dosya.write(satir)
            if not satir.endswith("\n"):
                dosya.write("\n")
    dosya.close()


def rapor_yazdir(sayilar, toplam_satir):
   
    print("")
    print("=" * 40)
    print("LOG OZET RAPORU")
    print("=" * 40)
    print("Toplam okunan satir:", toplam_satir)
    print("")
    print("INFO     :", sayilar["INFO"])
    print("WARNING  :", sayilar["WARNING"])
    print("HIGH     :", sayilar["HIGH"])
    print("CRITICAL :", sayilar["CRITICAL"])
    print("")
    uyari_toplam = sayilar["HIGH"] + sayilar["CRITICAL"]
    print("Uyari dosyasina yazilan (HIGH + CRITICAL):", uyari_toplam)
    print("=" * 40)
    print("")


def main():
  
    if len(sys.argv) > 1:
        log_dosyasi = sys.argv[1]
    else:
        log_dosyasi = "sample.log"

    print("Okunan dosya:", log_dosyasi)

    satirlar = oku_log_dosyasi(log_dosyasi)
    sayilar = sayim_yap(satirlar)
    uyari_satirlarini_kaydet(satirlar, "alerts.txt")
    rapor_yazdir(sayilar, len(satirlar))

    print("HIGH ve CRITICAL satirlar 'alerts.txt' dosyasina kaydedildi.")


if __name__ == "__main__":
    main()
