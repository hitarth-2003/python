#grade program
'''per=int(input("ënter the percentage here."))
if per >90:
    print("you got A grade..")
if per >=70 and per <=90:
    print("you got B grade..")
if per >=50 and per <=70:
    print("you got C grade..")
if per >= 40 and per < 50:
    print("you got a supplementry..")
if per < 40:
    print("you are failed..")'''

#tax program 50000=>0%,500000=>7%,1300000=>13%,1400000=>18%,1500000=>23%
tax=0
ain=int(input("enter your anual salary amount here:"))
if ain >1500000 :
    print(23/100*ain)
if ain >1000000 and ain <=1500000:
    print(18/100*ain)
if ain > 500000 and ain<=1000000:
    print(10/100*ain)
if ain > 100000 and ain <=500000:
    print(3/100*ain)
if ain < 100000:
    print("No Tax applied on your income.")

