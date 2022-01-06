import re
def check_A_z(t):
   t= t.lower()
   return t.islower()
    

file2 = open('movie_metada3ta3.txt', 'r') 
lins = file2.readlines()
print("started")
file2.close()

L=[]
for line in lins:
   data = line.split(",")
   if check_A_z(data[5]) or check_A_z(data[6]) or check_A_z(data[7]) :
    continue
   ix=f'movie(moviename({data[0]}),dirctor({data[1]}),actors({data[2]},{data[3]},{data[4]}),numeric({data[5]},{data[6]},{data[7]})).'
   ix=ix.replace(" ", "_")
   ix=ix.lower()
   ix=ix.replace("/", "")
   ix=ix.replace("(,", "(31515310.35,")
   ix=ix.replace(".", "")
   ix = re.sub(r'[^A-Za-z().,0123456789]', '', ix)
   ix=ix.strip()
   ix=ix+".\n"


   
   
   L=L+[ix]
print("Finshed")    



file1 = open('hell4.txt', 'w') 
file1.writelines((L)) 
file1.close()