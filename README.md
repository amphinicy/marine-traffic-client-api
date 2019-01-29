<h1>Marine Traffic API Client Python Library</h1>

[![PyPI version](https://badge.fury.io/py/Marine-Traffic-API.svg)](https://badge.fury.io/py/Marine-Traffic-API)

<h3>Installation</h3>
<p>Works on python 3.x.</p>

```
pip install marine-traffic-client-api
```

<h3>Usage</h3>

```python
from marinetrafficapi import MarineTrafficApi

# initialize API
api = MarineTrafficApi(api_key="__your_api_key_here__")

# fetch ship routes
routes = api.routes(port_start_id=1, 
                    port_target_id=10, 
                    include_alternatives=True, 
                    include_in_land=True)

# iterate over the routes
for route in routes:
	route.distance
	route.panama
	route.suez
	route.final_path

# fetch vessel positions
vessel_positions = api.vessel_track(period='daily', 
                                    days=3, 
                                    mmsi=241486000)

# iterate over positions
for position in vessel_positions:
	position.mmsi
	position.status
	position.speed
	position.longitude
	position.latitude
	position.course
	position.heading
	position.timestamp
	position.ship_id
	position.wind_angle
```

<h3>Debugging</h3>

<p>If you want to debug your code using the data regarding the API call.</p>

```python
# initialize with debug=True
api = MarineTrafficApi(api_key="...", debug=True)

# after every API call the client library will automatically print all the data to standard output
api.routes(...)

# and you can always have all debug data in your code
debug_data = api.request.debug.show()
```

<h3>Official documentation</h3>

<p>For more information visit official documentation: <a href="https://www.marinetraffic.com/en/ais-api-services/">https://www.marinetraffic.com/en/ais-api-services/</a></p>
