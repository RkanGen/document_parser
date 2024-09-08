---

# Efficient Document Parser with Entity Recognition and Search

This project is a powerful document parser built using **Streamlit**. It supports PDF and Word document uploads, performs **Named Entity Recognition (NER)** using **spaCy**, embeds text using **OpenAI embeddings** via **LangChain**, and stores and searches document embeddings using **Pinecone**.

## Features

- **Document Upload**: Users can upload PDF or Word documents.
- **Text Extraction**: Extracts and displays text from uploaded documents.
- **Named Entity Recognition**: Uses **spaCy** to recognize entities such as names, places, dates, and more.
- **Embeddings**: Text is embedded using **OpenAI embeddings** via **LangChain**.
- **Pinecone Integration**: Embeddings are stored in **Pinecone** for efficient storage and semantic search.
- **Search**: Allows users to search across uploaded documents using the stored embeddings.

## Project Structure

```
document_parser/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── parser.py               # Document parsing logic (PDF and DOCX)
├── nlp.py                  # NLP for entity recognition and embeddings
└── pinecone_search.py       # Pinecone storage and search logic
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/RkanGen/document-parser.git
cd document-parser
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

The key dependencies are:
- **Streamlit**: For building the web interface.
- **PyPDF2**: To extract text from PDFs.
- **python-docx**: To extract text from Word documents.
- **spaCy**: For Named Entity Recognition.
- **LangChain**: To embed text using OpenAI embeddings.
- **Pinecone**: For storing and searching document embeddings.
- **python-dotenv**: For securely managing environment variables.

### 3. Set Up Environment Variables

Create a `.env` file in the project root and add your API keys:

```
OPENAI_API_KEY=your_openai_api_key_here
PINECONE_API_KEY=your_pinecone_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Set Up Pinecone

To use Pinecone for storing and searching embeddings:
- Sign up at [Pinecone](https://www.pinecone.io/).
- Create an API key and add it to your `.env` file as `PINECONE_API_KEY`.

### 5. Run the Application

To run the Streamlit application, use the following command:

```bash
streamlit run app.py
```

Once the app is running, open your browser and go to `http://localhost:8501`.

## Usage

1. **Upload Document**: Upload a PDF or DOCX file using the file uploader.
2. **Extract Text**: The extracted text will be displayed.
3. **Entity Recognition**: Detected entities (names, places, etc.) are highlighted.
4. **Embed Text**: The extracted text is embedded using OpenAI embeddings.
5. **Store in Pinecone**: The embeddings are stored in Pinecone for later search.
6. **Search Documents**: You can search across uploaded documents using a query.


## Dependencies

All required libraries are listed in `requirements.txt`. Here's a list of key dependencies:
- `streamlit`
- `PyPDF2`
- `python-docx`
- `spacy`
- `langchain`
- `openai`
- `pinecone-client`
- `python-dotenv`

To install them manually:

```bash
pip install streamlit PyPDF2 python-docx spacy langchain openai pinecone-client python-dotenv
```

Additionally, download the spaCy model:

```bash
python -m spacy download en_core_web_sm
```

## Contribution
 💖✅♻ feel free to use this project and modified it    💖✅♻

---

