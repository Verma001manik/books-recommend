#!/bin/bash

set -e  # Exit on error
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing requirements..."
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn
pip install git+https://github.com/Verma001manik/recommendme.git

echo "Downloading FAISS index and metadata..."
mkdir -p data
wget -O data/hf_cleaned_faiss_index.bin https://huggingface.co/datasets/verma001mani/hf_books_embed/resolve/main/hf_cleaned_faiss_index.bin
wget -O data/hf_cleaned.json https://huggingface.co/datasets/verma001mani/hf_books_embed/resolve/main/hf_cleaned.json

echo "Starting Flask app with Gunicorn..."
gunicorn server:app --bind 0.0.0.0:8000
