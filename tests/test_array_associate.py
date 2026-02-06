"""
Tests for array .associate() method.
"""

from silk.interpreter import Interpreter


class TestArrayAssociate:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_associate_basic(self):
        output = self._run('''
let result = ["alice", "bob"].associate(|name| [name, name.length])
print(result.get("alice"))
print(result.get("bob"))
''')
        assert output[-2] == "5"
        assert output[-1] == "3"

    def test_associate_numbers(self):
        output = self._run('''
let result = [1, 2, 3].associate(|n| [n, n * n])
print(result.get(1))
print(result.get(3))
''')
        assert output[-2] == "1"
        assert output[-1] == "9"

    def test_associate_length(self):
        output = self._run('''
let result = ["a", "b", "c"].associate(|x| [x, 0])
print(result.length)
''')
        assert output[-1] == "3"
