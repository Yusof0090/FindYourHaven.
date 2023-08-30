def handleuploadedfile(f):
    with open('media/members'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)