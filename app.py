def fibonaci_series():
    a=0
    b=1
    print("Give the term number")
    n= int(input())
    print(a, b, end=" ")
    while(n):
        c=b
        b=a+b
        print(b, end=" ")
        a=c
        n-=1
        
if __name__=="__main__":
    fibonaci_series()