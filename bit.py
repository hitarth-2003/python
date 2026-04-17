data= input("enter the number here:")
count=0
stuffed_data=""
for bit in data:
    if bit =='1':
     count=count+1
     stuffed_data=stuffed_data+bit
     if bit=='5':
        stuffed_data=stuffed_data + '0'
        count=0
    else:
       stuffed_data+=bit
       count=0
print("stuffed_data",stuffed_data)
