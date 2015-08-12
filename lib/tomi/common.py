import logging
import json

logger = None

def setup_logging(name):
    """Setup console logging"""
    global logger
    if logger:
        return logger

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

def create_http_response(data, status_code=200, headers=None, redirect_url=None):
    """Utility method for compiling the reply of @route methods"""
    if not data:
        raise Exception("No data provided")
    if not headers:
        headers = {}
    if isinstance(data, basestring):
        headers["content-type"] = "text/html"
        reply = data
    elif isinstance(data, dict):
        headers["content-type"] = "application/json"
        reply = json.dumps(data)
    else:
        raise Exception("Cannot handle data of type %s" % type(data))
    if redirect_url:
        headers["Location"] = redirect_url
        status_code = 203
    return (reply, status_code, headers)
