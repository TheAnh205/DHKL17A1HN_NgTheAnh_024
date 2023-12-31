arivals = ['Adela','Fleda','Owen',
           'May','Mona','Gilbert','Ford']


def party_late(arivals,name):
    if(arivals.index(name)+1)==(len(arivals)):
        return False
    if(arivals.index(name)+1)>(len(arivals)/2):
        return True
    else:
        False

print(party_late(arivals,name='Gilbert'))
print(party_late(arivals,name="Ford"))
print(party_late(arivals,name="Mona"))
