import csv
import matplotlib.pyplot as plt

reader = csv.DictReader(open('RF.csv'))
result = {}
for row in reader:
    for column, value in row.iteritems():
        result.setdefault(column, []).append(value)

#=======2015========        
plt.figure(1)
plt.subplot(211)
plt.plot(result['No. of Papers'],result['2015_Probability'],"-o")
plt.ylabel("Probability(x)")
plt.title("2015 Probablity distribution", loc='center')
plt.grid()

plt.subplot(212)
plt.plot(result['No. of Papers'], result['2015_CumulativeProbability'],"o")
plt.ylim(0, 1.1)
plt.xlabel("x=No.of Papers")
plt.ylabel("Probability(x)")
plt.title("2015 CDF", loc='center')
plt.grid()
plt.show()
#=======2014=========
plt.figure(2)
plt.subplot(211)
plt.plot(result['No. of Papers'], result['2014_Probability'],"-o")
plt.ylabel("Probability(x)")
plt.title("2014 Probability distribution", loc='center')
plt.grid()

plt.subplot(212)
plt.plot(result['No. of Papers'], result['2014_CumulativeProbability'],"o")
plt.ylim(0, 1.1)
plt.xlabel("x=No.of Papers")
plt.ylabel("Probability(x)")
plt.title("2014 CDF", loc='center')
plt.grid()
plt.show()
#=======2013==========
plt.figure(3)
plt.subplot(211)
plt.plot(result['No. of Papers'], result['2013_Probability'], "-o")
plt.ylabel("Probability(x)")
plt.title("2013 Probability distribution", loc='center')
plt.grid()

plt.subplot(212)
plt.plot(result['No. of Papers'], result['2013_CumulativeProbability'],"o")
plt.ylim(0, 1.1)
plt.xlabel("x=No.of Papers")
plt.ylabel("Probability(x)")
plt.title("2013 CDF", loc='center')
plt.grid()
plt.show()
#==========2012=========
plt.figure(4)
plt.subplot(211)
plt.plot(result['No. of Papers'], result['2012_Probability'],"-o")
plt.ylabel("Probability(x)")
plt.title("2012 Probability distribution", loc='center')
plt.grid()

plt.subplot(212)
plt.plot(result['No. of Papers'], result['2012_CumulativeProbability'], "o")
plt.ylim(0, 1.1)
plt.xlabel("x=No.of Papers")
plt.ylabel("Probability(x)")
plt.title("2012 CDF", loc='center')
plt.grid()
plt.show()
#=========2011===========
plt.figure(5)
plt.subplot(211)
plt.plot(result['No. of Papers'], result['2011_Probability'], "-o")
plt.ylabel("Probability(x)")
plt.title("2011 Probability distribution", loc='center')
plt.grid()

plt.subplot(212)
plt.plot(result['No. of Papers'], result['2011_CumulativeProbability'],"o")
plt.ylim(0, 1.1)
plt.xlabel("x=No.of Papers")
plt.ylabel("Probability(x)")
plt.title("2011 CDF", loc='center')
plt.grid()
plt.show()











