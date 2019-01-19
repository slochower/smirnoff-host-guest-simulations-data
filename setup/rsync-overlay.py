import os
import subprocess as sp
from constants import systems

for system in systems:
    source = os.path.join(
        "/data/davids4/projects/smirnoff-host-guest-simulations-data/systems",
        system,
        "smirnoff",
        "r014",
    )
    destination = os.path.join("systems", system, "smirnoff/", "r014")
    if not os.path.isdir(destination):
        print(f"Creating {destination}...")
        os.makedirs(destination)

    rsync_list = [
        "rsync",
        "-armv",
        '-e "ssh"',
        '--include="overlay.pdb"',
        '--exclude="*"',
        "{}".format("davids4@kirkwood:" + source + "/"),
        "{}".format("."),
    ]
    p = sp.Popen([" ".join(rsync_list)], cwd=destination, shell=True)
    output, error = p.communicate()
    if p.returncode == 0:
        pass
    elif p.returncode == 1:
        print("Output: {}".format(output))
        print("Error: {}".format(error))

for system in systems:
    source = os.path.join(
        "/data/davids4/projects/smirnoff-host-guest-simulations-data/systems",
        system,
        "smirnoff",
        "a000",
    )
    destination = os.path.join("systems", system, "smirnoff/", "a000")
    if not os.path.isdir(destination):
        print(f"Creating {destination}...")
        os.makedirs(destination)

    rsync_list = [
        "rsync",
        "-armv",
        '-e "ssh"',
        '--include="overlay.pdb"',
        '--exclude="*"',
        "{}".format("davids4@kirkwood:" + source + "/"),
        "{}".format("."),
    ]
    p = sp.Popen([" ".join(rsync_list)], cwd=destination, shell=True)
    output, error = p.communicate()
    if p.returncode == 0:
        pass
    elif p.returncode == 1:
        print("Output: {}".format(output))
        print("Error: {}".format(error))


for system in systems:
    source = os.path.join(
        "/data/davids4/projects/smirnoff-host-guest-simulations-data/systems",
        system,
        "bgbg-tip3p",
    )
    destination = os.path.join("systems", system, "bgbg-tip3p/")
    if not os.path.isdir(destination):
        print(f"Creating {destination}...")
        os.makedirs(destination)

    rsync_list = [
        "rsync",
        "-armv",
        '-e "ssh"',
        '--include="overlay.pdb"',
        '--exclude="*"',
        "{}".format("davids4@kirkwood:" + source + "/"),
        "{}".format("."),
    ]
    p = sp.Popen([" ".join(rsync_list)], cwd=destination, shell=True)
    output, error = p.communicate()
    if p.returncode == 0:
        pass
    elif p.returncode == 1:
        print("Output: {}".format(output))
        print("Error: {}".format(error))
