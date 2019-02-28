from squaad import stats
from squaad import file
from squaad import db


#myConnection=db("config.json","cache")

stats=stats()

data = {"GROUP1":{True:100, False:3999}, "GROUP2":{True:2999,False:2939}}
results={}

results["comp"]=stats.gamesHowellBinomial(data)

#file.saveResultsExcel(results,"stat.xls")
