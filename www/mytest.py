import inspect
from inspect import signature

def foo(a,b,*,c,d=10):
    pass
sig=signature(foo)
for param in sig.parameters.values():
    if(param.kind==inspect.Parameter.KEYWORD_ONLY and param.default is param.empty):
        print('Parameter:',param)
