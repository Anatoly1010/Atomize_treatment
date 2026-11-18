"""Runtime files of the treatment tools, kept in the user config folder of the running app.

The plot buffers are the one-shot mailbox between the main window ("Send to Data
Treatment") and the tools. The last-used folders sit next to the main window's in
``lastdir/``.
"""
import os
from platformdirs import user_config_dir
from atomize.main.local_config import APP_NAME

_CONFIG_DIR = user_config_dir(APP_NAME)
BUFFER_DIR = os.path.join(_CONFIG_DIR, 'treatment')
LASTDIR_DIR = os.path.join(_CONFIG_DIR, 'lastdir')
os.makedirs(BUFFER_DIR, exist_ok=True)
os.makedirs(LASTDIR_DIR, exist_ok=True)

BUFFER_PATH = os.path.join(BUFFER_DIR, 'treatment_buffer.csv')
BUFFER_2D_PATH = os.path.join(BUFFER_DIR, 'treatment_buffer_2d.npz')


def lastdir_path(key):
    return os.path.join(LASTDIR_DIR, '%s_lastdir.txt' % key)
