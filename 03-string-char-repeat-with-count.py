#repeative char count problem
# aabceeetpp = 2abc3et2p

input_str = "aabceeetpp"
input_str = "kkpppeeett"

output_str = ""
count = 1
for i, x in enumerate(input_str): 
    if i == len(input_str)-1: 
        if count > 1:
            output_str += str(count)+ x
        else:
            output_str += x
        count = 1 
    elif x == input_str[i+1]:
        count = count + 1
    else:
        if count >1:
            output_str += str(count)+ x
        else:
            output_str += x
        count = 1
   
    
print(output_str)
