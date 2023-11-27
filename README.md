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
   conda:
   ```bash
   conda create --name myvenv python==3.8
   ```
3. Activate created virtual environment:
   linux: ```bash
   Source ./venv/bin/activate
   ```
   conda: ```bash
   conda activate venv
   ```
4. Install required libraries/ packages:
   ```pip install -r requirements.txt```
5. Download BERT Model Weights:
   ```bash
   bert-large-uncased-whole-word-masking-finetuned-squad
   ```
6. Set UP Environment Variables:
   ```bash
   Save API Keys inside ".env" file --- Do not use openly
   ```
7. Prepare CSV files:
   ```bash
   Read and preprocess dataset
   ```
8. Create application.py file using Flask:
   ```bash
   Use HTML,  CSS and FLASK concepts.
   ```
9. Run the Flask app:
   ```bash
   python application.py
   ```
10. Visit Output of Sample Query:
   - Query: What wax is a sculpting product in the Schwarzkopf line?
   - Answer: Taft Hair Wax

