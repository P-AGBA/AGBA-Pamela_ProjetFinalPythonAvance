from datetime import datetime

def generate_report(analyzer, filename="rapport.txt"):
    stats = analyzer.get_statistics()
    with open(filename, "w", encoding="utf-8") as f:
        f.write("RAPPORT DE SURVEILLANCE INTELLIGENTE\n")
            
        f.write(f"Date de génération : {datetime.now().isoformat()}\n\n")
        f.write(f"Nombre total d'événements      : {stats['total']}\n")
        f.write(f"Nombre d'événements CRITIQUES : {stats['critical']}\n")
        f.write(f"Nombre d'événements ERREURS   : {stats['error']}\n")
        f.write(f"Nombre d'alertes détectées     : {stats['alerts']}\n\n")

        f.write("Détails des alertes détectées :\n")
        for alert in analyzer.alerts:
            f.write(f"- [{alert['level']}] à {alert['alert_time']} (événements : {', '.join(alert['events'])})\n")
