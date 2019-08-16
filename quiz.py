import sys,os,csv
input_file = r"C:\Users\Hp\Documents\python\RH_Assets_Threats_points_messy_July_2019.csv"
# returns the csv as an object
data1 = csv.reader(open(input_file), delimiter = ',')
# returns the csv as a list of lists where each row
data = list(csv.reader(open(input_file), delimiter = ','))
#Combining multiple operations
newdata = []
for row in data:
     newline = [item.strip() for item in row]
     newline = [item.title() for item in newline]
     newline[2] = newline[2].lower()
     newline[2] = newline[2].capitalize()
       # more things here
     newdata.append(newline)
try:
    infile_name=os.path.splitext(input_file)[0]
    infile_ext=os.path.splitext(input_file)[1]
    #print(infile_name)
    #print(infile_ext )
    outfile=("{}{}{}".format(infile_name,'_cleaned',infile_ext))
    writer=csv.writer(open(outfile,'w'),delimiter=',')

except:
    print("you have a problem with your input_file")

for n in newdata:
   writer.writerow(n)
