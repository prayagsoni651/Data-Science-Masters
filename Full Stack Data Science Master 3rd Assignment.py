#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Why are functions advantageous to have in your programs?

"""Code organization and reusability: Functions allow you to break down your program into smaller, modular pieces of code. By dividing your code into logical functions, you can improve code organization, readability, and maintainability. Functions also promote code reuse since you can call a function multiple times from different parts of your program.

Abstraction and encapsulation: Functions allow you to abstract away complex operations or algorithms behind a simple interface. By encapsulating a set of instructions within a function, you can hide the implementation details and provide a higher-level abstraction. This makes it easier to understand and use the functionality without worrying about the underlying complexity.

Modularity and maintainability: Functions promote modular programming by dividing a program into smaller, self-contained units. This modular approach makes it easier to understand, modify, and maintain the codebase. When a bug or issue occurs, you can focus on a specific function rather than searching through the entire codebase.

Code reuse and DRY (Don't Repeat Yourself) principle: Functions allow you to define a piece of code once and reuse it multiple times throughout your program. This avoids duplication of code, which improves code maintainability and reduces the chances of introducing errors. When you need to make changes, you only need to modify the function in one place, and the changes will propagate to all the function calls.

Testing and debugging: Functions make it easier to test and debug your code. Since functions encapsulate specific functionality, you can write focused tests for each function. This facilitates unit testing and helps identify issues within isolated parts of your program. Additionally, when debugging, functions provide a clear scope where you can examine and trace the execution flow.

Code readability and comprehension: Well-designed functions with descriptive names can make your code more readable and understandable. Functions allow you to give meaningful names to different operations, which improves the overall comprehension of the codebase. By using functions, you can express complex logic in a more concise and readable manner.
"""


# In[2]:


# 2. When does the code in a function run: when it's specified or when it's called?
"""
The code in a function runs when the function is called, not when it is specified or defined.

When you define a function, you are essentially creating a reusable block of code with a specific name and set of instructions. The function definition specifies what the code inside the function should do when called.

To execute the code within a function, you need to call the function by using its name followed by parentheses (). When the function is called, the program flow jumps to the function's definition, and the code inside the function is executed from top to bottom. Once the code inside the function has finished executing or a return statement is encountered, the program flow returns to the point where the function was called, and the execution continues.

Here's a simple example to illustrate the concept:


def greet():
    print("Hello, world!")

print("Before function call")
greet()  # Calling the function
print("After function call")
In the example above, the function greet() is defined to print "Hello, world!" when called. The code inside the function will only run when the function is called. In this case, "Before function call" is printed, then the function greet() is called, which executes the code inside the function and prints "Hello, world!". Finally, "After function call" is printed.
"""


# In[3]:


# 3. What statement creates a function?

"""
In most programming languages, including Python, the def statement is used to create a function. The def statement is followed by the function name, parentheses (), and a colon :. Here's the syntax for creating a function:



def function_name(parameters):
    # Code block or function body
    # with instructions to be executed
    # when the function is called
Let's break down the different parts:

def: This keyword is used to indicate the start of a function definition.
function_name: This is the name you choose for your function, which should be descriptive and follow naming conventions. It's how you will refer to and call the function later in your code.
parameters: These are optional placeholders within the parentheses that you can use to pass data into the function. Parameters allow you to provide input values for the function to work with. If there are no parameters, the parentheses will be empty.
Colon :: It marks the end of the function definition header and indicates the start of the function's body.
Code block or function body: This is the indented block of code that contains the instructions to be executed when the function is called. It can consist of multiple statements, which define the behavior and logic of the function.
Here's a simple example:


def greet(name):
    print("Hello, " + name + "!")

greet("Alice")  # Calling the function
"""


# In[4]:


# 4. What is the difference between a function and a function call?
"""

The main difference between a function and a function call is as follows:

Function: A function is a reusable block of code that performs a specific task or a set of instructions. It 
is defined using the def statement followed by a function name, parentheses ( ), and a colon :. The code inside 
the function is executed when the function is called.

Function Call: A function call is an action that invokes or executes a function at a specific point in the program.
It is made by using the function name followed by parentheses ( ). The function call provides the necessary arguments
(if any) that the function expects. When a function call is encountered, the program flow jumps to the function's
definition, executes the code inside the function, and then returns back to the point of the function call.
"""


