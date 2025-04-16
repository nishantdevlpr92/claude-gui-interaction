from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    print("Index page loaded!!")
    return render_template("index.html")

@app.route("/download_cat", methods=["POST"])
def download_cat():
    print("🐱 Cat downloaded SuccessFully!")
    return jsonify({"message": "🐱 Cat downloaded SuccessFully!"})

@app.route("/clear", methods=["POST"])
def clear():
    print("Cleared button clicked!")
    return jsonify({"message": "Clicked clear button!"})

if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")
