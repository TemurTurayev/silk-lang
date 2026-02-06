"""
Tests for array .product() and .mapIndexed() methods.
"""

from silk.interpreter import Interpreter


class TestArrayProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_product_basic(self):
        output = self._run('''
print([1, 2, 3, 4].product())
''')
        assert output[-1] == "24"

    def test_product_with_zero(self):
        output = self._run('''
print([5, 0, 3].product())
''')
        assert output[-1] == "0"

    def test_product_single(self):
        output = self._run('''
print([7].product())
''')
        assert output[-1] == "7"

    def test_product_empty(self):
        output = self._run('''
print([].product())
''')
        assert output[-1] == "1"


class TestArrayMapIndexed:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_map_indexed_basic(self):
        output = self._run('''
let result = ["a", "b", "c"].mapIndexed(|i, v| f"{i}:{v}")
print(result)
''')
        assert output[-1] == "[0:a, 1:b, 2:c]"

    def test_map_indexed_multiply(self):
        output = self._run('''
print([10, 20, 30].mapIndexed(|i, v| v * i))
''')
        assert output[-1] == "[0, 20, 60]"
