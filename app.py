from flask import Flask, request, session, render_template, jsonify
import random
import vonage
from config import VONAGE_API_KEY, VONAGE_API_SECRET, SECRET_KEY
app = Flask(__name__)
app.secret_key = SECRET_KEY  # Needed to store OTP in session

# Vonage API Authentication
from vonage import Vonage, Auth

auth = Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET)
vonage = Vonage(auth=auth)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send-otp", methods=["POST"])
def send_otp():
    phone_number = request.json.get("phone_number")
    
    if not phone_number:
        return jsonify({"error": "Phone number is required"}), 400

    otp = str(random.randint(100000, 999999))  # Generate a random 6-digit OTP
    session["otp"] = otp  # Store OTP in session

    # Send SMS using Vonage API
    from vonage_sms import SmsMessage

    message = SmsMessage(to=phone_number, from_="Vonage", text=f"Your OTP is {otp}")
    print(message)
    response = vonage.sms.send(message)

    if response.messages[0].status == "0":
        return jsonify({"message": "OTP sent successfully!"})
    else:
        return jsonify({"error": "Failed to send OTP"}), 500

@app.route("/verify-otp", methods=["POST"])
def verify_otp():
    user_otp = request.json.get("otp")

    if not user_otp:
        return jsonify({"error": "OTP is required"}), 400

    if session.get("otp") == user_otp:
        session.pop("otp", None)  # Remove OTP from session after successful verification
        return jsonify({"message": "OTP verified successfully!"})
    else:
        return jsonify({"error": "Invalid OTP"}), 400

if __name__ == "__main__":
    app.run(debug=True)
