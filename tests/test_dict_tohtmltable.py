"""
Tests for dict .toHTMLTable() method.
"""

from silk.interpreter import Interpreter


class TestDictToHTMLTable:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toHTMLTable_basic(self):
        output = self._run('''
let d = {"name": "Bob"}
let html = d.toHTMLTable()
print(html.contains("<table>"))
''')
        assert output[-1] == "true"

    def test_toHTMLTable_has_td(self):
        output = self._run('''
let d = {"x": 1}
let html = d.toHTMLTable()
print(html.contains("<td>"))
''')
        assert output[-1] == "true"
