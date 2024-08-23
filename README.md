InfluxDB Data Export to CSV
============================

This script allows you to export data from an InfluxDB database to a CSV file. It uses the official InfluxDB Python client 
library to connect to the database, query data, and write the results to a CSV file. The script is compatible with Linux, macOS, 
and Windows operating systems.

Prerequisites
-------------

Before running the script, make sure you have the following installed:

1. **Python 3.7 or later**: You can download Python from the [official website](https://www.python.org/downloads/) for your 
specific operating system. Make sure to add Python to your PATH during installation.
2. **InfluxDB Python client library**: Install the InfluxDB Python client library using `pip`:
```
pip install influxdb-client
```
3. **CSV module**: The script uses the built-in `csv` module in Python, so no additional installation is required.

Configuration
-------------

Before running the script, you need to configure it with your InfluxDB connection details and specify the query and CSV file 
information. Here are the configuration variables:

* `filename`: The name of the output CSV file.
* `bucket`: The name of the bucket in your InfluxDB database.
* `org`: The organization in your InfluxDB database.
* `token`: A token with read access to your InfluxDB database. You can generate a new token from the [InfluxDB web 
interface](https://docs.influxdata.com/influxdb/v2.0/security/tokens/).
* `url`: The URL of your InfluxDB server, including the protocol (e.g., `http` or `https`).


Run 
----
To run the code, first ensure that you have made any necessary modifications. Then, open your terminal or command prompt, 
navigate to the directory where the code file is located, and enter : 
``` 
python3 main.py
```

Change the query in InfluxDB 
----------------------------

To change the query in InfluxDB, follow these steps:

1. **Connect to the InfluxDB website.**

Open your web browser and navigate to the InfluxDB website.

2. **Click on the "Data Explorer" button in the left-hand side of the page.**

This will take you to the data exploration interface.

3. **Select the data you want to export.**

Use the dropdown menus and search bars to select the _measurement or the field(s), for the data you want to export.

4. **Select the script editor and copy the third line.**

Once you have selected the data you want to export, click on the "Script Editor" button at the top of the page. This will open a 
window with a pre-populated InfluxQL query that corresponds to your data selection. Copy the third line of this query, which 
should look something like this:
```
from(bucket: "DHBW")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "compressor" or r["_measurement"] == "electrolyzer")
  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
  |> yield(name: "mean")
```
copy only this line : ```|> filter(fn: (r) => r["_measurement"] == "compressor" or r["_measurement"] == "electrolyzer")```

5. **Paste it into the Python request.**

   
