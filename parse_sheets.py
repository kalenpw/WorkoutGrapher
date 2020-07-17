import re

import models


def parse_sheet(values):
    # arbitrary since I go date name then sets
    all_exercies = []
    date_index = 0
    exercise_name_index = 1
    current_exercise = None
    current_date = None
    for row in values:
        if row == []:
            continue

        if _is_date(row[date_index]):
            current_date = row[date_index]

        exercise_name = row[exercise_name_index]
        current_exercise = models.Exercise(exercise_name, current_date)
        handle_row(current_exercise, row)
        all_exercies.append(current_exercise)

    return create_dict_from_list(all_exercies)


def create_dict_from_list(exercises):
    """ Creates a dict where each key is an exercie's name from a list of all exercies"""
    exercise_dict = {}

    for exercise in exercises:
        exercise_name = exercise.name.strip().lower()
        if not exercise_name in exercise_dict:
            exercise_dict[exercise_name] = []

        exercise_dict[exercise_name].append(exercise)
    
    return exercise_dict


def handle_row(exercise, row):
    if row == []:
        return
    start_sets_index = 2
    sets = row[start_sets_index:]
    for set in sets:
        weight, reps = set.split('x')
        exercise.add_set(weight, reps)


def _is_date(value):
    date_pattern = re.compile("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]")
    return date_pattern.match(value)


def _is_set(value):
    set_pattern = re.compile("[0-9]+x[0-9]+")
    return set_pattern.match(value)
