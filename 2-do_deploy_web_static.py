#!/usr/bin/python3
"""distributes an archive to your web servers, using the function do_deploy"""

from os.path import exists
from fabric.api import run, task, put, env

env.hosts = ['18.234.105.144', '54.165.39.106']


@task
def do_deploy(archive_path):
    """distributes an archive to your web servers"""

    # check if path exists
    if exists(archive_path) is False:
        return False
    try:
        name = archive_path.split('/')
        f_name = name[-1].split('.')

        # define variables
        path = f'/data/web_static/releases/{f_name[0]}/'
        f_file = f'/data/web_static/releases/{f_name[0]}/web_static/*'
        # final_path = '/data/web_static/releases/{f_name[0]}/'
        r_file = '/data/web_static/releases/{f_name[0]}/web_static'

        # uploading all file
        put(archive_path, '/tmp/')
        run(f'mkdir -p /data/web_static/releases/{f_name[0]}/')
        # extract all files to the folder
        run(f'tar -xzf /tmp/{f_name[0]}.tgz -C {path}')
        # delete arhcive
        run(f'rm -rf /tmp/{f_name[0]}.tgz')
        # mv file
        run(f'mv {f_file} /data/web_static/releases/{f_name[0]}/')
        run(f'rm -rf {r_file}')
        # delete symbolic link
        run('rm -rf /data/web_static/current')
        # create new the symbolic link /data/web_static/current
        current = '/data/web_static/current'
        run(f'ln -sf /data/web_static/releases/{f_name[0]}/ {current}')
        return True
    except Exception:
        return False
