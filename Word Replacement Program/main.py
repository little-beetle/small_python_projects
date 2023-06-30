def replace_word():
    """
    Replaces the specified word in the string with another specified word.

    :return: None
    """
    # The output line in which the replacement will be performed
    str_user = "hi guys, i am tomi, and hi hi hi hi"

    # Request the user to enter a replacement word
    word_to_replace = input("Enter the word to replace: ")

    # Request the user to enter the word to be replaced
    word_replacement = input("Enter the word to replacement: ")

    # Check if the replacement word is present in the source string
    if word_to_replace in str_user:
        # Replace all occurrences of the word
        print(str_user.replace(word_to_replace, word_replacement))
    else:
        # Output a message if the replacement word is not found
        print("The word to replace is not fount in the string.")


replace_word()