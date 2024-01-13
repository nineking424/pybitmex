# pybitmex

## Build
```
docker build -t nineking424/pybitmex --platform linux/amd64 .
docker image inspect nineking424/pybitmex
docker push nineking424/pybitmex
```

## Test
```
docker run --rm -it --network mykafka-net nineking424/pybitmex python3 wsdump_test.py
docker run --rm -it --network mykafka-net nineking424/pybitmex python3 wsdump_bitmex.py trade:XBTUSD
docker run --rm -it --network mykafka-net nineking424/pybitmex python3 wsdump_bitmex.py instrument:XBTUSD
```

## Run
```
docker run -d --name pybitmex-trade-XBTUSD --network mykafka-net nineking424/pybitmex python3 wsdump_bitmex.py trade:XBTUSD
docker run -d --name pybitmex-instrument-XBTUSD --network mykafka-net nineking424/pybitmex python3 wsdump_bitmex.py instrument:XBTUSD
```
