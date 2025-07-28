#!/usr/bin/env python3
import csv
import time
from pathlib import Path
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.filename_utils import clean_filename

def scrape_realgm_headshots():
    download_dir = Path('../RealGM_Headshots')
    download_dir.mkdir(exist_ok=True)
    
    # Lists to track results
    downloaded_players = []
    missed_players = []
    
    # Simplified Chrome options to prevent connection issues
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-web-security")
    
    try:
        print("Starting Chrome...")
        driver = webdriver.Chrome(options=options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        print("Loading RealGM...")
        driver.get("https://basketball.realgm.com/nba/players")
        time.sleep(3)
        
        # Load missing players from parent directory
        missing_players_data = []
        csv_path = Path(__file__).parent.parent / 'missing_players.csv'
        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                missing_players_data.append({
                    'team': row['Team'],
                    'player': row['Player'].strip(),
                    'cleaned_name': row['Cleaned_Name']
                })
        
        for i, player_data in enumerate(missing_players_data):
            player = player_data['player']
            team = player_data['team']
            print(f"\n[{i+1}/{len(missing_players_data)}] {player} ({team})")
            
            try:
                # Find search box quickly
                search_box = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "input.searchbox-text"))
                )
                
                # Clear and type
                search_box.clear()
                search_box.send_keys(player)
                search_box.send_keys(Keys.ENTER)
                time.sleep(2)
                
                # Check for multiple results
                try:
                    search_results = driver.find_element(By.XPATH, "//*[@id='site-takeover']/div[4]/div/div[1]/h1[1]")
                    if "Search Results" in search_results.text or "Players Found" in search_results.text:
                        missed_players.append(player_data)
                        continue
                except:
                    pass
                
                # Quick image search with exact selectors
                img_url = None
                selectors = [("//*[@id='site-takeover']/div[4]/div/div[2]/div[1]/div/div[1]/div[1]/img", "xpath"),("/html/body/div[1]/div[4]/div/div[2]/div[1]/div/div[1]/div[1]/img", "xpath"),(".player_profile_headshot img", "css"),("img[src*='profiles/photos']", "css"),("img[src*='profiles']", "css")]
                
                for selector, selector_type in selectors:
                    try:
                        if selector_type == "xpath":
                            img_element = driver.find_element(By.XPATH, selector)
                        else:
                            img_element = driver.find_element(By.CSS_SELECTOR, selector)
                        
                        src = img_element.get_attribute('src')
                        if src and ('profiles' in src or '.jpg' in src):
                            if src.startswith('/'):
                                img_url = f"https://basketball.realgm.com{src}"
                            else:
                                img_url = src
                            break
                    except:
                        continue
                
                if img_url:
                    # Download
                    try:
                        response = requests.get(img_url, timeout=5)
                        if response.status_code == 200:
                            filename = f"{clean_filename(player)}.jpg"
                            (download_dir / filename).write_bytes(response.content)
                            downloaded_players.append(player_data)
                            print(f"Downloaded: {filename}")
                        else:
                            missed_players.append(player_data)
                            print(f"Download failed")
                    except:
                        missed_players.append(player_data)
                        print(f"Download error")
                else:
                    missed_players.append(player_data)
                    print("No image found")
                    
            except Exception as e:
                missed_players.append(player_data)
                print(f"Error: {str(e)[:30]}")
            
            time.sleep(1)
        
        # Save results
        print(f"\nResults: Downloaded {len(downloaded_players)}, Missed {len(missed_players)}")
        
        if downloaded_players:
            with open('../realgm_downloaded.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Team', 'Player', 'Cleaned_Name'])
                for p in downloaded_players:
                    writer.writerow([p['team'], p['player'], p['cleaned_name']])
            print(f"Saved downloaded to: realgm_downloaded.csv")
        
        if missed_players:
            with open('../realgm_missed.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Team', 'Player', 'Cleaned_Name'])
                for p in missed_players:
                    writer.writerow([p['team'], p['player'], p['cleaned_name']])
            print(f"Saved missed to: realgm_missed.csv")
        
    except Exception as e:
        print(f"Critical error: {e}")
    finally:
        try:
            driver.quit()
        except:
            pass

if __name__ == "__main__":
    scrape_realgm_headshots()
