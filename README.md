# pio-arduinogiga

This repo contains a custom platformio board-configuration for Arduino GIGA R1. 
It is adapted from the board-definition  for the Arduino IDE [here](https://github.com/arduino/ArduinoCore-mbed/blob/main/boards.txt).

## Important: Modify platform-ststm32

The GIGA board requires a modification of the `platform-ststm32` platform in the [platform.py](https://github.com/platformio/platform-ststm32/blob/develop/platform.py) file.

Change the line 
```
if board.startswith(("portenta", "opta", "nicla_vision"))
```

to 

```
if board.startswith(("portenta", "opta", "nicla_vision", "giga"))
```

The `platform.py` file can be found in `~/.platformio/platforms/ststm32/platform.py` on linux.


## References

- [Custom board definition for Portenta X8](https://github.com/maxgerhardt/pio-portentax8/tree/main)
- [platform-ststm32 pull-request](https://github.com/platformio/platform-ststm32/pull/678/files) for similar board Arduino OPTA
