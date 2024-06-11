# Trajectory Collision Detector

A sample program to detect collision between a list of trajectories.
It is aimed to be used for aviation safety to detect collision between aircrafts.

## Conflict Resolution
There is a `resolve_conflict()` function, as a placeholder to resolve the conflict between two trajectories. 
You can implement your own logic to resolve the conflict.

## Usage
```python
from collision_detector import detect_collisions

aircraft_list = [
    {"latitude": 52.0, "longitude": 0.1, "altitude": 10000, "speed": 250, "direction": 90, "vertical_speed": 0},
    {"latitude": 52.0, "longitude": 0.2, "altitude": 10000, "speed": 250, "direction": 270, "vertical_speed": 0}
]

detect_collisions(aircraft_list, time_interval=1, num_steps=10, horizontal_separation=5, vertical_separation=300)

```
### Note
According to compass rose, 0 degrees is North, 90 degrees is East, 180 degrees is South, and 270 degrees is West.