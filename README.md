Detta är ett verktyg för att analysera loggar och få resultat av loggen.

För att köra appen: ha Python och Package Installer for Python aka pip installerat på datorn,

Klona detta repository till din dator,

Kör kommando "pip install -r requirements.txt" vilket kommer installera flet,

för att sen köra appen kör kommando: python app.py.

Ifall man vill köra detta som en egen app som t.ex. en .exe fil: Säkerställ att du har pyinstaller nedladdat och kör kommando "pyinstaller --onefile --name loggylator app.py". Detta kommer göra så att allt packas ihop och det skapas en .exe fil som kommer få namnet "Loggylator" istället för app.

Man får välja felmeddelanden först vilket för tillfället är "Error", "Warning" och "Caution". Efter det så får man välja filen man vill analysera och då kommer det visas upp hur många felmeddelande av alla de tre olika sorterna finns. Om man har valt ett speciellt felmeddelande så kommer den visa upp ett par i appen med tidsstämpel och inlägg.

Version:

1.0.0: Logg kan analyseras, dock bara med UTF-8 encoding.

1.1.0: Flera encoding val inlagda i appen

2.0.0: Lagt till appmöjligheter, styrs via flet och allt skrivs inte i terminalen längre.

2.1.0: Dropdown meny finns nu så man kan välja mellan de olika felmeddelande som finns för tillfället
