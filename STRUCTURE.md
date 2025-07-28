# NBA Summer League 2025 Headshots API - Project Structure

```
summer_league_headshot_api/
├── README.md                          # Package documentation and usage
├── STRUCTURE.md                       # This project structure document
├── pyproject.toml                     
├── setup.py                           # Legacy package setup (compatibility)
├── MANIFEST.in                        
├── LICENSE                            
├── .gitignore                         
├── missing_players.csv                # Development: Players without headshots
│
├── nba_summer_league_headshots/       
│   ├── __init__.py                    
│   ├── api.py                         # Core API implementation
│   ├── cli.py                         # Command-line interface
│   ├── NBA_Roster_Clean.csv           # Package data: 474 player roster
│   └── NBA_Combined_Headshots/        # Package data: 431 player images
│       ├── Player_Name.jpg/.png         
│       └── ...
│
└── scrapers/              
    ├── nba_api_scraper.py        # NBA API player matching
    ├── nba_site_scraper.py       # NBA.com Selenium scraper  
    ├── realgm_scraper.py         # RealGM scraper
    └── utils/                    # Utility functions
        ├── download_nba_headshots.py  # NBA API headshot downloader
        └── filename_utils.py      
```
