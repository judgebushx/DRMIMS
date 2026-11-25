import os

from django.core.wsgi import get_wsgi_application
from waitress import serve

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()

port = int(os.environ.get("SERVER_PORT", "8000"))

print(f"Starting DRMIMS on port {port}")

serve(
    application,
    host="127.0.0.1",
    port=port,
    threads=8,
)