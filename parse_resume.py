import pdfplumber
import json
import re
import spacy

# ===== PDF to Text =====
def extract_pdf_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Predefined skill keywords
SKILL_KEYWORDS = [
    "Python", "JavaScript", "React", "Node.js", "AWS", "Docker", "SQL", "Java", "C++", "HTML", "CSS", "TensorFlow",
    "Keras", "Pandas", "NumPy", "Git", "Kubernetes", "TypeScript"
]

# Categorization rules
TYPE_RULES = {
    "work": ["engineer", "developer", "manager", "consultant", "analyst", "designer", "specialist"],
    "education": ["bachelor", "master", "phd", "university", "college", "school", "diploma"],
    "certification": ["certification", "certified", "certificate"],
    "project": ["project", "research", "hackathon"]
}

def categorize_entry(title, description):
    text = (title + " " + description).lower()
    for category, keywords in TYPE_RULES.items():
        if any(kw in text for kw in keywords):
            return category
    return "work"

def extract_skills(text):
    return sorted(set([kw for kw in SKILL_KEYWORDS if re.search(rf"\b{kw}\b", text, re.IGNORECASE)]))

def parse_resume(text):
    doc = nlp(text)

    date_pattern = r"((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\s+\d{4}|Present|\d{4})"
    chunks = re.split(date_pattern, text)

    timeline = []
    for i in range(0, len(chunks)-2, 3):  
        start_date = chunks[i+1] + " " + chunks[i+2] if chunks[i+1] and chunks[i+2] else chunks[i+1]
        description = chunks[i].strip()

        if len(description) < 5:
            continue

        ent_doc = nlp(description)
        title = None
        company = None
        location = None

        for ent in ent_doc.ents:
            if ent.label_ == "ORG":
                company = ent.text
            elif ent.label_ in ["GPE", "LOC"]:
                location = ent.text
            elif ent.label_ in ["PERSON", "WORK_OF_ART"]:
                title = ent.text

        if not title:
            title = description.split("\n")[0]

        year_match = re.search(r"\b(19|20)\d{2}\b", start_date or "")
        year = year_match.group(0) if year_match else "N/A"

        details = [d.strip("-• ").strip() for d in description.split("\n") if len(d.strip()) > 5]

        entry_type = categorize_entry(title or "", description)

        timeline.append({
            "year": year,
            "title": title or "N/A",
            "company": company or "N/A",
            "type": entry_type,
            "description": description[:150] + ("..." if len(description) > 150 else ""),
            "details": details,
            "duration": start_date or "N/A",
            "location": location or "N/A"
        })

    timeline = sorted(timeline, key=lambda x: x["year"], reverse=True)

    total_years = len(set([t["year"] for t in timeline if t["year"].isdigit()]))
    current_role = timeline[0]["title"] if timeline else "N/A"
    education_entries = [t for t in timeline if t["type"] == "education"]

    summary = {
        "totalExperience": f"{total_years} years",
        "currentRole": current_role,
        "keySkills": extract_skills(text),
        "education": education_entries[0]["title"] if education_entries else "N/A"
    }

    return {
        "timeline": timeline,
        "summary": summary
    }

if __name__ == "__main__":
    pdf_path = "Sample path" 
    resume_text = extract_pdf_text(pdf_path)
    result = parse_resume(resume_text)
    print(json.dumps(result, indent=2))
