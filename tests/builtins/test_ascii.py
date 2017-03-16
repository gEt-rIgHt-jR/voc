from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class AsciiTests(TranspileTestCase):
    def test_ascii_without_unicode(self):
        self.assertCodeExecution("""
            print(ascii("Hello World!"))
            print(ascii('\u0041'))

            string = ''
            for i in range(100):
                print(ascii(chr(i)))
                string += chr(i)
            print(ascii(string))
            """)

    def tset_ascii_list(self):
        self.assertCodeExecution("""
            print(ascii([1, 2, 3, 4, 5]))
            l = ['hello', 'world', 'how', 'are', 'you']
            print(ascii(l))
        """)

    def test_ascii_defs(self):
        self.assertCodeExecution("""
            class TestClass:
                def __init__(self, value):
                    self.value = value;

                def get_incremented_value(self, by):
                    return self.value + by

            print(ascii(TestClass(5).get_incremented_value(5)))
        """)


class BuiltinAsciiFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["ascii"]

    not_implemented = [
        'test_class',
        'test_complex',
        'test_frozenset',
        'test_slice',
        'test_str'
    ]
