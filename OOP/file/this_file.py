text_this = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

import this
import re
from collections import Counter
#
class Text:
    def __init__(self):
        self.text = text_this

    def word_manipulation(self, old_word: str = 'Dutch', new_word: str = 'English'):
        self.text = text_this.replace(old_word, new_word)
        print(self.text)

    def count_symbols(self):
        char_count = Counter(self.text)
        print({
            "total_characters": len(self.text),
            "most_common_characters": char_count.most_common(10),
        })

    def take_fragments_in_words(self, fragment):
        print(f'Picked fragment "{fragment}" and how many times in text : ',self.text.lower().count(fragment.lower()))

    def save_to_seperate_file(self, file_name: str = 'new_text.txt'):
        with open(file_name, 'w') as f:
            f.write(self.text)

    def count_lines(self):
        print('How many lines :',len(self.text.split('\n')))

    def take_n_lines(self, n):
        lines = self.text.splitlines()
        print('Takes n Line : ', [lines[i] for i in range(0, len(lines), n)])

    def take_words_starts_with_capital_letter(self):
        capital_letters = re.findall(r'\b[A-Z][a-z]*\b', self.text)
        print('Words start with capital letter: ',capital_letters)

    def delete_words_with_same_symbols(self, x):
        words = self.text.split()
        filtered_words = [word for word in words if all(word.count(char) <= x for char in set(word))]
        print('Words with same symbols: ',filtered_words)

Text().word_manipulation('Dutch', 'Lithuanian')
Text().count_symbols()
Text().take_fragments_in_words('hou')
Text().count_lines()
Text.take_n_lines(Text(), 3)
Text().take_words_starts_with_capital_letter()
Text().delete_words_with_same_symbols(5)
Text().save_to_seperate_file()

