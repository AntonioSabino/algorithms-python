def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    counter = 0
    for time_in, time_out in permanence_period:
        if (
            type(time_in) is str or time_in is None or 
            time_out is None or type(time_out) is str
        ):
            return None
        if time_in <= target_time <= time_out:
            counter += 1
    return counter
    