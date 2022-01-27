# Minecraft server status discord bot

A simple discord bot to show a minecraft server status

## Install packages

```bash
pip install -r requirements.txt
```

## Run app (development)

```bash
python src/main.py
```

## Run app (docker for production)

### .env file required variables

- DISCORD_TOKEN
- MINECRAFT_SERVER_IP
- MINECRAFT_SERVER_PORT

### Commands

Build/Rebuild app (with --no-cache to reload env variables)

```bash
docker-compose build [--no-cache]
```

Start app

```bash
docker-compose up -d
```

Stop app

```bash
docker-compose stop
```

## Contributing

Feel free to make pull requests !