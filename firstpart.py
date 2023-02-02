filename = 'http_access_log.txt'

#list that includes requests made in the last 6 months
lines = []
count = 0
with open(filename, 'r') as f:
    day = 24
    month = 1
    year = 1994
    for line in f:
        #if line is empty, skip it
        if not line:
            continue

        count += 1
    #stop reading if the line includes '25/Apr/1995'
        if '25/Apr/1995' in line:
            break
        else:
            #add line to list
            lines.append(line.strip())


#create a file and write the list to it
with open('firstpart.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
print(len(lines))
print(count)