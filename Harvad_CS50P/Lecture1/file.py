
x = input('File name: ')

if x.endswith('.gif'):
    print('image/gif')
elif x.endswith('.jpg') or x.endswith('.jpeg'):
    print('image/jpeg')
elif x.endswith('.png'):
    print('image/png')
elif x.endswith('.pdf'):
    print('application/pdf')
elif x.endswith('.zip'):
    print('application/zip')
elif x.endswith('.txt'):
    print('text/plain')
else:
    print('application/octet-stream')



