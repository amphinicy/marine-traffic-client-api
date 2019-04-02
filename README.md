# Marine Traffic API Client Python Library

[![PyPI version](https://badge.fury.io/py/Marine-Traffic-API.svg)](https://badge.fury.io/py/Marine-Traffic-API)
[![Build Status](https://travis-ci.com/amphinicy/marine-traffic-client-api.svg?branch=master)](https://travis-ci.com/amphinicy/marine-traffic-client-api)
![GitHub](https://img.shields.io/github/license/amphinicy/marine-traffic-client-api.svg?color=blue)
![GitHub last commit](https://img.shields.io/github/last-commit/amphinicy/marine-traffic-client-api.svg?color=blue)

## Installation
Works with python 3.x.

```
pip install Marine-Traffic-API
```

## Initialize API

```python
from marinetrafficapi import MarineTrafficApi

api = MarineTrafficApi(api_key="__your_api_key_here__")
```

## Default params

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

## Vessels Positions

#### [PS01] Vessel History Track

```python
from marinetrafficapi import MarineTrafficApi

api = MarineTrafficApi(api_key="__your_api_key_here__")

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

#### [PS02] Vessel Positions of a Static Fleet

```python
from marinetrafficapi import MarineTrafficApi

api = MarineTrafficApi(api_key="__your_api_key_here__")

vessels = api.fleet_vessel_positions(time_span=10)

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

#### [PS03] Vessel Positions of a Dynamic Fleet
Same as PS02.

#### [PS04] Vessel Positions Within a port
Same as PS02.

#### [PS05] Vessel Positions in a Predefined Area
Same as PS02.

#### [PS06] Vessel Positions in a Predefined Area

```python
from marinetrafficapi import MarineTrafficApi

api = MarineTrafficApi(api_key="__your_api_key_here__")

vessels = api.fleet_vessel_positions(min_latitude=38.20882,
                                     max_latitude=40.24562,
                                     min_longitude=-6.7749,
                                     max_longitude=-4.13721,
                                     time_span=10)

for vessel in vessels.models:
	# same as PS02
```

#### [PS07] Single Vessel Positions

```python
from marinetrafficapi import MarineTrafficApi

api = MarineTrafficApi(api_key="__your_api_key_here__")

vessel = api.single_vessel_positions(time_span=20,
                                     mmsi=310627)

vessel = vessel.models[0]

vessel.mmsi
vessel.imo
vessel.longitude
vessel.latitude
vessel.speed
vessel.heading
vessel.status
vessel.course
vessel.timestamp
vessel.dsrc
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
vessel.type_name
vessel.ais_type_summary
vessel.destination
vessel.eta
vessel.eta_calc
vessel.current_port
vessel.current_port_id
vessel.current_port_unlocode
vessel.last_port
vessel.last_port_time
vessel.last_port_id
vessel.last_port_unlocode
vessel.next_port_id
vessel.next_port_unlocode
vessel.next_port_name
vessel.next_port_country
```

## Events

#### [EV01] Port Calls

```python
from marinetrafficapi import MarineTrafficApi

api = MarineTrafficApi(api_key="__your_api_key_here__")

events = api.port_calls(port_id=1,
                        gt_min=4000,
                        dwt_min=9000,
                        timespan=60)

for event in events.models:
    event.mmsi
    event.ship_name
    event.ship_id
    event.local_timestamp
    event.utc_timestamp
    event.move_type
    event.type_name
    event.unlocode
    event.draught
    event.load_status
    event.port_operation
    event.in_transit
    event.voyage_avg_speed
    event.voyage_max_speed
    event.voyage_idle_time
    event.elapsed_noanch
```

#### [EV02] Vessel Events

```python
from marinetrafficapi import MarineTrafficApi

api = MarineTrafficApi(api_key="__your_api_key_here__")

events = api.vessel_events(mmsi=355906000,
                           event_type=19,
                           timespan=160)

for event in events.models:
    event.mmsi
    event.ship_name
    event.timestamp
    event.event_id
    event.event_name
    event.event_content
```

#### [EV03] Berth Calls

```python
from marinetrafficapi import MarineTrafficApi

api = MarineTrafficApi(api_key="__your_api_key_here__")

berth_calls = api.berth_calls(dwt_min=2000,
                              dwt_max=70000,
                              timespan=20)

for berth_call in berth_calls.models:
    berth_call.ship_id
    berth_call.mmsi
    berth_call.imo
    berth_call.dock_local_time
    berth_call.dock_utc_time
    berth_call.dock_offset_time
    berth_call.undock_local_time
    berth_call.undock_utc_time
    berth_call.undock_offset_time
    berth_call.ship_name
    berth_call.type_name
    berth_call.grt
    berth_call.dwt
    berth_call.flag
    berth_call.year_built
    berth_call.berth_id
    berth_call.berth_name
    berth_call.terminal_id
    berth_call.terminal_name
    berth_call.port_name
    berth_call.port_id
    berth_call.unlocode
    berth_call.country_code
    berth_call.destination_id
    berth_call.destination
    berth_call.arrival_local_time
    berth_call.arrival_utc_time
    berth_call.arrival_draught
    berth_call.arrival_load_status
    berth_call.distance_travelled
    berth_call.voyage_average_speed
    berth_call.voyage_max_speed
    berth_call.voyage_idle_time
    berth_call.origin_name
    berth_call.origin_port_id
    berth_call.origin_departure_time
    berth_call.total_voyage_time
    berth_call.departure_local_time
    berth_call.departure_utc_time
    berth_call.departure_draught
    berth_call.departure_load_status
    berth_call.port_operation
    berth_call.time_at_berth
    berth_call.time_at_port
```

## Voyage Info

#### [VI03] Port Distance and Routes

```python
from marinetrafficapi import MarineTrafficApi

api = MarineTrafficApi(api_key="__your_api_key_here__")

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

## Exception Handling

```python
from marinetrafficapi import MarineTrafficApi
from marinetrafficapi import (MarineTrafficRequestApiException,
                              MarineTrafficClientApiException,
                              MarineTrafficFormatterException,
                              MarineTrafficException)

api = MarineTrafficApi(api_key="__your_api_key_here__")

try:
    routes = api.vessel_historical_track(...)
    
except MarineTrafficRequestApiException:
    """Handle Request Exceptions"""
    
except MarineTrafficClientApiException:
    """Handle Client Exceptions"""
    
except MarineTrafficFormatterException:
    """Handle Formatter Exceptions"""
    
except MarineTrafficException:
    """Handle All Marine Traffic Exceptions"""
    
```

## Debugging

If you want to debug your code using the data regarding the API call.

```python
from marinetrafficapi import MarineTrafficApi

# initialize with debug=True
api = MarineTrafficApi(api_key="...", debug=True)

# after every API call the client library will automatically print all the data to standard output
api.vessel_historical_track(...)

# and you can always have all debug data in your code
debug_data = api.request.debug.show()
```

## Official documentation

For more information visit official documentation: [https://www.marinetraffic.com/en/ais-api-services/](https://www.marinetraffic.com/en/ais-api-services/)

# Changelog

## 0.8.0

#### Added:
- EV03 - Berth Calls 

#### Fixed:
- default values for number field, real number field and datetime field

## 0.7.1

#### Fixed:
- better structure for exceptions 

## 0.7.0

#### Added:
- EV02 - Vessel Events 

## 0.6.1

#### Added:
- README badges fixed

## 0.6.0

#### Added:
- EV01 - Port Calls 