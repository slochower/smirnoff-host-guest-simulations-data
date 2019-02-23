import os
from glob import glob

systems = sorted(glob("systems/*"))
for system in systems:
    with open(os.path.join(system, ".gitignore"), "w") as file:
        gitignore_lines = f"""
/*
!smirnoff/
smirnoff/*
!smirnoff/*.mol2
!smirnoff/smirnoff.prmtop
!smirnoff/smirnoff.inpcrd

!bgbg-tip3p/
bgbg-tip3p/*
!bgbg-tip3p/full.crds
!bgbg-tip3p/full.crds

!bg2bg2-tip3p/
bg2bg2-tip3p/*
!bg2bg2-tip3p/full.crds
!bg2bg2-tip3p/full.crds
        """
        file.write(gitignore_lines)