
import logging

class EventLogger:
    def __init__(self):
        logging.basicConfig(
            filename="event_processing.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        self.logger = logging.getLogger()

    def log_event(self, event):
        self.logger.info(f"Event {event.event_id} processed: {event.message}")
