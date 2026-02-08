"""
Tests for dict .toXML() method - convert dict to XML string.
"""

from silk.interpreter import Interpreter


class TestDictToXML:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toXML_basic(self):
        output = self._run('''
let d = {"name": "Bob"}
print(d.toXML())
''')
        assert output[-1] == '<root><name>Bob</name></root>'

    def test_toXML_number(self):
        output = self._run('''
let d = {"age": 30}
print(d.toXML())
''')
        assert output[-1] == '<root><age>30</age></root>'
