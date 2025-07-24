from agents.observer import get_system_stats
import json

def main():
    stats = get_system_stats()
    print(json.dumps(stats, indent=2))

if __name__ == "__main__":
    main()
