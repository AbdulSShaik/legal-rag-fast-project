import re

def extract_sections(text):
    sections = {
        "observation": "",
        "compliance": "",
        "recommendation": "",
        "accounting": ""
    }

    patterns = {
        "observation": r"(?i)observation:\s*(.+?)(?=\n[A-Z]|\Z)",
        "compliance": r"(?i)compliance risks:\s*(.+?)(?=\n[A-Z]|\Z)",
        "recommendation": r"(?i)recommendation:\s*(.+?)(?=\n[A-Z]|\Z)",
        "accounting": r"(?i)accounting impact:\s*(.+?)(?=\n[A-Z]|\Z)"
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.DOTALL)
        if match:
            sections[key] = match.group(1).strip()

    return sections