questions = [
    ["who is Lata mangeshkar", "actor", "singer", "doctor", "dancer", "b"],
    ["what is python", "snake_name", "food", "song", "language", "d"],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", "c"],
    ["What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", "b"],
    ["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", "a"],
    ["What is the square root of 64?", "8", "10", "6", "12", "a"]
]

prize = [100, 200, 300, 400, 500, 700]

i = 0
for q1 in questions:
    print(q1[0])                # fixed: index 0 is the question
    print(f"a.{q1[1]}")
    print(f"b.{q1[2]}")
    print(f"c.{q1[3]}")
    print(f"d.{q1[4]}")

    a = input("choose valid option for the question from this: a/b/c/d\n")

    if a == q1[5]:
        print("correct answer")
    else:
        print("incorrect answer")
        break

    print(f"you won {prize[i]}")
    i = i + 1