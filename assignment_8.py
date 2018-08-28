#Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
print("\nSolution 1\n")
class circle:
    def __init__(self):
        self.rad=0
    def getArea(self,rad):
        area= 3.14*rad*rad
        print("Area is :- ",area)
    def getCircumference(self,rad):
        cir=2*3.14*rad
        print("Circumference is :- ",cir)        
rad=int(input("Enter Radius :-"))
c1=circle()
c1.getArea(rad)
c1.getCircumference(rad)

#Q.2- Create a Student class and initialize it with name and roll number. Make methods to :  1. Display - It should display all informations of the student.  2. setAge - It should assign age to student 3. setMarks - It should assign marks to the student.
print("\nSolution 2\n")
class Student:

    def __init__(self , name , rn ):
        self.name = name
        self.rn = rn
    def setAge(self, age):
        self.age=age

    def setMarks(self,marks):
        self.marks=marks
    def display(self):
        print('Name :- %s  \nRollNo :- %d  \nAge :- %d  \nMarks :- %d'%(self.name,self.rn,self.age,self.marks))

s1=Student('ABC' , 1)
s1.setAge(int(input("Enter Age :- ")))
s1.setMarks(int(input("Enter Marks :- ")))
print('\nSTUDENT INFORMATION')
s1.display()

#Q.3- Create a Temprature class and create two methods: 1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.  2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
print("\nSolution 3\n")
class temperature:

    def convertFahrenheit(self, cel):
        fah = (cel * 1.8) + 32
        print('The Temperature in %0.1f Celcius is %0.1f in Fahrenheit' %(cel , fah))
    def convertCelsius(self,fah):
        cel = (fah-32)/1.8
        print('The Temperature in %0.1f Fahrenheit is %0.1f in Celcius' %(cel , fah))

deg=temperature()

cel=float(input("Enter Temperature in Celcius :- "))
deg.convertFahrenheit(cel)
fah=float(input("Enter Temperature in Fahrenheit :- "))
deg.convertCelsius(fah)

#Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings . Make methods to 1. Display-Display the details. 2. Add- Add the movie details. 

print("\nSolution 4\n")
class MovieDetails:

    def __init__(self , name , year , ratings ):
        self.name=name
        self.year=year
        self.ratings=ratings
    def add(self , details):

        self.details=details

    def display(self):
        print('Artist Name :- %s \nYear of Release :- %d \nRatings :- %0.1f \nDetails :- %s ' %(self.name , self.year , self.ratings , self.details ))

m=MovieDetails('ABC' , 2016 , 9.2 )
m.add('QWERTY')
m.display()


#Q.5- Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.
print("\nSolution 5\n")
class Animal:

    def animal_attribute(self):
        print('The tiger is the largest cat species, most recognizable for its pattern of dark vertical stripes on reddish-orange fur with a lighter underside\n')
class Tiger(Animal):
    pass

t=Tiger()
t.animal_attribute()

#Q.6
print("\nSolution 6\n")
'''OUTPUT WILL BE'''
print('A' , 'B')
print('A' , 'B')
        
#Q.7- Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle and square which inherits shape and access the method Area.
print("\nSolution 7\n")
class shape:
    def method_area(self):
        pass
class rectangle(shape):
    def method_area(self):
        self.l=int(input("Enter The length of rectangle :- "))
        self.b=int(input("Enter the breadth of rectangle :- "))
        self.ar=self.l*self.b
        print('Area of Rectangle is :- ' ,self.ar)
class square(shape):
    def method_area(self):
        self.l=int(input("Enter The length :- "))
        self.ar=self.l*self.l
        print('Area of Square is :- ' ,self.ar)
        
sq=square()
rect=rectangle()
sq.method_area()
rect.method_area()

        
        



        

        
