# Analyser des logs JSON simulés pour détecter des anomalies critiques, générer des rapports, afficher des alertes, et produire des visualisations statistiques

Structure

- `main.py` : menu interactif + traitement asynchrone
- `event.py` : classe `Event`
- `logger.py` : classe `EventLogger`
- `rapport.py` : génération du rapport
- `visuel.py` : génération du graphique
- `alerts.json` : alertes sauvegardées
- `rapport.pdf` : rapport
- `graphique.png` : histogramme

## Fonctionnalités

- Lecture ligne par ligne avec délai simulé
- Détection de séquences critiques
- Sauvegarde des alertes en JSON
- Rapport automatique en `.pdf`
- Visualisation statistique avec `matplotlib`

## Exécution du projet

pip install -r requirements.txt
cd chemin/vers/Agba-Pamela_ProjetFinalPythonAvance
python main.py

>Lien vers la [vidéo de présentation](https://www.youtube.com/watch?v=3b1c2k0g4e8).

>Lien vers le dépôt [github](https://github.com/P-AGBA/AGBA-Pamela_ProjetFinalPythonAvance).
