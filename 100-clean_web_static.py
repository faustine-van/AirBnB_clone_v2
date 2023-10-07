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
    num = int(number)
    if num < 2:
        num = 1

    # Define paths for versions for local and releases on the remote server
    lpath = 'versions'
    rpath = '/data/web_static/releases'

    archives_to_keep = num

    # delete remotely
    with cd(rpath):
        r_archives = run('ls -tr').split()

        for archive in r_archives[:-archives_to_keep]:
            if "web_static_" in archive:
                run('rm -rf {}'.format(archive))

    # delete locally
    with cd(lpath):
        l_archives = local('ls -tr').split()
        for archive in l_archives[:-archives_to_keep]:
            local('rm -rf {}'.format(archive))
