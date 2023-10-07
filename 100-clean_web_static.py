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

    # Define versions for local and releases on the remote server
    l_archives = sorted(listdir('versions'))
    r_archives = sorted(listdir('/data/web_static/releases'))

    archives_to_keep = num

    # delete locally
    with cd(lpath):
        for archive in l_archives[:-archives_to_keep]:
            local('rm -rf {}'.format(archive))

    # delete remotely
    with cd(rpath):
        for archive in r_archives[:-archives_to_keep]:
            run('rm -rf {}'.format(archive))
