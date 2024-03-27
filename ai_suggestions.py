from config import google_api_key


import requests

def generate_ai_suggestion(completed_exercise, user_data):
    # Replace with your actual API endpoint URL and authentication details
    api_url = "https://aistudio.google.com/app/apikey"
    api_key = os.getenv("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")  # Assuming you're loading from config.py

    # Format data for the API request, replacing placeholders with relevant data
    request_data = {
        "completed_exercise": completed_exercise,
        "user_data": {
            "fitness_level": user_data["fitness_level"],  # Example user data
            # ... Include other relevant user data here ...
        }
    }

    # Set headers for authentication (replace with the API's required format)
    headers = {"Authorization": f"Bearer {api_key}"}  # Example authorization header

    try:
        response = requests.post(api_url, json=request_data, headers=headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        # Parse the response (assuming JSON format)
        suggestion = response.json()["suggestion"]  # Replace with actual response key
        return suggestion

    except requests.exceptions.RequestException as e:
        # Handle API request errors gracefully
        return f"AI suggestion failed: {str(e)}"

    except Exception as e:  # Catch other potential errors
        return f"An unexpected error occurred: {str(e)}"