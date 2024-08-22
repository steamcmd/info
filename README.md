[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

# SteamCMD Info API

Code and deployment configuration for the new info API.
The API is reachable on https://info.steamcmd.net.

## Development

First install the dependencies in a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Start a Redis instance for storing state and queueing:
```bash
docker run -ti -p 6379:6379 redis:7
```

Then run the Celery worker with beat for the scheduler:
```bash
celery -A main worker --loglevel=info --concurrency=10 --beat
```