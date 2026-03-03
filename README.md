SHL Assessment Recommendation Engine
Overview

This project implements an Assessment Recommendation System for SHL assessments. Given a user query describing job roles or required skills, the engine recommends the most relevant SHL assessments using semantic search on SHL’s assessment catalog.

The system is designed for the Research Engineer application assessment for SHL AI.

Features

Search SHL assessments by job roles, skills, or keywords

Returns relevant assessment names and URLs

Simple REST API endpoint for integration

Uses Sentence Transformers (all-MiniLM-L6-v2) for semantic embeddings

Files
File	Description
SHL_Recommendation.ipynb	Main Colab notebook demonstrating data processing, embedding generation, and recommendation API
shl_api.py	Flask API serving the recommendation engine
shl_full_catalog.json	SHL assessment catalog in JSON format
Gen_AI Dataset.xlsx	Original dataset used to build the catalog
README.md	Project documentation
Installation

Clone the repository:

git clone https://github.com/sibadrita23/SHL_Recommendation.git
cd SHL_Recommendation

Install required packages:

pip install -r requirements.txt

Dependencies include:

sentence-transformers

flask

pandas

numpy

scikit-learn

pyngrok (for demo hosting)

Usage
1. Run Recommendation API
python shl_api.py

API will run at http://127.0.0.1:5000

Use ngrok to expose public URL (optional):

from pyngrok import ngrok
public_url = ngrok.connect(5000)
print(public_url)
2. API Endpoints

Health Check

GET /health

Returns:

{"status": "ok"}

Recommendation

POST /recommend
Content-Type: application/json

Request Body:

{
  "text": "I am hiring for Java developers with data analysis skills"
}

Response:

{
  "query": "I am hiring for Java developers with data analysis skills",
  "recommendations": [
    "Java Developer Assessment 1",
    "Data Analysis Assessment 2"
  ]
}
How It Works

Load SHL assessment catalog from JSON.

Generate sentence embeddings for each assessment description using all-MiniLM-L6-v2.

Compute cosine similarity between user query and catalog embeddings.

Return the top 5 most relevant assessments.
