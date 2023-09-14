def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mul(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2

dict={"+":add,"-":sub,"*":mul,"/":div}
num1=int(input("enter first number"))
ans=0
while ans is not True:
  symbol=input("enter the symbol from the above mentioned operators:")
  num2=int(input("enter second number"))
  for operators in  dict:
     print(operators)
  caluculate=dict[symbol]
  answer = caluculate(num1,num2)
  print(f"Answer is {answer}")
  user=input("enter y to continue or any other to stop")
  if user=="y":
      num1=answer
      ans=False
  else:
      ans=True
      print(f"loop ended")