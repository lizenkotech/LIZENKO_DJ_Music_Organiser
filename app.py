
from pathlib import Path

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

projectmap = Path(__file__).parent
muziekbestand = projectmap / "nummers.txt"


def nummers_inlezen():
    if not muziekbestand.exists():
        return []

    with open(muziekbestand, "r", encoding="utf-8") as tekstbestand:
        inhoud = tekstbestand.read()

    inhoud = inhoud.replace("\r\n", "\n").strip()

    if not inhoud:
        return []

    nummers = []

    for nummer in inhoud.split("\n\n"):
        informatie = nummer.splitlines()

        if len(informatie) >= 3:
            nummers.append({
                "titel": informatie[0].strip(),
                "artiest": informatie[1].strip(),
                "muziekstijl": informatie[2].strip()
            })

    return nummers


@app.route("/", methods=["GET", "POST"])
def startpagina():
    melding = ""

    if request.method == "POST":
        titel_nummer = request.form.get("titel", "").strip()
        artiest = request.form.get("artiest", "").strip()
        muziekstijl = request.form.get("muziekstijl", "").strip()

        if titel_nummer and artiest and muziekstijl:
            bestaande_inhoud = ""

            if muziekbestand.exists():
                with open(muziekbestand, "r", encoding="utf-8") as tekstbestand:
                    bestaande_inhoud = tekstbestand.read()

            with open(muziekbestand, "a", encoding="utf-8") as tekstbestand:
                if bestaande_inhoud:
                    if not bestaande_inhoud.endswith("\n"):
                        tekstbestand.write("\n")
                    if not bestaande_inhoud.endswith("\n\n"):
                        tekstbestand.write("\n")

                tekstbestand.write(titel_nummer + "\n")
                tekstbestand.write(artiest + "\n")
                tekstbestand.write(muziekstijl + "\n\n")

            return redirect(url_for("startpagina", toegevoegd="ja"))

        melding = "Vul alle drie de velden in."

    if request.args.get("toegevoegd") == "ja":
        melding = "Nummer succesvol toegevoegd!"

    nummers = nummers_inlezen()
    zoekterm = request.args.get("zoekterm", "").strip()

    if zoekterm:
        nummers = [
            nummer for nummer in nummers
            if zoekterm.casefold() in nummer["titel"].casefold()
        ]

    return render_template(
        "index.html",
        nummers=nummers,
        zoekterm=zoekterm,
        melding=melding
    )


if __name__ == "__main__":
    app.run(debug=True)