# In[5]:


# 5. How many global scopes are there in a Python program? How many local scopes?

"""

Global Scope: The global scope refers to the outermost scope in a Python program. It is the scope in which variables, 
functions, and classes are defined at the top level of the program or module. The global scope is accessible from
anywhere within the program, including inside functions and classes defined in the module. In a Python program, 
there is only one global scope.

Local Scopes: Local scopes are created when functions or classes are defined. Each function or class has its own 
local scope, which is separate from the global scope and other local scopes. Variables, functions, and classes defined 
within a function or class are accessible only within that specific local scope. Local scopes are temporary and
exist only during the execution of the function or class. Once the function or class finishes executing, the local
scope is destroyed. In a Python program, there can be multiple local scopes, depending on the number of functions or 
classes defined.

Here's an example to illustrate the concept:


global_var = 42  # Global scope variable

def my_function():
    local_var = 10  # Local scope variable
    print(local_var)  # Accessing the local variable
    print(global_var)  # Accessing the global variable

my_function()  # Function call
print(global_var)  # Accessing the global variable outside the function
"""


# In[6]:


# 6. What happens to variables in a local scope when the function call returns
"""
When a function call returns, the local scope associated with that function is destroyed, and the
variables defined within that local scope cease to exist. The memory allocated for those variables is released, and they are no longer accessible.

Here's an example to illustrate this behavior:


def my_function():
    local_var = 42
    print(local_var)

my_function()  # Function call

print(local_var)  # Error: NameError: name 'local_var' is not defined
In the example above, within the my_function() function, the variable local_var is defined in the local scope.
When the function is called, the value of local_var is printed successfully. However, outside the function, 
attempting to access local_var results in a NameError because the variable no longer exists.
"""


# In[7]:


# 7. What is the concept of a return value? Is it possible to have a return value in an expression?

"""

The concept of a return value is associated with functions. A return value is the value that a function sends 
back or "returns" to the caller after executing its code. When a function is called, it can perform some
computations or operations and produce a result. This result, known as the return value, is typically used
to pass data or information back to the caller of the function.

In Python, you can use the return statement within a function to specify the value that should be returned.
The return statement terminates the function execution and immediately sends the specified value back to 
the caller. Once the return statement is encountered, the function exits, and control returns to the point
where the function was called.

Here's an example to illustrate the concept of a return value:


def add_numbers(a, b):
    result = a + b
    return result

sum_result = add_numbers(3, 4)
print(sum_result)  # Output: 7
"""


# In[8]:


# 8. If a function does not have a return statement, what is the return value of a call to that function?

"""
If a function does not have a return statement, or if the return statement is absent, the return value of a 
call to that function is None.

In Python, when a function does not explicitly return a value, it implicitly returns None, which is a special 
object representing the absence of a value. This means that if you assign the result of a function call without a return statement to a variable, that variable will be assigned the value None.

Here's an example to demonstrate this behavior:

python
Copy code
def my_function():
    print("This function does not have a return statement")

result = my_function()
print(result)  # Output: None
In the example above, the my_function() function does not have a return statement. When the function is called, 
it executes the print() statement but does not explicitly return a value. As a result, the variable result
assigned to the function call will have the value None.
"""


# In[9]:


# 9. How do you make a function variable refer to the global variable?

"""
To make a function variable refer to the global variable, you can use the global keyword within the function.
The global keyword allows you to access and modify a global variable from within a function, rather than 
creating a new local variable with the same name.

Here's an example to illustrate how to make a function variable refer to the global variable:


global_var = 42  # Global variable

def my_function():
    global global_var  # Using the global keyword to access the global variable
    global_var = 10    # Modifying the value of the global variable

print(global_var)    # Output: 42
my_function()
print(global_var)    # Output: 10
In the example above, global_var is a global variable with an initial value of 42. Inside the my_function()
function, the global keyword is used to indicate that we want to access the global variable global_var rather 
than creating a new local variable. The value of global_var is then modified to 10 within the function.

After calling my_function(), when we print the value of global_var again, we can see that it has been
updated to 10. This is because we used the global keyword to explicitly indicate that we want to work with
the global variable and modify its value within the function.
"""


# In[10]:


# 10. What is the data type of None?

