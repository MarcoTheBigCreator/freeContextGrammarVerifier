import nltk
import os

# Define the grammar rules
grammar1 = nltk.CFG.fromstring("""
S -> A B
A -> 'a' A A
A -> 'a' A
A -> 'a'
B -> 'b' B
B -> 'b'
""")

grammar2 = nltk.CFG.fromstring("""
E -> I
E -> E '+' E
E -> E '*' E
E -> '(' E ')'
I ->  ' ' | '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
""")

grammar3 = nltk.CFG.fromstring("""
S -> A B | C
A -> 'a' A 'b' | 'a' 'b'
B -> 'c' B 'd' | 'c' 'd'
C -> 'a' C 'd' | 'a' D 'd'
D -> 'b' D 'c' | 'b' 'c'
""")


def grammars(grammarChosen, sentence):
    # Create a parser using the grammar
    parser = nltk.EarleyChartParser(grammarChosen)

    # Parse the sentence using the grammar
    try:
        chart = parser.chart_parse(sentence)
        if any(chart.parses(grammarChosen.start())):
            print(f'{sentence} is a valid word in the grammar.')
        else:
            print(f'{sentence} is NOT a valid word in the grammar!')
    except ValueError:
        print(f'{sentence} is NOT a valid word in the grammar!')

    answer = input("Do you want to try another sentence? (y/n): ")
    if answer == 'y':
        os.system('cls')
        main()
    elif answer == 'n':
        exit()
    else:
        print("Invalid answer.")


def main():
    grammar = int(input("Enter the number of the grammar you want to use:\n1: Grammar 1\n2: Grammar 2\n3: Grammar "
                        "3\n4: Exit\nOption: "))
    if grammar == 1:
        # Define the input sentence to be parsed
        sentence = input("Enter a sentence: ")
        grammars(grammar1, sentence)
    elif grammar == 2:
        # Define the input sentence to be parsed
        sentence = input("Enter a sentence (use space for empty value): ")
        grammars(grammar2, sentence)
    elif grammar == 3:
        # Define the input sentence to be parsed
        sentence = input("Enter a sentence: ")
        grammars(grammar3, sentence)
    elif grammar == 4:
        exit()
    else:
        print("Invalid grammar number.")
        main()


main()
