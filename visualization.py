from matplotlib import pyplot as plt

#khs 평균(감독)
khs_file = open('khslineup.txt','r')

line = khs_file.readline()

while line != '\n':
    line = khs_file.readline()
line = khs_file.readline()
line = khs_file.readline()
while line != '\n':
    line.strip()
    p = line.split()
    line = khs_file.readline()
line = khs_file.readline()
khs_average = float(line)
khs_file.close()

#kg 평균(개발자)
kg_file = open('kglineup.txt','r')

line = kg_file.readline()

while line != '\n':
    line = kg_file.readline()
line = kg_file.readline()
line = kg_file.readline()
while line != '\n':
    line.strip()
    p = line.split()
    line = kg_file.readline()

line = kg_file.readline()
kg_average = float(line)
kg_file.close()

#kmj 평균(개발자)
kmj_file = open('kmjlineup.txt','r')

line = kmj_file.readline()

while line != '\n':
    line = kmj_file.readline()
line = kmj_file.readline()
line = kmj_file.readline()
while line != '\n':
    line.strip()
    p = line.split()
    line = kmj_file.readline()

line = kmj_file.readline()
kmj_average = float(line)
kmj_file.close()


#시각화 시작
name = ['KHS', 'KG', 'KMJ']
average = [khs_average, kg_average,kmj_average]

xs = [i+0.5 for i, _ in enumerate(name)]
plt.bar(xs, average, color = 'b', width = 0.25)
plt.axis([0,3,6.1,6.2])
plt.ylabel('Average')
plt.title('Manager & Developer Lineup : 10,000,000 Simulation Score Average')
plt.xticks([i + 0.5 for i, _ in enumerate(name)], name)
plt.show()
