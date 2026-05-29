# Sermaye Haritası'na Katkıda Bulunma Rehberi (CONTRIBUTING)

Bu açık kaynaklı repo, küresel sermayenin felsefi, sosyolojik ve istatistiksel köklerini incelemek için var. Birlikte daha karanlık, daha derin ve daha doğru bir veri tabanı inşa edebiliriz.

## Nasıl Katkı Sağlayabilirsiniz?

### 1. Yeni Milyarder veya Etnik Şifre Eklemek
- `README.md` dosyasındaki tabloda (veya `data/capital_registry.json` içinde) eksik veya hatalı olduğunu düşündüğünüz bir net varlık / etnik köken bilgisi varsa, güvenilir kaynaklarla (biyografiler, Forbes verileri) destekleyerek Pull Request (PR) açabilirsiniz.

### 2. Yeni Analiz ve Scriptler
- Veri seti üzerinden yapılabilecek yeni istatistiksel analizleriniz mi var? (Örneğin: Yaş/Sektör korelasyonu, Şirket kuruluş yılları ve Krizler)
- `scripts/` klasörüne yeni bir `.py` dosyası ekleyin. Çıktılarınızı (grafik vb.) `outputs/` klasörüne yönlendirecek şekilde kodlayın.

### 3. Felsefi Derinleştirme
- `docs/` klasörüne, sermayenin yapısını inceleyen yeni bir sosyolojik veya ekonomik doküman ekleyebilirsiniz. 
- Alıntı havuzumuzu genişletmek için `scripts/quote_generator.py` dosyasındaki `quotes` dizisine ufuk açıcı yeni aforizmalar ekleyebilirsiniz.

## Katkı Adımları (PR Akışı)
1. Projeyi fork'layın.
2. Kendi branch'inizi oluşturun (`git checkout -b feature/yeni-analiz`).
3. Değişikliklerinizi yapın ve commit'leyin (`git commit -m 'Yeni analiz motoru eklendi'`).
4. Branch'inizi push'layın (`git push origin feature/yeni-analiz`).
5. Bir Pull Request açın.
