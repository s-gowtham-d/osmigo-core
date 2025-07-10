import psutil
from datetime import datetime

def get_system_stats():
    stats = {
        "timestamp": datetime.now().isoformat(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory()._asdict(),
        "disk": psutil.disk_usage('/')._asdict(),
        # "network": psutil.net_io_counters()._asdict(),
    }
    return stats