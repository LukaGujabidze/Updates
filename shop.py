import smtplib, ssl
import os


#this lines creates classes for animals
class dog:
    name = ''
    age = 0
    color = ''
    eye_color = ''
    tail_lengh = 0
    def info(name):
        information = 'pet name is : %s pet age is %s pet color is %s pet eye color is %s pet tail lengh is %s' % (name.name, str(name.age), name.color, name.eye_color, str(name.tail_lengh))
        return information
        

class cat:
    name = ''
    age = 0
    color = ''
    eye_color = ''
    tail_lengh = 0
    def info(name):
        information = 'pet name is : %s pet age is %s pet color is %s pet eye color is %s pet tail lengh is %s' % (name.name, str(name.age), name.color, name.eye_color, str(name.tail_lengh))
        return information


class fish:
    name = ''
    age = 0
    color = ''
    def info(name):
        information = 'pet name is : %s pet age is %s pet color is %s ' % (name.name,str(name.age),name.color)
        return information



port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "druncha.fum@gmail.com"

#We take environment varieble from os(operation system)
password = str(os.environ.get('DRUNCHA'))

#this lines takes inputs from user

mail = input('Type your E-mail: ')
animal = input('Choose your animal: we only have(cat,dog,fish): ')

#this lines checks input and which animal want user
while True:
    if animal == 'dog':
        animal = dog
        #this inputs takes usets information for animal
        animal.name = input("Choose your animal name: ")
        animal.age = input('Choose your animal age: ')
        animal.color = input('Choose your animal color: ')
        animal.eye_color = input('Choose you animal eye color: ')
        animal.tail_lengh = input('Choose your animal tail lengh: ')
        break

    elif animal == 'cat':
        animal = cat
        #this inputs takes usets information for animal
        animal.name = input("Choose your animal name: ")
        animal.age = input('Choose your animal age: ')
        animal.color = input('Choose your animal color: ')
        animal.eye_color = input('Choose you animal eye color: ')
        animal.tail_lengh = input('Choose your animal tail lengh: ')
        break

    elif animal == 'fish':
        animal = fish
        #this inputs takes usets information for animal
        animal.name = input("Choose your animal name: ")
        animal.age = input('Choose your animal age: ')
        animal.color = input('Choose your animal color: ')
        break
    else:
        print('we only have cat, dog and fish')
        animal = input("Choose your animal: ")
        break

#this variebles stores animal information and message to send
animal_info = animal.info(animal)
message = 'Contgrants! Your animal sucsesfuly created! ' + '     ' + animal_info  


#this lines send message to user
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, mail, message)


