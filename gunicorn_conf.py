import json
import multiprocessing
import os

print( os.getenv("HOST"))
workers_per_core_str = os.getenv("WORKERS_PER_CORE", "2")
web_concurrency_str = os.getenv("WEB_CONCURRENCY", None)
host = os.getenv("HOST", "0.0.0.0")
port1 = os.getenv("PORT", "80")
#https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
port = os.getenv("PORT1", "84")
bind_env = os.getenv("BIND", None)
bind_env1 = os.getenv("BIND1", None)
use_loglevel = os.getenv("LOG_LEVEL", "info")
if bind_env:
    use_bind = bind_env
else:
    use_bind = f"{host}:{port}"
if bind_env1:
    use_bind1 = bind_env1
else:
    use_bind1 = f"{host}:{port1}"
cores = multiprocessing.cpu_count()
workers_per_core = float(workers_per_core_str)
default_web_concurrency = workers_per_core * cores
if web_concurrency_str:
    web_concurrency = int(web_concurrency_str)
    assert web_concurrency > 0
else:
    web_concurrency = int(default_web_concurrency)

# Gunicorn config variables
# VAR names are exported to config, so dont mess this up ( gunicorn/base.py -> def get_config_from_filename)
def post_request(worker, req, environ, resp):
    print("Post res")
    print("workerID %s", worker.pid)
loglevel = use_loglevel
workers = web_concurrency
bind = [ use_bind, use_bind1 ]
keepalive = 1
errorlog = "-"
#hostE = f"{host}:{port1},{host}:{port}"
# For debugging and testing
log_data = {
    "loglevel": loglevel,
    "workers": workers,
    "bind": bind,
    # Additional, non-gunicorn variables
    "workers_per_core": workers_per_core,
    #"host": hostE
}
print(json.dumps(log_data))