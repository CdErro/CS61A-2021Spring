# High Order Function

 ```python
 def same_length(a,b):
     """a_count=1
     while a>=10:
         a=a//10
         a_count+=1
     b_count=1
     while b>=10:
         b=b//10
         b_count+=1
 	return a_count==b_count"""
 	return num_digits(a)==num_digits(b)
 
 def num_digits(a,radix=10): # radix defalut parameter
     a_count=1
     while a>=10:
         a=a//10
         a_count+=1
     return a_count
 ```

## Documenting Functions

**documentation comment**:enough information of a function

​	precondition:valid inputs\call conditions

​	postcondition:resulting output/effect for correct inputs

## design priciples

- functions should do one well-defined thing
- don't repeat yourself

## functions as templates

a template for a computation

not only in place of numbers,but also slots for computations

```python
def suqare(n):
    n=n**2
    return n
def summaiton(n,term):
    n=n**term
   	return n
```

## funtions produce functions

functions are first-class values,meaning we can assign them to variavles,pass them to funcitons adn return them from functions,that's high order functions

```python
def h(x): return sin(x)+cos(x)

def combine_func(op):
    def combined(f,g):
    	def val(x)
    		return op(f(x),g(x))
    	return val
	return combined
```

