#!/usr/bin/env python3
import csv
import requests
from pathlib import Path
from filename_utils import clean_filename

def download_nba_headshots():
    input_file = '../../found_players.csv'
    download_dir = Path('../../NBA_API_Headshots')
    download_dir.mkdir(exist_ok=True)
    
    if not Path(input_file).exists():
        print(f"Error: {input_file} not found")
        return
    
    success = failed = 0
    
    with open(input_file, 'r') as f:
        players = list(csv.DictReader(f))
        
    for i, row in enumerate(players, 1):
        filename = clean_filename(row['Player'])
        url = f"https://cdn.nba.com/headshots/nba/latest/260x190/{row['NBA_ID']}.png"
        
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                (download_dir / f"{filename}.png").write_bytes(response.content)
                success += 1
            else:
                failed += 1
        except:
            failed += 1
    
    print(f"Downloaded: {success}, Failed: {failed}")

if __name__ == "__main__":
    download_nba_headshots()
