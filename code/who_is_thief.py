"""
Four suspects; one of them is a thief. In interrogation
    John said: I am not the thief.
    Paul said: George is the thief.
    George said: It must be Ringo.
    Ringo said: George is lying.

Among them, three are telling the truth while one is lying.
Could you find out who is the thief?

"""


suspects = ["John", "Paul", "George", "Ringo"]
for real_theif in suspects:
    if (
        sum(
            [
                "John" != real_theif,
                "George" == real_theif,
                "Ringo" == real_theif,
                "Ringo" != real_theif,
            ]
        )
        == 3
    ):
        print(real_theif)
