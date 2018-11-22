# duck-api

The api for child ducks to interact with the mother duck.

The api will be hosted on the mother duck, which will be setup as a wifi router,
child ducks will connect to the network provided by the mother duck and
communicate over the api.

## The api will need to
- Receive coordinates and compass directions from child ducks
- Transmit coordinates and compass directions to child ducks

## Resources
- gps:
  https://learn.adafruit.com/adafruit-ultimate-gps-on-the-raspberry-pi?view=all
- gpio: https://github.com/metachris/RPIO
