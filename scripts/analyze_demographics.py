import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

def analyze_demographics():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'capital_registry.json')
    out_dir = os.path.join(base_dir, 'outputs')
    os.makedirs(out_dir, exist_ok=True)
    
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    df = pd.DataFrame(data)
    
    # 1. Top 10 Citizenships
    plt.figure(figsize=(10, 6))
    citizenship_counts = df['citizenship'].value_counts().head(10)
    sns.barplot(y=citizenship_counts.index, x=citizenship_counts.values, palette='viridis')
    plt.title('Top 10 Citizenships among UHNWIs')
    plt.xlabel('Count')
    plt.ylabel('Citizenship')
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, 'top_citizenships.png'))
    plt.close()
    
    # 2. Extract keywords from ethnicity to find major groups
    ethnicity_text = " ".join(df['ethnicity_background'].dropna().tolist())
    keywords = ['Aşkenaz', 'Han Çinlisi', 'İngiliz', 'Alman', 'Rus', 'İtalyan', 'Gucerat', 'Fransız']
    
    keyword_counts = {k: 0 for k in keywords}
    for k in keywords:
        # basic substring count
        keyword_counts[k] = ethnicity_text.count(k)
        
    plt.figure(figsize=(10, 6))
    sns.barplot(x=list(keyword_counts.values()), y=list(keyword_counts.keys()), palette='magma')
    plt.title('Frequency of Key Ethnic Background Identifiers')
    plt.xlabel('Mention Count in Dataset')
    plt.ylabel('Ethnic Identifier')
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, 'ethnicity_keywords.png'))
    plt.close()
    
    print(f"Demographics analysis complete. Charts saved to {out_dir}")

if __name__ == '__main__':
    analyze_demographics()
