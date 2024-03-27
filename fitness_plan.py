import random

def generate_workout_plan(user_data):
    exercises = {
        "beginner": {
            "exercises": ["squats", "push-ups (modified)", "lunges", "planks"],
            "sets": {"low": 2, "high": 3},  # Beginner set range (2-3)
            "reps": {"low": 8, "high": 12},  # Beginner rep range (8-12)
        },
        "intermediate": {
            "exercises": ["squats (weighted)", "push-ups", "lunges (jumping)", "side planks"],
            "sets": {"low": 3, "high": 4},  # Intermediate set range (3-4)
            "reps": {"low": 10, "high": 15},  # Intermediate rep range (10-15)
        },
        "advanced": {
            "exercises": ["squats (jump squats)", "pull-ups", "lunges (single leg)", "hollow body holds"],
            "sets": {"low": 4, "high": 5},  # Advanced set range (4-5)
            "reps": {"low": 12, "high": 18},  # Advanced rep range (12-18)
        }
    }

    workout_plan = []

    fitness_level = user_data["fitness_level"]

    if fitness_level in exercises:
        exercise_list = exercises[fitness_level]["exercises"]
        level_sets = exercises[fitness_level]["sets"]
        level_reps = exercises[fitness_level]["reps"]

        for exercise in exercise_list:
            # Randomly choose set and rep values within the specified range
            sets = random.randint(level_sets["low"], level_sets["high"])
            reps = random.randint(level_reps["low"], level_reps["high"])

            workout_plan.append({
                "exercise": exercise,
                "sets": sets,
                "reps": reps,
            })

    return workout_plan
