#!/usr/bin/env python3

import io
import sys
import re

class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")  # Raise ValueError if value is not a string
        else:
            self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Split the string into sentences using period, question mark, and exclamation mark as delimiters
        sentences = filter(None, re.split(r'[.!?]', self.value))
        return sum(1 for sentence in sentences if sentence.strip())

# Ensure to import the re module for regular expressions
import re

class TestMyString:
    '''MyString in count_sentences.py'''

    def test_is_class(self):
        '''is a class with the name "MyString".'''
        string = MyString()
        assert(type(string) == MyString)

    def test_value_string(self):
        '''prints "The value must be a string." if not string.'''
        with io.StringIO() as captured_out:
            sys.stdout = captured_out
            try:
                string = MyString()
                string.value = 123
            except ValueError as e:
                assert str(e) == "The value must be a string."
            finally:
                sys.stdout = sys.__stdout__

    def test_is_sentence(self):
        '''returns True if value ends with a period and False otherwise.'''
        assert(MyString("Hello World.").is_sentence() == True)
        assert(MyString("Hello World").is_sentence() == False)

    def test_is_question(self):
        '''returns True if value ends with a question mark and False otherwise.'''
        assert(MyString("Is anybody there?").is_question() == True)
        assert(MyString("Is anybody there").is_question() == False)

    def test_is_exclamation(self):
        '''returns True if value ends with an exclamation mark and False otherwise.'''
        assert(MyString("It's me!").is_exclamation() == True)
        assert(MyString("It's me").is_exclamation() == False)

    def test_count_sentences(self):
        '''returns the number of sentences in the value.'''
        simple_string = MyString("one. two. three?")
        empty_string = MyString()
        complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
        assert(simple_string.count_sentences() == 3)
        assert(empty_string.count_sentences() == 0)
        assert(complex_string.count_sentences() == 4)
