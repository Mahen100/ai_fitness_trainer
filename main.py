import streamlit as st
import random

from fitness_plan import generate_workout_plan
from exercise_library import get_exercise_variations

# Function for generating workout plan (to be called from Streamlit)
def generate_plan(user_data):
    workout_plan = generate_workout_plan(user_data)
    return workout_plan

# Function for generating AI-powered suggestion (enhanced with error handling)
def generate_ai_suggestion(completed_exercise, user_data):
    try:
        # Replace with your actual API endpoint URL and authentication details (refer to API documentation)
        api_url = "https://api.example.com/generate_exercise_variation"
        api_key = os.getenv("GENERATIVE_AI_API_KEY")

        # Format data for the API request
        request_data = {
            "completed_exercise": completed_exercise,
            "user_data": user_data,
        }

        # Set headers for authentication (replace with the API's required format)
        headers = {"Authorization": f"Bearer {api_key}"}

        response = requests.post(api_url, json=request_data, headers=headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        # Parse the response (assuming JSON format)
        ai_response = response.json()["suggestion"]  # Replace with actual response key
        return ai_response

    except requests.exceptions.RequestException as e:
        print(f"API request failed: {str(e)}")
        return "Failed to generate suggestion. Using exercise library..."
    except Exception as e:  # Catch other potential errors
        print(f"An unexpected error occurred: {str(e)}")
        return "An error occurred. Using exercise library..."

# Main Streamlit app structure
def main():
    st.title("AI Fitness Trainer")
    st.write("This AI Fitness Trainer app helps you create personalized workout plans and suggests variations for completed exercises.")

    user_data = {}
    user_data["age"] = st.number_input("Enter your age:", min_value=18, max_value=100)
    fitness_level = st.selectbox("Choose your fitness level:", ["beginner", "intermediate", "advanced"])
    user_data["fitness_level"] = fitness_level
    user_data["weight"] = st.number_input("Enter your weight (kg):")  # Added weight input
    user_data["height"] = st.number_input("Enter your height (cm):")  # Added height input

    if st.button("Generate Workout Plan"):
        workout_plan = generate_plan(user_data)
        st.write("**Your Personalized Workout Plan:**")
        st.table(workout_plan)

        completed_exercise = st.selectbox("Select a completed exercise:", [exercise["exercise"] for exercise in workout_plan])

        if st.button("Get Variation Suggestion"):
            ai_response = generate_ai_suggestion(completed_exercise, user_data)
            st.write("**AI-Powered Variation Suggestion:**")
            st.write(ai_response)

            # If AI suggestion fails, use exercise library with better messaging
            if ai_response.startswith("Failed") or ai_response.startswith("An error"):
                variations = get_exercise_variations(completed_exercise)
                suggestion_index = random.randint(0, len(variations) - 1)
                suggestion = variations[suggestion_index]
                st.write("Have enough rest")
                st.write("Get healthy diet")

if __name__ == "__main__":
    main()
