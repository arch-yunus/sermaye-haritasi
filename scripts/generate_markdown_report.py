import os
import json
import pandas as pd
import datetime

def generate_report():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'capital_registry.json')
    report_dir = os.path.join(base_dir, 'reports')
    os.makedirs(report_dir, exist_ok=True)
    
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    df = pd.DataFrame(data)
    
    total_wealth = df['net_worth_billions'].sum()
    top_10 = df.head(10)
    top_10_wealth = top_10['net_worth_billions'].sum()
    
    # Aggregations
    citizenship_wealth = df.groupby('citizenship')['net_worth_billions'].sum().sort_values(ascending=False).head(5)
    
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    out_path = os.path.join(report_dir, f'wealth_report_2026.md')
    
    report_md = f"""# Küresel Sermaye Raporu (2026)

*Bu rapor `sermaye-haritasi` veri tabanı üzerinden **{date_str}** tarihinde otomatik olarak üretilmiştir.*

> *"Piyasalar her zaman siyasetin bir uzantısı olmuştur."*

---

## 📊 Makro Görünüm

Sistemimizde kayıtlı **{len(df)} UHNWI**'nin (Ultra Yüksek Net Değerli Birey) toplam varlığı **${total_wealth:,.1f} Milyar** (Billion) dolar seviyesindedir.

İnanılmaz bir eşitsizlik göstergesi olarak, sadece listedeki **ilk 10 kişinin** toplam serveti **${top_10_wealth:,.1f} Milyar** dolardır. (Bu rakam, listedeki diğer tüm isimlerin servetine oranlandığında devasa bir tekel durumunu işaret eder.)

## 🌍 Ülkelere Göre Konsolidasyon (İlk 5)

| Vatandaşlık | Toplam Varlık (Milyar $) |
|---|---|
"""
    for country, wealth in citizenship_wealth.items():
        report_md += f"| {country} | ${wealth:,.1f} B |\n"
        
    report_md += """
## 👑 Oyun Kurucular (Zirve 10)

Aşağıdaki tablo, dünya jeopolitiğini şirket yönetim kurullarından idare eden "Tekno-Feodal" ve "Eski Para" lordlarının anlık durumunu yansıtır:

| Sıra | İsim | Varlık | Şirket / Kaynak | Etnik / Kültürel Kökler |
|---|---|---|---|---|
"""
    for _, row in top_10.iterrows():
        report_md += f"| {row['rank']} | **{row['name']}** | ${row['net_worth_billions']} B | {row['company_source']} | {row['ethnicity_background']} |\n"

    report_md += """
---
*Otomatik Sistem Notu: Analiz motorları çalışmaya ve sermayenin gizli damarlarını deşifre etmeye devam edecektir.*
"""

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(report_md)
        
    print(f"Report generated successfully at {out_path}")

if __name__ == "__main__":
    generate_report()
