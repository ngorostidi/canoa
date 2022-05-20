files = []
nprocs = 8

for i in range(0, nprocs):
    files.append('DNNLibrary'+str(i+1)+'.csv')

with open('Library.csv', 'w+') as output:
    for fil in files:
        with open(fil, 'r') as f:
            lines = f.readlines()
            output.writelines(lines)

