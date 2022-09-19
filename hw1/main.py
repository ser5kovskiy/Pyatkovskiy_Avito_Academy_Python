class CountVectorizer():
    def __init__(self, lowercase=True):
        self.lowercase = lowercase
        self._vocabulary = {}

    def fit_transform(self, lines: list) -> list:
        for idx, line in enumerate(lines):
            for word in line.split():
                self._vocabulary[word.lower()] = 0

        print(lines)

        count_vect = []
        for idx, line in enumerate(lines):
            self._vocabulary = dict.fromkeys(self._vocabulary, 0)
            cur_line_count = []
            for word in line.split():
                self._vocabulary[word.lower()] += 1
            count_vect.append(list(self._vocabulary.values()))
        return count_vect

    def get_feature_names(self):
        return list(self._vocabulary.keys())


def test1():
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    assert(vectorizer.get_feature_names() ==
           ['crock', 'pot', 'pasta', 'never', 'boil',
            'again', 'pomodoro', 'fresh', 'ingredients',
            'parmesan', 'to', 'taste'])
    assert(count_matrix == [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]])


def test2():
    corpus = [
        'HELLO',
        'GOODBYE',
        'hello',
        'goodbye'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    assert(vectorizer.get_feature_names() == ['hello', 'goodbye'])
    assert(count_matrix == [[1, 0], [0, 1], [1, 0], [0, 1]])


def test3():
    corpus = [
        'HELLO hello HeLlO',
        'GOODBYE Hello goodbye',
        'hello',
        'goodbye'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    assert(vectorizer.get_feature_names() == ['hello', 'goodbye'])
    assert(count_matrix == [[3, 0], [1, 2], [1, 0], [0, 1]])


if __name__ == '__main__':
    test1()
    test2()
    test3()
