"""
Tests for array .scan() - running/cumulative reduce.
"""

from silk.interpreter import Interpreter


class TestArrayScan:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_scan_sum(self):
        output = self._run('''
print([1, 2, 3, 4].scan(|acc, x| acc + x, 0))
''')
        assert output[-1] == "[1, 3, 6, 10]"

    def test_scan_product(self):
        output = self._run('''
print([1, 2, 3, 4].scan(|acc, x| acc * x, 1))
''')
        assert output[-1] == "[1, 2, 6, 24]"

    def test_scan_empty(self):
        output = self._run('''
print([].scan(|acc, x| acc + x, 0))
''')
        assert output[-1] == "[]"

    def test_scan_single(self):
        output = self._run('''
print([5].scan(|acc, x| acc + x, 0))
''')
        assert output[-1] == "[5]"
