"""
Tests for nested/chained optional access (a?.b?.c).
"""

from silk.interpreter import Interpreter


class TestNestedOptionalChain:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_double_chain_null_first(self):
        output = self._run('''
let x = null
print(x?.a?.b)
''')
        assert output[-1] == "null"

    def test_double_chain_null_middle(self):
        output = self._run('''
struct Outer { inner }
let o = Outer { inner: null }
print(o?.inner?.name)
''')
        assert output[-1] == "null"

    def test_double_chain_valid(self):
        output = self._run('''
struct Inner { value }
struct Outer { inner }
let o = Outer { inner: Inner { value: 42 } }
print(o?.inner?.value)
''')
        assert output[-1] == "42"

    def test_chain_with_coalesce(self):
        output = self._run('''
struct Config { db }
let config = null
let host = config?.db?.host ?? "localhost"
print(host)
''')
        assert output[-1] == "localhost"

    def test_chain_with_method(self):
        output = self._run('''
struct User { name }
let u = User { name: "Alice" }
print(u?.name?.length)
''')
        assert output[-1] == "5"
