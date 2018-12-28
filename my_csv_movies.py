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
my_list = [["Top Gun", "Risky Business", "Minority Report"],
           ["Titanic", "The Revenant", "Inception"],
           ["Training Day", "Man on Fire", "Flight"]]
with open("movies.csv","w") as f:
    write = csv.writer(f)
    for movies in my_list:
        write.writerow(movies)
        
