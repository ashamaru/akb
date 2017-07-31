# akb #

Ich lass die Readme vorerst auf deutsch, aber wir sollten Projekt würd ich mal sagen später komplett auf Englisch ziehen.

## Überblick ##
Framework für Auktionen in Python. Framework trift vllt. nicht ganz zu, eher Packete und Module, welche die Logik sowie Datenstrukturen abdecken und später füreine Anwendung verwendet werden können. Am Anfang werden wir eh erstmal alles als Prototyp entwerfen, aber später sollte für jedes Modul ein entsprechender Test und Dokumentation zu existieren.
Test kann man z.B. über ein 
```python
if __name__ == "__main__":
  # test code
```
am Ende jedes Moduls mit eingebaut werden.
Stand [hier](https://docs.python.org/3/tutorial/modules.html#tut-modulesasscripts), wie man sonst am besten Testet bei Pythonprojekte, muss ich nochmal nachschlagen. Für Dokumentation sollten [Docstrings](https://docs.python.org/3/tutorial/controlflow.html#tut-docstrings) reichen, gibt Programme die daraus Docs erstellen.
Funktionalität:
- Accounts
- Authentifizierung und Sessionhandling
- Sql-Anbindung
- Inputvalidierung
- Auktionslogik, versteht sich
- Such- und Filterfuntionen für Positionslisten
- etc

Falls [Django](https://djangoproject.org) bereits was abdeckt, wird's erstmal verwendet. Wenn man Zeit und Interesse hat kann man's nochmal eigens implementieren. Sql, Accounts, Authentifizierung und sowas wird eigtl. standardmäßig mit Django abgedeckt. Saubere Inputvalidierung ist interessant, würd ich fast schon selber implementieren, Accounts, Verifizierung, etc. bin ich auch am Überlegen.

Das wars jetzt mal grob, muss mich jetzt erstmal noch weiter in Python einarbeiten. Genaueres vorgehen beim entwerfen und verwalten kommt noch.

## Datenbank ##
Wir verwenden [MariaDB](https://mariadb.org/), sauberer Open-Source Fork von MySql. Je nach dem was gefordert wird, gibts einen standardmäßigen Zugriffslevel für alle Benutzer der App. Am besten mal selber laufen lassen, gibt eigtl. in den Linux Standardrepositories ein **mariadb-server** package, alle relevanten Befehle beginnen dann mit `mysql`, so heißt auch der client, und `mysqld`, Serverbefehle zu starten, beenden und konfigurieren. Als Referenz für SQL-Befehle und Datenbank einfach mal in die [Knowledge Base](https://mariadb.com/kb/en/mariadb/documentation/) von *mariadb.com* reinschauen, findet man von *mariadb.org* nicht so gut.

## Webserver ##
Apache2, ist eine ähnliche Angelegenheit wie mit der Datenbank. Auf manchen Distributionen oftmals schon vorinstalliert, wenn nicht **apache2** package findet man relativ einfach. Standardmäßig auf die [Offizielle Dokumentation](http://httpd.apache.org/docs/2.4/) zugreifen, vllt. findest du aber auch was besseres.
