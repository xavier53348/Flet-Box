import ast

from ._unparse import unparse
from .utils import preserves_trailing_whitespaces, get_expr, noop_on_syntax_errors

@noop_on_syntax_errors
@preserves_trailing_whitespaces
def toggle_assert_style(s):
    returned = expr = ast.parse(s).body[0]
    if isinstance(expr, ast.Assert):
        returned = _assert_to_assert_method(expr)

    elif isinstance(expr.value, ast.Call) and isinstance(expr.value.func, ast.Attribute) and expr.value.func.value.id == "self":
        returned = _assert_method_to_assert(expr.value)

    return unparse(returned)

operator_to_assertion_method = {
    ast.Eq: "assertEquals",
    ast.GtE: "assertGreaterEqual",
    ast.LtE: "assertLessEqual",
    ast.Lt: "assertLess",
    ast.Gt: "assertGreater",
    ast.NotEq: "assertNotEqual",
    ast.Is: "assertIs",
    ast.IsNot: "assertIsNot",
    ast.In: "assertIn",
    ast.NotIn: "assertNotIn",
}
assertion_method_to_operator = {method_name: op for op, method_name in operator_to_assertion_method.items()}
assertion_method_to_operator["assertEqual"] = ast.Eq

def _assert_to_assert_method(expr):
    if isinstance(expr.test, ast.Compare):
        [op] = expr.test.ops
        assertion_method_name = operator_to_assertion_method.get(op.__class__)
        if assertion_method_name is None:
            return expr
        args = [expr.test.left, expr.test.comparators[0]]
        if args[1].id == 'None' and isinstance(op, (ast.Is, ast.IsNot)):
            args.pop(1)
            assertion_method_name = "assertIsNone" if isinstance(op, ast.Is) else "assertIsNotNone"
        if expr.msg is not None:
            args.append(expr.msg)
        return _construct_method(assertion_method_name, args)
    elif isinstance(expr.test, ast.UnaryOp) and isinstance(expr.test.op, ast.Not):
        return _construct_method("assertFalse", [expr.test.operand, expr.msg])
    return _construct_method("assertTrue", [expr.test, expr.msg])

def _assert_method_to_assert(expr):

    if expr.func.attr in ("assertTrue", "assert_", "assertFalse"):
        returned = ast.Assert()
        if expr.func.attr == "assertFalse":
            returned.test = ast.UnaryOp()
            returned.test.op = ast.Not()
            returned.test.operand = expr.args[0]
        else:
            returned.test = expr.args[0]
        returned.msg = expr.args[1] if len(expr.args) > 1 else None
        return returned

    if expr.func.attr in ("assertIsNone", "assertIsNotNone"):
        returned = ast.Assert()
        returned.test = ast.Compare()
        returned.test.ops = [ast.IsNot() if expr.func.attr == "assertIsNotNone" else ast.Is()]
        returned.test.left = expr.args[0]
        returned.test.comparators = [ast.Name()]
        returned.test.comparators[0].id = 'None'
        returned.msg = expr.args[1] if len(expr.args) > 1 else None
        return returned

    op = assertion_method_to_operator.get(expr.func.attr)
    if op is None:
        return expr

    returned = ast.Assert()
    returned.test = ast.Compare()
    returned.test.left=expr.args[0]
    returned.test.ops = [op()]
    returned.test.comparators = [expr.args[1]]
    returned.msg = expr.args[2] if len(expr.args) > 2 else None
    return returned

def _construct_method(name, args):
    args = [arg for arg in args if arg is not None]
    assertion = ast.Call()
    assertion.func = ast.Attribute(ast.Name("self", ast.Load()), name, ast.Load())
    assertion.args = list(args)
    assertion.keywords = []
    assertion.starargs = assertion.kwargs = None

    returned = ast.Expression()
    returned.value = assertion
    return returned
