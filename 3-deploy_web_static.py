#!/usr/bin/python3
"""distributes an archive to your web servers, using the function do_deploy"""

import os
from fabric.api import *

env.hosts = ['18.234.105.144', '54.165.39.106']


@task
def do_pack():
    """ archive all files
    """
    time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    name = "versions/web_static_{}.tgz".format(time)
    version = local("mkdir -p versions")
    tagz = local(f"tar -cvzf {name} web_static")
    if tagz.failed:
        return None
    return tagz


@task
def do_deploy(archive_path):
    """distributes an archive to your web servers
    args:
    archcive_path: file that is archive file

    """

    # check if path exists
    if exists(archive_path) is False:
        return False
    try:
        name = archive_path.split('/')
        f_name = name[-1].split('.')

        # define variables
        path = f'/data/web_static/releases/{f_name[0]}/'
        f_file = f'/data/web_static/releases/{f_name[0]}/web_static/*'
        final_path = '/data/web_static/releases/{f_name[0]}/'
        r_file = '/data/web_static/releases/{f_name[0]}/web_static'

        # uploading all file
        put(archive_path, '/tmp/')
        run(f'mkdir -p /data/web_static/releases/{f_name[0]}/')
        # extract all files to the folder
        run(f'tar -xzf /tmp/{f_name[0]}.tgz -C {path}')
        # delete arhcive
        run('rm -rf /tmp/{f_name[0]}.tgz')
        # mv file
        run(f'mv {f_file} {final_path}')
        run(f'rm -rf {r_file}')
        # delete symbolic link
        run('rm -rf /data/web_static/current')
        # create new the symbolic link /data/web_static/current
        run(f'ln -sf {final_path} /data/web_static/current')
        return True
    except Exception:
        return False


def deploy():
    """archive file and distributes an archive to your web servers
    """
    archive = do_pack()
    if not archive:
        return False
    return do_deploy(archive)
