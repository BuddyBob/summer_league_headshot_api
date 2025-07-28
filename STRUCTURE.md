# Project Structure

```
eluvioNBAscraper/
├── README.md                     # API documentation and usage
├── STRUCTURE.md                  # This project structure document
├── gleague_api.py                # Main API for accessing headshots
├── NBA_Roster_Clean.csv          # Clean roster data (474 players)
├── missing_players.csv           # Players without headshots (41 remaining)
├── scrapers/                     # All scraping scripts
│   ├── nba_api_scraper.py       # NBA API player matching
│   ├── nba_site_scraper.py      # NBA.com Selenium scraper  
│   ├── realgm_scraper.py        # RealGM scraper
│   └── utils/                   # Utility functions
│       ├── download_nba_headshots.py  # NBA API headshot downloader
│       └── filename_utils.py    # Name cleaning utilities
└── Data Directories:
    ├── NBA_API_Headshots/       # 171 official NBA headshots
    ├── NBA_Scraped_Headshots/   # Scraped NBA.com headshots  
    ├── RealGM_Headshots/        # 170 RealGM community headshots
    └── NBA_Combined_Headshots/  # 431 final combined dataset
```
