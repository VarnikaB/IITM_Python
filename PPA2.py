'''

Create a Triangle class that accepts three side-lengths of the triangle as a , b and c as
parameters at the time of object creation. Class Triangle should have the following methods:

Is_valid() :- Returns Valid if triangle is valid otherwise returns Invalid .
A triangle is valid when the sum of its two side-length are greater than the third one.
That means the triangle is valid if all three condition are satisfied:
a + b > c
a + c > b
b + c > a

Side_Classification() :- If the triangle is invalid then return Invalid . Otherwise, it returns
the type of triangle according to the sides of the triangle as follows:

Return Equilateral if all sides are of equal length.
Return Isosceles if any two sides are of equal length and third is different.
Return Scalene if all sides are of different lengths.

Angle_Classification() :- If the triangle is invalid then return Invalid . Otherwise, return
type of triangle using Pythagoras theorem.
Assume a <= b <= c . then
If return Acute
If return Right
If return Obtuse

Area() :- If the triangle is invalid then return Invalid . Otherwise, return the area of the
triangle.

'''
class Triangle:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.valid = 1
    def is_valid(self):
        if self.a + self.b + self.c > 2 * max(self.a,self.b, self.c):
            return 'Valid'
        else:
            self.valid = 0
            return 'Invalid'
    def Side_Classification(self):
        if self.valid == 0:
            return 'Invalid'
        if self.a == self.b and self.b == self.c:
            return 'Equilateral'
        if self.a == self.b or self.b == self.c or self.a == self.c:
            return 'Isosceles'
        return 'Scalene'
    def Angle_Classification(self):
        if self.valid == 0:
            return 'Invalid'
        mx = max(self.a,self.b,self.c)
        mn = min(self.a,self.b,self.c)
        sec = self.a + self.b + self.c - mx - mn
        if mn**2 + sec ** 2 > mx**2:
            return 'Acute'
        if mn**2 + sec ** 2 == mx**2: 
            return 'Right'
        if  mn**2 + sec ** 2 < mx**2:
            return 'Obtuse'
    def Area(self):
        if self.valid == 0:
            return 'Invalid'
        s = (self.a + self.b + self.c)/2
        area = s *(s-self.a)*(s-self.b)*(s-self.c)
        area = area ** 0.5
        return area
a=int(input())
b=int(input())
c=int(input())
T=Triangle(a,b,c)
print(T.is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())