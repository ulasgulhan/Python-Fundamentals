import validators

if validators.email(input('Email: ')):
    print('Valid')
else:
    print('Invalid')