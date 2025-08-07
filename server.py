from flask import Flask, render_template, redirect, request
import random
from recommendme.search import SearchEngine

app = Flask(__name__)

search_engine = None
data = []
DATA_LENGTH = 0

def load_search_engine():
    global search_engine, data, DATA_LENGTH
    if search_engine is None:
        search_engine = SearchEngine(
            index_path="embeddings/hf_cleaned_faiss_index.bin",
            metadata_path="embeddings/hf_cleaned.json"
        )
        data = search_engine.metadata
        DATA_LENGTH = len(data)

@app.route("/")
def home():
    load_search_engine()
    featured = random.sample(data, min(20, DATA_LENGTH))
    return render_template("more.html", results=featured, selected_movie=None)

@app.route("/search", methods=["GET", "POST"])
def search():
    load_search_engine()
    query = None 
    selected_movie = None 
    results = []

    if request.method == "POST":
        query = request.form.get("query")
        if not query or len(query) < 2:
            return redirect("/")
        results = search_engine.search(query, top_k=12)

    else:
        movie_id = request.args.get("q")
        if not movie_id or not movie_id.isdigit():
            return redirect("/")
        movie_id = int(movie_id)
        selected_movie = next((d for d in data if d['id'] == movie_id), None)

        if not selected_movie:
            return redirect("/")

        query = f"{selected_movie['title']}. {selected_movie['desc']}."
        results = search_engine.search(query, top_k=12, exclude_id=selected_movie['id'])

    return render_template("more.html", results=results, selected_movie=selected_movie, no_results=len(results) == 0)

if __name__ == '__main__':
    app.run(debug=True)
