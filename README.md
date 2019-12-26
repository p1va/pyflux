# pyflux
Just an InfluxDb test using Docker and Python

## Build and run

```sh
docker-compose build
```

```sh
docker-compose up
```

## Send machine metrics to InfluxDb

```sh
python pyflux.py --address=localhost --port=8086 --db=test
```

## Browse and visualize InfluxDb data

Chronograf running on port ```http://localhost:8888```

