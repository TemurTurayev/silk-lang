"""
Tests for dict .findKey() and .findValue() methods.
"""

from silk.interpreter import Interpreter


class TestDictFind:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_findKey_basic(self):
        output = self._run('''
let m = {"a": 1, "b": 2, "c": 3}
print(m.findKey(|k, v| v == 2))
''')
        assert output[-1] == "b"

    def test_findKey_not_found(self):
        output = self._run('''
let m = {"a": 1, "b": 2}
print(m.findKey(|k, v| v == 99))
''')
        assert output[-1] == "null"

    def test_findValue_basic(self):
        output = self._run('''
let m = {"x": 10, "y": 20, "z": 30}
print(m.findValue(|k, v| k == "y"))
''')
        assert output[-1] == "20"

    def test_findValue_not_found(self):
        output = self._run('''
let m = {"a": 1}
print(m.findValue(|k, v| k == "nope"))
''')
        assert output[-1] == "null"
