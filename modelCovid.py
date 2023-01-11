from modeller import *
from modeller.automodel import *    # Load the AutoModel class

log.verbose()
env = Environ()

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

class MyModel(AutoModel):
    def select_atoms(self):
        return Selection(self.residue_range('304:A', '306:A'))

a = MyModel(env, alnfile = 'alignment.ali',
            knowns = '5r84', sequence = '5r84_fill')
a.starting_model= 1
a.ending_model  = 2

a.make()