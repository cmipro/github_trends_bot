# GitHub Trends Bot
Telegram bot for tracking GitHub trends. Track your links from the 
configuration and publish them to your channel.

## My Channel
If you don't want to launch your bot, you can just follow the trends through 
my channel:

[@pythonGithubTrends](https://t.me/pythonGithubTrends)

Links tracked by default:

```
https://github.com/trending/python?since=daily
https://github.com/trending/python?since=weekly
https://github.com/trending/python?since=monthly
https://github.com/trending?since=daily
https://github.com/trending?since=weekly
https://github.com/trending?since=monthly
```

## Technologies
```
Python 3.11
Aiogram 3
SQLAlchemy
APScheduler
BS4
```

## Installation and launch

1. Clone the repository and go to it.

```
git clone https://github.com/cmipro/github_trends_bot
cd github_trends_bot
```

2. Create and activate a virtual environment.

```
Unix:
python3 -m venv env
source env/bin/activate

Windows:
python -m venv env
source env/Scripts/activate
```

3. Install dependencies.

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Create a file .env based on .env.example and fill it in.

```
BOT_TOKEN=YOUR_BOT_TOKEN_HERE
CHANNEL_ID=YOUR_CHANNEL_ID
CHANNEL_NAME=YOUR_CHANNEL_NAME
```

5. [Optional] Check the bot settings in config.py (see below).

6. Launch the project (you can use systemd, supervisor, or any other technology
you know to do this.).

```
python bot.py
```

## Config.py
The main settings to check in config_data/config.py.

```
UPDATE_TIME_MINUTES = 60 # Time to check for updates
PROJECTS_LIMIT = 10 # The number of projects in the top, by default TOP10, maximum TOP25
GITHUB_URLS # Links for tracking ratings
```

## Contacts

Telegram: [@hardnaz](https://t.me/hardnaz)

E-mail: info@wifigid.ru

Made by [WiFiGid.ru](https://wifigid.ru)