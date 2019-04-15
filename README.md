# Data for setting up host-guest calculations with SMIRNOFF99Frosst using the attach-pull-release method

This repository contains files that help setup and check simulations 

## Introduction

## Testing and caveats

## Manifest
- `analysis`/: Contains files to compute the free energy of binding and enthalpy of binding after the simulations are completed. Some of the functions written into these files have been incorporated into pAPRika v0.0.4. *N.B.* I moved some of these into the `analysis` subdirectory after running them, and therefore, some paths will need to be updated for re-analysis.
    - `analyze*.py`: Compute binding free energies
    - `enthalpy*.py`: Compute binding enthalpies
    - `parse_mden.py`: Helper function to read energies from AMBER `mden` files
    - `vac.py`: Create trajectories containing only the host and guest for faster postprocessing
- `geometry/`: Contains structures of alpha- and beta-cyclodextrin minimized with SMIRNOFF99Frosst and GAFF v1.7 and input files, in the `trimer` subdirectory, to run an MM energy scan along dihedral coordinates using three glucose units.
- `setup/`: Python files used to prepare the simulations.
    - `anchor_atoms.py`: Defines a helper function to determine the anchor atoms used to setup the APR calculation, based on the scheme in [Henriksen, et al. (2017)](https://pubs.acs.org/doi/abs/10.1021/acs.jctc.7b00359).
    - `process.py`: An example file converting the system `a-bam-p` from GAFF v1.7 parameters to SMIRNOFF99Frosst parameters. This relies on a local copy of `smirnovert.utils`, which is not currently in this directory -- and so it will not run -- but it is useful for me to keep it here as a historical artifact.
    - `release.py`: Setup a single release calculation for each cyclodextrin. This step computes the work of releasing the conformational restraints on the host, in the absence of guest, and therefore only needs to be computed once for each unique host.
    - `restraints.py`: Defines helper functions to setup APR restraints on cyclodextrins.
    - `setup_restraints.py`: Uses `smirnovert` to convert systems from GAFF v1.7 to SMIRNOFF99Frosst, sets up the restraint scheme using `paprika`, and then writes the AMBER restraint file (`disang.rest`) in each window for each system.
- `simulation/`: Python files used to run and check the completion status of the simulations.
    - `simulate.py`: Main simulation file, intended to be run in each window of each system.
    - `simulate-enthalpy.py`: Adaptation of `simulate.py` to run the end points to 1 us for enthalpy calculations.
    - `link*.py`/`check*.py`/`clean.py`/`run.py`: Utility files to create links and check of the status of the simulations.
- `systems/`: The host-guest complexes considered in this study. To put this on GitHub, I have not included any files from individual APR windows. There are `prmtop` files for GAFF v1.7 and GAFF v2.1 simulations. For SMIRNOFF99Frosst, there are individual `mol2` files for the host and guest (in GAFF format and Tripos/SYBYL format) along with initial coordinates and `prmtop` files.


## Execution

## Assumptions