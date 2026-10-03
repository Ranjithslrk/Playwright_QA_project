import logging
from pathlib import Path

log_dir = Path("logs")
log_dir.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename="logs/test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)