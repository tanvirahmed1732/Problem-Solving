# cook your dish here
for i in range(int(input())):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    # print(len(alp))
    n = int(input())
    s = input()
    s_list = list(s) 
    j = 0
    while j < n - 1:
        s_list[j], s_list[j + 1] = s_list[j + 1], s_list[j]
        j += 2
    for i in range(n):
        ind = alp.index(s_list[i]) + 1
        s_list[i] = alp[-ind]
    modified_s = ''.join(s_list)
    print(modified_s)
    
