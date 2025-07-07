
from datetime import datetime

def generate_report(analyzer, filename="rapport.txt"):
    stats = analyzer.get_statistics()
    with open(filename, "w") as f:
        f.write("RAPPORT DE SURVEILLANCE INTELLIGENTE\n")
        f.write("="*40 + "\n")
        f.write(f"Date de génération : {datetime.now().isoformat()}\n\n")
        f.write(f"Nombre total d'événements      : {stats['total']}\n")
        f.write(f"Nombre d'événements CRITIQUES : {stats['critical']}\n")
        f.write(f"Nombre d'alertes détectées     : {stats['alerts']}\n\n")

        f.write("Horodatages des alertes :\n")
        for alert in analyzer.alerts:
            f.write(f"- {alert['alert_time']} (événements : {', '.join(alert['events'])})\n")
