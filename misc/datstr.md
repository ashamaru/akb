# Datenbank Dateitypen#
id:
  - Primärschlüssel
  - Typ:  bigint
  - Form: <auktionsid><positionsid>
  
Positionsname:
  - Typ:  verlinkt zur historie

Aktuelles Gebot:
  - Typ:  decimal

Fremdschlüssel zur Gebotshistorie:
  - Typ:  bigint

Daten bzw. Beschreibung:
  - Typ:  text

Fremdschlüssel zur Imagetabelle
  - Typ:  bigint

Ende des Gebots:
  - Type: timefied
