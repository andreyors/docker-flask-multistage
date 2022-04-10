# Server mechanics
bind = '0.0.0.0:5000'
backlog = 2048
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None
proc_name = None

errorlog = '-'
loglevel = 'info'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
workers = 1
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2

spew = False
reload = True


def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)


def pre_fork(server, worker):
    pass


def pre_exec(server):
    server.log.info("Forked child, re-executing.")


def when_ready(server):
    server.log.info("Server is ready. Spawning workers")


def worker_int(worker):
    worker.log.info("worker received INT or QUIT signal")

    # get traceback info
    import threading, sys, traceback
    id2name = dict([(th.ident, th.name) for th in threading.enumerate()])
    code = []
    for thread_id, stack in sys._current_frames().items():
        code.append(f"\n# Thread: {id2name.get(thread_id, '')} ({thread_id:d})")

        for filename, lineno, name, line in traceback.extract_stack(stack):
            code.append(f'File: "{filename}", line {lineno:d}, in {name}')
            if line:
                code.append(f"{line.strip()}")
    worker.log.debug("\n".join(code))


def worker_abort(worker):
    worker.log.info("worker received SIGABRT signal")
