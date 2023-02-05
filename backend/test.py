i = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
chunk_size=5
overlap=2
new_list=[]
j=0
while j < len(i):
    j=j+chunk_size+overlap
    new_list.append(j)