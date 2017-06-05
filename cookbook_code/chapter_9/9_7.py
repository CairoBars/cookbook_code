'''利用装饰器强制函数上的类型检查'''
#注意：
#signature在python3 中才有

from inspect import signature
from functools import wraps

def typeassert(*ty_args,**ty_kwargs):
	def decorator(func):
		#if in optimized mode,disable type checking
		if not __debug__:
			return func 
		sig=signature(func)
		bound_types=sig.bind_partial()