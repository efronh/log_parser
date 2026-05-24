# Log Parser — Kritik Log Filtreleyici

Büyük log dosyalarından kritik olayları otomatik olarak ayıklayan, sade Python ile yazılmış bir araç.

## Neden yaptım

SOC analistleri her gün binlerce log satırıyla çalışır. 
Bunları elle okumak imkansızdır. Bu script tüm logları 
tarayarak yalnızca HIGH ve CRITICAL olanları ayırır — 
önce en önemlilere odaklanmayı sağlar.

## Ne yapar

- Log dosyasını satır satır okur
- Seviye tespiti yapar: INFO, WARNING, HIGH, CRITICAL
- Her seviyeden kaç satır olduğunu sayar
- HIGH ve CRITICAL satırları alerts.txt dosyasına kaydeder
- Ekrana özet rapor yazdırır

## Kullanım

```bash
python log_parser.py sample.log
```

Ya da varsayılan örnek dosyayla:
```bash
python log_parser.py
```

## Örnek çıktı
LOG OZET RAPORU
Toplam okunan satir: 20
INFO     : 9
WARNING  : 4
HIGH     : 3
CRITICAL : 2
Uyari dosyasina yazilan (HIGH + CRITICAL): 5
## Teknoloji

- Python 3 — yalnızca yerleşik kütüphaneler kullanıldı

## Motivasyon

Gerçek SOC ortamlarında log analizinin nasıl çalıştığını 
anlamak ve Python becerilerimi geliştirmek için yaptım.
