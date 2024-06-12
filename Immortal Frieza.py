# Immortal Frieza

for _ in range(int(input())):

    s=input()

    ss='frieza'

    r=''

    n=len(s)

    t=1

    if s[0] in ss:

        f=True

    else:

        f=False

    for i in range(1,n):

        if s[i] in ss:

            if f:

                t+=1

            else:

                f=True

                r+=str(t)

                t=1

        else:

            if f == False:

                t+=1

            else:

                f=False

                r+=str(t)

                t=1

    print(r+str(t))
