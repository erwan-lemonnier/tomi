# tomi
Just a programming experiment :-)

This is a self-contained website showcasing the use of python/Flask/jinja2/bootstrap/jquery.

## Running the server

Install dependencies:

```bash
sudo pip install requests flask click
```

Start the web server:
```bash
cd bin; python www
```

Then open 'http://127.0.0.1:8080' in your web browser.

## Introspecting the database

```bash
cd db; sqlite3 tomi.db
