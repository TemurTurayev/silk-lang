"""
Tests for dict .toSystemdUnit() method - convert dict to systemd unit file format.
"""

from silk.interpreter import Interpreter


class TestDictToSystemdUnit:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSystemdUnit_basic(self):
        output = self._run('''
let d = {"ExecStart": "/usr/bin/nginx"}
print(d.toSystemdUnit())
''')
        assert output[-1] == 'ExecStart=/usr/bin/nginx'

    def test_toSystemdUnit_number(self):
        output = self._run('''
let d = {"Restart": "always"}
print(d.toSystemdUnit())
''')
        assert output[-1] == 'Restart=always'
