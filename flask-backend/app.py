from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/submit", methods=["GET", "POST"])
def submit():

    if request.method == "GET":
        return jsonify({"message": "Submit endpoint working. Use POST to send data."})

    if request.method == "POST":
        data = request.get_json()

        if not data:
            return jsonify({"error": "No JSON data received"}), 400

        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        return jsonify({
            "status": "success",
            "received": {
                "name": name,
                "email": email,
                "message": message
            }
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
