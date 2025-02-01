# Chess.com Monthly Archive Downloader

A Python script to automate the download of monthly chess game archives (in PGN format) for any Chess.com user. The script utilizes the Chess.com public API to fetch archive URLs, processes them, and saves the game data locally with proper naming conventions.

## Features
- Fetches and processes monthly game archive URLs via the Chess.com API.
- Downloads game archives in PGN format and stores them locally.
- Easily customizable for different Chess.com usernames.

## Technologies Used
- **Language**: Python 3
- **Libraries**: `urllib`

## Usage
1. Clone the repository to your local machine.
2. Open the script and update the `username` variable with the desired Chess.com username.
3. Run the script:
   ```bash
   python3 chess_com_pgn_downloader.py
