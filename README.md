# Ground Station

Software for managing a satellite ground station.

## Plan

Have this program constantly running with a CLI that we can interact with. We should be able to see the state of the system and input commands as required. Ideally, there would be some web interface so we can interact with the system without having to actually remote in to the Raspberry Pi.

Functionality:

1. Communicate with Arduino to track satellite passes
2. Communicate with EPS
3. Manage signal processing workflow
4. Manage decoding workflow

## Todo

- [ ] Set up `sat-tracker` to communicate with the Arduino
- [ ] Integrate with EPS
- [ ] Set up automatic signal processing and decoding
