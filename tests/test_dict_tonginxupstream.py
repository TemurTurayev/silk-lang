"""
Tests for dict .toNginxUpstream() method - Nginx upstream format.
"""

from silk.interpreter import Interpreter


class TestDictToNginxUpstream:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNginxUpstream_basic(self):
        output = self._run('''
let d = {"backend": "127.0.0.1:8080"}
print(d.toNginxUpstream())
''')
        assert output[-1] == 'server 127.0.0.1:8080;'

    def test_toNginxUpstream_number(self):
        output = self._run('''
let d = {"weight": 5}
print(d.toNginxUpstream())
''')
        assert output[-1] == 'server 5;'
