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
    MemberAccess
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
            return Identifier(t.value)

        elif t.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            expr = self.parse_expression()
            self.eat(TokenType.RPAREN)
            return expr

        elif t.type == TokenType.LBRACKET:
            return self.parse_array_literal()

        else:
            raise ParseError(
                f"Unexpected token: {t.type.name} ({t.value!r})",
                t.line, t.col
            )

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
