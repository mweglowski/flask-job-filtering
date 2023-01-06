from flask import Flask, render_template, request

app = Flask(__name__)

JOBS = [
  "Python Developer", "JavaScript Engineer", "Data Scientist", "Software Engineer", "React Developer", "Swift Developer", "Project Manager", "ML Engineer"
]


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/search")
def search():
  query = request.args.get("q")
  
  matching_jobs = [job for job in JOBS if query in job and query != ""]

  return render_template("search.html", jobs=matching_jobs)
