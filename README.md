# Stores-Sales-Prediction

# 🛒 BigMart Sales Prediction

This project predicts the sales of products in BigMart stores based on various features such as item weight, visibility, outlet size, and type. The application is built using Streamlit for the frontend and Random Forest Regressor for predictions. It is deployed on an AWS EC2 instance.

🚀 Features

User-friendly web interface built with Streamlit

Predicts sales based on input features

Implements logging and an ML pipeline for better monitoring

Hosted on AWS EC2 for global accessibility

🏷️ Project Structure

📺 Stores-Sales-Prediction
│️️️ 📺 data/                  # Dataset files (if applicable)
│️️️ 📺 models/                # Trained model files (.pkl)
│️️️ 📺 logs/                  # Logging information
│️️️ 📺 ui/                    # Streamlit UI files
│️️️ app.py                    # Main application script
│️️️ model_training.py          # Model training script
│️️️ requirements.txt           # Python dependencies
│️️️ README.md                  # Project documentation
│️️️ Dockerfile (if applicable)  # Docker setup for deployment


📦 Installation

Clone the repository

git clone https://github.com/Harishkarthik07/Stores-Sales-Prediction.git
cd Stores-Sales-Prediction


Install dependencies

pip install -r requirements.txt


Run the Streamlit app

streamlit run app.py


🌐 Deployment on AWS EC2

Launch an EC2 instance (Ubuntu) and set up security groups.

Transfer project files to the instance using SCP or Git.

Install Python, Pip, and required dependencies.

Run the Streamlit app and configure the instance to keep it running.

Access the app using the public EC2 IP address.


📌 Technologies Used

Python (pandas, numpy, scikit-learn, joblib)

Machine Learning (Random Forest Regressor)

Streamlit (UI framework)

AWS EC2 (Deployment)

Logging & Ops Pipeline (For monitoring and debugging)


👤 Author

Harish Karthik

