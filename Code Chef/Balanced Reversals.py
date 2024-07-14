# Balanced Reversals
for _ in range(int(input())):
    n = int(input())
    st = input()
    c = st.count('1')
    print('0'*(n-c) + '1'*c)
