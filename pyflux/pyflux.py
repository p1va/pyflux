
import argparse
from help import get_metric_object
from influxdb import InfluxDBClient

# Setup command line interface
parser = argparse.ArgumentParser(description='a tool for writing machine CPU percentage into InfluxDb')
parser.add_argument("--address", default="influxdb", help="the InfluxDb address")
parser.add_argument("--port", default=8086, help="the InfluxDb port")
parser.add_argument("--db", default="pyflux", help="the InfluxDb database name")

# Parse the args
args = parser.parse_args()

# Initialize variables
INFLUX_ADDRESS = args.address
INFLUX_PORT = args.port
INFLUX_DB_NAME = args.db

print("Attempting a connection to db {} at {}:{}...".format(INFLUX_DB_NAME, INFLUX_ADDRESS, INFLUX_PORT))

# Create a new InfluxDB client
client = InfluxDBClient(host=INFLUX_ADDRESS, port=INFLUX_PORT)

# Create a new database
client.create_database(INFLUX_DB_NAME)

# Start using it
client.switch_database(INFLUX_DB_NAME)

try:
    print('Sending CPU metrics...')

    while True:
        # Declare the JSON body
        json_body = get_metric_object()

        # Write the metric
        is_successful=client.write_points(json_body)

except KeyboardInterrupt:
    print('Stopping...')

