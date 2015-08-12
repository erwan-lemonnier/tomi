import os
import sqlite3
from contextlib import contextmanager

log = None

db_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'db')
db_path = os.path.join(db_dir, 'tomi.db')

schema = [
# Table holding every published message
"""
CREATE TABLE     messages (
    id           INTEGER PRIMARY KEY,
    content      CHAR(1000) NOT NULL,
    date         DATE NOT NULL
)"""
]


class DBException(Exception):
    pass

@contextmanager
def get_cursor(autocommit=False):
    with sqlite3.connect(db_path) as conn:
        yield conn.cursor()
        if autocommit:
            conn.commit()

def create_database(logger):
    """Create database, with initial sql schema"""
    global log
    log = logger

    if not os.path.exists(db_dir):
        os.mkdir(db_dir)

    with get_cursor(True) as c:

        for r in c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"):
            if r[0] in ('messages'):
                log.debug("DB already created. Delete %s to force recreation" % db_path)
                return

        log.info("Creating database")
        for statement in schema:
            c.execute(statement)
