import nltk

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
I ->  epsilon | '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
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
    parser = nltk.ChartParser(grammarChosen)

    # Parse the sentence using the grammar
    try:
        trees = parser.parse(sentence.split())
        print("Sentence is grammatically correct!")
        for tree in trees:
            print(tree)
    except ValueError:
        print("Sentence is not grammatically correct.")
    main()


def main():
    grammar = int(input("Enter the number of the grammar you want to use (1, 2, 3, 4(exit)): "))
    if grammar == 1:
        # Define the input sentence to be parsed
        sentence = input("Enter a sentence (separate the characters with a space): ")
        grammars(grammar1, sentence)
    elif grammar == 2:
        # Define the input sentence to be parsed
        sentence = input("Enter a sentence (separate the characters with a space): ")
        grammars(grammar2, sentence)
    elif grammar == 3:
        # Define the input sentence to be parsed
        sentence = input("Enter a sentence (separate the characters with a space): ")
        grammars(grammar3, sentence)
    elif grammar == 4:
        exit
    else:
        print("Invalid grammar number.")
        main()

main()