# 📊 SmartClaims Dashboard

SmartClaims Dashboard is a dynamic and interactive data analytics web application built with Streamlit. It allows users to explore synthetic insurance claim data, uncover business trends, and gain insights into key metrics like approval rates, average claim amounts, and regional claim distributions.

# 🚀 Features

- 🔍 Interactive Visualizations  
  Explore claims by region, policy type, and incident type using Plotly charts.

- 📈 Time Series Analysis 
  View monthly claim trends and volume over time.

- 📊 Summary Metrics  
  Instantly view total claims, average claim value, and approval rate.

- 🎯 Dynamic Filtering 
  Filter by incident type and policy category to focus on specific insights.

# 🛠️ Tech Stack

- Python
- Streamlit – for building the dashboard interface
- Pandas – for data manipulation and aggregation
- Plotly – for interactive charts and visualizations
- NumPy – for numerical operations

# 📁 Project Structure
- app.py # Main Streamlit app
- insurance_claims.csv # Synthetic dataset

  
# 📄 Dataset Overview

The synthetic dataset simulates real-world insurance claims and includes:
- `claim_id`, `customer_age`, `policy_type`
- `incident_type`, `claim_status`, `claim_amount`
- `region`, `claim_date`

# 🧪 How to Run the App

1. Clone the repository:
   ```bash
   git clone https://github.com/laibashahid24/smartclaims-dashboard.git
   cd smartclaims-dashboard
2. Install required packages: pip install -r requirements.txt
3. Run the Streamlit app: streamlit run app.py
4. Open your browser and go to: http://localhost:8501

Purpose: This project demonstrates the ability to analyze business data through an intuitive and interactive dashboard. It simulates real-world insurance analytics tasks relevant to roles in data analysis, business intelligence, and financial services.

