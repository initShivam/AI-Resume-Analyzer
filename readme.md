# 🤖 AI Resume Analyzer

An AI-powered Resume Analyzer built with **Flask**, **Groq LLM**, and **Pydantic** that helps recruiters automatically analyze resumes, compare them with a job description, calculate candidate match scores, and rank applicants based on their suitability.

---

## 📌 Features

- 📄 Paste any Job Description
- 📂 Upload one or multiple resumes (PDF/DOCX)
- 🤖 AI-powered Job Description Parsing
- 📑 AI-powered Resume Parsing
- 🎯 Candidate Match Score (0–100%)
- ✅ Matching Skills Detection
- ❌ Missing Skills Detection
- 💼 Experience Requirement Validation
- 🏆 Candidate Ranking
- 🌐 Simple Web Interface using Flask

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- Groq API
- Pydantic

### AI
- Llama 3.3 70B Versatile (Groq)

### Resume Parsing
- PyPDF
- python-docx

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- Jinja2 Templates

---

## 📁 Project Structure

```
AI-Resume-Analyzer/
│
├── templates/
│   ├── index.html
│   └── results.html
│
├── uploads/
│
├── app.py
├── resume_score.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/AI-Resume-Analyzer.git

cd AI-Resume-Analyzer
```

---

### 2. Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install flask groq python-dotenv pydantic pypdf python-docx
```

---

### 4. Create `.env`

```env
GROQ_API_KEY=your_groq_api_key
```

---

### 5. Run the Project

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 💻 How It Works

```
Recruiter

      │

      ▼

Paste Job Description

      │

      ▼

Upload Candidate Resumes

      │

      ▼

Flask Backend

      │

      ▼

Job Description Parser
(Groq AI)

      │

      ▼

Resume Parser
(Groq AI)

      │

      ▼

Resume Matching Engine

      │

      ▼

Candidate Scoring

      │

      ▼

Ranking

      │

      ▼

Results Dashboard
```

---

# 📸 Screenshots

### Home Page

> Add screenshot here

```
screenshots/home.png
```

---

### Results Page

> Add screenshot here

```
screenshots/results.png
```

---

# 📊 Candidate Evaluation

The AI evaluates candidates based on:

- Required Skills
- Preferred Skills
- Experience
- Education
- Overall Resume Match
- Missing Skills
- Final Recommendation

---

# 📂 Supported Resume Formats

- PDF (.pdf)
- Microsoft Word (.docx)

---

# 📦 Future Improvements

- User Authentication
- Recruiter Dashboard
- Resume Database
- PostgreSQL Integration
- Candidate Search
- Export Results to Excel/PDF
- Email Candidate Reports
- OCR Support for Scanned PDFs
- Resume History
- Dark Mode

---

# ⚙️ Requirements

- Python 3.10+
- Groq API Key
- Internet Connection

---

# 👨‍💻 Author

**Shivam Singh**

Aspiring Data Analyst & Python Developer

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

# 📜 License

This project is licensed under the MIT License.

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub.