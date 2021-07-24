input_lst =input().split(',')
res_str=[]
chars_lst=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def get_rank(string):
    rank=0
    for char in string:
        if char !='"':
            indx=chars_lst.index(char)
            rank+=indx
    return rank+len(string)
for i in range(len(input_lst)):
    temp_lst=[input_lst[i]]
    r1=get_rank(input_lst[i])
    for j in range(i+1,len(input_lst)):
        r2=get_rank(input_lst[j])
        if r1==r2:
            temp_lst+=[input_lst[j]]
    if len(temp_lst)>1:
        res_str+=[temp_lst]
print(res_str)