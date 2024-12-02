from transformers import pipeline

# Load a pre-trained model for zero-shot classification
emotion_model = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Function to predict emotion from the text
def predict_emotion(text, candidate_labels):
    result = emotion_model(text, candidate_labels=candidate_labels)
    return result['labels'][0]

# Example usage
if __name__ == "__main__":
    candidate_labels = ["joy", "anger", "sadness", "fear", "disgust", "surprise", "neutral"]
    sample_text = "I feel really stressed"
    predicted_emotion = predict_emotion(sample_text, candidate_labels)
    print(f"Predicted Emotion: {predicted_emotion}")
