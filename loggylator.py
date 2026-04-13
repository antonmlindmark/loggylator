import sys
from collections import Counter

LEVELS=("ERROR", "CAUTION", "WARNING")

    #Encodingfunktion beroende på vilken encoding filen har
def read_lines_with_fallback(path: str):
    encodings = ["utf-8", "utf-8-sig", "utf-16", "utf-16-le", "cp1252", "latin-1"]

    for enc in encodings:
        try:
            with open(path, "r", encoding=enc) as f:
                lines=f.readlines()
            return lines, enc
        except UnicodeError:
            continue
    
    #Fallback kod ifall Encoding def ej fungerar
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.readlines(), "utf-8 (errors=ignore"

    #Logganalyskod
def analyze_log(path: str):
    counts = Counter()
    matched_lines = []

    lines, used_encoding = read_lines_with_fallback(path)
    print(f"DEBUG: Läste {len(lines)} rader från {path}")
    print(f"DEBUG: Encoding {used_encoding}")
    print(f"DEBUG: Första rad:", lines[0].strip() if lines else "INGEN RAD")
        
    for line in lines:
        u = line.upper()

        if "ERROR" in u:
            counts["ERROR"] += 1
            matched_lines.append(("ERROR", line.strip()))
        elif "WARNING" in u:
            counts["WARNING"] += 1
            matched_lines.appedn(("WARNING", line.strip()))
        elif "CAUTION" in u:
            counts["CAUTION"] += 1
            matched_lines.append(("CAUTION", line.strip()))

    return counts, matched_lines

def print_report(path, counts, matched_lines):
    print(f"\nANALYS AV: {path}")
    print("-" * 40)
    for level in LEVELS:
        print(f"{level:8}: {counts.get(level, 0)}")

    print(f"\nExempelrader:")
    for level, text in matched_lines[:10]:
        print(f"[{level}] {text}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Användning :python loggylator.py <loggfil>")
        sys.exit(1)

    log_file = sys.argv[1]
    counts, matched = analyze_log(log_file)
    print_report(log_file, counts, matched)
