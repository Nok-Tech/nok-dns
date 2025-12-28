import signal
import time
from threading import Event

from .config import GeneralConfig, load_config


class DaemonScheduler:
    def __init__(self, config: GeneralConfig):
        self.config = config
        self.stop_event = Event()
        self.reload_event = Event()
        signal.signal(signal.SIGHUP, self.handle_sighup)
        signal.signal(signal.SIGTERM, self.handle_sigterm)

    def handle_sighup(self, signum, frame):
        self.reload_event.set()

    def handle_sigterm(self, signum, frame):
        self.stop_event.set()

    def run(self):
        while not self.stop_event.is_set():
            if self.reload_event.is_set():
                self.config = load_config()
                self.reload_event.clear()

            for zone in self.config.zones:
                for record in zone.records:
                    pass

            time.sleep(self.config.interval_seconds)

