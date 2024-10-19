class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = [file_names]

    def get_all_words(self):
        all_words = {}
        for open_file in self.file_names[0]:
            with open(open_file, 'r', encoding='utf-8') as file:
                files = file.read().lower()
                punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for element in punctuation:
                    files.replace(element, '')
                split = files.split()
                all_words[open_file] = split
        return all_words

    def find(self, word):
        dict_ = {}
        ase = 0
        for name, words in WordsFinder.get_all_words(self).items():
            for element in words:
                ase += 1
                if word.lower() in element:
                    dict_[name] = ase
                    break
        return dict_

    def count(self, word):
        dict_ = {}
        ase = 0
        for name, words in WordsFinder.get_all_words(self).items():
            for element in words:
                if word.lower() in element:
                    ase += 1
                    dict_[name] = ase
        return dict_


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

# finder1 = WordsFinder('Rudyard Kipling - If.txt',)
#
# print(finder1.get_all_words())
# print(finder1.find('if'))
# print(finder1.count('if'))
