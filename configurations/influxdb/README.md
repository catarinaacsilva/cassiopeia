# InfluxDB configurations

Add the following configurations on configuration file of Home Assistant: `configuration.yaml`

```
influxdb:
  api_version: 2
  ssl: false
  host: influxdb
  port: 8086
  token: admintoken123
  organization: it
  bucket: cassiopeiainflux
  include:
    entities:
      - sensor.temperature_1

```
