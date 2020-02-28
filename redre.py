with open('roll.txt') as f:
    lines = f.read().splitlines()
print(lines)

for i in lines:
    try:
         open("ece17241a0"+i+".py",'r')
    except:
        file = open("ece17241a04"+i+".py",'w') 
        file.write("#import test")
        file.write("\n")
        file.write("print(\""+i+" empty\")")


file = open("execute.py",'w')
file.write("#import test\n")
for i in lines:
    file.write("try:\n")
    file.write("\timport ece17241a04"+i+".py\n")
    file.write("except:\n")
    file.write("\tprint()\n")
file.close()

import execute

