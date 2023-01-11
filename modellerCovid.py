from modeller import *
#Get the sequence pdb file and write to an alignment file

code = '5r84'
e = Environ()
m = Model(e, file=code)
aln = alignment(e)
aln.append_model(m, align_codes=code)
aln.write(file=code+'.seq')

