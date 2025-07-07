
import matplotlib.pyplot as plt
from collections import Counter

def generate_event_graph(events, output_file="graphique.png"):
    levels = [event.level for event in events]
    counter = Counter(levels)

    plt.figure(figsize=(8, 5))
    plt.bar(counter.keys(), counter.values(), color="skyblue")
    plt.title("Répartition des événements par niveau")
    plt.xlabel("Niveau (INFO, WARN, ERROR, CRITICAL)")
    plt.ylabel("Nombre d’événements")
    plt.savefig(output_file)
    plt.close()
