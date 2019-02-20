<h1>Marine Traffic API Client Python Library</h1>

[![PyPI version](https://badge.fury.io/py/Marine-Traffic-API.svg)](https://badge.fury.io/py/Marine-Traffic-API)
[![Build Status](https://travis-ci.com/arrrlo/marine-traffic-client-api.svg?branch=master)](https://travis-ci.com/arrrlo/marine-traffic-client-api)

<h3>Installation</h3>
<p>Works on python 3.x.</p>

```
pip install Marine-Traffic-API
```

<h3>Initialize API</h3>

```python
from marinetrafficapi import MarineTrafficApi

api = MarineTrafficApi(api_key="__your_api_key_here__")
```

<h3>Default params</h3>

```python
response = api.__api_call_method__(protocol='json'|'jsono'|'csv'|'xml', # default is jsono
                                   msg_type='simple'|'extended',  # default is simple
                                   timeout=10) # default is 5 (5 seconds)

# protocol and msg_type are call params 
# that could be used in any api call. 
# json protocol is not supported by models, for now.
# extended msg_type returns a lot more data but cost 
# a lot more api credits as well.

response.raw_data  # raw data from api call (json, csv or xml)
response.formatted_data  # data list
response.models  # list of Client models representing the data
```

<h3>Vessels Positions</h3>

<h4>[PS01] Vessel History Track</h4>

```python
vessel_positions = api.vessel_historical_track(period='daily', 
                                               days=3, 
                                               mmsi=241486000)

for position in vessel_positions.models:
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

<h4>[PS02] Vessel Positions of a Static Fleet</h4>

```python
vessels = api.static_fleet_vessel_positions(time_span=10)

for vessel in vessels.models:
	vessel.mmsi
	vessel.imo
	vessel.ship_id
	vessel.longitude
	vessel.latitude
	vessel.speed
	vessel.heading
	vessel.status
	vessel.course
	vessel.timestamp
	vessel.dsrc
	vessel.utc_seconds
	vessel.ship_name
	vessel.ship_type
	vessel.call_sign
	vessel.flag
	vessel.length
	vessel.width
	vessel.grt
	vessel.dwt
	vessel.draught
	vessel.year_built
	vessel.rot
	vessel.type_name
	vessel.ais_type_summary
	vessel.destination
	vessel.eta
	vessel.current_port
	vessel.last_port
	vessel.last_port_time
	vessel.current_port_id
	vessel.current_port_unlocode
	vessel.current_port_country
	vessel.last_port_id
	vessel.last_port_unlocode
	vessel.last_port_country
	vessel.next_port_id
	vessel.next_port_unlocode
	vessel.next_port_name
	vessel.next_port_country
	vessel.eta_calc
	vessel.eta_updated
	vessel.distance_to_go
	vessel.distance_travelled
	vessel.awg_speed
	vessel.max_speed
```

<h4>[PS03] Vessel Positions of a Dynamic Fleet</h4>

```python
vessels = api.dynamic_fleet_vessel_positions(time_span=10)

for vessel in vessels.models:
	vessel.mmsi
	vessel.imo
	vessel.ship_id
	vessel.longitude
	vessel.latitude
	vessel.speed
	vessel.heading
	vessel.status
	vessel.course
	vessel.timestamp
	vessel.dsrc
	vessel.utc_seconds
	vessel.ship_name
	vessel.ship_type
	vessel.call_sign
	vessel.flag
	vessel.length
	vessel.width
	vessel.grt
	vessel.dwt
	vessel.draught
	vessel.year_built
	vessel.rot
	vessel.type_name
	vessel.ais_type_summary
	vessel.destination
	vessel.eta
	vessel.current_port
	vessel.last_port
	vessel.last_port_time
	vessel.current_port_id
	vessel.current_port_unlocode
	vessel.current_port_country
	vessel.last_port_id
	vessel.last_port_unlocode
	vessel.last_port_country
	vessel.next_port_id
	vessel.next_port_unlocode
	vessel.next_port_name
	vessel.next_port_country
	vessel.eta_calc
	vessel.eta_updated
	vessel.distance_to_go
	vessel.distance_travelled
	vessel.awg_speed
	vessel.max_speed
```

<h3>Voyage Info</h3>

<h4>[VI03] Port Distance and Routes</h4>

```python
routes = api.port_distances_and_routes(port_start_id=1, 
                                       port_target_id=10, 
                                       include_alternatives=True, 
                                       include_in_land=True)

for route in routes.models:
	route.distance
	route.panama
	route.suez
	route.final_path
```

<h3>Debugging</h3>

<p>If you want to debug your code using the data regarding the API call.</p>

```python
# initialize with debug=True
api = MarineTrafficApi(api_key="...", debug=True)

# after every API call the client library will automatically print all the data to standard output
api.vessel_historical_track(...)

# and you can always have all debug data in your code
debug_data = api.request.debug.show()
```

<h3>Official documentation</h3>

<p>For more information visit official documentation: <a href="https://www.marinetraffic.com/en/ais-api-services/">https://www.marinetraffic.com/en/ais-api-services/</a></p>
