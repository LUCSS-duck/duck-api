# duck-api

The api for child ducks to interact with the mother duck.

The api will be hosted on the mother duck, which will be setup as a wifi router,
child ducks will connect to the network provided by the mother duck and
communicate over the api.

## Running the web server

``` shell
poetry run uvicorn duck-api.api:app
```

## API interaction

- We'll need an event processor that processes requests, `/forward` should
  submit a request to move forward, etc.
- Requests should be processed serially, we don't want concurrent movement
  requests to cause the robot to enter some invalid state (motors stuck on,
  etc).
- Thus there should probable be an endpoint to clear all requests and if there
  is a currently running movement request, clear the current request and
  stopping the duck.

## The api will need to
- Receive coordinates and compass directions from child ducks
- Transmit coordinates and compass directions to child ducks

## Resources
- gps:
  https://learn.adafruit.com/adafruit-ultimate-gps-on-the-raspberry-pi?view=all
- gpio: https://github.com/metachris/RPIO
- motor controller:
  https://howtomechatronics.com/tutorials/arduino/arduino-dc-motor-control-tutorial-l298n-pwm-h-bridge/

## Modules
Submodules of the program, and what they will have to do.

### Position transmission system
- Transmits the position of the mother and child duck to all other ducks
- If all ducks are using a RPI then each duck just needs to know the coords of
  at least the mother duck, and decides what to do itself.

### Video & audio streaming system
- Streams video and audio to an online video feed
- The duck will play audio streamed/ sent to it (on every duck or just the
  mother duck?)

### Command distribution system
If we're using a distributed BT5 system where not all ducks may be connected to
eduroam but hopefully atleast one is, and all ducks are interconnected through
bluetooth, we will need a system to have the ducks distribute commands issued
to the entire fleet & ensure each duck has seen the command.

We will also need a system that takes action to recover from when a duck has
lost connection with all other ducks & eduroam, this could be something like
having all ducks track the location of all other ducks, and have ducks regularly
ping the entire swarm (ducks would relay pings), when a duck hasn't been seen
pinging after a period of time, then the closest few ducks should attempt to
seek the last known position of the missing duck in attempt to regain
connection.

### Autonomous roaming AI
The ducks will roam autonomously until swarm mode is engaged, there should be a
system that makes the ducks act like real ducks until they receive a command
from the command distribution system to swarm to the mother duck.

### Pathfinding and GPS system
From the AI & Swarm mode systems, the ducks will need to be able to generate a
path to get them to a desired location, using their current position and a
system of waypoints on campus paths (we'll need to come up with something to
generate this map of waypoints).

