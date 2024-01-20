# pybitmex

## Prepare
```bash
git clone https://github.com/nineking424/pybitmex.git
cd pybitmex
```

## Build
```bash
docker buildx create --name cross-platform-builder --driver docker-container --use
docker buildx build -t nineking424/pybitmex --platform=linux/amd64,linux/arm64 .
docker image inspect nineking424/pybitmex
docker push nineking424/pybitmex
```

## Build(Cross-platform)
```bash
docker buildx inspect
docker buildx create --name cross-platform-builder --driver docker-container --use
docker buildx build -t nineking424/pybitmex --platform=linux/amd64,linux/arm64 --push .
```

## Run Test(1) - Command
```bash
docker run --rm -it -e SUBSCRIBE=instrument:XBTUSD -e BOOTSTRAP_SERVERS=192.168.1.3:9092 --pull always nineking424/pybitmex
docker run --rm -it -e SUBSCRIBE=trade:XBTUSD -e BOOTSTRAP_SERVERS=192.168.1.3:9092 --pull always nineking424/pybitmex
docker run --rm -it -e SUBSCRIBE=orderBookL2_25:XBTUSD -e BOOTSTRAP_SERVERS=192.168.1.3:9092 --pull always nineking424/pybitmex
docker run --rm -it -e SUBSCRIBE=orderBookL2:XBTUSD -e BOOTSTRAP_SERVERS=192.168.1.3:9092 --pull always nineking424/pybitmex
```

## Run Test(2) - Docker compose
```bash
docker compose -f docker-compose-local.yaml up # connect to 192.168.1.3:9092
docker compose -f docker-compose.yaml up
docker compose -f docker-compose-all.yaml up
```
