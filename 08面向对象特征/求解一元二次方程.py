import math
    
def main(a,b,c):
    r = b*2 - 4*a*c
    if r < 0:
        return "此一元二次方程无根"
    elif r == 0:
        r1,r2 = ((-b+math.sqrt(r))/(2*a),(-b+math.sqrt(r))/(2*a))
        return "此一元二次方程仅有一个根{}={}".format(r1,r2)
    elif r > 0:
        r1,r2 = ((-b+math.sqrt(r))/(2*a),(-b-math.sqrt(r))/(2*a))
        return "此一元二次方程有两个根{}".format((r1,r2))

a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))
q = main(a,b,c)
print(q)