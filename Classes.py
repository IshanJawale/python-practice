class Point:                # to capitalise the first letter; do not use underscore to seperate multiple words, write them together with first letter capitalised like EmailClient
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 35
print(point2.x)
