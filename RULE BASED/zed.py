
import re
count =0
with open('fuck.txt') as fuck:
    for line in fuck:
        if re.search('\n$',line):
            line = line[0:len(line)-1]
        line = line.split(' ')
        
        if line[len(line)-2] != "NE":
            count +=1
        print(str(line)+ "//"+str(len(line)))

print("ggggg :"+str(count))
'''
what            what 
we              should
have            be

1 NE              NG  -> add words from NG comments to neg files
2 NE              PO  -> add words from PO comments to pos files

3 NG              NE  -> delete words from NE comments in neg files
4 NG              PO  -> delete words from PO comments in neg files

5 PO              NE  -> delete words from NE comments in pos files
6 PO              NG  -> delete words from NG comments in pos files

-> add words in neg and pos files only if they dont belong to NE comments 

3 tiers for pos and neg 


'''
