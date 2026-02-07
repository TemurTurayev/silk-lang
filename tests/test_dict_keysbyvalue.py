"""
Tests for dict .keysByValue(val) method.
"""

from silk.interpreter import Interpreter


class TestDictKeysByValue:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_keysByValue_found(self):
        output = self._run('''
let d = {"a": 1, "b": 2, "c": 1, "d": 3}
print(d.keysByValue(1))
''')
        assert output[-1] == '[a, c]'

    def test_keysByValue_none(self):
        output = self._run('''
let d = {"a": 1, "b": 2}
print(d.keysByValue(99))
''')
        assert output[-1] == '[]'
