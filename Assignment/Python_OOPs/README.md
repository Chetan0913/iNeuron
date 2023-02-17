Q1. What is the purpose of Python's OOP?
In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming. It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming. The main concept of OOPs is to bind the data and the functions that work on that together as a single unit so that no other part of the code can access this data.


Q2. Where does an inheritance search look for an attribute?
An inheritance search looks for an attribute first in the instance object, then in the class the instance was created from, then in all higher superclasses, progressing from left to right (by default). The search stops at the first place the attribute is found.


Q3. How do you distinguish between a class object and an instance object?
Object is an instance of a class. Class is a blueprint or template from which objects are created. Object is a real world entity such as pen, laptop, mobile, bed, keyboard, mouse, chair etc. Class is a group of similar objects.
class object is like a blueprint for intance object but instance object is a concrete item in out code.


Q4. What makes the first argument in a class’s method function special?
The calling process is automatic while the receiving process is not (its explicit). This is the reason the first parameter of a function in class must be the object itself. Writing this parameter as self is merely a convention. It is not a keyword and has no special meaning in Python.


Q5. What is the purpose of the init method?
The __init__ method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes. It is also called as constructor


Q6. What is the process for creating a class instance?
We need to give name to class instance and then need to provide the arguments which should matches to the attributes of classes


Q7. What is the process for creating a class?
Class is a blueprint. Need to initialize the class with init method (If we need to pass values to class) and add attributes which will also contain 'self'. self uses as a referance for the instance.


Q8. How would you define the superclasses of a class?
A superclass is the class from which many subclasses can be created. The subclasses inherit the characteristics of a superclass. The superclass is also known as the parent class or base class.


Q9. What is the relationship between classes and modules?
When we create a python program, the program may contain inside it functions, variables, and even classes.If we want to reuse the same piece of function code or the same class, rewriting it would make our code redundant and repetitive. Instead, we can import that entire file as a module into another program.


Q10. How do you make instances and classes?
To create instances of a class, you call the class using class name and pass in whatever arguments its __init__ method accepts.


Q11. Where and how should be class attributes created?
Class attributes are the variables defined directly in the class that are shared by all objects of the class.


Q12. Where and how are instance attributes created?
Instance attributes are attributes or properties attached to an instance of a class. Instance attributes are defined in the constructor.


Q13. What does the term "self" in a Python class mean?
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
It is not any keyword in python, we can use our names insted of 'self'


Q14. How does a Python class handle operator overloading?
The operator overloading in Python means provide extended meaning beyond their predefined operational meaning. Such as, we use the "+" operator for adding two integers as well as joining two strings or merging two lists. We can achieve this as the "+" operator is overloaded by the "int" class and "str" class.


Q15. When do you consider allowing operator overloading of your classes?
when user need to define data type with the special meaning of a operator. then we need to use operator overloading.


Q16. What is the most popular form of operator overloading?
A very popular and convenient example is the Addition (+) operator


Q17. What are the two most important concepts to grasp in order to comprehend Python OOP code?
Both inheritance and polymorphism are fundamental concepts of object oriented programming. These concepts help us to create code that can be extended and easily maintainable.


Q18. Describe three applications for exception processing.
1. exception processing wont stop the program processing
2. exception processing help to raise user define exception
3. exception processing can add exception from super class 'Exception' or from many other sub class of exception


Q19. What happens if you don't do something extra to treat an exception?
if program got unexpected input while running the code, it will create an exception and program stop working.
If we need to handle that exception, then we need to use exception handling in code. So program can handle it and continue further.


Q20. What are your options for recovering from an exception in your script?
can use try and except block to handle the exception


Q21. Describe two methods for triggering exceptions in your script.
print(5/a) -- if user provided zero as input(a) then it will trigger an exception
print(5 + a) -- here 5 is an int and a is string. Here program will trigger an exception


Q22. Identify two methods for specifying actions to be executed at termination time, regardless of whether or not an exception exists.
I could not understand this question. kindly add a note on it while evaluating this


Q23. What is the purpose of the try statement?
The try statement allows you to define a block of code to be tested for errors while it is being executed.


Q24. What are the two most popular try statement variations?
try, except and try,except,else


Q25. What is the purpose of the raise statement?
The raise keyword is used to raise an exception. You can define what kind of error to raise, and the text to print to the user.


Q26. What does the assert statement do, and what other statement is it like?
The assert keyword is used when debugging code.The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.


Q27. What is the purpose of the with/as argument, and what other statement is it like?
In Python, with statement is used in exception handling to make the code cleaner and much more readable. It simplifies the management of common resources like file streams.


Q28. What are *args, **kwargs?
The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-key worded, variable-length argument list. 
The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star.


Q29. How can I pass optional or keyword parameters from one function to another?
To pass, collect the arguments using the * and ** in the function’s parameter list. Through this, you will get the positional arguments as a tuple and the keyword arguments as a dictionary. Pass these arguments when calling another function by using * and **


Q30. What are Lambda Functions?
A lambda function is a small anonymous function. This function can take any number of arguments, but can only have one expression.
syntax -lambda arguments : expression
ex - x = lambda a : a + 10
	print(x(5))

Q31. Explain Inheritance in Python with an example?
Inheritance is one of the imp concept in OOPs. Inheritance allow uses to inherits attributes/methods from parent/superclass
There are different type of inheritance -- single level, multilevel, multiple, hybrid etc
see below ex -
class abc:
	def process(self):
		print("class abc executed successfully")

class xyz(abc):
	pass

x = xyz()
x.process()

In above example xyz is subclass and abc is superclass. But when we created a object of xyz, then it can also access process class.


Q32. Suppose class C inherits from classes A and B as class C(A,B).Classes A and B both have their own versions of method func(). If we call func() from an object of class C, which version gets invoked?
if we are using c(A,B) and both have same name function then object of class c will inherite funtion from class A.


Q33. Which methods/functions do we use to determine the type of instance and inheritance?
The isinstance() method checks whether an object is an instance of a class whereas issubclass() method asks whether one class is a subclass of another class.


Q34.Explain the use of the 'nonlocal' keyword in Python.
The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.
Use the keyword nonlocal to declare that the variable is not local.

Q35. What is the global keyword?
The global keyword is used to create global variables from a no-global scope, e.g. inside a function.
