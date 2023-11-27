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
   ```bash
   python -m venv venv
   ```
   conda: ```bash
   conda create --name myvenv python==3.8
   ```
2. Activate created virtual environment:
   linux: ```bash
   Source ./venv/bin/activate
   ```
   conda: ```bash
   conda activate venv
   ```
3. Install required libraries/ packages:
   ```pip install -r requirements.txt```
4. Download BERT Model Weights:
   ```bash
   bert-large-uncased-whole-word-masking-finetuned-squad
   ```
5. Set UP Environment Variables:
   ```bash
   Save API Keys inside ".env" file --- Do not use openly
   ```
6. Prepare CSV files:
   ```bash
   Read and preprocess dataset
   ```
7. Create application.py file using Flask:
   ```bash
   Use HTML,  CSS and FLASK concepts.
   ```
8. Run the Flask app:
   ```bash
   python application.py
   ```
9. Visit Output of Sample Query:
    bash```
    Query: What wax is a sculpting product in the Schwarzkopf line?
   ```
   bash```
   Answer: Taft Hair Wax
   ```
