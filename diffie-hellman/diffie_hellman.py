import secrets

def private_key(p):
    x=secrets.choice(range(2,p))
    return x

    pass


def public_key(p, g, private):
    a=private
    A=(g**a)%p

    return A

    pass


def secret(p, public, private):

    s=(public**private)%p
    return s

    pass
