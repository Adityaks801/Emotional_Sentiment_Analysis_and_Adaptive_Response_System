import os
import pandas as pd
from sklearn.model_selection import train_test_split

# Create the 'data' directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Load dataset
df = pd.read_csv('D:\smec\Emotional_Sentiment_Analysis_and_Adaptive_Response_System\Emotional_Sentiment_Analysis_and_Adaptive_Response_System\data\go_emotions_dataset.csv')

# Clean data (remove null values)
df = df.dropna()

# Define X (text) and y (emotion labels)
X = df['text']
y = df.drop(['id', 'text', 'example_very_unclear'], axis=1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save cleaned data for later use
X_train.to_csv('data/X_train.csv', index=False)
X_test.to_csv('data/X_test.csv', index=False)
y_train.to_csv('data/y_train.csv', index=False)
y_test.to_csv('data/y_test.csv', index=False)

print("Data cleaned and saved successfully!")
