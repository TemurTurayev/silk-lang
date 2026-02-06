"""
Tests for HashMap/Dict data type.

Syntax: { "key": value, "key2": value2 }
Access: map["key"] or map.get("key")
"""

import pytest
from silk.lexer import Lexer
from silk.tokens import TokenType
from silk.parser import Parser
from silk.ast import HashMapLiteral
from silk.interpreter import Interpreter


# ═══════════════════════════════════════════════════════════
# PARSER
# ═══════════════════════════════════════════════════════════

class TestHashMapParser:

    def test_parse_empty_hashmap(self):
        tokens = Lexer('{:}').tokenize()
        ast = Parser(tokens).parse()
        node = ast.statements[0]
        assert isinstance(node, HashMapLiteral)
        assert len(node.pairs) == 0

    def test_parse_hashmap_literal(self):
        tokens = Lexer('{"name": "Alice", "age": 30}').tokenize()
        ast = Parser(tokens).parse()
        node = ast.statements[0]
        assert isinstance(node, HashMapLiteral)
        assert len(node.pairs) == 2

    def test_parse_hashmap_in_let(self):
        tokens = Lexer('let m = {"x": 1}').tokenize()
        ast = Parser(tokens).parse()
        assert len(ast.statements) == 1


# ═══════════════════════════════════════════════════════════
# INTERPRETER
# ═══════════════════════════════════════════════════════════

class TestHashMapInterpreter:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_create_hashmap(self):
        output = self._run('''
let m = {"name": "Alice", "age": 30}
print(type(m))
''')
        assert output[-1] == "map"

    def test_hashmap_index_access(self):
        output = self._run('''
let m = {"name": "Alice", "age": 30}
print(m["name"])
print(m["age"])
''')
        assert output[0] == "Alice"
        assert output[1] == "30"

    def test_hashmap_index_assign(self):
        output = self._run('''
let mut m = {"x": 1}
m["x"] = 42
m["y"] = 100
print(m["x"])
print(m["y"])
''')
        assert output[0] == "42"
        assert output[1] == "100"

    def test_hashmap_print(self):
        output = self._run('''
let m = {"a": 1}
print(m)
''')
        assert output[-1] == '{"a": 1}'

    def test_empty_hashmap(self):
        output = self._run('''
let m = {:}
print(m)
''')
        assert output[-1] == '{}'

    def test_hashmap_length(self):
        output = self._run('''
let m = {"a": 1, "b": 2, "c": 3}
print(m.length)
''')
        assert output[-1] == "3"

    def test_hashmap_keys(self):
        output = self._run('''
let m = {"x": 10, "y": 20}
let k = m.keys()
print(len(k))
''')
        assert output[-1] == "2"

    def test_hashmap_values(self):
        output = self._run('''
let m = {"x": 10, "y": 20}
let v = m.values()
print(len(v))
''')
        assert output[-1] == "2"

    def test_hashmap_contains_key(self):
        output = self._run('''
let m = {"name": "Alice"}
print(m.has("name"))
print(m.has("missing"))
''')
        assert output[0] == "true"
        assert output[1] == "false"

    def test_hashmap_delete(self):
        output = self._run('''
let mut m = {"a": 1, "b": 2}
m.delete("a")
print(m.length)
print(m.has("a"))
''')
        assert output[0] == "1"
        assert output[1] == "false"

    def test_hashmap_int_keys(self):
        output = self._run('''
let m = {1: "one", 2: "two"}
print(m[1])
print(m[2])
''')
        assert output[0] == "one"
        assert output[1] == "two"

    def test_hashmap_iterate_keys(self):
        output = self._run('''
let m = {"a": 1, "b": 2}
for key in m.keys() {
    print(key)
}
''')
        assert len(output) == 2

    def test_hashmap_nested(self):
        output = self._run('''
let m = {"inner": {"x": 42}}
print(m["inner"]["x"])
''')
        assert output[-1] == "42"

    def test_hashmap_with_expressions(self):
        output = self._run('''
let m = {"sum": 1 + 2, "prod": 3 * 4}
print(m["sum"])
print(m["prod"])
''')
        assert output[0] == "3"
        assert output[1] == "12"

    def test_hashmap_undefined_key_error(self):
        output = self._run('''
let m = {"a": 1}
try {
    let x = m["missing"]
} catch e {
    print("caught")
}
''')
        assert output[-1] == "caught"

    def test_hashmap_in_function(self):
        output = self._run('''
fn make_point(x, y) {
    return {"x": x, "y": y}
}
let p = make_point(3, 4)
print(p["x"])
print(p["y"])
''')
        assert output[0] == "3"
        assert output[1] == "4"
