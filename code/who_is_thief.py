"""
Four individuals are suspected of theft, but only one of them is the actual thief. During an interrogation, they made the following statements:

    John: "I am not the thief."
    Paul: "George is the thief."
    George: "It must be Ringo."
    Ringo: "George is lying."

An informant has revealed that among these four suspects, three are telling the truth, and one is lying. Can you determine who the actual thief is based on these statements?
"""


















suspects = ["John", "Paul", "George", "Ringo"]

for real_theif in suspects:
    statements = [
        "John" != real_theif,
        "George" == real_theif,
        "Ringo" == real_theif,
        "Ringo" != real_theif,
    ]
    if sum(statements) == 3:
        print(real_theif)
