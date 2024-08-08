import ast

from ._unparse import unparse
from .utils import (get_expr, noop_on_syntax_errors,
                    preserves_trailing_whitespaces)


def toggle_dict_style(s):
    if s.startswith("{"):
        return curly_to_dict(s)
    return dict_to_curly(s)

@noop_on_syntax_errors
@preserves_trailing_whitespaces
def curly_to_dict(s):
    expr = get_expr(s)
    returned = ast.Call()
    returned.func = ast.Name()
    returned.func.id = 'dict'
    returned.args = []
    returned.keywords = []
    for key, value in zip(expr.keys, expr.values):
        if not isinstance(key, ast.Str):
            return s
        keyword = ast.keyword(arg=key.s, value=value)
        returned.keywords.append(keyword)
    returned.starargs = None
    returned.kwargs = None
    return unparse(returned)

@preserves_trailing_whitespaces
def dict_to_curly(s):
    expr = get_expr(s)
    returned = ast.Dict()
    returned.keys = []
    returned.values = []
    for keyword in expr.keywords:
        returned.keys.append(ast.Str(s=keyword.arg))
        returned.values.append(keyword.value)
    return unparse(returned)
