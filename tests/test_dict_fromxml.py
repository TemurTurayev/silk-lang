"""
Tests for dict .fromXML(xml) static-like method via string.
"""

from silk.interpreter import Interpreter


class TestDictFromXML:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_fromXML_basic(self):
        output = self._run('''
let xml = "<person><name>Alice</name><age>30</age></person>"
let d = xml.parseXML()
print(d.get("name"))
''')
        assert output[-1] == "Alice"

    def test_fromXML_value(self):
        output = self._run('''
let xml = "<item><x>1</x></item>"
let d = xml.parseXML()
print(d.get("x"))
''')
        assert output[-1] == "1"
