from datetime import timedelta
import json

class EventAnalyzer:
    def __init__(self):
        self.events = []
        self.alerts = []

    def add_event(self, event):
        self.events.append(event)
        self._detect_anomaly()

    def _detect_anomaly(self):
        if len(self.events) >= 3:
            last_three = self.events[-3:]
            if all(e.is_alert_level() for e in last_three):
                delta = last_three[-1].timestamp - last_three[0].timestamp
                if delta <= timedelta(seconds=30):
                    self.alerts.append({
                        "alert_time": last_three[-1].timestamp.isoformat(),
                        "events": [e.event_id for e in last_three],
                        "level": last_three[-1].level.upper()
                    })

    def get_statistics(self):
        return {
            "total": len(self.events),
            "critical": sum(e.is_critical() for e in self.events),
            "error": sum(e.is_error() for e in self.events),
            "alerts": len(self.alerts)
        }

    def save_alerts(self, filename="alerts.json"):
        with open(filename, "w") as f:
            json.dump(self.alerts, f, indent=4)
