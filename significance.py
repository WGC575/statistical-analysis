from squaad import stats
from squaad import file

#Initiation
stats=stats()
results={}


#Added lines of code in commits (True for Neutral commits, False for Breakers)
data_addtion = {"<10":      {True:218,  False:59},
                ">=10":     {True:227,  False:103},
                ">=100":    {True:118,  False:94},
                ">=500":    {True:17,   False:38}, 
                ">=1000":   {True:20,   False:32} 
}
#Deleted lines of code in commits (True for Neutral commits, False for Breakers)
data_deletion = {"<10":     {True:336,  False:97},
                ">=10":     {True:187,  False:121},
                ">=100":    {True:60,   False:64},
                ">=500":    {True:7,    False:26}, 
                ">=1000":   {True:10,   False:18} 
}
#Distribution of commits by taxonomy (True for Neutral commits (multi-tagged), False for Breakers)
#Only non-zero couples are allowed by the package
#The execution of this program on this set of data is time-consuming
data_taxonomy = {"DPD":     {True:6,    False:18},
                "VER":      {True:13,   False:14},
                "DOC":      {True:45,   False:15},
                "TST":      {True:7,    False:5},
                "BRC":      {True:1,    False:3},
                "NFT":      {True:174,  False:121},
                "MOD":      {True:118,  False:58}, 
                "DEL":      {True:23,   False:22},
                "FIX":      {True:157,  False:54},
                "ANT":      {True:16,   False:5},
                "RFT":      {True:22,   False:28},
                "IMP":      {True:8,    False:1}, 
                "RMN":      {True:34,   False:16},
                "CLN":      {True:26,   False:10},
                "CMT":      {True:18,   False:2}
}

#Result assignment
results["Addition"]=stats.gamesHowellBinomial(data_addtion)
results["Deletion"]=stats.gamesHowellBinomial(data_deletion)
results["Taxonomy"]=stats.gamesHowellBinomial(data_taxonomy)

#File output
file.saveResultsExcel(results,"Results.xls")