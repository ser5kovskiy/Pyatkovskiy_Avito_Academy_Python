import pytest


LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': ' '
}


MORSE_TO_LETTER = dict([(value, key)
                       for key, value in LETTER_TO_MORSE.items()])


@pytest.mark.parametrize(
    "morse_message, result",
    [('.... . .-.. .-.. ---  - .... . .-. .', 'HELLO THERE'),
     ('--. . -. . .-. . .- .-..  -.- . -. --- -... ..', 'GENEREAL KENOBI'),
     ('... --- ...', 'SOS'), ],
)
def test_decode(morse_message, result) -> str:
    """
    Декодирует строку из азбуки Морзе в английский
    """

    decoded_letters = [
        MORSE_TO_LETTER[letter] if letter else ' ' for letter in morse_message.split(' ')
    ]

    cur_result = ''.join(decoded_letters)
    assert cur_result == result
