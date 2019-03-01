from squaad import stats
from squaad import file

stats=stats()

data_addtion = {"<10":      {True:218,  False:59},
                ">=10":     {True:227,  False:103},
                ">=100":    {True:118,  False:94},
                ">=500":    {True:17,   False:38}, 
                ">=1000":   {True:20,   False:32} 
}

data_deletion = {"<10":      {True:336,  False:97},
                ">=10":     {True:187,  False:121},
                ">=100":    {True:60,  False:64},
                ">=500":    {True:7,   False:26}, 
                ">=1000":   {True:10,   False:18} 
}
results={}

results["comp"]=stats.gamesHowellBinomial(data_addtion)
file.saveResultsExcel(results,"addition.xls")
results["comp"]=stats.gamesHowellBinomial(data_deletion)
file.saveResultsExcel(results,"deletion.xls")
