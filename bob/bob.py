def response(hey_bob):
    if(hey_bob.strip().endswith("?")==True and hey_bob.isupper()==False ):
        return 'Sure.'
    elif(hey_bob.isupper()==True and hey_bob.endswith("?")==False):
        return 'Whoa, chill out!'
    elif(hey_bob.isupper()==True and hey_bob.endswith("?")==True):
        return "Calm down, I know what I'm doing!"
    elif(len(hey_bob.strip())==0):
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
    pass
