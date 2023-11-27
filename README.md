# LLM-with-Vector-DB-Chaabi-Assignment
Implementation of an LLM on the Vector DB Embeddings to provide the contextual answers to the queries strictly from the database.

## Requirements:
- flask
- os
- pandas
- numpy
- qdrant-client
- openai
- transformers

## Setup Instructions:
1. Crate a virtual environment:
   ```python -m venv venv```
   conda: ```conda create --name myvenv python==3.8```
3. Activate created virtual environment:
   linux: ```Source ./venv/bin/activate```
   conda: ```conda activate venv```
5. Install required libraries/ packages:
   ```pip install -r requirements.txt```
7. Download BERT Model Weights:
   ```bert-large-uncased-whole-word-masking-finetuned-squad```
8. Set UP Environment Variables:
   ```Save API Keys inside ".env" file --- Do not use openly```
9. Prepare CSV files:
   ```Read and preprocess dataset```
10. Create application.py file using Flask:
   ```Use HTML,  CSS and FLASK concepts.```
11. Run the Flask app:
   ```python application.py```
12. Visit Output of Sample Query:
    Query: What wax is a sculpting product in the Schwarzkopf line?
    Answer: Taft Hair Wax 
