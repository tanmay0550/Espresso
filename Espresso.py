import copy
on_set = []
off_set = []
val = int(input("enter number of literals "))
val1= int(input("enter number of on_set elements "))

for i in range (0,val1):
    p= int(input("enter minterm of on set "))
    on_set.append(p)

val1= int(input("enter number of off_set elements "))

for i in range (0,val1):
    p= int(input("enter minterm of off set "))
    off_set.append(p)

print("min terms of on set is ",on_set)
print("min terms of on set is ",off_set)
on_set_binary=[]
on_set_positional=[]
off_set_binary=[]
off_set_positional=[]
for x in on_set:
   b = bin(x).replace("0b", "")
   a = b.rjust(val, '0')
   on_set_binary.append(a)
for x in off_set:
   b = bin(x).replace("0b", "")
   a = b.rjust(val, '0')
   off_set_binary.append(a)
#print(off_set_binary)
for i in range(len(on_set_binary)):
    column = []
    for j in range (0,val):
        if on_set_binary[i][j] == '0':
            r= '10'
        elif on_set_binary[i][j] == '1':
            r= '01'
        column.append(r)
    on_set_positional.append(column) 
for i in range(len(off_set_binary)):
     column = []
     for j in range (0,val):
        if off_set_binary[i][j] == '0':
            r= '10'
        elif off_set_binary[i][j] == '1':
            r= '01'
        column.append(r)
     off_set_positional.append(column) 
print("on set is",on_set_positional)
print("off set is",off_set_positional)
print("start")
count=0
done=True
to_remove1=[]
while(done):
    print(on_set_positional[count])
    for i in range(0,val):
        ele= on_set_positional[count][i]
        on_set_positional[count][i] = "11"
        #print(ele)
        #print(temp1[count][i])
        for j in range(len(off_set_binary)):
            flag=0
            #print(off_set_positional[j])
            for k in range(0,val):
                print (on_set_positional[count])
                print(off_set_positional[j][k])
            #print( (temp[0][k] == "10" and off_set_positional[j][k] == "01") or (temp[0][k] == "01" and off_set_positional[j][k] == "10"))
                if( (on_set_positional[count][k] == "10" and off_set_positional[j][k] == "01") or (on_set_positional[count][k] == "01" and off_set_positional[j][k] == "10") ):
                     flag = flag + 1
                print(flag)
            if(flag == 0):
                on_set_positional[count][i] = ele
    print("on set is",on_set_positional)
    new=on_set_positional[count]
    for i in range(len(on_set_positional)):
     if(new != on_set_positional[i] ):
        #print (temp[0])
        #print(on_set_positional[i])
        for j in range(0,val):
            if((new[j] == "10" and on_set_positional[i][j] == "10") or (new[j] == "01" and on_set_positional[i][j] == "01") ):
                #on_set_positional.pop(i)
                to_remove1.append(i)
    print("list is", to_remove1)
    for i in range(len(to_remove1)):
        on_set_positional.pop(to_remove1[i])
    to_remove1.clear()
    print("on set is",on_set_positional)
    count=count+1
    if(count==len(on_set_positional)):
        done=False
m=[]
print("final optimized logic is", on_set_positional)
for i in range(len(on_set_positional)):
    for j in range(0,val):
        if(on_set_positional[i][j]=="11"):
            m.append('x')
        elif(on_set_positional[i][j]=="01"):
            m.append('1')
        elif(on_set_positional[i][j]=="10"):
            m.append('0')
    print(m)
    m.clear()
   
