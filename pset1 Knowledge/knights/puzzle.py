from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Puzzle rules
    # A can be Knight OR Knave but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # Puzzle implications
    # A is a Knight if A is a Knight and a Knave
    Implication(AKnight, And(AKnight, AKnave)),
    # A is a Knave if A is not a Knight and a Knave
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Puzzle Rules
    # A can be Knight OR Knave but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # B can be Knight OR Knave but not both
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # Puzzle Conditions
    # A is a Knight if A and B are Knaves
    Implication(AKnight, And(AKnave, BKnave)),
    # A is a Knave if A and B are not Knaves
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Puzzle rules
    # Perhaps this isn't required
    # A can be a Knight OR a Knave
    Or(AKnight, AKnave),
    # A is a Knight if A is not a Knave
    Implication(AKnight, Not(AKnave)),
    # B can be a Knight OR a Knave
    Or(BKnight, BKnave),
    # B is a Knight if B is not a Knave
    Implication(BKnight, Not(BKnave)),

    # Puzzle conditions
    # A is a Knight if and only if A is not a Knave
    Biconditional(AKnight, Not(AKnave)),

    # B is a Knight if and only if B is not a Knave
    Biconditional(BKnight, Not(BKnave)),

    # A is a Knight if and only if A and B are Knaves
    Biconditional(AKnight, And(AKnave, BKnave))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Puzzle Rules
    # A is a Knight OR a Knave
    Or(AKnight, AKnave),
    # A is a Knight therefore not a Knave
    Implication(AKnight, Not(AKnave)),
    # B is a Knight OR a Knave
    Or(BKnight, BKnave),
    # B is a Knight therefore not a Knave
    Implication(BKnight, Not(BKnave)),
    # C is a Knight OR a Knave
    Or(CKnight, CKnave),
    # C is a Knight therefore not a Knave
    Implication(CKnight, Not(CKnave)),

    # Puzzle Conditions
    # A is a Knight or Knight if and only if A is a Knight or a Knave
    Biconditional(AKnight, Or(AKnight, AKnave)),
    # B is a Knight if and only if A is a Knight( if and only if A is a Knave)
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),
    # B is a Knight if and only if C is a Knave
    Biconditional(BKnight, CKnave),
    # C is a Knight if C is a Knave
    Biconditional(CKnight, AKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
