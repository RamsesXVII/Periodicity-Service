from ResultFetcher import ResultFetcherProxy
from DataAdapter import ResultDataAdapter
from AutocorrelationUtility import AutocorrelationUtility
from PeriodicityCharacterizer import PeriodicityCharacterizer

# resultFetcher=ResultFetcherProxy(2957509,1494233600,1494737600,6270)
# data=resultFetcher.fetchResults()

# dataAdapter=ResultDataAdapter(1494233600,data)
# tracerouteToID,tracerouteIDsequence=dataAdapter.adaptResults()

# print(tracerouteToID)
tracerouteIDsequence=list()
for counter in range(0,144):
	tracerouteIDsequence.append(counter%16)
tracerouteIDsequence.append(1)
tracerouteIDsequence.append(2)
tracerouteIDsequence.append(3)
tracerouteIDsequence.append(4)
tracerouteIDsequence.append(1)
tracerouteIDsequence.append(2)
tracerouteIDsequence.append(3)
tracerouteIDsequence.append(4)
tracerouteIDsequence.append(1)
tracerouteIDsequence.append(2)
tracerouteIDsequence.append(3)
tracerouteIDsequence.append(4)
tracerouteIDsequence.append(1)
tracerouteIDsequence.append(2)
tracerouteIDsequence.append(3)
tracerouteIDsequence.append(4)

#dataAdapter.getGDBdiagram(tracerouteIDsequence)

autocorrelationUtility=AutocorrelationUtility(tracerouteIDsequence)
lagToACFValue=autocorrelationUtility.computeACF() #dictionaru
lagToPeakValues=autocorrelationUtility.getLag2ValuesOfPeaks()
candidatePeriodsToCount=autocorrelationUtility.getPeriods(lagToPeakValues)

periodicityCharacterizer=PeriodicityCharacterizer(candidatePeriodsToCount,tracerouteIDsequence)
patterns=periodicityCharacterizer.getPatterns()
patterns=periodicityCharacterizer.removeDuplicate(patterns)

periodicityToStartAndStop=periodicityCharacterizer.getPeriodicities(patterns,tracerouteIDsequence)

# print(tracerouteIDsequence)
# print(lagToACFValue)
print(lagToPeakValues)
#print(candidatePeriodsToCount)
#print(patterns)
print(periodicityToStartAndStop)