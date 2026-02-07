"""
Tests for dict .toYAML() method.
"""

from silk.interpreter import Interpreter


class TestDictToYAML:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toYAML_basic(self):
        output = self._run('''
let d = {"name": "Alice", "age": 30}
let yaml = d.toYAML()
print(yaml.contains("name: Alice"))
''')
        assert output[-1] == "true"

    def test_toYAML_format(self):
        output = self._run('''
let d = {"x": 1}
let yaml = d.toYAML()
print(yaml)
''')
        assert output[-1] == "x: 1"
