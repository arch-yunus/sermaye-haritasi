import os
import json
import re

def parse_readme():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    readme_path = os.path.join(base_dir, 'README.md')
    
    # Try different encodings
    content = ""
    for enc in ['utf-16', 'utf-8']:
        try:
            with open(readme_path, 'r', encoding=enc) as f:
                content = f.read()
            break
        except UnicodeDecodeError:
            continue
            
    if not content:
        raise ValueError("Could not read README.md with utf-16 or utf-8")

    lines = content.split('\n')
    registry = []
    
    # Regex for table rows starting and ending with |
    row_pattern = re.compile(r'^\s*\|(.*)\|\s*$')
    
    for line in lines:
        match = row_pattern.match(line)
        if match:
            # Split by |
            cells = [cell.strip() for cell in match.group(1).split('|')]
            if len(cells) >= 6:
                rank_str = cells[0].strip()
                if rank_str.isdigit():
                    # Parse data
                    name = cells[1].replace('**', '').strip()
                    net_worth_raw = cells[2]
                    company = cells[3]
                    citizenship = cells[4]
                    ethnicity = cells[5]
                    
                    # Clean net worth (e.g., "$839.1 B" -> 839.1)
                    net_worth_val = 0.0
                    try:
                        nw_clean = net_worth_raw.replace('$', '').replace('B', '').strip()
                        net_worth_val = float(nw_clean)
                    except ValueError:
                        pass
                        
                    registry.append({
                        "rank": int(rank_str),
                        "name": name,
                        "net_worth_billions": net_worth_val,
                        "company_source": company,
                        "citizenship": citizenship,
                        "ethnicity_background": ethnicity
                    })

    # Output to data/capital_registry.json
    data_dir = os.path.join(base_dir, 'data')
    os.makedirs(data_dir, exist_ok=True)
    out_path = os.path.join(data_dir, 'capital_registry.json')
    
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(registry, f, ensure_ascii=False, indent=4)
        
    print(f"Extracted {len(registry)} records to {out_path}")

if __name__ == "__main__":
    parse_readme()
