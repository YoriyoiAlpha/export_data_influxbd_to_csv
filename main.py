# Import necessary modules
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
from time import mktime
from datetime import datetime
import csv

# Define variables for InfluxDB connection and CSV file
filename = ''
org = ""
token = ""
url=""

# Set start and stop times for the query in Unix timestamp format
start_time = int(mktime(datetime(year=2024, month=8,day=22,hour=16,minute=10,second=0).timetuple()))
stop_time = int(mktime(datetime(year=2024,month=8,day=22,hour=16,minute=50,second=0).timetuple()))

# Create a client object to connect to InfluxDB
client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)

# Create a query API object and define the query
query_api = client.query_api()
bucket_name = ""
query = f'from(bucket: "{bucket_name}")\
  |> range(start: {start_time}, stop: {stop_time})\
  |> filter(fn: (r) => r["_measurement"] == "electrolyzer")'

# Execute the query and store the results in a variable
result = query_api.query(org=org, query=query)

# Initialize an empty list to store the results
results = []

# Open the CSV file for writing
with open(filename, 'w', newline='\n') as files:
     writer = csv.writer(files,delimiter='\t')
     row_name=["time"]
     row=[]
     for i in range(len(result[0].records)):
         for j in range(len(result)):
             if i == 0 :
                 row_name.append(result[j].records[i]['_field'])
             if j == 0 :
                 row.append(result[j].records[i]['_time'])
             row.append(result[j].records[i]['_value'])
         if i == 0:
           writer.writerow(row_name)
         writer.writerow(row)
         row = []
