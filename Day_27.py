#DAY_27 : Exercise 3: Kaun Banega Crorepati (KBC) 

que = [ "What is the capital of France?",
        "Who is the author of 'Harry Potter' series?",
        "What is the chemical symbol for water?",
        "Which planet is known as the Red Planet?",
        "Who painted the Mona Lisa?",]

options = [
        ["A. Paris", "B. Rome", "C. Madrid", "D. London"],
        ["A. J.K. Rowling", "B. Stephen King", "C. George R.R. Martin", "D. Dan Brown"],
        ["A. H2O", "B. CO2", "C. O2", "D. N2"],
        ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        ["A. Leonardo da Vinci", "B. Michelangelo", "C. Vincent van Gogh", "D. Pablo Picasso"],
    ]

ca= [ "a", "a","a","b", "a"]
prz = [1000,2000,5000,10000,20000]

tp = 0

print("Welcome to KBC! Answer the following questions to win money.")
print("You can quit anytime by typing 'quit'.")
print("")

for i in range(len(que)):
    print(f"Que {i + 1 }: {que[i]}")
    for option in options[i]:
        print(option)
    ua = input("Your Anser (a - d): ")

    if ua  == "quit" or ua == " QUIT":
        break

    if ua == ca[i]:
        print("Correct")
        tp += prz[i]
        print(f"You won Rs. {tp}")
    else:
        print("Incorrect")
        break
print(f"Total Amount: {tp}")