import matplotlib.pyplot as plt
from collections import Counter

def generate_event_graph(events, output_file="graphique.png"):
    levels = [event.level for event in events]
    counter = Counter(levels)

    # Préparation des données
    labels = list(counter.keys())
    values = list(counter.values())
    colors = {
        "INFO": "#6EC1E4",
        "WARN": "#F7B801",
        "ERROR": "#F45B69",
        "CRITICAL": "#D7263D"
    }
    bar_colors = [colors.get(label, "#999999") for label in labels]

    # Création du graphique
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, values, color=bar_colors, edgecolor='black')

    # Ajout des étiquettes sur chaque barre
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{int(yval)}', ha='center', va='bottom', fontsize=12)

    # Titres et axes
    plt.title("Répartition des événements par niveau", fontsize=16, fontweight='bold')
    plt.xlabel("Niveau d'événement", fontsize=12)
    plt.ylabel("Nombre d'événements", fontsize=12)

    # Grille
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    # Affichage soigné
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()
