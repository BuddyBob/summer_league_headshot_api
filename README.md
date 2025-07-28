# NBA Summer League Headshots

A comprehensive collection of NBA Summer League player headshots with an easy-to-use Python API.

## Installation

```bash
pip install nba-summer-league-headshots
```

## Usage

### Python API

```python
from nba_summer_league_headshots import get_headshot, copy_headshot, download_players

# Get path to a player's headshot (in package installation directory)
headshot_path = get_headshot("Bronny James")
print(f"Bronny James headshot: {headshot_path}")

# Copy a player's headshot to your local directory
local_path = copy_headshot("Bronny James", "./my_headshots")
print(f"Copied to: {local_path}")

# Download multiple players to a directory
players = ["Bronny James", "Dalton Knecht", "Reed Sheppard"]
result = download_players(players, "./my_headshots")
print(f"Downloaded: {result['total_found']}, Missing: {result['total_missing']}")
```

> **Note**: `get_headshot()` returns the path to the image in the package installation directory. Use `copy_headshot()` to copy the image to your local working directory for easier access.

### Command Line Interface

```bash
# Get a player's headshot
nba-headshots get "Bronny James"

# List all players
nba-headshots list

# Get a random player
nba-headshots random

# Search for players
nba-headshots search "Cooper"
```

### Advanced Usage

```python
from nba_summer_league_headshots import GLeagueAPI

api = GLeagueAPI()

# Get player headshot
headshot = api.get_player("Player Name")

# Get all players from a team
team_players = api.get_team("Atlanta Hawks")

# Search players by name
matches = api.search_players("johnson")

# List all available players
all_players = api.list_all_players()

# Batch download with results
result = api.batch_download(["Player 1", "Player 2"], "./output")
print(f"Downloaded: {result['total_found']}, Missing: {result['total_missing']}")
```

## Data Sources

The headshots are collected from multiple sources:
- NBA Official API
- RealGM
- Other publicly available sources

## Methods

| Method | Description | Returns |
|--------|-------------|---------|
| `get_headshot(name)` | Get player headshot path (package location) | `str` or `None` |
| `copy_headshot(name, output_dir)` | Copy headshot to local directory | `str` or `None` |
| `download_players(names, output_dir)` | Download multiple players | `Dict` with results |
| `get_player(name)` | Get single player headshot path | `str` or `None` |
| `get_team(team_name)` | Get all players from team | `List[Dict]` |
| `batch_download(names, output_dir)` | Download multiple players | `Dict` with results |
| `search_players(query)` | Search players by name | `List[str]` |
| `list_all_players()` | List all available players | `List[str]` |

## Data Structure

Player objects contain:
```python
{
    'name': 'Player Name',
    'team': 'Team Name', 
    'headshot_path': '/path/to/image.jpg'
}
```

Batch download results:
```python
{
    'found': [{'name': 'Player', 'file': '/path/to/copy.jpg'}],
    'not_found': ['Missing Player'],
    'total_found': 2,
    'total_missing': 1,
    'output_dir': '/output/path'
}
```
