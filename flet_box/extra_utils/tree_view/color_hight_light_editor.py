import flet as ft
import re

from dataclasses import dataclass


@dataclass
class GitHubDark:
    editor_bg:       str = "#001000"
    keyword:         str = "#ff007f"  # bright red for keywords
    function:        str = "#001000"  # soft purple for function definitions
    function_call:   str = "#00ff51"  # function calls match function definitions
    string:          str = "#fff261"  # light blue for strings
    comment:         str = "#8b949e"  # muted gray for comments
    parameter:       str = "#ffa657"  # orange for parameters
    type_annotation: str = "#ff007f"  # bright red for type annotations, matching keywords
    class_name:      str = "#00aeff"  # soft purple for class names
    exception:       str = ft.colors.PURPLE_ACCENT_200  # bright red for exceptions controls content
    builtin:         str = "#00ff48"  # bright red for built-in constants and functions
    number:          str = "#ffa657"  # blue for numbers
    docstring:       str = "#4b4b4b"  # muted gray for docstrings, matching comments
    decorator:       str = "#ffa657"  # orange for decorators
    instance:        str = "#79c0ff"  # blue for instance references

theme = GitHubDark()

# Define syntax highlighting rules
syntax_rules = {
    "python": {
        "keywords": (
            r"\b(?P<KEYWORD>False|.|all|only|None|True|Container|GridView|Row|Column|Stack|self|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)\b",
            theme.keyword,
        ),
        "exceptions": (
            r"([^.'\"\\#]\b|^)(?P<EXCEPTION>ArithmeticError|on_click|on_hover|on_accept|AssertionError|AttributeError|BaseException|BlockingIOError|BrokenPipeError|BufferError|BytesWarning|ChildProcessError|ConnectionAbortedError|ConnectionError|ConnectionRefusedError|ConnectionResetError|DeprecationWarning|EOFError|Ellipsis|EnvironmentError|Exception|FileExistsError|FileNotFoundError|FloatingPointError|FutureWarning|GeneratorExit|IOError|ImportError|ImportWarning|IndentationError|IndexError|InterruptedError|IsADirectoryError|KeyError|KeyboardInterrupt|LookupError|MemoryError|ModuleNotFoundError|NameError|NotADirectoryError|NotImplemented|NotImplementedError|OSError|OverflowError|PendingDeprecationWarning|PermissionError|ProcessLookupError|RecursionError|ReferenceError|ResourceWarning|RuntimeError|RuntimeWarning|StopAsyncIteration|StopIteration|SyntaxError|SyntaxWarning|SystemError|SystemExit|TabError|TimeoutError|TypeError|UnboundLocalError|UnicodeDecodeError|UnicodeEncodeError|UnicodeError|UnicodeTranslateError|UnicodeWarning|UserWarning|ValueError|Warning|WindowsError|ZeroDivisionError)\b",
            theme.exception,
        ),
        "builtins": (
            r"([^.'\"\\#]\b|^)(?P<BUILTIN>abs|_|:|,|all|any|e|ascii|bin|breakpoint|content|ft|controls|callable|chr|classmethod|compile|complex|copyright|credits|delattr|dir|divmod|enumerate|eval|exec|exit|filter|format|frozenset|getattr|globals|hasattr|hash|help|hex|id|input|isinstance|issubclass|iter|len|license|locals|map|max|memoryview|min|next|oct|open|ord|pow|print|quit|range|repr|reversed|round|set|setattr|slice|sorted|staticmethod|sum|type|vars|zip)\b",
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
            r"\b(?P<TYPES>bool|bytearray|bytes|dict|ft.|float|int|list|str|tuple|object)\b",
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
            r"(?<=\bclass)[ \t]+(?P<CLASSDEF>\w+)[ \t]*[:\(]|__init__",  # recolor of DEFINITION for class definitions
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


def apply_syntax_highlighting(
                              text:      str = "",
                              language:  str = "python" ,
                              text_size: int = 11
                              ):
    """
    THANKS TO
    """
    rules = syntax_rules.get(language, {})
    formatted_lines: list = []
    full_lines = ft.ListView(spacing=0 )

    lines = text.split("\n")
    for idx, line in enumerate(lines):
        parts:    list = []
        last_idx: int  = 0
        matches:  list = []

        for element, (pattern, color) in rules.items():
            for match in re.finditer(pattern, line):
                matches.append((match.start(), match.end(), match.group(0), color))

        matches.sort(key=lambda x: (x[0], -x[1]))

        # Improved overlap handling
        for start, end, matched_text, color in matches:
            if start >= last_idx:
                if start > last_idx:
                    parts.append(
                        ft.Text(
                                value       = line[last_idx:start],
                                font_family = "Code",
                                size        = text_size,
                                color       = ft.colors.TEAL_900,
                                weight      = ft.FontWeight.BOLD,

                                ) # ATTRIBUTES
                    )
                parts.append(
                    ft.Text(
                        value       = matched_text,
                        style       = ft.TextStyle(color=color),
                        font_family = "Code",
                        size        = text_size,
                        weight      = ft.FontWeight.BOLD,
                    )
                )
                last_idx = end

        # Handle remaining text after last match
        if last_idx < len(line):
            parts.append( ft.Text(
                                    value       = line[last_idx:],
                                    font_family = "Code",
                                    size        = text_size,
                                    color       = ft.colors.TEAL_ACCENT_700,
                                    weight      = ft.FontWeight.BOLD,
                                    ))

        # Create a Row and add all parts to it without introducing new spaces
        line_number = ft.Container(
                                   padding=ft.padding.only(left=0,right=26,bottom=0,top=0),
                                   content= ft.Text(
                                            value      = f"{idx + 1}",
                                            color      = "#60676f",
                                            size       = text_size,
                                            weight     = ft.FontWeight.BOLD,
                                            width      = 20,
                                            text_align = ft.TextAlign.RIGHT,                                    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END


                                            ),)

        formatted_lines.append(ft.Row(controls=[line_number] + parts, wrap=None, spacing=0))

    full_lines.controls.extend(formatted_lines)
    return full_lines


if __name__ == '__main__':
    text_code_exemple = '''
    from ..app_style_manager import styles
    from ..app_events_manager import *

    import flet as ft


    class Screen1(ft.Container):
        def __init__(self):
            super().__init__()

            dict_keys: dict   = self.dict_style('_2222')
            self: list        = [self.__setattr__(_ , dict_keys.get(_)) for _ in dict_keys]

        def build(self):
            self.content = ft.Container(
                                    **self.dict_style('_2921'),
                                    content = ft.Column(
                                                **self.dict_style('_2922'),
                                                controls = [
                                                        ft.Container(
                                                                **self.dict_style('_2925'),
                                                                content = ft.Text(
                                                                        **self.dict_style('_2926'),
                                                                ),),
                                                        ft.Container(
                                                                **self.dict_style('_2933'),
                                                                content = ft.ElevatedButton(
                                                                        **self.dict_style('_2934'),
                                                                        on_click=lambda _: event_2222(data='_2934'),
                                                                ),),
                                        ],),) # <<< LAYER 0 END BRAKETS


        def dict_style(self,code):
            return styles.get(code)
    '''

    def main(page: ft.Page):
        page.fonts = {
            "Code": "SourceCodePro-Medium.ttf",
        }
        page.theme_mode = ft.ThemeMode.DARK
        page.bgcolor = theme.editor_bg
        page.title = "Syntax Highlighting Example"
        page.scroll = True
        # Choose the language
        code = apply_syntax_highlighting(text=text_code_exemple, language="python")
        page.add(code)
        page.update()

    ft.app(target=main)