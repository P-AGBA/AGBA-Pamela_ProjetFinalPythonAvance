
import asyncio
from event import Event
from analyse import EventAnalyzer
from logger import EventLogger
from rapport import generate_report
from visuel import generate_event_graph

analyzer = EventAnalyzer()
logger = EventLogger()

async def process_log(file_path):
    print("Démarrage du traitement du fichier log...")
    with open(file_path, "r") as f:
        for line in f:
            await asyncio.sleep(2)
            event = Event(line)
            analyzer.add_event(event)
            logger.log_event(event)
            print(f"[+] Event {event.event_id} traité ({event.level.upper()})")
            # Afficher une alerte si nouvellement détectée
            if len(analyzer.alerts) > 0 and analyzer.alerts[-1]['alert_time'] == event.timestamp.isoformat():
                print(f"[!] Alerte détectée à {event.timestamp.isoformat()} !")

def display_menu():
    print("\n--- Menu ---")
    print("1. Lancer le traitement")
    print("2. Afficher les alertes")
    print("3. Générer le rapport")
    print("4. Générer le graphique")
    print("5. Quitter")

async def main():
    while True:
        display_menu()
        choice = input("Choix : ")
        if choice == "1":
            await process_log("events.log")
        elif choice == "2":
            print("\nAlertes détectées :")
            for alert in analyzer.alerts:
                print(alert)
        elif choice == "3":
            analyzer.save_alerts()
            generate_report(analyzer)
            print("Rapport généré.")
        elif choice == "4":
            generate_event_graph(analyzer.events)
            print("Graphique généré.")
        elif choice == "5":
            print("Fermeture du programme.")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    asyncio.run(main())
