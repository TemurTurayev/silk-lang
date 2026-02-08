"""
Tests for dict .toRabbitmqConfig() method - RabbitMQ config format.
"""

from silk.interpreter import Interpreter


class TestDictToRabbitmqConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRabbitmqConfig_basic(self):
        output = self._run('''
let d = {"listeners.tcp.default": 5672}
print(d.toRabbitmqConfig())
''')
        assert output[-1] == 'listeners.tcp.default = 5672'

    def test_toRabbitmqConfig_string(self):
        output = self._run('''
let d = {"default_user": "guest"}
print(d.toRabbitmqConfig())
''')
        assert output[-1] == 'default_user = guest'
