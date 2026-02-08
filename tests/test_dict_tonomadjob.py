"""
Tests for dict .toNomadJob() method - convert dict to Nomad job format.
"""

from silk.interpreter import Interpreter


class TestDictToNomadJob:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNomadJob_basic(self):
        output = self._run('''
let d = {"datacenters": "dc1"}
print(d.toNomadJob())
''')
        assert output[-1] == 'datacenters = "dc1"'

    def test_toNomadJob_number(self):
        output = self._run('''
let d = {"count": 3}
print(d.toNomadJob())
''')
        assert output[-1] == 'count = 3'
