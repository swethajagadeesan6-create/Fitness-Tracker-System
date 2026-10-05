from groq import Groq

API_KEY = "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"

def fitness_assistant(activity, duration, calories):

    client = Groq(api_key=API_KEY)

    prompt = f"""
    Give a simple fitness suggestion based on this workout.

    Activity: {activity}
    Duration: {duration} minutes
    Calories Burned: {calories}

    Give:
    1. A short comment about the workout
    2. One simple fitness suggestion
    3. One recovery suggestion
    4. One hydration suggestion
    5. One simple nutrition suggestion

    Keep the answer simple and beginner-friendly.
    Do not give medical advice.
    """

    response = client.chat.completions.create(
        model= "openai/gpt-oss-20b",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
    
    
    
    
    
