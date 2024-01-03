def study_schedule(permanence_period, target_time):
    count = 0
    for student in permanence_period:
        if all((
                isinstance(student[0], int),
                isinstance(student[1], int),
                isinstance(target_time, int))):
            if student[0] <= target_time and student[1] >= target_time:
                count += 1
        else:
            return None
    return count
