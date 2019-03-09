from scipy.stats import wasserstein_distance
from readfcol import fcol2list

outputfile = open("WAS_result.output", "wt")

file_1 = open("data/distribution_breaker_multi.data", "rt")
file_2 = open("data/distribution_neutral.data", "rt")


dist_1 = fcol2list(file_1)
dist_2 = fcol2list(file_2)

result = wasserstein_distance(dist_1, dist_2)

outputfile.writelines(str(result))
outputfile.close()

pass