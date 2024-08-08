import flet as ft
import re
from dataclasses import dataclass


@dataclass
class GitHubDark:
    editor_bg: str = "#0D1117"
    keyword: str = "#ff7b72"  # bright red for keywords
    function: str = "#d2a8ff"  # soft purple for function definitions
    function_call: str = "#d2a8ff"  # function calls match function definitions
    string: str = "#a5d6ff"  # light blue for strings
    comment: str = "#8b949e"  # muted gray for comments
    parameter: str = "#ffa657"  # orange for parameters
    type_annotation: str = (
        "#ff7b72"  # bright red for type annotations, matching keywords
    )
    class_name: str = "#d2a8ff"  # soft purple for class names
    exception: str = "#f85149"  # bright red for exceptions
    builtin: str = "#ff7b72"  # bright red for built-in constants and functions
    number: str = "#79c0ff"  # blue for numbers
    docstring: str = "#8b949e"  # muted gray for docstrings, matching comments
    decorator: str = "#ffa657"  # orange for decorators
    instance: str = "#79c0ff"  # blue for instance references

theme = GitHubDark()

# Define syntax highlighting rules
syntax_rules = {
    "python": {
        "keywords": (
            r"\b(?P<KEYWORD>False|None|True|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)\b",
            theme.keyword,
        ),
        "exceptions": (
            r"([^.'\"\\#]\b|^)(?P<EXCEPTION>ArithmeticError|AssertionError|AttributeError|BaseException|BlockingIOError|BrokenPipeError|BufferError|BytesWarning|ChildProcessError|ConnectionAbortedError|ConnectionError|ConnectionRefusedError|ConnectionResetError|DeprecationWarning|EOFError|Ellipsis|EnvironmentError|Exception|FileExistsError|FileNotFoundError|FloatingPointError|FutureWarning|GeneratorExit|IOError|ImportError|ImportWarning|IndentationError|IndexError|InterruptedError|IsADirectoryError|KeyError|KeyboardInterrupt|LookupError|MemoryError|ModuleNotFoundError|NameError|NotADirectoryError|NotImplemented|NotImplementedError|OSError|OverflowError|PendingDeprecationWarning|PermissionError|ProcessLookupError|RecursionError|ReferenceError|ResourceWarning|RuntimeError|RuntimeWarning|StopAsyncIteration|StopIteration|SyntaxError|SyntaxWarning|SystemError|SystemExit|TabError|TimeoutError|TypeError|UnboundLocalError|UnicodeDecodeError|UnicodeEncodeError|UnicodeError|UnicodeTranslateError|UnicodeWarning|UserWarning|ValueError|Warning|WindowsError|ZeroDivisionError)\b",
            theme.exception,
        ),
        "builtins": (
            r"([^.'\"\\#]\b|^)(?P<BUILTIN>abs|all|any|ascii|bin|breakpoint|callable|chr|classmethod|compile|complex|copyright|credits|delattr|dir|divmod|enumerate|eval|exec|exit|filter|format|frozenset|getattr|globals|hasattr|hash|help|hex|id|input|isinstance|issubclass|iter|len|license|locals|map|max|memoryview|min|next|oct|open|ord|pow|print|quit|range|repr|reversed|round|set|setattr|slice|sorted|staticmethod|sum|type|vars|zip)\b",
            theme.builtin,
        ),
        "docstrings": (
            r"(?P<DOCSTRING>(?i:r|u|f|fr|rf|b|br|rb)?'''[^'\\]*((\\.|'(?!''))[^'\\]*)*(''')?|(?i:r|u|f|fr|rf|b|br|rb)?\"\"\"[^\"\\]*((\\.|\"(?!\"\"))[^\"\\]*)*(\"\"\")?)",
            theme.docstring,
        ),
        "strings": (
            r"(?P<STRING>(?i:r|u|f|fr|rf|b|br|rb)?'[^'\\\n]*(\\.[^'\\\n]*)*'?|(?i:r|u|f|fr|rf|b|br|rb)?\"[^\"\\\n]*(\\.[^\"\\\n]*)*\"?)",
            theme.string,
        ),
        "types": (
            r"\b(?P<TYPES>bool|bytearray|bytes|dict|float|int|list|str|tuple|object)\b",
            theme.type_annotation,
        ),
        "numbers": (
            r"\b(?P<NUMBER>((0x|0b|0o|#)[\da-fA-F]+)|((\d*\.)?\d+))\b",
            theme.number,
        ),
        "function_calls": (
            r"(?<!\.)\b(\w+)\s*(?=\()",  # not preceded by a dot (.)
            theme.function_call,
        ),
        "class_definitions": (
            r"(?<=\bclass)[ \t]+(?P<CLASSDEF>\w+)[ \t]*[:\(]",  # recolor of DEFINITION for class definitions
            theme.class_name,
        ),
        "decorators": (
            r"(^[ \t]*(?P<DECORATOR>@[\w\d\.]+))",
            theme.decorator,
        ),
        "instances": (
            r"\b(?P<INSTANCE>super|self|cls)\b",
            theme.instance,
        ),
        "comments": (
            r"(?P<COMMENT>#[^\n]*)",
            theme.comment,
        ),
    },
}


