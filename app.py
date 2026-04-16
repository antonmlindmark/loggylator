import flet as ft
from collections import Counter

def main(page: ft.Page):
    page.title = "Loggylator"
    page.window.width = 600
    page.window.height = 600
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    matched_lines = []

    def read_lines_with_fallback(path: str):
        encodings = ["utf-8", "utf-8-sig", "utf-16", "utf-16-le", "cp1252", "latin-1"]

        for enc in encodings:
            try:
                with open(path, "r", encoding=enc) as f:
                    return f.readlines(), enc
            except UnicodeError:
                continue
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.readlines(), "utf-8 (errors=ignore)"
        
    def analyze_log(path: str):
        counts = Counter()
        found = []

        lines, used_encoding = read_lines_with_fallback(path)
            
        for line in lines:
            u = line.upper()
            t = line.strip()

            if "ERROR" in u:
                counts["ERROR"] += 1
                found.append(("ERROR", t))
            elif "WARNING" in u:
                counts["WARNING"] += 1
                found.append(("WARNING", t))
            elif "CAUTION" in u:
                counts["CAUTION"] += 1
                found.append(("CAUTION", t))
        return counts, found, used_encoding
    info_text = ft.Text("Ingen fil vald")
    counts_text = ft.Text("")
    result_list = ft.Column(scroll=ft.ScrollMode.AUTO, height=420)
    def show_selected(level: str):
        result_list.controls.clear()
        for tag, msg in matched_lines:
            if tag == level:
                result_list.controls.append(ft.Text("msg"))
        if not result_list.controls:
            result_list.controls.append(ft.Text("Inga loggar för val."))
        page.update()
    def on_dropdown_change(e):
        selected_value = e.control.value
        show_selected(selected_value)
    level_dropdown = ft.Dropdown(
            label="Välj Felmeddelande",
            width=220,
            options=[
                ft.DropdownOption("Error"),
                ft.DropdownOption("Warning"),
                ft.DropdownOption("Caution"),
            ]
        )

    level_dropdown.on_change = on_dropdown_change
    page.update()

    async def choose_file(e):
        nonlocal matched_lines
        file = await ft.FilePicker().pick_files(allow_multiple=True)
        if not files:
            return
        counts, matched, enc = analyze_log(files[0].path)
        matched_lines = matched
        info_text.value = f"Fil: {files[0].name} | Encoding: {enc}"
        counts_text.value = (
            f"ERROR: {counts.get('ERROR', 0)} | "
            f"WARNING: {counts.get('WARNING', 0)} | "
            f"CAUTION: {counts.get('CAUTION', 0)}"
        )
        show_selected(level_dropdown.value)
        page.update()

        #page.add(
            #ft.Text(counts)
        #)
        #page.update()

    page.add(
        ft.Button("Välj Fil", on_click=choose_file),
        info_text,
        counts_text,
        level_dropdown,
        ft.Divider(),
        result_list,
        )
    page.update()
ft.run(main)
