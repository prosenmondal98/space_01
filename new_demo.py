questions = {'what is your name?': 'A)rohit B)seema C)rishav D) prosenjit', 'how old are you?': 'A)18 B)19 C)24 D) 22'}
answer = []
correct = ['D', 'C']
marks = 0


def qanda(questions, correct, marks):
    i = 0
    for key, value in questions.items():
        print(key)
        print(value)
        while True:
            user_input = input().upper()
            if user_input in 'ABCD':
                if user_input == correct[i]:
                    marks += 1

                else:
                    print('correct answer is ', correct[i])
                break
            else:
                continue

        i += 1
    return marks


result = qanda(questions, correct, marks)
print('result=', result)