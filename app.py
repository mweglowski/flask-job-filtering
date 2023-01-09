from flask import Flask, render_template, request

app = Flask(__name__)

JOBS = [
  "Python Developer", "JavaScript Engineer", "Data Scientist", "Software Engineer", "React Developer", "Swift Developer", "Project Manager", "ML Engineer"
]

JOBS_DATA = [
  {
    "name": "Junior React Developer",
    "props": ["Junior", "React", "Redux", "Communication Skills", "Citical Thinking", "Problem Solving", "TypeScript"]
  }
]


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/search")
def search():
  query = request.args.get("q")
  
  matching_jobs = [job["name"] for job in JOBS_DATA if query in job['name'] and query != ""]

  return render_template("search.html", jobs=matching_jobs)
