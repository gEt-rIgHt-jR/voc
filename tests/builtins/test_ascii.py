from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class AsciiTests(TranspileTestCase):
    def test_ascii_without_unicode(self):
        self.assertCodeExecution("""
            print(ascii("Hello World!"))
            print(ascii('\u0041'))

            string = ''
            for i in range(300):
                print(ascii(chr(i)))
                string += chr(i)
            print(ascii(string))
            """)

    def test_ascii_strings_with_quotes(self):
        self.assertCodeExecution(r"""
            for word in ["'", '"', "''''", """""", "'\"\"'",
                "'\"'\"'\"", '\'"\'"\'"', "I'm using \"quotes\"!", 'I"m using \'quotes\'']:
                print(ascii(word))
            """)

    def test_ascii_list(self):
        self.assertCodeExecution("""
            print(ascii([1, 2, 3, 4, 5]))
            l = ['hello', 'world', 'how', 'are', 'you']
            print(ascii(l))
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
