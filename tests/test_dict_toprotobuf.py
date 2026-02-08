"""
Tests for dict .toProtobuf() method - convert dict to protobuf-style message.
"""

from silk.interpreter import Interpreter


class TestDictToProtobuf:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toProtobuf_basic(self):
        output = self._run('''
let d = {"name": "Bob"}
print(d.toProtobuf())
''')
        assert output[-1] == 'name: "Bob"'

    def test_toProtobuf_number(self):
        output = self._run('''
let d = {"port": 8080}
print(d.toProtobuf())
''')
        assert output[-1] == 'port: 8080'
