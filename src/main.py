from nok_dns.config import load_config
from nok_dns.scheduler.daemon_scheduler import DaemonScheduler

def main():
    config = load_config()
    scheduler = DaemonScheduler(config)
    scheduler.run()

if __name__ == "__main__":
    main()
