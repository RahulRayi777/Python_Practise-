#Input:   
#Output: [4, 5, 1, 2, 3]  


 
s="interview"
result=[]
for char in s:
    for i in range(len(result)):
        if result[i][0]==char:
            result[i]=(char,result[i][1]+1)
    else:
        result.append((char,1))

print(result)
 
