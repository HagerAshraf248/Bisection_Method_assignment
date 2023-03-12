import math as math
ea=100
xr_old=0

xl=float(input("Enter the lower: "))
xu=float(input("Enter the upper: "))

while ea>0.001:
     xr=(xl+xu)/2
     fxl=math.pow((math.pow(xl,2)+1),2)-25
     fxr=math.pow((math.pow(xr,2)+1),2)-25

     r3=fxl*fxr

     if r3<0:
       xu=xr
     elif r3>0:
       xl=xr

     if xr_old!=0:
       ea=((xr-xr_old)/xr)*100
       if ea<0:
          ea=ea*-1
       
     xr_old=xr

print("The root: ",xr)
print("The error: ",ea)