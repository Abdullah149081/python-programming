"""
================================================================================
                             OOP CONCEPTS OVERVIEW
================================================================================

1.  CLASS (Blueprint for creating objects)
    └── Constructor (__init__): Initializes an object.

2.  OBJECT (Instance of a class)
    └── Created based on the blueprint (Class).

3.  INHERITANCE (Acquiring properties from a parent class)
    ├── Allows a class to inherit attributes and methods from another class.
    └── Example: A class Student inheriting from Person.

4.  POLYMORPHISM (Same method name, different behaviors)
    └── Methods in different classes can have the same name but behave differently.
    └── Example: A method `view_info()` in both Student and Teacher classes.

5.  ENCAPSULATION (Hiding internal data using private/protected members)
    ├── Protects data from outside access by making attributes private.
    └── Uses getters and setters for controlled access.

6.  ABSTRACTION (Hiding complex implementation details)
    └── Using abstract classes or interfaces to provide a simple interface for users.

7.  METHOD OVERRIDING (Redefining a method in a derived class)
    └── A derived class can override a method from its parent class.

8.  METHOD OVERLOADING (Simulating multiple methods with the same name)
    └── Python doesn't support true overloading, but it simulates it using default or variable arguments.

9.  STATIC METHOD (Doesn't depend on class/instance data)
    └── A utility function within a class that doesn't access instance data.

10. CLASS METHOD (Operates on the class, not instance)
    └── A method that takes the class itself as the first argument.

11. COMPOSITION (Using objects of one class inside another)
    └── Example: A class Management containing multiple Student and Teacher objects.

12. DECORATORS (Functions modifying behavior of other functions)
    └── A function that wraps another function to modify its behavior.
    └── Example: `@log_action` to log method calls.

13. GETTER/SETTER (Accessing and modifying private attributes)
    └── Using special methods to get or set private attributes.
    └── Example: `get_name()` and `set_name()`.

14. MULTIPLE INHERITANCE (A class can inherit from multiple parent classes)
    └── Combines attributes and behaviors of multiple parent classes.
    └── Example: Class Student can inherit from both Person and PartTimeJob classes.

15. SUPER() FUNCTION (Calling methods from the parent class)
    └── Used to call a method from the parent class within a subclass.

16. LAZY INITIALIZATION (Delaying object creation to optimize resource usage)
    └── Delaying the creation of an object until it is actually needed.

17. MIXIN CLASS (Adding specific functionality to other classes)
    └── A class that adds specific methods without being the primary parent class.

18. DUCK TYPING (Object type determined by behavior, not class)
    └── "If it looks like a duck, quacks like a duck, it must be a duck."

19. METHOD RESOLUTION ORDER (MRO) (Order in which methods are looked up in a class hierarchy)
    └── Determines the search order for methods in case of multiple inheritance.

20. INTERFACE (Simulated through abstract base classes)
    └── Defines methods that must be implemented in subclasses.
    └── Example: Abstract classes with abstract methods.

21. ABSTRACT BASE CLASS (ABC) (Defines abstract methods to be implemented in subclasses)
    └── Cannot instantiate; used as a blueprint for other classes.
    └── Example: `ABC` from `abc` module.

22. GARBAGE COLLECTION (Automatic memory management in Python)
    └── Python's automatic process to clean up memory by removing unused objects.

23. OBJECT CLONING (Creating a copy of an object)
    └── Done using `copy` module or custom methods to clone objects.

24. EVENT-DRIVEN PROGRAMMING (Program flow driven by events such as user actions)
    └── Events like clicks or messages trigger program flow.

================================================================================
                            RELATIONSHIPS BETWEEN CONCEPTS
================================================================================

- INHERITANCE & POLYMORPHISM:
    └── Inheritance allows methods to be overridden in subclasses, enabling polymorphism.

- ENCAPSULATION & ABSTRACTION:
    └── Abstraction hides the complex details, and encapsulation hides the data.

- METHOD OVERRIDING & SUPER() FUNCTION:
    └── Super() allows a child class to call a parent method, which is overridden.

- COMPOSITION & MULTIPLE INHERITANCE:
    └── Composition is when one class uses instances of another class; multiple inheritance combines classes.

- LAZY INITIALIZATION & GARBAGE COLLECTION:
    └── Lazy initialization optimizes resource use, while garbage collection frees unused resources.

- ABSTRACT BASE CLASS (ABC) & INTERFACE:
    └── ABC defines abstract methods for a blueprint; interfaces (via ABC) enforce method implementation.

- STATIC METHOD & CLASS METHOD:
    └── Both methods belong to the class, but static methods don't require access to the class or instance data.
    
================================================================================
"""