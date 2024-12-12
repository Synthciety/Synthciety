import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Title and description
st.title("Enhanced Streamlit App with Data Processing and Visualization")
st.write("This app demonstrates data processing and visualization using Streamlit, NumPy, Pandas, Matplotlib, and Scikit-learn.")

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target
df = pd.DataFrame(X, columns=iris.feature_names)
df['species'] = y

# Display dataset
st.write("### Iris Dataset")
st.write(df.head())

# Data visualization
st.write("### Data Visualization")
fig, ax = plt.subplots()
ax.hist(df['sepal length (cm)'], bins=20, color='skyblue', edgecolor='black')
ax.set_title('Sepal Length Distribution')
ax.set_xlabel('Sepal Length (cm)')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Scatter plot
st.write("### Scatter Plot")
fig, ax = plt.subplots()
scatter = ax.scatter(df['sepal length (cm)'], df['sepal width (cm)'], c=df['species'], cmap='viridis')
ax.set_title('Sepal Length vs Sepal Width')
ax.set_xlabel('Sepal Length (cm)')
ax.set_ylabel('Sepal Width (cm)')
legend1 = ax.legend(*scatter.legend_elements(), title="Species")
ax.add_artist(legend1)
st.pyplot(fig)

# Model training
st.write("### Model Training")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
st.write(f"Model trained successfully with an accuracy of {accuracy:.2f}!")

# Confusion matrix
st.write("### Confusion Matrix")
conf_matrix = confusion_matrix(y_test, y_pred)
st.write(conf_matrix)

# User input for prediction
st.write("### Make a Prediction")
sepal_length = st.slider('Sepal Length (cm)', min_value=4.0, max_value=8.0, step=0.1)
sepal_width = st.slider('Sepal Width (cm)', min_value=2.0, max_value=4.5, step=0.1)
petal_length = st.slider('Petal Length (cm)', min_value=1.0, max_value=7.0, step=0.1)
petal_width = st.slider('Petal Width (cm)', min_value=0.1, max_value=2.5, step=0.1)

# Prediction
input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = model.predict(input_data)
prediction_proba = model.predict_proba(input_data)

st.write(f"Predicted Species: {iris.target_names[prediction][0]}")
st.write(f"Prediction Probability: {prediction_proba}")

# Run the app
if __name__ == '__main__':
    st.run()
