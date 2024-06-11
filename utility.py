from math import radians, cos, sin, sqrt, atan2


# Calculate the great-circle distance between two points on the Earth's surface.
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Radius of the Earth in kilometers
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance


def predict_future_positions(aircraft, time_interval, num_steps):
    """

    Args:
        aircraft: dictionary containing the current position and motion parameters of the aircraft
        time_interval: time interval between each step
        num_steps: number of steps to predict

    Returns:
        future positions of the aircraft

    """
    positions = []
    for step in range(num_steps):
        future_time = step * time_interval
        speed_kms = aircraft["speed"] / 3600  # Convert speed from km/h to km/s
        future_position = {
            "latitude": aircraft["latitude"] + speed_kms * future_time * sin(radians(90 - aircraft["direction"])),
            "longitude": aircraft["longitude"] + speed_kms * future_time * cos(radians(90 - aircraft["direction"])),
            "altitude": aircraft["altitude"] + aircraft["vertical_speed"] * future_time
        }
        positions.append(future_position)
    return positions
