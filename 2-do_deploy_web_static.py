#!/usr/bin/python3
"""distributes an archive to your web servers, using the function do_deploy
"""
import os
from fabric.api import *

env.hosts = ['18.234.105.144', '54.165.39.106']
env.user = 'ubuntu'

# define variables
path = '/data/web_static/releases/web_static_20231005220524/'
f_file = '/data/web_static/releases/web_static_20231005220524/web_static/*'
final_path = '/data/web_static/releases/web_static_20231005220524/'
r_file = '/data/web_static/releases/web_static_20231005220524/web_static'


def do_deploy(archive_path):
    """distributes an archive to your web servers"""

    # check if path exists
    if not os.path.exists(archive_path):
        return False

    # uploading all file
    upload = put(archive_path, '/tmp/')
    if upload.failed:
        return False

    new = run('mkdir -p /data/web_static/releases/web_static_20231005220524/')
    if new.failed:
        return False

    # extract all files to the folder
    extract = run(f'tar -xzf /tmp/web_static_20231005220524.tgz -C {path}')
    if extract.failed:
        return False

    # mv file
    mv_file = run(f'mv {f_file} {final_path}')
    if mv_file.failed:
        return False

    # delete arhcive
    rem = run('rm -rf /tmp/web_static_20231005220524.tgz')
    if rem.failed:
        return False
    rem_r_file = run(f'rm -rf {r_file}')
    if rem_r_file.failed:
        return False
    # delete symbolic link

    removelink = run('rm -rf /data/web_static/current')
    if removelink.failed:
        return False

    # create new the symbolic link /data/web_static/current
    new_link = run(f'ln -sf {final_path} /data/web_static/current')
    if new_link.failed:
        return False

    return True
