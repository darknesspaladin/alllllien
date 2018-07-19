user_names=['intel','nvidia','amd','admin']
if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print('Hello admin,would you like ti see a status report?')
        else:
            print('hello'+user_name+','+'you are the best!')
else:
    print('we need fing sonme users!')