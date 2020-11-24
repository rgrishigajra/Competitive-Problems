# Enter your code here. Read input from STDIN. Print output to STDOUT
cases = input()
for _ in range(int(cases)):
    ip = input()
    m1,m2 = ip.split(' ')
    n = 0 
    m1 = int(m1)
    m2=int(m2)
    while True:
        if m1 >= m2:
            if m1 - n <0:
                break
            m1-=n
        else:
            if m2 -n<0:
                break
            m2-=n
        n+=1
    print(str(n)+' '+str(m1)+' '+str(m2))