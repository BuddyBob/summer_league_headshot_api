# NBA Summer League 2025 Player Headshots

A Python API for accessing NBA Summer League 2025 player headshots. Contains 431 verified player images across all 30 NBA teams.


## Usage

### Basic Usage

```python
from gleague_api import get_headshot, download_players

# Get single player headshot path
headshot_path = get_headshot("Javan Johnson")

# Batch download multiple players
players = ["Javan Johnson", "Ben Gregg", "Dwight Murray, Jr."]
result = download_players(players, "./output_directory")
```

### Advanced Usage

```python
from gleague_api import GLeagueAPI

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

## Dataset

- **Total Players**: 431
- **Teams**: All 30 NBA teams
- **File Formats**: PNG (NBA official), JPG (community sources)
- **Location**: `NBA_Combined_Headshots/`

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
