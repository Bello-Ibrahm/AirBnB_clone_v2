#!/usr/bin/python3
from fabric.api import env, run, lcd, cd, local
from os import listdir

env.hosts = ["54.144.134.116", "54.144.150.121"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_clean(number=0):
    """ Deletes out-of-date archives.

    Args:
        number(int): number of the archives, including the most
        recent, to keep.

    If number is 0 or 1, keep only the most recent version of your archive.
    if number is 2, keep the most recent,
    and second most recent versions of your archive. etc.
    """
    numb = 1 if int(number) == 0 else int(number)

    arc_files = sorted(listdir("versions"))
    [arc_files.pop() for i in range(numb)]

    with lcd("versions"):
        [local("rm ./{}".format(x)) for x in arc_files]

    with cd("/data/web_static/releases"):
        arc_files = run("ls -tr").split()
        arc_files = [x for x in arc_files if "wewb_static_" in x]
        [arc_files.pop() for y in range(numb)]
        [run("rm -rf ./{}".format(x) for x in arc_files)]
