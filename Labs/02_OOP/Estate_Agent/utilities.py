

def get_valid_input(input_question: str, valid_options: tuple):
    input_question += " ({}): ".format(','.join(valid_options))

    response = input(input_question)

    while response.lower() not in valid_options:
        print('Please type into valid options.!')
        response = input(input_question)

    return response
