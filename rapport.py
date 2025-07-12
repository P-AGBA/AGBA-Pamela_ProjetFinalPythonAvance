from fpdf import FPDF
from datetime import datetime

def generate_report(analyzer, filename="rapport.pdf"):
    stats = analyzer.get_statistics()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)

    # Titre
    pdf.cell(0, 10, "RAPPORT DE SURVEILLANCE" \
    "", ln=True, align="C")
    pdf.ln(10)

    # Date
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Date de génération : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
    pdf.ln(10)

    # Statistiques globales
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Statistiques générales :", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, f"- Total d'événements     : {stats['total']}", ln=True)
    pdf.cell(0, 8, f"- Événements CRITIQUES   : {stats['critical']}", ln=True)
    pdf.cell(0, 8, f"- Événements ERREURS     : {stats['error']}", ln=True)
    pdf.cell(0, 8, f"- Nombre d'alertes       : {stats['alerts']}", ln=True)
    pdf.ln(10)

    # Détails des alertes
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Alertes détectées :", ln=True)
    pdf.set_font("Arial", "", 12)
    if analyzer.alerts:
        for alert in analyzer.alerts:
            pdf.cell(0, 8, f"[{alert['level']}] à {alert['alert_time']} (événements : {', '.join(alert['events'])})", ln=True)
    else:
        pdf.cell(0, 8, "Aucune alerte détectée.", ln=True)

    pdf.output(filename)
