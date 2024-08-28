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

## Docker Compose

You can use Docker compose with the `docker-compose.yml`
file to quickly start and setup test containers like Minio
as an object storage:
```
docker compose up
```
The Minio bucket is automatically created and can be reached
locally on the default Minio port. For example to request app
id **1615011** [http://localhost:9000/steamcmd/app/1615011.json](http://localhost:9000/steamcmd/app/1615011.json).

To manage Minio, for example to test changes to the bucket
or easily browse files in the bucket you can login to the
admin interface on [http://localhost:9001](http://localhost:9001)
and use **steamcmd** / **steamcmd** as the username / password.