"""
Silk Parser

Converts tokens into an Abstract Syntax Tree (AST).
"""

from .tokens import Token, TokenType
from .errors import ParseError
from .ast import (
    Program, NumberLiteral, StringLiteral, BoolLiteral, NullLiteral,
    ArrayLiteral, Identifier, BinaryOp, UnaryOp, Assignment,
    CompoundAssignment, LetDeclaration, IfStatement, WhileLoop,
    ForLoop, FunctionDef, FunctionCall, ReturnStatement,
    BreakStatement, ContinueStatement, IndexAccess, IndexAssign,
    MemberAccess, StructDef, StructField, StructInstance,
    EnumDef, EnumVariant, MatchExpr, MatchArm, ImplBlock,
    InterfaceDef, InterfaceMethodSig, ImportStmt,
    TestBlock, AssertStatement, StringInterp
)


class Parser:
    """Recursive descent parser for Silk."""

    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.pos = 0

    def current(self) -> Token:
        """Get current token."""
        return self.tokens[self.pos]

    def peek(self, offset: int = 1) -> Token:
        """Look ahead at token."""
        idx = self.pos + offset
        if idx < len(self.tokens):
            return self.tokens[idx]
        return self.tokens[-1]

    def eat(self, type_: TokenType) -> Token:
        """Consume token of expected type."""
        token = self.current()
        if token.type != type_:
            raise ParseError(
                f"Expected {type_.name}, got {token.type.name} ({token.value!r})",
                token.line, token.col
            )
        self.pos += 1
        return token

    def skip_newlines(self) -> None:
        """Skip newline tokens."""
        while self.pos < len(self.tokens) and self.current().type == TokenType.NEWLINE:
            self.pos += 1

    def match(self, *types: TokenType) -> bool:
        """Check if current token is one of the given types."""
        return self.current().type in types

    def is_struct_instance_start(self) -> bool:
        """Check if current position starts a struct instantiation.

        Looks for pattern: { identifier : ...
        This distinguishes struct literals from blocks.
        Handles newlines after the opening brace.
        """
        if not self.match(TokenType.LBRACE):
            return False
        # Skip newlines when peeking
        offset = 1
        while self.peek(offset).type == TokenType.NEWLINE:
            offset += 1
        next_token = self.peek(offset)
        if next_token.type != TokenType.IDENTIFIER:
            return False
        offset += 1
        while self.peek(offset).type == TokenType.NEWLINE:
            offset += 1
        after_ident = self.peek(offset)
        return after_ident.type == TokenType.COLON

    def parse(self) -> Program:
        """Parse the entire program."""
        statements = []
        self.skip_newlines()

        while not self.match(TokenType.EOF):
            stmt = self.parse_statement()
            if stmt is not None:
                statements.append(stmt)
            self.skip_newlines()

        return Program(statements)

    def parse_statement(self):
        """Parse a single statement."""
        self.skip_newlines()
        t = self.current()

        if t.type == TokenType.LET:
            return self.parse_let()
        elif t.type == TokenType.FN:
            return self.parse_function_def()
        elif t.type == TokenType.IF:
            return self.parse_if()
        elif t.type == TokenType.WHILE:
            return self.parse_while()
        elif t.type == TokenType.FOR:
            return self.parse_for()
        elif t.type == TokenType.RETURN:
            return self.parse_return()
        elif t.type == TokenType.BREAK:
            self.pos += 1
            return BreakStatement()
        elif t.type == TokenType.CONTINUE:
            self.pos += 1
            return ContinueStatement()
        elif t.type == TokenType.STRUCT:
            return self.parse_struct_def()
        elif t.type == TokenType.ENUM:
            return self.parse_enum_def()
        elif t.type == TokenType.MATCH:
            return self.parse_match()
        elif t.type == TokenType.IMPL:
            return self.parse_impl_block()
        elif t.type == TokenType.INTERFACE:
            return self.parse_interface_def()
        elif t.type == TokenType.IMPORT:
            return self.parse_import()
        elif t.type == TokenType.TEST:
            return self.parse_test_block()
        elif t.type == TokenType.ASSERT:
            return self.parse_assert()
        else:
            return self.parse_expression_statement()

    def parse_let(self) -> LetDeclaration:
        """Parse let declaration."""
        self.eat(TokenType.LET)

        mutable = False
        if self.match(TokenType.MUT):
            self.eat(TokenType.MUT)
            mutable = True

        name = self.eat(TokenType.IDENTIFIER).value
        type_hint = None

        if self.match(TokenType.COLON):
            self.eat(TokenType.COLON)
            type_hint = self.current().value
            self.pos += 1

        self.eat(TokenType.ASSIGN)
        value = self.parse_expression()

        return LetDeclaration(name, mutable, type_hint, value)

    def parse_function_def(self) -> FunctionDef:
        """Parse function definition."""
        self.eat(TokenType.FN)
        name = self.eat(TokenType.IDENTIFIER).value
        self.eat(TokenType.LPAREN)

        params = []
        while not self.match(TokenType.RPAREN):
            pname = self.eat(TokenType.IDENTIFIER).value
            ptype = None
            if self.match(TokenType.COLON):
                self.eat(TokenType.COLON)
                ptype = self.current().value
                self.pos += 1
            params.append((pname, ptype))
            if self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)

        self.eat(TokenType.RPAREN)

        return_type = None
        if self.match(TokenType.ARROW):
            self.eat(TokenType.ARROW)
            return_type = self.current().value
            self.pos += 1

        body = self.parse_block()
        return FunctionDef(name, params, return_type, body)

    def parse_if(self) -> IfStatement:
        """Parse if/elif/else statement."""
        self.eat(TokenType.IF)
        condition = self.parse_expression()
        body = self.parse_block()

        elif_branches = []
        else_body = None

        self.skip_newlines()
        while self.match(TokenType.ELIF):
            self.eat(TokenType.ELIF)
            elif_cond = self.parse_expression()
            elif_body = self.parse_block()
            elif_branches.append((elif_cond, elif_body))
            self.skip_newlines()

        if self.match(TokenType.ELSE):
            self.eat(TokenType.ELSE)
            else_body = self.parse_block()

        return IfStatement(condition, body, elif_branches, else_body)

    def parse_while(self) -> WhileLoop:
        """Parse while loop."""
        self.eat(TokenType.WHILE)
        condition = self.parse_expression()
        body = self.parse_block()
        return WhileLoop(condition, body)

    def parse_for(self) -> ForLoop:
        """Parse for-in loop."""
        self.eat(TokenType.FOR)
        var_name = self.eat(TokenType.IDENTIFIER).value
        self.eat(TokenType.IN)
        iterable = self.parse_expression()
        body = self.parse_block()
        return ForLoop(var_name, iterable, body)

    def parse_return(self) -> ReturnStatement:
        """Parse return statement."""
        self.eat(TokenType.RETURN)
        value = None
        if not self.match(TokenType.NEWLINE, TokenType.EOF, TokenType.RBRACE):
            value = self.parse_expression()
        return ReturnStatement(value)

    def parse_struct_def(self) -> StructDef:
        """Parse struct definition."""
        self.eat(TokenType.STRUCT)
        name = self.eat(TokenType.IDENTIFIER).value
        self.eat(TokenType.LBRACE)
        self.skip_newlines()

        fields = []
        while not self.match(TokenType.RBRACE):
            field_name = self.eat(TokenType.IDENTIFIER).value
            field_type = None
            if self.match(TokenType.COLON):
                self.eat(TokenType.COLON)
                field_type = self.eat(TokenType.IDENTIFIER).value
            fields.append(StructField(field_name, field_type))

            if self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)
            self.skip_newlines()

        self.eat(TokenType.RBRACE)
        return StructDef(name, fields)

    def parse_struct_instance(self, struct_name: str) -> StructInstance:
        """Parse struct instantiation: Name { field: value, ... }"""
        self.eat(TokenType.LBRACE)
        self.skip_newlines()

        field_values = {}
        while not self.match(TokenType.RBRACE):
            field_name = self.eat(TokenType.IDENTIFIER).value
            self.eat(TokenType.COLON)
            field_value = self.parse_expression()
            field_values[field_name] = field_value

            if self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)
            self.skip_newlines()

        self.eat(TokenType.RBRACE)
        return StructInstance(struct_name, field_values)

    def parse_enum_def(self) -> EnumDef:
        """Parse enum definition."""
        self.eat(TokenType.ENUM)
        name = self.eat(TokenType.IDENTIFIER).value
        self.eat(TokenType.LBRACE)
        self.skip_newlines()

        variants = []
        while not self.match(TokenType.RBRACE):
            variant_name = self.eat(TokenType.IDENTIFIER).value
            variants.append(EnumVariant(variant_name))

            if self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)
            self.skip_newlines()

        self.eat(TokenType.RBRACE)
        return EnumDef(name, variants)

    def parse_interface_def(self) -> InterfaceDef:
        """Parse interface definition with method signatures."""
        self.eat(TokenType.INTERFACE)
        name = self.eat(TokenType.IDENTIFIER).value
        self.eat(TokenType.LBRACE)
        self.skip_newlines()

        methods = []
        while not self.match(TokenType.RBRACE):
            self.eat(TokenType.FN)
            method_name = self.eat(TokenType.IDENTIFIER).value
            self.eat(TokenType.LPAREN)

            params = []
            while not self.match(TokenType.RPAREN):
                pname = self.eat(TokenType.IDENTIFIER).value
                ptype = None
                if self.match(TokenType.COLON):
                    self.eat(TokenType.COLON)
                    ptype = self.current().value
                    self.pos += 1
                params.append((pname, ptype))
                if self.match(TokenType.COMMA):
                    self.eat(TokenType.COMMA)
            self.eat(TokenType.RPAREN)

            return_type = None
            if self.match(TokenType.ARROW):
                self.eat(TokenType.ARROW)
                return_type = self.current().value
                self.pos += 1

            methods.append(InterfaceMethodSig(method_name, params, return_type))
            self.skip_newlines()

        self.eat(TokenType.RBRACE)
        return InterfaceDef(name, methods)

    def parse_impl_block(self) -> ImplBlock:
        """Parse impl block: impl Name { ... } or impl Name : Interface { ... }"""
        self.eat(TokenType.IMPL)
        struct_name = self.eat(TokenType.IDENTIFIER).value

        interface_name = None
        if self.match(TokenType.COLON):
            self.eat(TokenType.COLON)
            interface_name = self.eat(TokenType.IDENTIFIER).value

        self.eat(TokenType.LBRACE)
        self.skip_newlines()

        methods = []
        while not self.match(TokenType.RBRACE):
            if self.match(TokenType.FN):
                methods.append(self.parse_function_def())
            else:
                raise ParseError(
                    f"Expected 'fn' in impl block, got {self.current().type.name}",
                    self.current().line, self.current().col
                )
            self.skip_newlines()

        self.eat(TokenType.RBRACE)
        return ImplBlock(struct_name, methods, interface_name)

    def parse_import(self) -> ImportStmt:
        """Parse import statement: import path or import path as alias.

        Path is built from IDENTIFIER and SLASH tokens.
        Supports: import silk/math, import ./utils, import ./lib/geo as geo
        """
        self.eat(TokenType.IMPORT)

        # Build path from tokens
        parts = []

        # Handle ./ prefix for relative imports
        if self.match(TokenType.DOT):
            self.eat(TokenType.DOT)
            self.eat(TokenType.SLASH)
            parts.append(".")

        # Consume first identifier
        parts.append(self.eat(TokenType.IDENTIFIER).value)

        # Consume remaining /identifier segments
        while self.match(TokenType.SLASH):
            self.eat(TokenType.SLASH)
            parts.append(self.eat(TokenType.IDENTIFIER).value)

        # Build path string
        if parts[0] == ".":
            path = "./" + "/".join(parts[1:])
        else:
            path = "/".join(parts)

        # Optional alias
        alias = None
        if self.match(TokenType.AS):
            self.eat(TokenType.AS)
            alias = self.eat(TokenType.IDENTIFIER).value

        return ImportStmt(path, alias)

    def parse_test_block(self) -> TestBlock:
        """Parse test block: test "name" { body }"""
        self.eat(TokenType.TEST)
        name = self.eat(TokenType.STRING).value
        body = self.parse_block()
        return TestBlock(name, body)

    def parse_assert(self) -> AssertStatement:
        """Parse assert statement: assert expression"""
        self.eat(TokenType.ASSERT)
        expression = self.parse_expression()
        return AssertStatement(expression)

    def parse_match(self) -> MatchExpr:
        """Parse match expression."""
        self.eat(TokenType.MATCH)
        value = self.parse_expression()
        self.eat(TokenType.LBRACE)
        self.skip_newlines()

        arms = []
        while not self.match(TokenType.RBRACE):
            # Parse pattern
            if self.current().value == '_':
                pattern = Identifier('_')  # Wildcard
                self.pos += 1
            else:
                pattern = self.parse_postfix()  # Handles Identifier, MemberAccess, literals

            # Optional guard: if condition
            guard = None
            if self.match(TokenType.IF):
                self.eat(TokenType.IF)
                guard = self.parse_expression()

            self.eat(TokenType.ARROW_MATCH)

            # Parse body (expression or block)
            if self.match(TokenType.LBRACE):
                body = self.parse_block()
            else:
                body = self.parse_expression()

            arms.append(MatchArm(pattern, guard, body))

            if self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)
            self.skip_newlines()

        self.eat(TokenType.RBRACE)
        return MatchExpr(value, arms)

    def parse_block(self) -> list:
        """Parse a block { ... }."""
        self.skip_newlines()
        self.eat(TokenType.LBRACE)
        statements = []
        self.skip_newlines()

        while not self.match(TokenType.RBRACE):
            stmt = self.parse_statement()
            if stmt is not None:
                statements.append(stmt)
            self.skip_newlines()

        self.eat(TokenType.RBRACE)
        return statements

    def parse_expression_statement(self):
        """Parse expression or assignment statement."""
        expr = self.parse_expression()

        # Check for assignment
        if isinstance(expr, Identifier) and self.match(TokenType.ASSIGN):
            self.eat(TokenType.ASSIGN)
            value = self.parse_expression()
            return Assignment(expr.name, value)

        # Compound assignment
        if isinstance(expr, Identifier) and self.match(
            TokenType.PLUS_ASSIGN, TokenType.MINUS_ASSIGN,
            TokenType.STAR_ASSIGN, TokenType.SLASH_ASSIGN
        ):
            op_map = {
                TokenType.PLUS_ASSIGN: '+',
                TokenType.MINUS_ASSIGN: '-',
                TokenType.STAR_ASSIGN: '*',
                TokenType.SLASH_ASSIGN: '/',
            }
            op = op_map[self.current().type]
            self.pos += 1
            value = self.parse_expression()
            return CompoundAssignment(expr.name, op, value)

        # Index assignment: arr[i] = val
        if isinstance(expr, IndexAccess) and self.match(TokenType.ASSIGN):
            self.eat(TokenType.ASSIGN)
            value = self.parse_expression()
            return IndexAssign(expr.obj, expr.index, value)

        return expr

    # ═══════════════════════════════════════════════════════════
    # Expression parsing (precedence climbing)
    # ═══════════════════════════════════════════════════════════

    def parse_expression(self):
        """Parse expression (entry point)."""
        return self.parse_or()

    def parse_or(self):
        """Parse OR expression."""
        left = self.parse_and()
        while self.match(TokenType.OR):
            self.pos += 1
            right = self.parse_and()
            left = BinaryOp(left, 'or', right)
        return left

    def parse_and(self):
        """Parse AND expression."""
        left = self.parse_not()
        while self.match(TokenType.AND):
            self.pos += 1
            right = self.parse_not()
            left = BinaryOp(left, 'and', right)
        return left

    def parse_not(self):
        """Parse NOT expression."""
        if self.match(TokenType.NOT):
            self.pos += 1
            operand = self.parse_not()
            return UnaryOp('not', operand)
        return self.parse_comparison()

    def parse_comparison(self):
        """Parse comparison expression."""
        left = self.parse_addition()
        while self.match(
            TokenType.EQ, TokenType.NEQ,
            TokenType.LT, TokenType.GT,
            TokenType.LTE, TokenType.GTE
        ):
            op_map = {
                TokenType.EQ: '==',
                TokenType.NEQ: '!=',
                TokenType.LT: '<',
                TokenType.GT: '>',
                TokenType.LTE: '<=',
                TokenType.GTE: '>=',
            }
            op = op_map[self.current().type]
            self.pos += 1
            right = self.parse_addition()
            left = BinaryOp(left, op, right)
        return left

    def parse_addition(self):
        """Parse addition/subtraction."""
        left = self.parse_multiplication()
        while self.match(TokenType.PLUS, TokenType.MINUS):
            op = '+' if self.current().type == TokenType.PLUS else '-'
            self.pos += 1
            right = self.parse_multiplication()
            left = BinaryOp(left, op, right)
        return left

    def parse_multiplication(self):
        """Parse multiplication/division/modulo."""
        left = self.parse_power()
        while self.match(TokenType.STAR, TokenType.SLASH, TokenType.PERCENT):
            op_map = {
                TokenType.STAR: '*',
                TokenType.SLASH: '/',
                TokenType.PERCENT: '%'
            }
            op = op_map[self.current().type]
            self.pos += 1
            right = self.parse_power()
            left = BinaryOp(left, op, right)
        return left

    def parse_power(self):
        """Parse exponentiation (right-associative)."""
        left = self.parse_unary()
        if self.match(TokenType.POWER):
            self.pos += 1
            right = self.parse_power()  # right-associative
            left = BinaryOp(left, '**', right)
        return left

    def parse_unary(self):
        """Parse unary minus."""
        if self.match(TokenType.MINUS):
            self.pos += 1
            operand = self.parse_unary()
            return UnaryOp('-', operand)
        return self.parse_postfix()

    def parse_postfix(self):
        """Parse postfix operations (call, index, member)."""
        expr = self.parse_primary()

        while True:
            if self.match(TokenType.LPAREN):
                # Function call
                self.eat(TokenType.LPAREN)
                args = []
                while not self.match(TokenType.RPAREN):
                    args.append(self.parse_expression())
                    if self.match(TokenType.COMMA):
                        self.eat(TokenType.COMMA)
                self.eat(TokenType.RPAREN)
                expr = FunctionCall(expr, args)

            elif self.match(TokenType.LBRACKET):
                # Index access
                self.eat(TokenType.LBRACKET)
                index = self.parse_expression()
                self.eat(TokenType.RBRACKET)
                expr = IndexAccess(expr, index)

            elif self.match(TokenType.DOT):
                # Member access
                self.eat(TokenType.DOT)
                member = self.eat(TokenType.IDENTIFIER).value
                expr = MemberAccess(expr, member)

                # Check for namespaced struct: mod.Struct { field: value }
                if self.match(TokenType.LBRACE) and self.is_struct_instance_start():
                    instance = self.parse_struct_instance(member)
                    instance.struct_ref = expr
                    expr = instance

            else:
                break

        return expr

    def parse_primary(self):
        """Parse primary expression (literals, identifiers, etc.)."""
        t = self.current()

        if t.type == TokenType.INT:
            self.pos += 1
            return NumberLiteral(t.value)

        elif t.type == TokenType.FLOAT:
            self.pos += 1
            return NumberLiteral(t.value)

        elif t.type == TokenType.STRING:
            self.pos += 1
            return StringLiteral(t.value)

        elif t.type == TokenType.BOOL:
            self.pos += 1
            return BoolLiteral(t.value)

        elif t.type == TokenType.NULL:
            self.pos += 1
            return NullLiteral()

        elif t.type == TokenType.IDENTIFIER:
            self.pos += 1
            if self.match(TokenType.LBRACE) and self.is_struct_instance_start():
                return self.parse_struct_instance(t.value)
            return Identifier(t.value)

        elif t.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            expr = self.parse_expression()
            self.eat(TokenType.RPAREN)
            return expr

        elif t.type == TokenType.LBRACKET:
            return self.parse_array_literal()

        elif t.type == TokenType.MATCH:
            return self.parse_match()

        elif t.type == TokenType.FSTRING:
            return self.parse_fstring()

        else:
            raise ParseError(
                f"Unexpected token: {t.type.name} ({t.value!r})",
                t.line, t.col
            )

    def parse_fstring(self) -> StringInterp:
        """Parse f-string into alternating string/expression parts.

        The FSTRING token value is a raw template like: "hello {name}, age {age}"
        We split on { } to extract expressions, then lex+parse each one.
        """
        template = self.eat(TokenType.FSTRING).value
        parts = []
        i = 0

        while i < len(template):
            if template[i] == '{':
                # Find matching closing brace
                depth = 1
                start = i + 1
                i += 1
                while i < len(template) and depth > 0:
                    if template[i] == '{':
                        depth += 1
                    elif template[i] == '}':
                        depth -= 1
                    i += 1
                expr_src = template[start:i - 1]
                # Lex and parse the expression
                from .lexer import Lexer
                expr_tokens = Lexer(expr_src).tokenize()
                expr_parser = Parser(expr_tokens)
                expr_node = expr_parser.parse_expression()
                parts.append(expr_node)
            else:
                # Collect literal text until next { or end
                start = i
                while i < len(template) and template[i] != '{':
                    i += 1
                parts.append(StringLiteral(template[start:i]))

        if not parts:
            parts.append(StringLiteral(""))

        return StringInterp(parts)

    def parse_array_literal(self) -> ArrayLiteral:
        """Parse array literal [...]."""
        self.eat(TokenType.LBRACKET)
        elements = []

        while not self.match(TokenType.RBRACKET):
            elements.append(self.parse_expression())
            if self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)

        self.eat(TokenType.RBRACKET)
        return ArrayLiteral(elements)
