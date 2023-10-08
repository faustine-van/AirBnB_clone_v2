#!/usr/bin/python3
# Fabfile to delete out-of-date archives.
import os
from fabric.api import *

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.

    """
    number = 1 if int(number) == 0 else int(number)

    archives1 = sorted(os.listdir("versions"))
    [archives1.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives1]

    with cd("/data/web_static/releases"):
        archives2 = run("ls -tr").split()
        archives2 = [a for a in archives2 if "web_static_" in a]
        [archives2.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives2]