"""
The data type of None in Python is NoneType. NoneType is a built-in data type in Python that represents
the absence of a value or the lack of a return value.

Here's an example that demonstrates the data type of None:


result = None
print(type(result))  # Output: <class 'NoneType'>


In the example above, the variable result is assigned the value None. By using the type() function,
we can determine the data type of result, which is NoneType.
"""


# In[11]:


# 11. What does the sentence import areallyourpetsnamederic do?

"""

The sentence import areallyourpetsnamederic does not have any inherent meaning in Python. It appears to 
be an arbitrary sentence that includes the import keyword followed by a module name (areallyourpetsnamederic
in this case).

In Python, the import statement is used to import modules, which are files containing Python
code that can be reused in multiple programs. Modules provide additional functionality and features
beyond what is available in the Python standard library.

However, the sentence import areallyourpetsnamederic does not correspond to any standard or
commonly used Python module. If you were to execute this line of code in a Python program, it
would likely result in a ModuleNotFoundError because the module areallyourpetsnamederic does not exist
"""


# In[12]:


# 12. If you had a bacon() feature in a spam module, what would you call it after importing spam?

"""
If you imported the spam module, which contains a bacon() feature, you can call the bacon() function using the 
following syntax:


import spam
spam.bacon()


In the above code, the spam module is imported using the import statement. To call the bacon() 
function, you use the module name (spam) followed by a dot (.) and the function name (bacon()).
This syntax indicates that you are calling the bacon() function from the spam module.
"""


# In[13]:


# 13. What can you do to save a programme from crashing if it encounters an error?

"""
To save a program from crashing when it encounters an error, you can use error handling techniques to gracefully 
handle exceptions. In Python, exceptions are raised when errors or exceptional conditions occur during program 
execution. By handling exceptions, you can prevent the program from abruptly terminating and take appropriate actions instead.

Here are a few error handling techniques that you can use to save a program from crashing:

Try-Except: You can wrap the code that might raise an exception inside a try block and use an except block to
handle the specific exception(s) you anticipate. If an exception occurs within the try block, the corresponding
except block will execute, allowing you to handle the exception and continue program execution. By catching exceptions,
you can prevent the program from crashing.

Finally: You can use a finally block along with the try-except structure. The finally block is executed 
of whether an exception occurred or not. It is often used to perform cleanup tasks, such as closing files or
releasing resources, ensuring that necessary actions are taken regardless of whether an exception occurred.

Exception Types: Python provides different types of exceptions that can be caught individually. By catching specific 
exception types, you can handle different types of errors differently and take appropriate actions accordingly. For
example, you can catch FileNotFoundError to handle file-related errors and ValueError to handle invalid input errors.

Logging: You can use Python's logging module to record error messages or exceptions. Logging allows you to track and
analyze errors that occur during program execution. It helps in identifying issues and provides valuable information 
for debugging and troubleshooting.

Graceful Degradation: In certain scenarios, you may want to gracefully degrade functionality when an error
occurs instead of crashing the program completely. You can design your program to handle errors and continue
with reduced functionality or fallback mechanisms.
"""


# In[14]:


# 14. What is the purpose of the try clause? What is the purpose of the except clause?

"""
The purpose of the try clause in Python is to enclose a block of code that might raise an exception. It allows
you to specify the code that could potentially cause an error or exception. By placing this code inside a try
block, you are telling Python to attempt the execution of that code.

The general syntax of a try block is as follows:


try:
    # Code that might raise an exception
    # ...
except ExceptionType:
    # Code to handle the specific exception
    # ...
The purpose of the except clause is to define the code that should be executed when a specific exception
occurs within the corresponding try block. The except block specifies the specific exception type(s) that
it can handle and provides the code to handle the exception.

When an exception is raised within the try block, Python checks if there is an except block that matches the
type of the exception. If a matching exception is found, the code within the corresponding except block is
executed, allowing you to handle the exception gracefully.

Here's an example to illustrate the purpose of the try and except clauses:


try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: Invalid input, please enter a valid number")
In this example, the try block attempts to convert user input to an integer and perform a division. If the user 
enters 0 as the input, a ZeroDivisionError will be raised. If the user enters a non-numeric value, a ValueError 
will be raised.

The except ZeroDivisionError block handles the ZeroDivisionError exception and prints an appropriate error message.
Similarly, the except ValueError block handles the ValueError exception and provides an error message for invalid input.

"""


# In[ ]:




