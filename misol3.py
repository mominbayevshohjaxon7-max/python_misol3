# # 11-misol
n = int(input("n ni kiriting: "))
s = n*(n+1)/2
print("mana savol javobi: ",s)

# 12-misol
m = int(input("massani kiriting: "))
g = 9.8
j = m*g
print("mana savol javobi: ",j)
 
# 13-misol
m = int(input('massani kiriting: '))
a = int("tezlikni kiriting: ")
f = m*a 
print("mana savol javobi: ",f )

# 14-misol
u = int(input('kuchlanishni kiriting: ')) 
r = int(input('qarshilikni kiriting: '))
i = u/r
print("mana savol javobi: ",i)

# 15-misol
r1 = int(input("R1 ni kiriting: "))
r2 = int(input("R2 ni kiriting: "))
r3 = int(input("R3 ni kiriting: "))
ru = 1/( 1/r1 + 1/r2 + 1/r3)
print("javob: ",ru)

#16-misol
import math
x = float(input())
y = float(input())
c1 = (x + y) / (y*y + (y*y + 2) / (x + x*x*x)) + math.e**(y - 2)
print(f"{c1:.2f}")

#17-misol  
import math
x = float(input())
y = float(input())
f1 = (2 * math.tan(x + math.pi/6)) / (1/3 + math.cos(y + x*x)**2) + math.log10(x*x - 2)
print(f"{f1:.2f}")

#18-misol
import math
x = float(input())
y = float(input())
denominator = x + 2/(x*x) + 3/(x*x*x)
numerator = math.atan(x + y) + (5 + x)**2
f2 = (1/denominator + math.e**(x*x - 3*x)) / numerator - math.cos(y*y + x*x/2)**2
print(f"{f2:.2f}")

#19-misol
import math
x = int(input())
y = int(input())
part = x - (x*y) / (x*x/2 - 5)
inside = (x + y)**2 + math.sqrt(abs(y) + 2 - part)
result = math.log(inside + (math.cos(x + y)**2) / math.sqrt(x + y))
print(f"{result:.2f}")

#20-misol
import math
x = float(input())
y = float(input())
y_prime = y
numerator = x*x + 1
denominator = x*x + (x*y_prime + y*y) / (y_prime*y_prime + (y + x*y_prime) / (abs(x*y) + 5))
result = numerator / denominator + 1 / (1 + math.cos(x) + 1 / math.sin(abs(x)))
print(f"{result:.2f}")