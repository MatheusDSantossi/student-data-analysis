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
        
def _clean_campus(value):
    if pd.isna(value):
        return value
    s = str(value)
    s = _normalize_mojibake(s)
    # Transliterate accents to ASCII (e.g., Â -> A, Ã -> A)
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    # Remove commas
    s = s.replace(",", "")
    # Normalize whitespace
    s = re.sub(r"\s+", " ", s).strip()
    return s
