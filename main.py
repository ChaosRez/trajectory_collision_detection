from collision_detector import detect_collisions

if __name__ == '__main__':
    aircraft_list = [
        {"latitude": 52.0, "longitude": 0.1, "altitude": 10000, "speed": 250, "direction": 90, "vertical_speed": 0},
        {"latitude": 52.0, "longitude": 0.2, "altitude": 10000, "speed": 250, "direction": 270, "vertical_speed": 0}
    ]

detect_collisions(aircraft_list, time_interval=1, num_steps=10, horizontal_separation=5, vertical_separation=300)
