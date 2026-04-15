import flet as ft
from collections import Counter

def main(page: ft.Page):
    page.title = "Loggylator"
    page.window.width = 600
    page.window.height = 600
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    #file_picker = ft.FilePicker()
    #page.overlay.append(file_picker)

    def read_lines_with_fallback(path: str):
        encodings = ["utf-8", "utf-8-sig", "utf-16", "utf-16-le", "cp1252", "latin-1"]

        for enc in encodings:
            try:
                with open(path, "r", encoding=enc) as f:
                    lines = f.readlines()
                return lines, enc
            except UnicodeError:
                continue
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.readlines(), "utf-8 (errors=ignore)"
        
    def analyze_log(path: str):
        counts = Counter()
        matched_lines = []

        lines, used_encoding = read_lines_with_fallback(path)
            
        for line in lines:
            u = line.upper()

            if "ERROR" in u:
                counts["ERROR"] += 1
                matched_lines.append(("ERROR", line.strip()))
            elif "WARNING" in u:
                counts["WARNING"] += 1
                matched_lines.append(("WARNING", line.strip()))
            elif "CAUTION" in u:
                counts["CAUTION"] += 1
                matched_lines.append(("CAUTION", line.strip()))
        return counts, matched_lines
            
    async def choose_file(e: ft.Event[ft.Button]):
        file = await ft.FilePicker().pick_files(allow_multiple=False)

        counts, matched = analyze_log(file[0].path)

        page.add(
            ft.Text(counts)
        )
        page.update()

    page.add(
        ft.Button(
                "Choose File:",
                on_click = choose_file,
        )
    )
ft.run(main)
