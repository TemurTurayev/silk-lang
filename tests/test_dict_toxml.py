"""
Tests for dict .toXML(root) method.
"""

from silk.interpreter import Interpreter


class TestDictToXML:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toXML_basic(self):
        output = self._run('''
let d = {"name": "Alice", "age": 30}
let xml = d.toXML("person")
print(xml.contains("<name>Alice</name>"))
''')
        assert output[-1] == "true"

    def test_toXML_root(self):
        output = self._run('''
let d = {"x": 1}
let xml = d.toXML("item")
print(xml.starts_with("<item>"))
''')
        assert output[-1] == "true"
