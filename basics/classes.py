# A class is a template for a data type. It describes the kinds of information that class will hold and how a programmer
# will interact with that data.

# define an empty class
#  We used the pass keyword in Python to indicate that the body of the class was intentionally left blank so we do not
#  cause an IndentationError.


class Facade:
    pass


# create an instance of the class
facade_1 = Facade()


# A class instance is also called an object.
# Instantiation takes a class and turns it into an object, the type() function does the opposite of that.
# When called with an object, it returns the class that the object is an instance of.
print(type(facade_1))
# <type 'instance'>

########################################################################################################################
# class methods
# Convention recommends that we name this first argument self. Methods always have at least this one argument.
# were able to refer to self in the function body. When you call a method it automatically passes the object calling
# the method as the first argument.


class Rules:
    def washing_brushes(self):
        return "Point bristles towards the basin while washing your brushes."


class Circle:
    pi = 3.14

    def area(self, radius):
        return Circle.pi * radius ** 2


circle = Circle()
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)

########################################################################################################################
# constructor
# __init__ method - This method is used to initialize a newly
# created object. It is called every time the class is instantiated.
# programmers who refer to a constructor in Python are usually talking about the __init__ method.


class Circle:
    pi = 3.14

    # Add constructor here:
    def __init__(self, diameter):
        print("New circle with diameter: {diameter}".format(diameter=diameter))


teaching_table = Circle(36)

########################################################################################################################
# Instance Variables


class Store:
    pass


alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"


########################################################################################################################
# Attribute Functions
# Instance variables and class variables are both accessed similarly in Python. This is no mistake, they are both
# considered attributes of an object. If we attempt to access an attribute that is neither a class variable nor an
# instance variable of the object Python will throw an AttributeError.

# hasattr
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in how_many_s:
    if hasattr(element, "count"):
        print(element.count("s"))

########################################################################################################################
# Attributes can be added to user-defined objects after instantiation, so it is possible for an object to have some
# attributes that are not explicitly defined in an object constructor. We can use the dir() function to investigate an
# object attributes at runtime. dir() is short for directory and offers an organized presentation of object attributes.

print(dir(5))

########################################################################################################################
# __repr__  This is a method we can use to tell Python what we want the string representation of the class to be.
# __repr__ can only have one parameter, self, and must return a string.

class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2

    def area(self):
        return self.pi * self.radius ** 2

    def circumference(self):
        return self.pi * 2 * self.radius

    def __repr__(self):
        return "Circle with radius {radius}".format(radius=self.radius)


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)

########################################################################################################################
# Inheritance
# Sometimes a base class is called a parent class. In these terms, the class inheriting from it, the subclass, is also
# referred to as a child class.


class Bin:
    pass


# RecyclingBin is a subclass of Bin
class RecyclingBin(Bin):
    pass

########################################################################################################################
# Exceptions
# There is one very important family of class definitions built in to the Python language. An Exception is a class that
# inherits from Python Exception class.


print(issubclass(ZeroDivisionError, Exception))
# True


# Define your exception up here:
class OutOfStock(Exception):
    pass


# Update the class below to raise OutOfStock
class CandleShop:
    name = "Here's a Hot Tip: Buy Drip Candles"

    def __init__(self, stock):
        self.stock = stock

    def buy(self, color):
        if self.stock[color] < 1:
            raise OutOfStock
        self.stock[color] = self.stock[color] - 1


candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

# candle_shop.buy('green')

########################################################################################################################
# Overriding Methods


class Message:
    def __init__(self, sender, recipient, text):
        self.sender = sender
        self.recipient = recipient
        self.text = text


class User:
    def __init__(self, username):
        self.username = username

    def edit_message(self, message, new_text):
        if message.sender == self.username:
            message.text = new_text


class Admin(User):
    def edit_message(self, message, new_text):
        message.text = new_text


########################################################################################################################
# super

class PotatoSalad:
    def __init__(self, potatoes, celery, onions):
        self.potatoes = potatoes
        self.celery = celery
        self.onions = onions


class SpecialPotatoSalad(PotatoSalad):
    def __init__(self, potatoes, celery, onions):
        super().__init__(potatoes, celery, onions)
        self.raisins = 40


########################################################################################################################
# Interfaces
# When two classes have the same method names and attributes, we say they implement the same interface.


class InsurancePolicy:
    def __init__(self, price_of_item):
        self.price_of_insured_item = price_of_item


class VehicleInsurance(InsurancePolicy):
    def get_rate(self):
        return self.price_of_insured_item * 0.001


class HomeInsurance(InsurancePolicy):
    def get_rate(self):
        return self.price_of_insured_item * 0.00005


########################################################################################################################
# polymorphism
# Polymorphism is the term used to describe the same syntax (like the + operator here, but it could be a method name)
# doing different actions depending on the type of data.
# defining class hierarchies that all implement the same interface is a way of introducing polymorphism to our code.

a_list = [1, 18, 32, 12]
a_dict = {'value': True}
a_string = "Polymorphism is cool!"

print(len(a_list))
print(len(a_dict))
print(len(a_string))

########################################################################################################################
# Dunder Methods
# One way that we can introduce polymorphism to our class definitions is by using Python special dunder methods. We have
# explored a few already, the constructor __init__ and the string representation method __repr__,
# but that is only scratching the tip of the iceberg.


class Atom:
    def __init__(self, label):
        self.label = label

    def __add__(self, other):
        return Molecule([self, other])


class Molecule:
    def __init__(self, atoms):
        if type(atoms) is list:
            self.atoms = atoms


sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
salt = sodium + chlorine


########################################################################################################################
class SortedList(list):
  def append(self, value):
    super().append(value)
    self.sort()