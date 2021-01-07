Haushaltsbuch

Das Programm rechent, ordnet und zeigt die ihm gegeben Einahmen und Ausgabe.
So erhält der Nutzer einen besseren Überblick über seine persöhnliche Finanzen.

Um das Programm auszuführen muss Flask, jsonify und request installiert sein.

Gestartet wird das Programm durch das Ausführen des bootstrap.sh.
Im Terminal ist dann der link http://0.0.0.0:5000/ zu finden.
Diesen muss man anschliessend öffnen.

Auf der ersten Seite wird man begrüsst.
Unter calculator/plus, calculator/minus, calculator/multiply und calculator/divide kann man mit den jeweiligen Operatoren Zahlen gleichnamiger Gruppen verrechnen.
Unter der Seite calculator/main werden die gleichnamigen Gruppen addiert wie auch subtrahiert. So kann man zum Beispiel auführen, wie viel Geld man auf der Bank hat oder wie hoch der Gewinn von etwas nach Abzug der Kosten ist.
Um unter eine der Seiten einen Eintrag zu tätigen gibt man dies ins Terminal:
curl -X POST -H "Content-Type: application/json" -d '{
  "name": Betrag.0
}' http://localhost:5000/calculator/?
