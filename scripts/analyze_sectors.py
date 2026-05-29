import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_sectors():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'capital_registry.json')
    out_dir = os.path.join(base_dir, 'outputs')
    os.makedirs(out_dir, exist_ok=True)
    
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    df = pd.DataFrame(data)
    
    # Simple sector classification based on keywords in company_source
    def get_sector(company):
        c = company.lower()
        if any(kw in c for kw in ['google', 'microsoft', 'amazon', 'meta', 'oracle', 'yazılım', 'tiktok', 'tencent']):
            return 'Technology/Software'
        elif any(kw in c for kw in ['finans', 'bank', 'fon', 'hedge', 'capital', 'yatırım', 'bloomberg']):
            return 'Finance/Investment'
        elif any(kw in c for kw in ['tesla', 'çelik', 'maden', 'enerji', 'otomotiv', 'sanayi', 'demir', 'kömür']):
            return 'Heavy Industry/Energy'
        elif any(kw in c for kw in ['lvmh', 'chanel', 'perakende', 'zara', 'walmart', 'gıda', 'nutella', 'l\'oréal']):
            return 'Retail/Consumer'
        else:
            return 'Other/Diversified'
            
    df['Sector'] = df['company_source'].apply(get_sector)
    
    # 1. Sector Distribution
    plt.figure(figsize=(8, 8))
    sector_counts = df['Sector'].value_counts()
    plt.pie(sector_counts.values, labels=sector_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Sectoral Distribution of UHNWIs')
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, 'sector_distribution.png'))
    plt.close()
    
    # 2. Total Net Worth by Sector
    plt.figure(figsize=(10, 6))
    sector_nw = df.groupby('Sector')['net_worth_billions'].sum().sort_values(ascending=False)
    sns.barplot(x=sector_nw.values, y=sector_nw.index, palette='cubehelix')
    plt.title('Total Net Worth by Sector (Billions USD)')
    plt.xlabel('Total Net Worth')
    plt.ylabel('Sector')
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, 'sector_net_worth.png'))
    plt.close()

    print(f"Sector analysis complete. Charts saved to {out_dir}")

if __name__ == '__main__':
    analyze_sectors()
