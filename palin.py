def is_palindrome(s: str) -> bool:
    # Remove spaces and convert to lowercase for uniformity
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Example usage
word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
