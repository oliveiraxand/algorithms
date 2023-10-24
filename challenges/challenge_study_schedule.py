def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if target_time == None:
        return None
    counter = 0
    for pp in permanence_period:
        if not (isinstance(pp[0], int) and isinstance(pp[1], int)):
            return None
        if pp[0] <= target_time <= pp[1]:
            counter += 1
    return counter
    # raise NotImplementedError

study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 5)