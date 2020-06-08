import pyrosetta
from tqdm import tqdm

def PackChainsMini(pose):
    # test
    movemap = pyrosetta.MoveMap()
    movemap.set_bb(True)
    nmoves = 10
    kT = 1.0
    smallmover = SmallMover(movemap, nmoves, kT)
    smallmover.apply(pose)

def PackSideChainsSimple(pose):
    # takes ages
    print('\x1b[31m') #red
    print('Packing side chains')
    task_pack = pyrosetta.standard_packer_task(pose)
    task_pack.or_include_current(True)  # considers the original sidechains
    sfxn = pyrosetta.pyrosetta.get_fa_scorefxn()
    pack_mover =  pyrosetta.rosetta.protocols.minimization_packing.PackRotamersMover(sfxn, task_pack)
    pack_mover.apply(pose)

def BackrubMinimise(pose):
    backrub = pyrosetta.rosetta.protocols.backrub.BackrubMover()
    minimize = pyrosetta.rosetta.protocols.minimization_packing.MinMover()
    print('\x1b[31m')
    print('Backrub + minimise')
    for i in tqdm(range(100)):
        backrub.apply(pose)
        minimize.apply(pose)
