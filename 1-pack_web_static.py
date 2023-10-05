#!/usr/bin/python3
# generates a .tgz archive from the contents of the web_static folder

from fabric.api import local
from datetime import datetime


def do_pack():
    time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    name = "versions/web_static_{}.tgz".format(time)
    version = local("mkdir -p versions")
    tagz = local(f"tar -cvzf {name} web_static")
    if tagz.failed:
        return None
    return tagz
