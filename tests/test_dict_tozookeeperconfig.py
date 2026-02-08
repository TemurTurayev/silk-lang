"""
Tests for dict .toZookeeperConfig() method - ZooKeeper config format.
"""

from silk.interpreter import Interpreter


class TestDictToZookeeperConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toZookeeperConfig_basic(self):
        output = self._run('''
let d = {"dataDir": "/var/zookeeper"}
print(d.toZookeeperConfig())
''')
        assert output[-1] == 'dataDir=/var/zookeeper'

    def test_toZookeeperConfig_number(self):
        output = self._run('''
let d = {"tickTime": 2000}
print(d.toZookeeperConfig())
''')
        assert output[-1] == 'tickTime=2000'
