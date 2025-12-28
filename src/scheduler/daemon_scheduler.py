import time
import signal
from threading import Event

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
                self.config = load_config()  # Recarregar a configuração
                self.reload_event.clear()

            # Executar lógica de atualização para cada zona e registro
            for zone in self.config.zones:
                for record in zone.records:
                    # Exemplo de lógica: obter IP, comparar, atualizar DNS se necessário
                    # ...

            # Espera até o próximo ciclo
            time.sleep(self.config.interval_seconds)

        # Limpeza e encerramento aqui (se necessário)
