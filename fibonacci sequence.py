#python program to print the fibonacci sequence using while loop
#number of terms to display n_terms=int(input("enter thenumber of fibonacci terms to display:"))
#first two terms
a,b=0,1
count=0
#check if the number term is vaild
if n_terms<=0:
    print("pleas enter a positive integer:")
elif n_term==1:
    print("fibonacci sequence:")
    print(a)
else:
    print("fibonacci sequence:")
    while count<n_terms:
     print(a,end="")
     #update values
     a,b=b,a+b
     count+=1
