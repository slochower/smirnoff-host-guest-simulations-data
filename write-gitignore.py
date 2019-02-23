import os
from glob import glob

systems = sorted(glob("systems/*"))
with open(".gitignore", "a") as file:
    for system in systems:
        gitignore_lines = f"""
systems/{system}/rsync.log
systems/{system}/smirnoff/*
!systems/{system}/smirnoff/*.mol2
!systems/{system}/smirnoff/smirnoff.prmtop
!systems/{system}/smirnoff/smirnoff.inpcrd

systems/{system}/bgbg-tip3p/*
!systems/{system}/bgbg-tip3p/full.crds
!systems/{system}/bgbg-tip3p/full.crds

systems/{system}/bg2bg2-tip3p/*
!systems/{system}/bgbg-tip3p/full.crds
!systems/{system}/bgbg-tip3p/full.crds
        """
        file.write(gitignore_lines)