def apply_syntax_highlighting(text, language):
    rules = syntax_rules.get(language, {})
    formatted_lines = []
    full_lines = ft.ListView(spacing=0)

    lines = text.split("\n")
    for idx, line in enumerate(lines):
        parts = []
        last_idx = 0
        matches = []

        for element, (pattern, color) in rules.items():
            for match in re.finditer(pattern, line):
                matches.append((match.start(), match.end(), match.group(0), color))

        matches.sort(key=lambda x: (x[0], -x[1]))

        # Improved overlap handling
        for start, end, matched_text, color in matches:
            if start >= last_idx:
                if start > last_idx:
                    parts.append(
                        ft.Text(value=line[last_idx:start], font_family="Code")
                    )
                parts.append(
                    ft.Text(
                        value=matched_text,
                        style=ft.TextStyle(color=color),
                        font_family="Code",
                    )
                )
                last_idx = end

        # Handle remaining text after last match
        if last_idx < len(line):
            parts.append(ft.Text(value=line[last_idx:], font_family="Code"))

        # Create a Row and add all parts to it without introducing new spaces
        line_number = ft.Container(ft.Text(f"{idx + 1}", color="#60676f"), width=40)
        line_widgets = ft.Row(controls=[line_number] + parts, wrap=None, spacing=0)
        formatted_lines.append(line_widgets)

    full_lines.controls.extend(formatted_lines)
    return full_lines


def main(page: ft.Page):
    page.fonts = {
        "Code": "SourceCodePro-Medium.ttf",
    }
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = theme.editor_bg
    page.title = "Syntax Highlighting Example"
    # page.scroll = True
    code_text = '''
# Example Python script to test syntax highlighting features

import math
from datetime import datetime

# Global variable
PI = math.pi

# Function definition
def calculate_area(radius):
    """Calculate the area of a circle."""
    return PI * (radius ** 2)

# Control structures
if __name__ == "__main__":
    radius = 5
    area = calculate_area(radius)
    print(f"The area of a circle with radius {radius} is {area:.2f}")

    # List comprehension
    squares = [x * x for x in range(10)]
    print("Squares of numbers from 0 to 9:", squares)

    # Exception handling
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Attempted to divide by zero.")
    finally:
        print("Operation attempted.")

# Class declaration
class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        current_time = datetime.now()
        if current_time.hour < 12:
            return f"Good morning, {self.name}!"
        elif current_time.hour < 18:
            return f"Good afternoon, {self.name}!"
        else:
            return f"Good evening, {self.name}!"

# Using the class
g = Greeter("Alice")
message = g.greet()
print(message)

# Dictionary comprehension
cube_dict = {x: x**3 for x in range(5)}
print("Cubes from 0 to 4:", cube_dict)

# Using modules
print("Value of PI:", PI)

# Multi-line string
multi_line_string = """This is a multi-line string example
that spans several lines."""
print(multi_line_string)
    '''

    # Choose the language
    language = "python"

    code = apply_syntax_highlighting(text=code_text, language=language)

    page.add(code)
    page.update()


ft.app(target=main)