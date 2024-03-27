exercise_data = {
    "squats": {
        "description": "A lower body exercise that strengthens the quads, hamstrings, and glutes.",
        "variations": [
            "bodyweight squats",
            "weighted squats (dumbbells, barbell)",
            "jump squats",
            "pulse squats",
        ]
    },
    # ... Add more exercises and variations ...
}

def get_exercise_variations(exercise_name):
    """
    Retrieves exercise variations from the library.
    """

    return exercise_data.get(exercise_name, {}).get("variations", [])
