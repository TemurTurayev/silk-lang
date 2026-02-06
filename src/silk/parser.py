"""
Silk Parser

Converts tokens into an Abstract Syntax Tree (AST).
"""

from .tokens import Token, TokenType
from .errors import ParseError
from .ast import (
    Program, NumberLiteral, StringLiteral, BoolLiteral, NullLiteral,
    ArrayLiteral, Identifier, BinaryOp, UnaryOp, Assignment,
    CompoundAssignment, LetDeclaration, IfStatement, WhileLoop, DoWhileLoop,
    ForLoop, FunctionDef, FunctionCall, ReturnStatement,
    BreakStatement, ContinueStatement, IndexAccess, IndexAssign,
    MemberAccess, ImportStmt,
    TestBlock, AssertStatement, StringInterp, TryCatch,
    HashMapLiteral, ThrowStatement, TernaryExpr, MemberAssign,
    MemberCompoundAssign, IndexCompoundAssign, SpreadExpr,
    RangeExpr, TypeofExpr, DestructureLetArray, DestructureLetDict,
    LambdaExpr, OptionalChain, RepeatLoop
)
from .parser_types import TypeParserMixin


class Parser(TypeParserMixin):
    """Recursive descent parser for Silk."""

    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.pos = 0

    def current(self) -> Token:
        return self.tokens[self.pos]

    def peek(self, offset: int = 1) -> Token:
        idx = self.pos + offset
        if idx < len(self.tokens):
            return self.tokens[idx]
        return self.tokens[-1]

    def eat(self, type_: TokenType) -> Token:
        token = self.current()
        if token.type != type_:
            raise ParseError(
                f"Expected {type_.name}, got {token.type.name} ({token.value!r})",
                token.line, token.col
            )
        self.pos += 1
        return token

    def skip_newlines(self) -> None:
        while self.pos < len(self.tokens) and self.current().type == TokenType.NEWLINE:
            self.pos += 1

    def match(self, *types: TokenType) -> bool:
        return self.current().type in types

    def _eat_member_name(self) -> str:
        """Eat a member name after dot - allows keywords as member names."""
        t = self.current()
        if t.type == TokenType.IDENTIFIER:
            self.pos += 1
            return t.value
        if t.value and isinstance(t.value, str) and t.value.isalpha():
            self.pos += 1
            return t.value
        raise ParseError(f"Expected member name, got {t.type.name}", t.line, t.col)

    def is_struct_instance_start(self) -> bool:
        """Check if current position starts a struct instantiation."""
        if not self.match(TokenType.LBRACE):
            return False
        offset = 1
        while self.peek(offset).type == TokenType.NEWLINE:
            offset += 1
        next_token = self.peek(offset)
        if next_token.type != TokenType.IDENTIFIER:
            return False
        offset += 1
        while self.peek(offset).type == TokenType.NEWLINE:
            offset += 1
        return self.peek(offset).type == TokenType.COLON

    def is_hashmap_start(self) -> bool:
        """Check if current position starts a hashmap literal."""
        if not self.match(TokenType.LBRACE):
            return False
        offset = 1
        while self.peek(offset).type == TokenType.NEWLINE:
            offset += 1
        next_token = self.peek(offset)
        if next_token.type == TokenType.COLON:
            return True
        if next_token.type in (
            TokenType.STRING, TokenType.INT, TokenType.FLOAT, TokenType.BOOL
        ):
            offset += 1
            while self.peek(offset).type == TokenType.NEWLINE:
                offset += 1
            return self.peek(offset).type == TokenType.COLON
        return False

    # ═══════════════════════════════════════════════════════════
    # Top-level parsing
    # ═══════════════════════════════════════════════════════════

    def parse(self) -> Program:
        statements = []
        self.skip_newlines()
        while not self.match(TokenType.EOF):
            stmt = self.parse_statement()
            if stmt is not None:
                statements.append(stmt)
            self.skip_newlines()
        return Program(statements)

    def parse_statement(self):
        self.skip_newlines()
        t = self.current()

        if t.type == TokenType.LET:
            return self.parse_let()
        elif t.type == TokenType.CONST:
            return self.parse_const()
        elif t.type == TokenType.FN:
            if self.peek().type == TokenType.IDENTIFIER:
                return self.parse_function_def()
            return self.parse_expression_statement()
        elif t.type == TokenType.IF:
            return self.parse_if()
        elif t.type == TokenType.UNLESS:
            return self.parse_unless()
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
        elif t.type == TokenType.TRY:
            return self.parse_try_catch()
        elif t.type == TokenType.THROW:
            return self.parse_throw()
        elif t.type == TokenType.DO:
            return self.parse_do_while()
        elif t.type == TokenType.REPEAT:
            return self.parse_repeat()
        else:
            return self.parse_expression_statement()

    def parse_block(self) -> list:
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

    # ═══════════════════════════════════════════════════════════
    # Statement parsers
    # ═══════════════════════════════════════════════════════════

    def parse_let(self):
        self.eat(TokenType.LET)
        mutable = False
        if self.match(TokenType.MUT):
            self.eat(TokenType.MUT)
            mutable = True
        if self.match(TokenType.LBRACKET):
            return self._parse_destructure_array()
        if self.match(TokenType.LBRACE):
            return self._parse_destructure_dict()
        name = self.eat(TokenType.IDENTIFIER).value
        type_hint = None
        if self.match(TokenType.COLON):
            self.eat(TokenType.COLON)
            type_hint = self.current().value
            self.pos += 1
        self.eat(TokenType.ASSIGN)
        value = self.parse_expression()
        return LetDeclaration(name, mutable, type_hint, value)

    def parse_const(self):
        self.eat(TokenType.CONST)
        name = self.eat(TokenType.IDENTIFIER).value
        type_hint = None
        if self.match(TokenType.COLON):
            self.eat(TokenType.COLON)
            type_hint = self.current().value
            self.pos += 1
        self.eat(TokenType.ASSIGN)
        value = self.parse_expression()
        return LetDeclaration(name, False, type_hint, value)

    def parse_unless(self):
        self.eat(TokenType.UNLESS)
        condition = UnaryOp('not', self.parse_expression())
        body = self.parse_block()
        else_body = None
        self.skip_newlines()
        if self.match(TokenType.ELSE):
            self.eat(TokenType.ELSE)
            else_body = self.parse_block()
        return IfStatement(condition, body, [], else_body)

    def _parse_destructure_array(self) -> DestructureLetArray:
        self.eat(TokenType.LBRACKET)
        names = []
        rest_name = None
        while not self.match(TokenType.RBRACKET):
            if self.match(TokenType.SPREAD):
                self.eat(TokenType.SPREAD)
                rest_name = self.eat(TokenType.IDENTIFIER).value
            else:
                names.append(self.eat(TokenType.IDENTIFIER).value)
            if self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)
        self.eat(TokenType.RBRACKET)
        self.eat(TokenType.ASSIGN)
        value = self.parse_expression()
        return DestructureLetArray(names, rest_name, value)

    def _parse_destructure_dict(self) -> DestructureLetDict:
        self.eat(TokenType.LBRACE)
        self.skip_newlines()
        names = []
        while not self.match(TokenType.RBRACE):
            names.append(self.eat(TokenType.IDENTIFIER).value)
            if self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)
            self.skip_newlines()
        self.eat(TokenType.RBRACE)
        self.eat(TokenType.ASSIGN)
        value = self.parse_expression()
        return DestructureLetDict(names, value)

    def _parse_params(self) -> list:
        """Parse function parameter list. Returns (name, type_hint, default_expr) tuples."""
        params = []
        self.skip_newlines()
        while not self.match(TokenType.RPAREN):
            pname = self.eat(TokenType.IDENTIFIER).value
            ptype = None
            default = None
            if self.match(TokenType.COLON):
                self.eat(TokenType.COLON)
                ptype = self.current().value
                self.pos += 1
            if self.match(TokenType.ASSIGN):
                self.eat(TokenType.ASSIGN)
                default = self.parse_expression()
            params.append((pname, ptype, default))
            if self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)
            self.skip_newlines()
        return params

    def parse_function_def(self) -> FunctionDef:
        self.eat(TokenType.FN)
        name = self.eat(TokenType.IDENTIFIER).value
        self.eat(TokenType.LPAREN)
        params = self._parse_params()
        self.eat(TokenType.RPAREN)
        return_type = None
        if self.match(TokenType.ARROW):
            self.eat(TokenType.ARROW)
            return_type = self.current().value
            self.pos += 1
        body = self.parse_block()
        return FunctionDef(name, params, return_type, body)

    def parse_if(self):
        self.eat(TokenType.IF)
        condition = self.parse_expression()
        # Ternary form: if cond then expr else expr
        if self.match(TokenType.THEN):
            self.eat(TokenType.THEN)
            then_expr = self.parse_expression()
            self.eat(TokenType.ELSE)
            else_expr = self.parse_expression()
            return TernaryExpr(condition, then_expr, else_expr)
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
        self.eat(TokenType.WHILE)
        condition = self.parse_expression()
        body = self.parse_block()
        else_body = None
        self.skip_newlines()
        if self.match(TokenType.ELSE):
            self.eat(TokenType.ELSE)
            else_body = self.parse_block()
        return WhileLoop(condition, body, else_body)

    def parse_do_while(self) -> DoWhileLoop:
        self.eat(TokenType.DO)
        body = self.parse_block()
        self.skip_newlines()
        self.eat(TokenType.WHILE)
        condition = self.parse_expression()
        return DoWhileLoop(body, condition)

    def parse_repeat(self) -> RepeatLoop:
        self.eat(TokenType.REPEAT)
        count = self.parse_expression()
        body = self.parse_block()
        return RepeatLoop(count, body)

    def parse_for(self) -> ForLoop:
        self.eat(TokenType.FOR)
        first = self.eat(TokenType.IDENTIFIER).value
        index_name = None
        if self.match(TokenType.COMMA):
            self.eat(TokenType.COMMA)
            index_name = first
            first = self.eat(TokenType.IDENTIFIER).value
        self.eat(TokenType.IN)
        iterable = self.parse_expression()
        body = self.parse_block()
        else_body = None
        self.skip_newlines()
        if self.match(TokenType.ELSE):
            self.eat(TokenType.ELSE)
            else_body = self.parse_block()
        return ForLoop(first, iterable, body, index_name, else_body)

    def parse_return(self) -> ReturnStatement:
        self.eat(TokenType.RETURN)
        value = None
        if not self.match(TokenType.NEWLINE, TokenType.EOF, TokenType.RBRACE):
            value = self.parse_expression()
        return ReturnStatement(value)

    def parse_import(self) -> ImportStmt:
        self.eat(TokenType.IMPORT)
        parts = []
        if self.match(TokenType.DOT):
            self.eat(TokenType.DOT)
            self.eat(TokenType.SLASH)
            parts.append(".")
        parts.append(self.eat(TokenType.IDENTIFIER).value)
        while self.match(TokenType.SLASH):
            self.eat(TokenType.SLASH)
            parts.append(self.eat(TokenType.IDENTIFIER).value)
        if parts[0] == ".":
            path = "./" + "/".join(parts[1:])
        else:
            path = "/".join(parts)
        alias = None
        if self.match(TokenType.AS):
            self.eat(TokenType.AS)
            alias = self.eat(TokenType.IDENTIFIER).value
        return ImportStmt(path, alias)

    def parse_test_block(self) -> TestBlock:
        self.eat(TokenType.TEST)
        name = self.eat(TokenType.STRING).value
        body = self.parse_block()
        return TestBlock(name, body)

    def parse_assert(self) -> AssertStatement:
        self.eat(TokenType.ASSERT)
        expression = self.parse_expression()
        return AssertStatement(expression)

    def parse_try_catch(self) -> TryCatch:
        self.eat(TokenType.TRY)
        try_body = self.parse_block()
        self.skip_newlines()
        self.eat(TokenType.CATCH)
        error_name = self.eat(TokenType.IDENTIFIER).value
        catch_body = self.parse_block()
        return TryCatch(try_body, error_name, catch_body)

    def parse_throw(self) -> ThrowStatement:
        self.eat(TokenType.THROW)
        expression = self.parse_expression()
        return ThrowStatement(expression)

    def parse_expression_statement(self):
        expr = self.parse_expression()

        if isinstance(expr, Identifier) and self.match(TokenType.ASSIGN):
            self.eat(TokenType.ASSIGN)
            value = self.parse_expression()
            return Assignment(expr.name, value)

        if isinstance(expr, Identifier) and self.match(
            TokenType.PLUS_ASSIGN, TokenType.MINUS_ASSIGN,
            TokenType.STAR_ASSIGN, TokenType.SLASH_ASSIGN
        ):
            op_map = {
                TokenType.PLUS_ASSIGN: '+', TokenType.MINUS_ASSIGN: '-',
                TokenType.STAR_ASSIGN: '*', TokenType.SLASH_ASSIGN: '/',
            }
            op = op_map[self.current().type]
            self.pos += 1
            value = self.parse_expression()
            return CompoundAssignment(expr.name, op, value)

        if isinstance(expr, IndexAccess) and self.match(TokenType.ASSIGN):
            self.eat(TokenType.ASSIGN)
            value = self.parse_expression()
            return IndexAssign(expr.obj, expr.index, value)

        if isinstance(expr, IndexAccess) and self.match(
            TokenType.PLUS_ASSIGN, TokenType.MINUS_ASSIGN,
            TokenType.STAR_ASSIGN, TokenType.SLASH_ASSIGN
        ):
            op_map = {
                TokenType.PLUS_ASSIGN: '+', TokenType.MINUS_ASSIGN: '-',
                TokenType.STAR_ASSIGN: '*', TokenType.SLASH_ASSIGN: '/',
            }
            op = op_map[self.current().type]
            self.pos += 1
            value = self.parse_expression()
            return IndexCompoundAssign(expr.obj, expr.index, op, value)

        if isinstance(expr, MemberAccess) and self.match(TokenType.ASSIGN):
            self.eat(TokenType.ASSIGN)
            value = self.parse_expression()
            return MemberAssign(expr.obj, expr.member, value)

        if isinstance(expr, MemberAccess) and self.match(
            TokenType.PLUS_ASSIGN, TokenType.MINUS_ASSIGN,
            TokenType.STAR_ASSIGN, TokenType.SLASH_ASSIGN
        ):
            op_map = {
                TokenType.PLUS_ASSIGN: '+', TokenType.MINUS_ASSIGN: '-',
                TokenType.STAR_ASSIGN: '*', TokenType.SLASH_ASSIGN: '/',
            }
            op = op_map[self.current().type]
            self.pos += 1
            value = self.parse_expression()
            return MemberCompoundAssign(expr.obj, expr.member, op, value)

        return expr

    # ═══════════════════════════════════════════════════════════
    # Expression parsing (precedence climbing)
    # ═══════════════════════════════════════════════════════════

    def parse_expression(self):
        return self.parse_pipe()

    def parse_pipe(self):
        left = self.parse_null_coalesce()
        while self.match(TokenType.PIPE):
            self.pos += 1
            right = self.parse_or()
            left = BinaryOp(left, '|>', right)
        return left

    def parse_null_coalesce(self):
        left = self.parse_or()
        while self.match(TokenType.DOUBLE_QUESTION):
            self.pos += 1
            right = self.parse_or()
            left = BinaryOp(left, '??', right)
        return left

    def parse_or(self):
        left = self.parse_and()
        while self.match(TokenType.OR):
            self.pos += 1
            right = self.parse_and()
            left = BinaryOp(left, 'or', right)
        return left

    def parse_and(self):
        left = self.parse_not()
        while self.match(TokenType.AND):
            self.pos += 1
            right = self.parse_not()
            left = BinaryOp(left, 'and', right)
        return left

    def parse_not(self):
        if self.match(TokenType.NOT):
            self.pos += 1
            return UnaryOp('not', self.parse_not())
        return self.parse_comparison()

    def parse_comparison(self):
        left = self.parse_range()
        while self.match(
            TokenType.EQ, TokenType.NEQ, TokenType.LT,
            TokenType.GT, TokenType.LTE, TokenType.GTE
        ):
            op_map = {
                TokenType.EQ: '==', TokenType.NEQ: '!=',
                TokenType.LT: '<', TokenType.GT: '>',
                TokenType.LTE: '<=', TokenType.GTE: '>=',
            }
            op = op_map[self.current().type]
            self.pos += 1
            right = self.parse_range()
            left = BinaryOp(left, op, right)
        return left

    def parse_range(self):
        left = self.parse_addition()
        if self.match(TokenType.DOTDOT):
            self.pos += 1
            right = self.parse_addition()
            return RangeExpr(left, right)
        return left

    def parse_addition(self):
        left = self.parse_multiplication()
        while self.match(TokenType.PLUS, TokenType.MINUS):
            op = '+' if self.current().type == TokenType.PLUS else '-'
            self.pos += 1
            right = self.parse_multiplication()
            left = BinaryOp(left, op, right)
        return left

    def parse_multiplication(self):
        left = self.parse_power()
        while self.match(TokenType.STAR, TokenType.SLASH, TokenType.PERCENT):
            op_map = {
                TokenType.STAR: '*', TokenType.SLASH: '/', TokenType.PERCENT: '%'
            }
            op = op_map[self.current().type]
            self.pos += 1
            right = self.parse_power()
            left = BinaryOp(left, op, right)
        return left

    def parse_power(self):
        left = self.parse_unary()
        if self.match(TokenType.POWER):
            self.pos += 1
            right = self.parse_power()
            left = BinaryOp(left, '**', right)
        return left

    def parse_unary(self):
        if self.match(TokenType.MINUS):
            self.pos += 1
            return UnaryOp('-', self.parse_unary())
        if self.match(TokenType.TYPEOF):
            self.pos += 1
            return TypeofExpr(self.parse_unary())
        return self.parse_postfix()

    def parse_postfix(self):
        expr = self.parse_primary()
        while True:
            if self.match(TokenType.LPAREN):
                self.eat(TokenType.LPAREN)
                self.skip_newlines()
                args = []
                while not self.match(TokenType.RPAREN):
                    args.append(self.parse_expression())
                    if self.match(TokenType.COMMA):
                        self.eat(TokenType.COMMA)
                    self.skip_newlines()
                self.eat(TokenType.RPAREN)
                expr = FunctionCall(expr, args)
            elif self.match(TokenType.LBRACKET):
                self.eat(TokenType.LBRACKET)
                index = self.parse_expression()
                self.eat(TokenType.RBRACKET)
                expr = IndexAccess(expr, index)
            elif self.match(TokenType.DOT):
                self.eat(TokenType.DOT)
                member = self._eat_member_name()
                expr = MemberAccess(expr, member)
                if self.match(TokenType.LBRACE) and self.is_struct_instance_start():
                    instance = self.parse_struct_instance(member)
                    instance.struct_ref = expr
                    expr = instance
            elif self.match(TokenType.QUESTION_DOT):
                self.eat(TokenType.QUESTION_DOT)
                member = self._eat_member_name()
                expr = OptionalChain(expr, member)
            else:
                break
        return expr

    def parse_primary(self):
        t = self.current()
        if t.type in (TokenType.INT, TokenType.FLOAT):
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
        elif t.type == TokenType.LBRACE and self.is_hashmap_start():
            return self.parse_hashmap()
        elif t.type == TokenType.IF:
            return self.parse_if()
        elif t.type == TokenType.MATCH:
            return self.parse_match()
        elif t.type == TokenType.FSTRING:
            return self.parse_fstring()
        elif t.type == TokenType.FN:
            return self.parse_anonymous_fn()
        elif t.type == TokenType.BAR:
            return self.parse_lambda()
        else:
            raise ParseError(
                f"Unexpected token: {t.type.name} ({t.value!r})",
                t.line, t.col
            )

    # ═══════════════════════════════════════════════════════════
    # Literal / special parsers
    # ═══════════════════════════════════════════════════════════

    def parse_lambda(self) -> LambdaExpr:
        self.eat(TokenType.BAR)
        params = []
        while not self.match(TokenType.BAR):
            params.append(self.eat(TokenType.IDENTIFIER).value)
            if self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)
        self.eat(TokenType.BAR)
        body = self.parse_expression()
        return LambdaExpr(params, body)

    def parse_anonymous_fn(self) -> FunctionDef:
        self.eat(TokenType.FN)
        self.eat(TokenType.LPAREN)
        params = self._parse_params()
        self.eat(TokenType.RPAREN)
        return_type = None
        if self.match(TokenType.ARROW):
            self.eat(TokenType.ARROW)
            return_type = self.current().value
            self.pos += 1
        body = self.parse_block()
        return FunctionDef("", params, return_type, body)

    def parse_fstring(self) -> StringInterp:
        template = self.eat(TokenType.FSTRING).value
        parts = []
        i = 0
        while i < len(template):
            if template[i] == '{':
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
                from .lexer import Lexer
                expr_tokens = Lexer(expr_src).tokenize()
                expr_parser = Parser(expr_tokens)
                expr_node = expr_parser.parse_expression()
                parts.append(expr_node)
            else:
                start = i
                while i < len(template) and template[i] != '{':
                    i += 1
                parts.append(StringLiteral(template[start:i]))
        if not parts:
            parts.append(StringLiteral(""))
        return StringInterp(parts)

    def parse_hashmap(self) -> HashMapLiteral:
        self.eat(TokenType.LBRACE)
        self.skip_newlines()
        pairs = []
        if self.match(TokenType.COLON):
            self.eat(TokenType.COLON)
            self.eat(TokenType.RBRACE)
            return HashMapLiteral(pairs)
        while not self.match(TokenType.RBRACE):
            key = self.parse_expression()
            self.eat(TokenType.COLON)
            value = self.parse_expression()
            pairs.append((key, value))
            if self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)
            self.skip_newlines()
        self.eat(TokenType.RBRACE)
        return HashMapLiteral(pairs)

    def parse_array_literal(self):
        self.eat(TokenType.LBRACKET)
        self.skip_newlines()
        elements = []
        while not self.match(TokenType.RBRACKET):
            if self.match(TokenType.SPREAD):
                self.eat(TokenType.SPREAD)
                elements.append(SpreadExpr(self.parse_expression()))
            else:
                elements.append(self.parse_expression())
            if self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)
            self.skip_newlines()
        self.eat(TokenType.RBRACKET)
        return ArrayLiteral(elements)
