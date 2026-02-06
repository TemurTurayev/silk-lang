"""
Tests for string .partition() method.
"""

from silk.interpreter import Interpreter


class TestStringPartition:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_partition_basic(self):
        output = self._run('''
let parts = "hello-world-test".partition("-")
print(parts[0])
print(parts[1])
print(parts[2])
''')
        assert output[-3] == "hello"
        assert output[-2] == "-"
        assert output[-1] == "world-test"

    def test_partition_not_found(self):
        output = self._run('''
let parts = "hello".partition("-")
print(parts[0])
print(parts[1])
print(parts[2])
''')
        assert output[-3] == "hello"
        assert output[-2] == ""
        assert output[-1] == ""

    def test_partition_at_start(self):
        output = self._run('''
let parts = "-hello".partition("-")
print(parts[0])
print(parts[2])
''')
        assert output[-2] == ""
        assert output[-1] == "hello"
