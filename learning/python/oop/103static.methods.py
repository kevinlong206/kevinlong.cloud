class String:

    @staticmethod
    def is_palindrome(s, case_insensitive=True):
        # we allow only letters and numbers
        s = ''.join(c for c in s if c.isalnum()) # study this

        # for case insensitive comparison, we lowercase s
        if case_insensitive:
            s = s.lower()

        for c in range(len(s) // 2):
            if s[c] != s[-c -1]:
                return False
            return True

    @staticmethod
    def get_unique_words(sentence):
        return set(sentence.split())

print(String.is_palindrome('Radar', case_insensitive=False))

print(String.is_palindrome('A nut for a har of tuna'))

print(String.is_palindrome('Never Odd, Or Even!'))

print(String.is_palindrome('In Girum Imus Nocte Consumimur Igni'))

print(String.get_unique_words('I love palindromes. I really really love them!'))
