
# Projet Python – Système de surveillance intelligente

## 🎯 Objectif
Analyser des logs JSON simulés pour détecter des anomalies critiques, générer des rapports, afficher des alertes, et produire des visualisations statistiques.

## 📂 Structure
- `main.py` : menu interactif + traitement asynchrone
- `event.py` : classe `Event`
- `analyzer.py` : classe `EventAnalyzer`
- `logger.py` : classe `EventLogger`
- `report.py` : génération du rapport
- `visual.py` : génération du graphique
- `alerts.json` : alertes sauvegardées
- `rapport.txt` : rapport texte
- `graphique.png` : histogramme

## 🚀 Lancement
```bash
python main.py
```

## 🧪 Fonctionnalités
- Lecture ligne par ligne avec délai simulé
- Détection de séquences critiques
- Sauvegarde des alertes en JSON
- Rapport automatique en `.txt`
- Visualisation statistique avec `matplotlib`
