from squaad import stats
from squaad import file
from readfcol import readData

#Getting data from datafile (column-designed)
col_true = {}
col_false = {}

#reading one column file
datafile = open("data/add_ntl.data", "rt")
col_true = fcol2dict(datafile)
datafile = open("data/add_brk.data", "rt")
col_false = fcol2dict(datafile)

i = 0
data_formatted = {}
size = min(len(col_false), len(col_true))

while i < size:
    data_formatted["Group_" + str(i)] = {}
    data_formatted["Group_" + str(i)][True] = int(col_true[i])
    data_formatted["Group_" + str(i)][False] = int(col_false[i])
    i += 1

#Initiation
stats=stats()
results={}

#debug
print(data_formatted)

#Result assignment
results["output"]=stats.gamesHowellBinomial(data_formatted)

#File output
file.saveResultsExcel(results,"GH_output.xls")
pass