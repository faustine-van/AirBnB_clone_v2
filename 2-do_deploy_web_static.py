#!/usr/bin/env bash
"""distributes an archive to your web servers, using the function do_deploy
"""
from os import os.path
from fabric.api import *

env.hosts = ['316762-web-01', '316762-web-02']
env.user = 'ubuntu'


def def do_deploy(archive_path):
    """distributes an archive to your web servers"""

    if not exists(archive_path):
        return False
    put(archive_path, '/tmp/')
    run('mkdir -p /data/web_static/releases/web_static_20231005220524/')

    # extract all files to the folder
    path = '/data/web_static/releases/web_static_20231005220524/'
    run(f'tar -xzf /tmp/web_static_20231005220524.tgz -C {path}')

    f_file = '/data/web_static/releases/web_static_20231005220524/web_static/*'
    final_path = '/data/web_static/releases/web_static_20231005220524/'
    run(f'mv {f_file} {final_path}')
    # delete arhcive
    run('rm -rf /tmp/web_static_20231005220524.tgz')
    r_file = '/data/web_static/releases/web_static_20170315003959/web_static'
    run(f'rm -rf {r_file}')
    # delete symbolic link
    run('rm -rf /data/web_static/current')
    # create new the symbolic link /data/web_static/current
    run(f'ln -sf {final_path} /data/web_static/current')
