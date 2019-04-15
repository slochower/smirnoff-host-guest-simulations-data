# Data for setting up host-guest calculations with SMIRNOFF99Frosst using the attach-pull-release method

This repository contains files that help setup and check simulations 

## Introduction

## Testing and caveats

## Manifest
- `geometry/`: Contains structures of alpha- and beta-cyclodextrin minimized with SMIRNOFF99Frosst and GAFF v1.7 and input files, in the `trimer` subdirectory, to run an MM energy scan along dihedral coordinates using three glucose units.
- `setup/`: Python files used to prepare the simulations.
    - `anchor_atoms.py`: Defines a helper function to determine the anchor atoms used to setup the APR calculation, based on the scheme in [Henriksen, et al. (2017)](https://pubs.acs.org/doi/abs/10.1021/acs.jctc.7b00359).
    - `process.py`: An example file converting the system `a-bam-p` from GAFF v1.7 parameters to SMIRNOFF99Frosst parameters. This relies on a local copy of `smirnovert.utils`, which is not currently in this directory -- and so it will not run -- but it is useful for me to keep it here as a historical artifact.
    - `restraints.py`: Defines helper functions to setup APR restraints on cyclodextrins.
    - `setup_restraints.py`: Uses `smirnovert` to convert systems from GAFF v1.7 to SMIRNOFF99Frosst, sets up the restraint scheme using `paprika`, and then writes the AMBER restraint file (`disang.rest`) in each window for each system.
- `simulation/`: Python files used to run and check the completion status of the simulations.
    - `simulate.py`: Main simulation file, intended to be run in each window of each system.
    - `simulate-enthalpy.py`: Adaptation of `simulate.py` to run the end points to 1 us for enthalpy calculations.
    - `link*.py`/`check*.py`/`clean.py`/`run.py`: Utility files to create links and check of the status of the simulations.
- `systems/`: The host-guest complexes considered in this study. To put this on GitHub, I have not included any files from individual APR windows.


## Execution

## Assumptions