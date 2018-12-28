import csv

#csvfile = open("d:/self-taught/st.csv","w")
#csvfile.write=["one","two","three"]
#csvfile.close()
#read_result=csv.reader(csvfile)
#for line in read_result:
#    print(line)
with open("st.csv","w") as f:
    write = csv.writer(f)
    write.writerow(["one","two","three"])
    write.writerow(["four","five","six"])
