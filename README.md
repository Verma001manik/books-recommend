# 📚 Book Recommendation System

A semantic search engine that helps users discover books based on the meaning of their queries. It uses embeddings and FAISS vector search to return similar books from a dataset.

![Screenshot](images/ss.png)
---

## 🗂️ Datasets Used

* Goodreads Book Descriptions (Hugging Face) (1m entries)
* Kaggle Books Dataset (~7,000 entries)

---

## 🚀 How to Run

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/your-username/book-recommendation-system.git](https://github.com/your-username/book-recommendation-system.git)
    cd book-recommendation-system
    ```

2.  **Run setup**
    ```bash
    chmod +x setup.sh
    ./setup.sh
    ```
    This will:
    * Create a virtual environment in `.venv/`
    * Activate it
    * Install dependencies from `requirements.txt` and also embeddings and metadata that was created.

3.  **Start the server**
    ```bash
    python server.py
    ```
    Visit `http://localhost:5000` in your browser.