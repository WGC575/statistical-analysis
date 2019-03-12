from scipy.stats import ks_2samp
from readfcol import fcol2list

outputfile = open("KS_result.json", "wt")

file_1 = open("data/distribution_breaker_multi.data", "rt")
file_2 = open("data/distribution_neutral.data", "rt")


dist_1 = fcol2list(file_1)
dist_2 = fcol2list(file_2)

result = ks_2samp(dist_1, dist_2)

outputfile.writelines(str(result))
file_1.close()
file_2.close()
outputfile.close()

pass



