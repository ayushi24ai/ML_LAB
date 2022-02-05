import csv

a = []
with open('finds.csv - finds.csv.csv') as csfile:
     reader = csv.reader(csfile)
     for line in reader:
         a.append(line)
         print(line)
print (a)
num_attributes = len(a[0])-1

print('The most general hypothesis:',['?']*num_attributes)
print('The most specific hypothesis:',['0']*num_attributes)

#Algorithm implementation

hypothesis = a[0][:-1]
print(hypothesis)
print(num_attributes)
print(a[0][num_attributes])
print('\n Find S: Finding a maximally specific hypothesis')
for i in range(len(a)):
    if a[i][num_attributes] == 'Yes':
        for j in range(num_attributes):
            if a[i][j] != hypothesis[j]:
                hypothesis[j]='?'
    print('The training example no:',i+1 ,'The hypothesis is:',hypothesis)
print('\n The maximally specific hypothesisfor training set is')
print(hypothesis)


