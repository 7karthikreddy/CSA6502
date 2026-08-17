print("COLLEGE DOMAIN CHATBOT")
print("=" * 35)

knowledge = {
    "admission": "Admissions are based on eligibility and entrance requirements.",
    "fees": "Students can pay fees through the college payment portal.",
    "attendance": "Students should maintain the required attendance percentage.",
    "exam": "Examinations are conducted according to the academic schedule."
}

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Bot: Goodbye!")
        break

    found = False

    for key in knowledge:

        if key in question.lower():

            print("Bot:", knowledge[key])
            found = True
            break

    if not found:
        print("Bot: Sorry, I could not find the answer.")
