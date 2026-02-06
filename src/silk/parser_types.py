"""
Silk Type System Parser Mixin

Parsing for struct, enum, interface, impl, and match constructs.
Extracted from parser.py to keep file sizes manageable.
"""

from .tokens import TokenType
from .errors import ParseError
from .ast import (
    Identifier, StructDef, StructField, StructInstance,
    EnumDef, EnumVariant, InterfaceDef, InterfaceMethodSig,
    ImplBlock, MatchExpr, MatchArm
)


class TypeParserMixin:
    """Mixin for type-system related parsing."""

    def parse_struct_def(self) -> StructDef:
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

    def parse_match(self) -> MatchExpr:
        self.eat(TokenType.MATCH)
        value = self.parse_expression()
        self.eat(TokenType.LBRACE)
        self.skip_newlines()

        arms = []
        while not self.match(TokenType.RBRACE):
            if self.current().value == '_':
                pattern = Identifier('_')
                self.pos += 1
            else:
                pattern = self.parse_postfix()

            guard = None
            if self.match(TokenType.IF):
                self.eat(TokenType.IF)
                guard = self.parse_expression()

            self.eat(TokenType.ARROW_MATCH)

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
