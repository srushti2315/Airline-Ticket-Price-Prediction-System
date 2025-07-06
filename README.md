# Airline-Ticket-Price-Prediction-System
✈️ Airline Ticket Price Prediction System
This is a Data Science project developed using Jupyter Notebooks. The goal of this project is to predict flight ticket prices based on key features such as:

Airline Name

Source & Destination

Total Stops

Journey Time

Duration

The model uses data preprocessing, feature extraction, and is trained using the Random Forest Regressor algorithm for accurate price predictions.

📌 Project Features
Built using Python in Jupyter Notebook

Data cleaning, preprocessing, and visualization steps

Feature extraction (e.g., total stops, duration, etc.)

Trained using Random Forest Regressor

Predicts ticket price based on flight details

🛠 Installation Guide
Follow the steps below to set up the environment using Anaconda and Jupyter Notebook:

✅ Step 1: Download and Install Anaconda
Visit https://www.anaconda.com/products/distribution

Download the installer for your OS (Windows/Mac/Linux)

Run the installer and complete the installation

✅ Step 2: Launch Jupyter Notebook
Open Anaconda Navigator

Click on Jupyter Notebook to launch it in your browser

Navigate to the project folder and open the notebook (.ipynb file)

📂 Project Structure
bash
Copy
Edit
Airline-Ticket-Price-Prediction/
│
├── data/                     # Dataset used for training
│   └── flight_data.csv       
│
├── notebook/                 # Jupyter Notebook files
│   └── price_prediction.ipynb
│
├── models/                   # Saved model (if any)
│   └── random_forest_model.pkl
│
└── README.md                 # Project documentation
📊 Technologies Used
Python

Pandas

NumPy

Matplotlib & Seaborn

Scikit-learn

Jupyter Notebook

💡 How It Works
Data is loaded and cleaned

Important features are extracted from columns like Date_of_Journey, Duration, Total_Stops, etc.

Data is encoded using label/one-hot encoding as needed

A Random Forest Regressor is trained on the processed data

The model is then used to predict the price of tickets based on new inputs

📈 Example Prediction
Given:

Airline: Indigo

Source: Delhi

Destination: Bangalore

Total Stops: 1

Duration: 5h 30m

Journey Date: 2023-07-06

→ Predicted Price: ₹4,850 (example output)
