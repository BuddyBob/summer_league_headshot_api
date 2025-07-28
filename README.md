# NBA Summer League Headshots

A comprehensive collection of NBA Summer League player headshots with an easy-to-use Python API.

## Installation

```bash
pip install nba-summer-league-headshots
```

## Usage

### Python API

```python
from nba_summer_league_headshots import get_headshot, download_players

# Get a specific player's headshot
headshot_path = get_headshot("Bronny James")
print(f"Bronny James headshot: {headshot_path}")

# Download multiple players to a directory
players = ["Bronny James", "Dalton Knecht", "Reed Sheppard"]
result = download_players(players, "./my_headshots")
print(f"Downloaded: {result['total_found']}, Missing: {result['total_missing']}")
```

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

## Features

- **700+ Player Headshots**: Comprehensive collection of NBA Summer League players
- **Easy Python API**: Simple functions to access player headshots
- **Command Line Interface**: Use from terminal for quick access
- **Search Functionality**: Find players by partial name matching
- **Random Player Selection**: Get random player headshots
- **Bundled Images**: All headshots included in the package

## Data Sources

The headshots are collected from multiple sources:
- NBA Official API
- RealGM
- Other publicly available sources

## Methods

| Method | Description | Returns |
|--------|-------------|---------|
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
