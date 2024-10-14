chaine1 = "kayak"
chaine2 = "bonjour"
chaine3 = "radar"
chaine4 = "a"

def palindrome(chaine):
    if chaine == chaine[::-1]:
        return True
    else:
        return False

print(palindrome(chaine1), palindrome(chaine2), palindrome(chaine3), palindrome(chaine4))