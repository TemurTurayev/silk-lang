"""
Tests for dict .toMarkdown() method - markdown table row.
"""

from silk.interpreter import Interpreter


class TestDictToMarkdown:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMarkdown_basic(self):
        output = self._run('''
let d = {"name": "Bob", "age": 30}
let md = d.toMarkdown()
print(md.contains("name"))
''')
        assert output[-1] == "true"

    def test_toMarkdown_header(self):
        output = self._run('''
let d = {"x": 1}
let md = d.toMarkdown()
print(md.contains("|"))
''')
        assert output[-1] == "true"
