from openforcefield.utils import *
from openforcefield.typing.engines.smirnoff.forcefield import *
from openforcefield.topology import Topology
from openeye.oechem import (
    oemolistream, oemolostream, OEIFlavor_MOL2_Forcefield,
    OEIFlavor_Generic_Default, OEIFlavor_PDB_Default, OEIFlavor_PDB_ALL,
    OEFormat_MOL2, OEFormat_MOL2H, OEWriteMolecule, OETriposAtomNames, OEMol,
    OEFormat_PDB, OESmilesToMol, OEAddExplicitHydrogens, OEHasAtomIdx,
    OEAtomGetResidue)

ifs = oemolistream()
molecules = []

ifs.open("../../systems/a-bam-p/smirnoff/a000/MGO-sybyl.mol2")

for mol in ifs.GetOEMols():
    molecules.append(OEMol(mol))

topology = Topology.from_openeye(molecules[0])

ff = ForceField('forcefield/smirnoff99Frosst.offxml')

system = ff.create_system(topology, molecueles, 
	nonbondedCutoff=1.1 * unit.nanometer,
	ewaldErrorTolerance = 1e-4)
# Then test to see if ff.forces works.


labels = ff.label_molecules(molecules, verbose = True )
print(labels)