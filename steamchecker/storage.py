import json
import csv
from pathlib import Path

def save_stats(data, path):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.suffix == '.csv':
        keys = data[0].keys() if isinstance(data, list) and data else []
        with open(p, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            if isinstance(data, list):
                writer.writerows(data)
            else:
                writer.writerow(data)
    else:
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
