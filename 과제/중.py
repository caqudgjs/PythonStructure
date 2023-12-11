def is_palindrome(s):
    # Function to remove punctuation, spaces, and convert to lowercase
    def preprocess_string(s):
        return ''.join(char.lower() for char in s if char.isalnum())

    # Check if the processed string is a palindrome
