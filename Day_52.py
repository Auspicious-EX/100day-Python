# DAY 52: Lambda functions in Python

# def double(x):
#     return x*2

""" 
Lambda Functions in Python
In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:

lambda arguments: expression

Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.

Here is an example of how to use a lambda function:
 """
double = lambda x: x*2

cube = lambda x: x*x*x

print(double(5))
print(cube(2))

""" 
Lambda Functions in Python
In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:

lambda arguments: expression

Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.

Here is an example of how to use a lambda function:
 """
sum = lambda x,y : (x+y)/2
print(sum(5,6))

sum = lambda x,y,z : (x+y+z)/3
print(sum(5,6,8))


def appl(fx,value):
    return 6 + fx(value)
print(appl(lambda x: x*x , 2))

""" 
In the above example, the lambda function includes a print statement, but it is still limited to a single expression.

Lambda functions are often used in conjunction with higher-order functions, such as map, filter, and reduce which we will look into later.
 """
