spørsmål = ["Hva er verdens største kontinent målt i areal? ",
            "Hvilket land har flest innbyggere i verden?",
            "Hva heter verdens lengste elv?",
            "Hvilket hav er det største?",
            "Hva er hovedstaden i Canada?",
            "Hvilket land ligger både i Europa og Asia?",
            "Hva heter verdens høyeste fjell?",
            "Hvilket av disse landene har ingen kystlinje?",
            "Hvilken ørken er den største ørkenen i verden?",
            "Hvilket land består av flest øyer i verden?"
            ]

svar = ["Asia",
        "India",
        "Nilen",
        "Stillehavet",
        "Ottawa",
        "Tyrkia",
        "Mount Everest",
        "Bolivia",
        "Sahara",
        "Sverige"
        ]

valg = [["Afrika", "Europa", "Asia", "Sør-Amerika"],
        ["USA", "Kina", "Russland","India"],
        ["Amazonas", "Mississippi", "Yangtze","Nilen"],
        ["Atlanterhavet", "Det indiske hav", "Sørishavet","Stillehavet"],
        ["Toronto", "Vancouver", "Ottawa","Montreal"],
        ["Hellas", "Tyrkia", "Italia","Spania"],
        ["K2", "Mount Kilimanjaro", "Mount Everest","Mont Blanc"],
        ["Peru", "Vietnam", "Bolivia","Thailand"],
        ["Gobi", "Sahara", "Kalahari","Atacama"],
        ["Indonesia", "Filippinene", "Japan","Sverige"],
]

poeng = 0
for i in range(len(spørsmål)):
    print(spørsmål[i])
    for idx, v in enumerate(valg[i]):
        print(f"{idx + 1}. {v}")
    svar_input = input("Velg riktig alternativ (skriv tallet):")
    if svar_input.isdigit() and int(svar_input) in range(1, 5):
        if valg[i][int(svar_input) - 1].lower() == svar[i].lower():
            poeng += 1
            print("Riktig")
        else: 
            print("Feil")
    else:
        print("Uyldig svar")

print(f"du fikk {poeng} av {len(spørsmål)} poeng!")

    
