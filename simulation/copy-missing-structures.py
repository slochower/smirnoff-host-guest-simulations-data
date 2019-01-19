import os as os
import glob as glob
import shutil

directories = glob.glob("../systems/*/smirnoff/r014")
directories = [i for i in directories if os.path.isdir(i)]

for directory in sorted(directories):
    print(directory)
    try:
        os.symlink("../p045/smirnoff.prmtop", os.path.join(directory,
                                                               "smirnoff.prmtop"))
    except:
    	pass
    try:
    	os.symlink("../p045/smirnoff.inpcrd", os.path.join(directory,
                                                               "smirnoff.inpcrd"))
    except:
    	pass