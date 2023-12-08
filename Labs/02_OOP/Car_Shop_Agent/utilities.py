
def get_valid_input(question: str, answer: tuple):
    question += " ({}): ".format(','.join(answer))

    response = input(question)

    while response.lower() not in answer:
        print('Pleas enter valid answer')
        response = input(question)
    return response
