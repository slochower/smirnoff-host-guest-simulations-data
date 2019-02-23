import os
from glob import glob

systems = sorted(glob("systems/*"))
with open(".gitignore", "a") as file:
    for system in systems:
        gitignore_lines = f"""
!{system}/smirnoff/*.mol2
!{system}/smirnoff/smirnoff.prmtop
!{system}/smirnoff/smirnoff.inpcrd

!{system}/bgbg-tip3p/full.crds
!{system}/bgbg-tip3p/full.crds

!{system}/bgbg-tip3p/full.crds
!{system}/bgbg-tip3p/full.crds
        """
        file.write(gitignore_lines)