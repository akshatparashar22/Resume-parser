# Resume Parser

A Python-based resume parsing tool that extracts structured information from PDF resumes. 
Currently uses **spaCy** (NLP) + **regex** for parsing, with planned LLM integration for improved accuracy.

---

## Features

- 📄 **PDF to Text** conversion using `pdfplumber`
- 🔍 **Named Entity Recognition (NER)** via spaCy for detecting companies, job titles, and locations
- 🗂 **Categorization** into work, education, certification, and projects
- 🛠 **Skill Extraction** from predefined keyword lists
- 📊 **Structured JSON Output** with timeline and summary
- 🧠 **LLM Integration (coming soon)** for better accuracy on unstructured resumes

---

## Example Output

```json
{
  "timeline": [
    {
      "year": "2024",
      "title": "Senior Software Engineer",
      "company": "Tech Corp",
      "type": "work",
      "description": "Brief description of role and achievements",
      "details": [
        "Key responsibility or achievement 1",
        "Key responsibility or achievement 2"
      ],
      "duration": "Jan 2024 - Present",
      "location": "City, Country"
    }
  ],
  "summary": {
    "totalExperience": "5 years",
    "currentRole": "Senior Software Engineer",
    "keySkills": ["React", "Node.js", "Python"],
    "education": "Bachelor's in Computer Science"
  }
}
```

---

## Prerequisites

- **Python** >= 3.10 (recommended)
- **pip** (Python package manager)

---

## Installation & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/akshatparashar22/Resume-parser.git
cd Resume-parser
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
```

### 3️⃣ Activate the virtual environment
**Mac/Linux:**
```bash
source venv/bin/activate
```

**Windows (PowerShell):**
```bash
venv\Scripts\activate
```

### 4️⃣ Install dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

*(If `requirements.txt` does not exist yet, install manually:)*
```bash
pip install pdfplumber spacy
python -m spacy download en_core_web_sm
```

### 5️⃣ Run the parser
Edit `parse_resume.py` and set the correct `pdf_path`:
```python
pdf_path = "/path/to/your/resume.pdf"
```
Then run:
```bash
python parse_resume.py
```

---

## Roadmap

- [ ] Improve date parsing logic
- [ ] Expand skill keyword list dynamically
- [ ] Add **LLM-powered extraction** (e.g., OpenAI/Claude)
- [ ] Build API endpoints for integration with Next.js frontend
- [ ] Deploy as a web service

---

## Contributing

Contributions are welcome!  
Feel free to fork, create a new branch, and submit a pull request.

---

## License

MIT License © 2025 [Akshat Parashar](https://github.com/akshatparashar22)
