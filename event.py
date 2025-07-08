import json
from datetime import datetime

class Event:
    def __init__(self, raw_line: str):
        self.raw_data = json.loads(raw_line)
        self.timestamp = datetime.fromisoformat(self.raw_data["timestamp"].replace("Z", "+00:00"))
        self.level = self.raw_data["level"]
        self.node = self.raw_data["node"]
        self.component = self.raw_data["component"]
        self.message = self.raw_data["message"]
        self.event_id = self.raw_data["event_id"]

    def is_critical(self):
        return self.level.upper() == "CRITICAL"

    def is_error(self):
        return self.level.upper() == "ERROR"

    def is_alert_level(self):
        return self.level.upper() in ["CRITICAL", "ERROR"]
