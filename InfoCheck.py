#raxmlHPC-PTHREADS-AVX -T 64 -f i -t cluster10003_1rr_1rr_1rr_MIortho1rr.fa.at.aln.best.fas-cln.treefile -z cluster10003_1rr_1rr_1rr_MIortho1rr.fa.at.aln.best.fas-cln.boottrees -m GTRGAMMA -n TC_your_run

import sys,os,subprocess

if len(sys.argv) != 2:
	print((sys.argv[0],"Treefile"))
	sys.exit()

os.system("rm RAxML*")
Tree = sys.argv[1].split(".")[:-1]
TreeString = ".".join(Tree)

cmd = "raxmlHPC-PTHREADS-AVX -T 64 -f i -t " + sys.argv[1] + " -z " + TreeString + ".boottrees -m GTRGAMMA -n " + TreeString
results = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
split_lines = str(results.communicate()[0]).split("\\n")
p_line = TreeString 
for line in split_lines:
	
	check_line = line.split(": ")
	if check_line[0] == "Tree certainty for this tree":
		p_line += "," + check_line[1]
	elif check_line[0] == "Relative tree certainty for this tree":
		p_line += "," + check_line[1]
	elif check_line[0] == "Tree certainty including all conflicting bipartitions (TCA) for this tree":
		p_line += "," + check_line[1]
	elif check_line[0] == "Relative tree certainty including all conflicting bipartitions (TCA) for this tree":
		p_line += "," + check_line[1]

#print(p_line)
cmd = "pxlstr -t " + sys.argv[1]
results = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
split_lines = str(results.communicate()[0]).split("\\n")
for line in split_lines:
	
	check_line = line.split(": ")
	if check_line[0] == "nterminal":
		p_line += "," + check_line[1]
	elif check_line[0] == "treelength":
		p_line += "," + check_line[1]

#Stuff pythia gives
#num_sites: 582
#num_patterns: 230
#num_patterns/num_taxa: 6.39
#num_sites/num_taxa: 16.17
#num_patterns/num_sites: 0.4
#proportion_gaps: 0.06
#proportion_invariant: 0.64
#entropy: 0.19
#bollback: -2387.24
#pattern_entropy: 1318.05
#avg_rfdist_parsimony: 0.58
#proportion_unique_topos_parsimony: 1.0
#The predicted difficulty for MSA cluster9999_1rr_1rr_1rr_1rr_MIortho1rr.fa.at.aln.best.fas-cln is: 0.61
cmd = "pythia -m " + TreeString
results = subprocess.Popen(cmd,shell=True,stderr=subprocess.PIPE)
split_lines = str(results.communicate()[1]).split("\\n")
for line in split_lines:
	
	check_lines = line.split(": ")
	if check_lines[0] == "The predicted difficulty for MSA " + TreeString + " is":
		p_line += "," + check_lines[1]

print(p_line)

