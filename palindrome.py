def palindrome(mots: list):
    compte = 0
    for mot in mots:
        if mot == mot[::-1]:
            compte += 1
    return compte
