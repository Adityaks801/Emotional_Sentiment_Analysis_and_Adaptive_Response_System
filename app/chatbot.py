from models.emotion_model import predict_emotion
from models.response_model import generate_response

# List of emotions that the model will recognize
candidate_labels = ["joy", "anger", "sadness", "fear", "disgust", "surprise", "neutral"]


# Main function to get chatbot response
def chatbot_response(text):
    # Step 1: Detect emotion
    emotion = predict_emotion(text, candidate_labels)

    # Step 2: Generate response based on emotion
    response = generate_response(emotion)

    return response


# Example chatbot interaction
if __name__ == "__main__":
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print(f"Bot: {response}")
