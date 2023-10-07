#!/usr/bin/python3
"""deletes out-of-date archives, using the function do_clean
"""
from os.path import exists
from fabric.api import run, local, env

env.hosts = ['18.234.105.144', '54.165.39.106']


def do_clean(number=0):
    """deletes out-of-date archives
        args:
          - number: number of the archives, including the most recent, to keep.
    """
    if number < 2:
        return  # Nothing to clean if keeping 0 or 1 archive

    # Define paths for versions for local and releases on the remote server
    lpath = 'versions'
    rpath = '/data/web_static/releases'

    if env.local_run:
        # Clean locally in the "versions" directory
        local("cd {} && ls -1tr | head -n -{} | xargs -d '\n' rm -f --".format(
            lpath, number))
    else:
        run("cd {} && ls -1tr | head -n -{} | xargs -d '\n' rm -f --".format(
            rpath, number))
