"""
Nota trecătoare la un test.
Presupunem că pentru a avea o notă trecătoare la un test,
elevii trebuie să obţină minim 15 puncte.
Scrieţi un program care citeşte de la tastatură punctajul obţinut de un elev şi
afişează dacă elevul are o notă trecătoare sau va trebui să mai susţină încă o dată testul.
"""
trecere = 15
punctaj=(input("Introduceti punctajul dmv:"))
if int(punctaj) >= int(trecere):
    print("Felicitari,ai sustinut examenul")
else:
    print("Va trebui sa sustineti din nou examenul")
