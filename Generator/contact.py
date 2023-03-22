from model.contact import Contact
import random
import string
import re
import jsonpickle
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n=5
f="..\\data\\contacts.json"

for o,a in opts:
    if o=="-n":
        n=int(a)
    elif o=="-f":
        f=a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix+"".join(
                         [random.choice(symbols) for i in range(
                                                                random.randrange(maxlen))])# случайная длина
def clear(s):
    return re.sub("  ", " ", s)

# Одна пустой и 5 непустых контактов
testdata =[Contact(firstname="", lastname="", address="")]+ [Contact(
    firstname = clear(str.strip(random_string("firstname",10))), lastname = clear(str.strip(random_string("lastname",20))),
                                                         address=clear(str.strip(random_string("address",15))))
                                                   for i in  range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), f)
with open(file, "w") as out:
    #out.write(json.dumps(testdata, default = lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(testdata))