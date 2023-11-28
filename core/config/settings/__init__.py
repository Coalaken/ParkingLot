from pathlib import Path
import os
from split_settings.tools import (
    include,
    optional
)


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

LOCAL_SETTINGS_PATH = BASE_DIR / 'locals/settings.dev.py'


include(
    'base.py', 
    optional(LOCAL_SETTINGS_PATH)
)