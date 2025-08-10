# Resume-parser
Python ML model to parse Resume


---

## Prerequisites

Python ( 3.10 > preferably)

---

## To start the project:

1. create a python environment:

```bash
python -m venv venv
```

2. Activate it:

> Mac/Linux

```bash
source venv/bin/activate
```

> Windows (PowerShell)

```bash
venv\Scripts\activate
```

3. Install Dependencies:

```bash
pip install pdfplumber spacy
python -m spacy download en_core_web_sm #spaCy English model
```

4. Run the code:

In file `parse_resmue.py` change the `pdf_path` to the desired path 

Execute the command:

```bash
python parse_resume.py
```

---