"""
Tests for dict .withDefaults(other) method.
"""

from silk.interpreter import Interpreter


class TestDictWithDefaults:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_withDefaults_basic(self):
        output = self._run('''
let d = {"a": 1}
let defaults = {"a": 99, "b": 2, "c": 3}
print(d.withDefaults(defaults))
''')
        assert output[-1] == '{"a": 1, "b": 2, "c": 3}'

    def test_withDefaults_no_overlap(self):
        output = self._run('''
let d = {"a": 1}
let defaults = {"b": 2}
print(d.withDefaults(defaults))
''')
        assert output[-1] == '{"b": 2, "a": 1}'
