# OTP Verification System

## 📌 Overview
A Flask-based OTP verification system that allows users to enter their phone number, receive an OTP via SMS using the **Vonage API**, and verify it on the website.

## 🚀 Features
- 📱 Send OTP to any valid phone number worldwide.
- 🔐 Secure OTP storage using Flask sessions.
- ✅ OTP verification system.
- 🌍 Supports multiple country codes.
- 🖥️ Simple and user-friendly interface.

## 🛠️ Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **SMS Service:** Vonage API

## 📦 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Muhammad-waqas1/OTP-Verification-System.git
cd OTP-Verification-System
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up API Keys

Create a .env file in the root directory and add your **Vonage API credentials**:
```bash
VONAGE_API_KEY=your_api_key
VONAGE_API_SECRET=your_api_secret  
SECRET_KEY=your_flask_secret_key   `
```
### 4️⃣ Run the Flask App
```bash
python app.py   `
```
### 5️⃣ Open in Browser

Visit http://127.0.0.1:5000/ in your web browser.

🔥 Future Improvements
----------------------

*   ✅ Add database support for OTP storage.
    
*   🎨 Enhance UI with Bootstrap for a modern look.
    
*   📨 Support OTP verification via email.
    
*   📊 Implement rate-limiting for enhanced security.
    

🤝 Contributing
---------------

Feel free to fork this repository and submit a pull request! 🎉
