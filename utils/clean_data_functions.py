import re
import unicodedata
import pandas as pd

def _normalize_mojibake(text: str) -> str:
    # Try common mojibake fix: text was decoded as Latin-1 instead of UTF-8
    try:
        return text.encode("latin1").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        # Try Windows-1252 as a secondary common case
        try:
            return text.encode("cp1252").decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            return text
        
# Normalizer: strip, uppercase, remove accents or punctuation
def normalize_text(value):
    if pd.isna(value):
        return value
    s = str(value)
    s = _normalize_mojibake(s)
    # Transliterate accents to ASCII (e.g., Â -> A, Ã -> A)
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    # Remove commas
    s = s.replace(",", "")
    
    # replace non letters / numbers with single space
    s = re.sub(r'[^A-Z0-9\s]', '', s)
    
    # Normalize whitespace
    s = re.sub(r"\s+", " ", s).strip()
    return s

STOPWORDS = {'DE','DO','DA','DOS','DAS','E'}

def initials_from_name(norm_name):
    if norm_name:
        return None
    parts = [p for p in norm_name.split() if p and p not in STOPWORDS]
    
    if len(parts) == 0:
        return None
    
    if len(parts) == 1:
        word = parts[0]
        # if it's already 2 letters (maybe used typed "MG") return as-is
        if len(word) == 2:
            return word
        
        # Otherwise take first two letters as a reasonable guess
        return word[:2]
    
    # Take first letter of first signifcant word + first lettter of last sig
    return (parts[0][0] + parts[-1][0]).upper()
