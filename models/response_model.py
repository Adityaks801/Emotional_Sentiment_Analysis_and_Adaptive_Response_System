# Function to generate an empathetic response based on the emotion
def generate_response(emotion):
    responses = {
        'joy': "That's great to hear! Keep smiling!",
        'sadness': "I'm really sorry you're feeling this way. It will get better!",
        'stress': "Take a deep breath. You got this!",
        'anxiety': "I understand you're feeling anxious. Try to relax, everything will be okay.",
        'anger': "It's okay to feel angry, but try to calm down and take a break.",
        'disgust': "I understand. Sometimes, things can be overwhelming.",
        'fear': "It's okay to feel scared. You're not alone in this.",
        'surprise': "Wow! That sounds interesting.",
        'neutral': "I see. Anything else you'd like to talk about?"
    }

    return responses.get(emotion, "I'm here for you!")


# Example usage
if __name__ == "__main__":
    emotion = "sadness"
    print(generate_response(emotion))
