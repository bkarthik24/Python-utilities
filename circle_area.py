class Area: 
    def __init__(self):
        self.r = 0
    def area_of_circle(self,r):
        return 3.14 * pow(r,2)
radius = int(input("Enter the radius of the circle: "))
c1= Area() 
print(c1.area_of_circle(radius))