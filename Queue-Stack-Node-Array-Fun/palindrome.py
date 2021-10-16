'''
Author: Kamron Cole
Originally created for assignment 13.1
Prompts the user for a string and then prints that string's palindrome
'''
import list_stack

def string_to_palindrome(string):
    '''
    Takes in a string and returns its palindrome using a list stack.
    '''
    stack = list_stack.Stack()
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = string
    if string[-1] in vowels:
        for letter in string[:-1]:
            stack.push(letter)
    else:
        for letter in string:
            stack.push(letter)

    for _ in range(stack.size()):
        result += stack.pull()

    return result


def main():
    '''
    Prompts the user for a string and then prints that string's palindrome
    '''
    string = input('Enter a string: ')
    print(string_to_palindrome(string))  


if __name__ == "__main__":
    main()
