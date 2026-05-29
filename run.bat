@echo off
echo ==============================================
echo 🗺️ Sermaye Haritasi - Sistem Baslatiliyor...
echo ==============================================

echo [1/4] Gerekli kutuphaneler kontrol ediliyor...
pip install -r requirements.txt -q

echo.
echo [2/4] Veri cikartimi (Data Extraction) yapiliyor...
python scripts\extract_data.py

echo.
echo [3/4] Analiz Motorlari Calistiriliyor...
python scripts\analyze_demographics.py
python scripts\analyze_sectors.py

echo.
echo [4/4] Otomatik Ansiklopedi (Rapor) Uretiliyor...
python scripts\generate_markdown_report.py

echo.
echo ==============================================
echo Tum sistem calistirildi. Çıktılar "outputs\" ve "reports\" klasorlerinde.
echo ==============================================
echo.

echo Rastgele bir felsefi aforizma icin quote_generator baslatiliyor:
python scripts\quote_generator.py

echo.
echo ==============================================
echo 🌐 INTERAKTIF WEB DASHBOARD BASLATILIYOR...
echo ==============================================
echo Tarayicinizda http://localhost:8000/dashboard adresine gidin.
echo (Kapatmak icin CTRL+C yapin)
python -m http.server 8000

