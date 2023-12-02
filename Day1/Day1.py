import re
#part1
def CreateNumber(line):

    x = re.findall("\d", line)
    try:
        return int(x[0]+x[-1])
    except IndexError:
        return 0
with open("input.txt","r") as File:
    lines= (File.readlines())
    Total=0
    for i in lines:
        #print(CreateNumber(i))
        Total += CreateNumber(i)

    print(Total)

#part 2
numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
def convertLine(line):
    numberlist = (re.findall('\d|zero|one|two|three|four|five|six|seven|eight|nine',line))
    Output = []
    for number in numberlist:
        try:
            number = int(number)
            Output.append(number)

        except ValueError:
            for i in numbers:
                if number == i:
                    number = numbers.index(i)
                    Output.append(number)
                    break
    return Output

total = 0
for i in lines:
    #
    print(convertLine(i))
    total+= int(str(convertLine(i)[0])+str(convertLine(i)[-1]))
print(total)


#print(Total)
