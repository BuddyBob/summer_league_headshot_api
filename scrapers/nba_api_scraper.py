#!/usr/bin/env python3
import csv
from nba_api.stats.static import players

def find_nba_players():
    found_players = []
    
    with open('../NBA_Roster_Clean.csv', 'r') as f:
        roster = list(csv.DictReader(f))
        
    for row in roster:
        player_name = row['Player'].strip().strip('"')
        matches = players.find_players_by_full_name(player_name)
        
        if len(matches) == 1:
            player = matches[0]
            found_players.append([
                row['Team'], player_name, player['id'], 
                player['full_name'], player['is_active']
            ])
    
    with open('../found_players.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Team', 'Player', 'NBA_ID', 'Full_Name', 'Is_Active'])
        writer.writerows(found_players)
    
    print(f"Found: {len(found_players)}/{len(roster)} players")

if __name__ == "__main__":
    find_nba_players()