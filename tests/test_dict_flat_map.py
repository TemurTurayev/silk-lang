"""
Tests for dict .flatMap() method.
"""

from silk.interpreter import Interpreter


class TestDictFlatMap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_flatMap_basic(self):
        output = self._run('''
let d = {"a": [1, 2], "b": [3, 4]}
let result = d.flatMap(|k, v| v)
print(result)
''')
        assert output[-1] == "[1, 2, 3, 4]"

    def test_flatMap_transform(self):
        output = self._run('''
let d = {"x": 1, "y": 2}
let result = d.flatMap(|k, v| [k, v])
print(result.length)
''')
        assert output[-1] == "4"
