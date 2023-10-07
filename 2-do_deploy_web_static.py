#!/usr/bin/python3
"""distributes an archive to your web servers, using the function do_deploy
"""
import os
from fabric.api import *

env.hosts = ['18.234.105.144', '54.165.39.106']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """distributes an archive to your web servers"""

    # check if path exists
    if not os.path.exists(archive_path) is False:
        return False
    name = archive_path.split('/')
    f_name = name[-1].split('.')

    # define variables
    path = f'/data/web_static/releases/{f_name[0]}/'
    f_file = f'/data/web_static/releases/{f_name[0]}/web_static/*'
    final_path = '/data/web_static/releases/{f_name[0]}/'
    r_file = '/data/web_static/releases/{f_name[0]}/web_static'

    # uploading all file
    upload = put(archive_path, '/tmp/')
    if upload.failed:
        return False

    if run(f'mkdir -p /data/web_static/releases/{f_name[0]}/').failed is True:
        return False

    # extract all files to the folder
    if run(f'tar -xzf /tmp/{f_name[0]}.tgz -C {path}').failed is True:
        return False

    # delete arhcive
    if run('rm -rf /tmp/{f_name[0]}.tgz').failed is True:
        return False

    # mv file
    if run(f'mv {f_file} {final_path}').failed is True:
        return False

    rem_r_file = sudo(f'rm -rf {r_file}')
    if rem_r_file.failed:
        return False
    # delete symbolic link

    removelink = sudo('rm -rf /data/web_static/current')
    if removelink.failed:
        return False

    # create new the symbolic link /data/web_static/current
    new_link = sudo(f'ln -sf {final_path} /data/web_static/current')
    if new_link.failed:
        return False

    return True
