# agents/observer_daemon.py

import time
from agents.observer import get_system_stats
from memory.historian import log_system_metrics


def run_observer_daemon(interval=5):
    print(f"[Observer Daemon] Running system monitor every {interval} seconds...")
    while True:
        try:
            stats = get_system_stats()
            log_system_metrics(stats)
            print("[Observer] Logged system stats:", stats)
            time.sleep(interval)
        except KeyboardInterrupt:
            print("\n[Observer Daemon] Stopped by user.")
            break
        except Exception as e:
            print(f"[Observer Daemon] Error: {e}")


if __name__ == "__main__":
    run_observer_daemon()
