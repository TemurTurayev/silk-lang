"""
Tests for dict .toHTMLList() method.
"""

from silk.interpreter import Interpreter


class TestDictToHTMLList:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toHTMLList_basic(self):
        output = self._run('''
let d = {"name": "Bob"}
let html = d.toHTMLList()
print(html.contains("<li>"))
''')
        assert output[-1] == "true"

    def test_toHTMLList_has_ul(self):
        output = self._run('''
let d = {"x": 1}
let html = d.toHTMLList()
print(html.contains("<ul>"))
''')
        assert output[-1] == "true"
