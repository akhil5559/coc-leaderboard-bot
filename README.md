# Discord Leaderboard Bot

A Discord bot for managing Clash of Clans leaderboards with automatic trophy tracking and daily offense/defense tracking.

## Features

- **Player Registration**: Register players to the leaderboard
- **Account Linking**: Link multiple Clash of Clans accounts to Discord users
- **Leaderboard Display**: View sorted leaderboards with trophy counts
- **Automatic Updates**: Auto-refresh leaderboard every minute
- **Pagination**: Navigate through leaderboard pages
- **Admin Commands**: Administrator-only commands for management

## Commands

- `!register` - Register your linked account to the leaderboard
- `!link <tag>` - Link a Clash of Clans account to your Discord user
- `!unlink <tag>` - Unlink a Clash of Clans account
- `!leaderboard [name] [color]` - Display the leaderboard (Admin only)
- `!remove <tag>` - Remove a player from the leaderboard (Admin only)
- `!unregister <tag>` - Unregister a player from the leaderboard
- `!set_log_channel` - Set the log channel for bot events (Admin only)

## Setup

### Prerequisites

- Python 3.8 or higher
- Discord Bot Token

### Installation

1. **Clone or download the project files**

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your Discord bot token:**
   ```bash
   export DISCORD_TOKEN="your_discord_bot_token_here"
   ```
   
   Or create a `.env` file:
   ```
   DISCORD_TOKEN=your_discord_bot_token_here
   ```

5. **Run the bot:**
   ```bash
   python main.py
   ```

## Bot Permissions

Make sure your Discord bot has the following permissions:
- Send Messages
- Embed Links
- Add Reactions
- Read Message History
- Use Slash Commands (if using slash commands)

## File Structure

```
├── main.py                 # Main bot file
├── database.py             # Database operations
├── utils.py                # Utility functions
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── test_basic.py          # Basic functionality tests
├── data/                  # Data storage directory
│   ├── players.json       # Player data
│   └── leaderboard.json   # Leaderboard data
└── commands/              # Bot command modules
    ├── leaderboard.py     # Leaderboard display
    ├── register.py        # Player registration
    ├── link.py           # Account linking
    ├── unlink.py         # Account unlinking
    ├── remove.py         # Player removal
    ├── unregister.py     # Player unregistration
    └── set_log_channel.py # Log channel setup
```

## Testing

Run the test script to verify everything works:

```bash
python test_basic.py
```

This will test:
- Import functionality
- Database operations
- Command module loading

## Troubleshooting

### Common Issues

1. **"No module named 'discord'"**
   - Make sure you've activated the virtual environment
   - Run `pip install -r requirements.txt`

2. **"Token is None"**
   - Set the `DISCORD_TOKEN` environment variable
   - Check that your bot token is correct

3. **"No such file or directory: 'data/players.json'"**
   - The bot will create the data directory automatically
   - If issues persist, manually create the `data` directory

4. **Permission errors**
   - Ensure your bot has the required Discord permissions
   - Check that the bot is in the server where you're trying to use commands

## Development

The bot uses a modular command system. To add new commands:

1. Create a new file in the `commands/` directory
2. Follow the pattern of existing command files
3. Include the `setup(bot)` function at the end
4. The bot will automatically load new command files

## Data Storage

The bot stores data in JSON files:
- `data/players.json` - Player account links
- `data/leaderboard.json` - Leaderboard data

These files are created automatically when the bot starts.

## License

This project is open source. Feel free to modify and distribute as needed.