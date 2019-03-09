from squaad import stats
from squaad import file
from readfcol import readData

#Getting data from datafile (column-designed)
column_1 = {}
column_2 = {}
column_3 = {}

#reading one column file
datafile = open("data/datafile_entry", "rt")
column_1 = fcol2dict(datafile)
datafile = open("data/datafile_true", "rt")
column_2 = fcol2dict(datafile)
datafile = open("data/datafile_false", "rt")
column_3 = fcol2dict(datafile)

i = 0
data_formatted = {}
for i in column_1:
    data_formatted[column_1[i]] = {}
    data_formatted[column_1[i]][True] = int(column_2[i])
    data_formatted[column_1[i]][False] = int(column_3[i])

#Initiation
stats=stats()
results={}


#Added lines of code in commits (True for Neutral commits, False for Breakers)
#data_addtion = {"<10":      {True:218,  False:59},
#                ">=10":     {True:227,  False:103},
#                ">=100":    {True:118,  False:94},
#                ">=500":    {True:17,   False:38}, 
#                ">=1000":   {True:20,   False:32} 
#}
#Deleted lines of code in commits (True for Neutral commits, False for Breakers)
#data_deletion = {"<10":     {True:336,  False:97},
#                ">=10":     {True:187,  False:121},
#                ">=100":    {True:60,   False:64},
#                ">=500":    {True:7,    False:26}, 
#                ">=1000":   {True:10,   False:18} 
#}
#Distribution of commits by taxonomy (True for Neutral commits (multi-tagged), False for Breakers)
#Only non-zero couples are allowed by the package
#The execution of this program on this set of data is time-consuming

#debug
print(data_formatted)

#Result assignment
#results["Addition"]=stats.gamesHowellBinomial(data_addtion)
#results["Deletion"]=stats.gamesHowellBinomial(data_deletion)
results["Taxonomy"]=stats.gamesHowellBinomial(data_formatted)

#File output
file.saveResultsExcel(results,"GH_result.xls")