from utility import haversine, predict_future_positions


# Calculate the haversine distance between two points on the Earth's surface given their latitude and longitude.
def check_for_conflict(positions1, positions2, horizontal_separation, vertical_separation):
    """
    For each pair of aircraft, compare their predicted positions to check if they are within a critical distance (horizontal and vertical) at any time step.
    Args:
        positions1: list of future positions of the first aircraft
        positions2: list of future positions of the second aircraft
        horizontal_separation: critical horizontal distance for conflict detection
        vertical_separation: critical vertical distance for conflict detection

    Returns:
        Boolean: True if conflict is detected, False otherwise.
    """
    for pos1, pos2 in zip(positions1, positions2):
        horizontal_distance = haversine(pos1["latitude"], pos1["longitude"], pos2["latitude"], pos2["longitude"])
        vertical_distance = abs(pos1["altitude"] - pos2["altitude"])
        if horizontal_distance < horizontal_separation and vertical_distance < vertical_separation:
            return True
    return False


# resolves conflict between two aircrafts
def resolve_conflict(aircraft1, aircraft2):
    """
    If a conflict is detected, initiate conflict resolution measures, such as changing altitude, direction, or speed.
    """
    # TODO Implement conflict resolution strategy, e.g., change altitude or direction
    pass


# Main algorithm
# Iterates over all aircraft pairs, and calls resolve_conflict if a conflict is detected.
def detect_collisions(aircraft_list, time_interval, num_steps, horizontal_separation, vertical_separation):
    """
    Detect potential conflicts between pairs of aircraft in the aircraft_list.
    Args:
        aircraft_list: list of dictionaries containing the current position and motion parameters of the aircraft
        time_interval: time interval between each step
        num_steps: number of steps to predict
        horizontal_separation: critical horizontal distance for conflict detection
        vertical_separation: critical vertical distance for conflict detection

    Returns:
        None (assumes that conflicts are resolved within the function)

    """
    no_coflict = True
    for i, aircraft1 in enumerate(aircraft_list):
        positions1 = predict_future_positions(aircraft1, time_interval, num_steps)
        for j, aircraft2 in enumerate(aircraft_list):
            if i < j:
                positions2 = predict_future_positions(aircraft2, time_interval, num_steps)
                if check_for_conflict(positions1, positions2, horizontal_separation, vertical_separation):
                    no_coflict = False
                    resolve_conflict(aircraft1, aircraft2)
    print("No conflict detected!" if no_coflict else "Conflict detected, but not resolved yet!")
