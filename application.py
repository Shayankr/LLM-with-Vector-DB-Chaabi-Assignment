from flask import Flask, render_template, request, jsonify, redirect
from src.components.solution import QueryResult as qr
import os


application = Flask(__name__)
app = application




@app.route("/")
def home_page():
	return render_template("index.html")
	

@app.route("/search", method = ["POST"])
def search():
	try:
		data = request.get_json()
		query = data['query']

		# Write code here:

		# Get top-k relevant results
		top_k_res = qr.find_k_relevant(question, top_k=5)

		# Extract answer
		result = qr.extract_answer(question, top_k_res)

		return jsonify({'answer': result})

	except Exception as e:
		return jsonify({"message": result})
	
	
if __name__ == "__main__":
	app.run(host = "0.0.0.0", debug = True)
	
