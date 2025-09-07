# Azriel Ehrlich 213662539
# principles of programming languages - ex1.3

gematria = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5,
    'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
    'י': 10, 'כ': 20, 'ל': 30, 'מ': 40,
    'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90,
    'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400
}
def gematria_value(word):
    """Return the gematria value of a Hebrew word."""
    return sum(map(lambda char: gematria.get(char, 0), word))

# example
print(gematria_value('מגניב'))