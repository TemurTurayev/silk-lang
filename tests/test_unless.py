"""
Tests for unless statement (syntactic sugar for if not).
"""

from silk.interpreter import Interpreter


class TestUnless:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_unless_false_executes(self):
        output = self._run('''
let x = false
unless x {
    print("executed")
}
''')
        assert output[-1] == "executed"

    def test_unless_true_skips(self):
        output = self._run('''
let x = true
unless x {
    print("should not print")
}
print("done")
''')
        assert output[-1] == "done"

    def test_unless_else(self):
        output = self._run('''
let x = true
unless x {
    print("no")
} else {
    print("yes")
}
''')
        assert output[-1] == "yes"

    def test_unless_condition(self):
        output = self._run('''
let age = 20
unless age < 18 {
    print("adult")
}
''')
        assert output[-1] == "adult"
