# 🕵️‍♂️ Plagiarism Detection System

This project is a **Web-based Plagiarism Detector** that uses **Google Custom Search API** and **Cosine Similarity** to detect content similarity and possible plagiarism in user-provided text or documents.


## 🚀 Features

- 🔍 Web-based text and file input interface (via Django)  
- 🌐 Real-time Web Search using Google API  
- 🧠 Cosine Similarity based content comparison  
- 🧾 Text and PDF file upload supported  
- 📊 Detailed percentage output and matching link highlights  
- 💬 NLTK-based preprocessing with stopword removal  


## 🛠️ Tech Stack

- **Frontend**: HTML, Bootstrap  
- **Backend**: Django, Python  
- **Web Search API**: Google Custom Search JSON API  
- **Similarity Algorithm**: Cosine Similarity using term frequency  
- **Preprocessing**: NLTK  


## 📁 Project Structure

```
Plagiarism-Detection-System/
│
├── PlagCheck/                     # Main Django App
│   ├── templates/
│   ├── static/
│   ├── algorithm/
│   │   ├── ConsineSim.py         # Cosine similarity calculator
│   │   ├── searchWeb.py          # Google Search API integration
│   │   └── similarity.py         # Query generation and analysis
│
├── Plagarism_Detection/          # Django project settings
│
├── manage.py
├── requirements.txt
├── .env                          # Contains Google API credentials
└── README.md
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Plagiarism-Detection-System.git
cd Plagiarism-Detection-System
```

### 2. Create virtual environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Google API Keys

Create a `.env` file in the root directory with the following:

```env
SEARCH_ENGINE_ID=your_custom_search_engine_id
SEARCH_ENGINE_API_KEY=your_api_key
```

Visit `http://127.0.0.1:8000` in your browser.

---

## 🧪 How It Works

1. **Input**: Users can enter text or upload a file (PDF/DOCX).  
2. **Preprocessing**: Text is cleaned and broken into n-grams using NLTK.  
3. **Web Search**: Each n-gram is searched using Google API.  
4. **Similarity Calculation**: Cosine similarity is used to compare search snippets with input.  
5. **Output**: Total similarity percentage and matching sources are displayed.


Sure! Here's your updated **📊 Output / Results** section in the same format as the pedestrian detection example — clean, centered, and well-presented for GitHub:

---

## 📊 Output / Results

Here are some sample outputs and a demo video of the plagiarism detection system in action.

🖼️ *Screenshot*

<p align="center">
  <img src="screenshots/plagiarism_output.png" alt="Plagiarism Detection Screenshot" width="500"/>
</p>

🎥 *Demo Video*

<p align="center">
  <video src="screenshots/demo.mp4" controls width="600"></video>
</p>

---


## 📚 Dependencies

See `requirements.txt`:

```
Django==3.1.2
nltk==3.6.2
google-api-python-client==1.12.5
python-dotenv==0.15.0
PyPDF2
python-docx
gunicorn
```


## 🙏 Acknowledgements

- [Google Custom Search API](https://developers.google.com/custom-search/)
- [NLTK - Natural Language Toolkit](https://www.nltk.org/)
