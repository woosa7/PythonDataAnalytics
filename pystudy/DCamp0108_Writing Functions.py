"""
Writing Functions in Python

First-class fuction
함수 자체를 인자(argument)로써 다른 함수에 전달하거나 다른 함수의 결과값으로 리턴할 수도 있고, 함수를 변수에 할당하거나 데이터 구조안에 저장할 수 있다.
"""

# -------------------------------------------
# docstring

def count_letter(content, letter):
    """Count the number of times `letter` appears in `content`.

    Args:
      content (str): The string to search.
      letter (str): The letter to search for.

    Returns:
      int

    Raises:
      ValueError: If `letter` is not a one-character string.
    """
    if (not isinstance(letter, str)) or len(letter) != 1:
        raise ValueError('`letter` must be a single character string.')

    return len([char for char in content if char == letter])

# -------------------------------------------
# Retrieving docstrings

import inspect

def build_tooltip(function):
    """Create a tooltip for any function that shows the function's docstring.

    Args:
      function (callable): The function we want a tooltip for.

    Returns:
      str
    """
    # Use 'inspect' to get the docstring
    docstring = inspect.getdoc(function)
    border = '#' * 28
    return '{}\n{}\n{}'.format(border, docstring, border)


print(build_tooltip(count_letter))

# -------------------------------------------
# Extract a function

import pandas as pd

def standardize(column):
    """Standardize the values in a column.

    Args:
      column (pandas Series): The data to standardize.

    Returns:
      pandas Series: the values as z-scores
    """
    # Finish the function so that it returns the z-scores
    z_score = (column - column.mean()) / column.std()
    return z_score


# Use the standardize() function to calculate the z-score
df = pd.read_csv('data/chap01/us_life_expectancy.csv')

df['life_exp_z'] = standardize(df.life_expectancy)
print(df.head())

# -------------------------------------------
# Best practice for default arguments

# Use an immutable variable for the default argument
def better_add_column(values, df=None):
    # Update the function to create a default DataFrame
    if df is None:
        df = pd.DataFrame()

    df['col_{}'.format(len(df.columns))] = values
    return df

# -------------------------------------------
# Using context managers

# Open "alice.txt" and assign the file to "file"
with open('data/chap01/anna.txt') as file:
    text = file.read()

n = 0
for word in text.split():
    if word.lower() in ['love', 'loved']:
        n += 1

print('Anna Karenina uses the word `love` {} times'.format(n))

# -------------------------------------------
# Writing context managers

import contextlib
import time

# Add a decorator that will make timer() a context manager
@contextlib.contextmanager
def timer():
    """Time the execution of a context block.

    Yields:
      None
    """
    start = time.time()
    # Send control back to the context block
    yield
    end = time.time()
    print('Elapsed: {:.2f}s'.format(end - start))


with timer():
    print('This should take approximately 0.25 seconds')
    time.sleep(0.25)

# -------------------------------------------
# A read-only open() context manager

@contextlib.contextmanager
def open_read_only(filename):
    """Open a file in read-only mode.

    Args:
      filename (str): The location of the file to read

    Yields:
      file object
    """
    read_only_file = open(filename, mode='r')
    yield read_only_file
    read_only_file.close()


with open_read_only('data/chap01/anna.txt') as my_file:
    scripts = my_file.read()
    # print(scripts)

# -------------------------------------------
# Modifying variables outside local scope
# Sometimes your functions will need to modify a variable that is outside of the local scope of that function.

# 1
call_count = 0

def my_function():
    # Use a keyword that lets us update call_count
    global call_count
    call_count += 1

    print("You've called my_function() {} times!".format(call_count))


for _ in range(5):
    my_function()


# 2
import random

def wait_until_done():
    def check_is_done():
        # Add a keyword so that wait_until_done() doesn't run forever
        global done
        if random.random() < 0.1:
            done = True

    while not done:
        check_is_done()


done = False
wait_until_done()

print('Work done? {}'.format(done))

# -------------------------------------------
"""
Closure
클로저는 일반 함수와는 다르게, 자신의 영역 밖에서 호출된 함수의 변수값과 레퍼런스를 복사하고 저장한 뒤, 이 캡처한 값들에 액세스할 수 있게 도와준다.
"""
# Closures

def return_a_func(arg1, arg2):
    def new_func():
        print('arg1 was {}'.format(arg1))
        print('arg2 was {}'.format(arg2))

    return new_func


my_func = return_a_func(2, 17)
print(my_func)

# Show that my_func()'s closure is not None
print(my_func.__closure__ is not None)
print(len(my_func.__closure__) == 2)    # no. of variables in closure

# Get the values of the variables in the closure
closure_values = [
    my_func.__closure__[i].cell_contents for i in range(2)
]
print(closure_values == [2, 17])

# -------------------------------------------
# Closures keep your values safe

def my_special_function():
    print('You are running my_special_function()')

def get_new_func(func):
    def call_func():
        func()

    return call_func


new_func = get_new_func(my_special_function)

# Redefine my_special_function() to just print "hello"
def my_special_function():
    print("hello")

# new_func는 클로저이기 때문에 이전의 원래 동작을 그대로 실행한다.
new_func()

# Delete my_special_function(). 이 함수를 삭제해도 저장된 클로저는 문제없이 동작한다.
del (my_special_function)

new_func()

# -------------------------------------------
"""
Decorator : 클로저를 활용해 함수를 확장
"""

def double_args(func):
    def wrapper(a, b):
        return func(a * 2, b * 2)
    return wrapper


# normal syntax
def my_function(a, b):
    print(a + b)

# Decorate my_function() with the print_args() decorator
my_function = double_args(my_function)
my_function(1, 2)


# Decorator syntax
@double_args
def my_function(a, b):
    print(a + b)

my_function(1, 2)

# -------------------------------------------
# Defining a decorator

def print_before_and_after(func):
    def wrapper(*args):
        print('Before {}'.format(func.__name__))
        # Call the function being decorated with *args
        func(*args)
        print('After {}'.format(func.__name__))

    return wrapper


@print_before_and_after
def multiply(a, b):
    print(a * b)


multiply(5, 10)

# -------------------------------------------
# Real world examples
# -------------------------------------------
# Print the return type
# decorating 하는 함수의 모든 호출에서 리턴되는 변수의 유형을 출력

def print_return_type(func):
    # Define wrapper(), the decorated function
    def wrapper(*args, **kwargs):
        # Call the function being decorated
        result = func(*args, **kwargs)
        print('{}() returned type {}'.format(
            func.__name__, type(result)
        ))
        return result

    return wrapper


@print_return_type
def foo(value):
    return value


print(foo(42))
print(foo([1, 2, 3]))
print(foo({'a': 42}))

# -------------------------------------------
# Counter

def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        # Call the function being decorated and return the result
        return func(*args, **kwargs)

    wrapper.count = 0

    return wrapper


# Decorate foo() with the counter() decorator
@counter
def foo():
    print('calling foo()')


foo()
foo()

print('foo() was called {} times.'.format(foo.count))

# -------------------------------------------
