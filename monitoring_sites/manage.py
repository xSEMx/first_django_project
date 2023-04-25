#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import threading
from async_update import start_updating_db
from telegram_bot import start_bot
# define a function to start async_update in a separate thread

def main():
    """Run administrative tasks."""
    threading.Thread(target=start_updating_db, daemon=True).start()
    threading.Thread(target=start_bot, daemon=True).start()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitoring_sites.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
