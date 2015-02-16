import pylab

principal = 10000 # 初期投資額
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal * interestRate

pylab.plot(values)
#pylab.plot(values, 'ro') # red o
#pylab.plot(values, linewidth=30)

pylab.title('5% Growth, Compound Annually')
#pylab.title('5% Growth, Compound Annually', fontsize='xx-large')
pylab.xlabel('Years of Compound')
#pylab.xlabel('Years of Compound', fontsize='x-small')
pylab.ylabel('Value of Principal ($)')
pylab.show()
