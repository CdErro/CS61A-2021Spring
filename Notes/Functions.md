# Functions,Expressions,

pure function

获取输入然后输出

impure function

除了输出之外产生额外的影响

```python
print(5)-->return None but display '5'
```



call expressions

operator and operand themselves expressions

sunsitution

```python
def hmmm(x):
    def f(x):
        return x
    return f
```

if we call hmmm(5),x of f(x) wont ne substitued to 5, as the x of f(x) is defined in the enviroment of f(x) itself, the x of hmmm(x) is different from x of f(x).

# Environment

an Environment is a mapping from names to values,used as data structure in interpreter /in excuting programm(函数运行空间/作用域)

environment is related to variable scope

```python
def id(x):
    return x
print(id(id)(id(13)))

----------------------
--->id(id) return id itself
```

