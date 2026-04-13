import sys
from collections import Counter

LEVELS=("ERROR", "CAUTION", "WARNING")

def analyze_log(path: str):
    counts = Counter()
    matched_lines = []

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
        print(f"DEBUG: Läste {len(lines)} rader från {path}")
        print("DEBUG första rad:", lines[0].strip() if lines else "INGEN RAD")
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
