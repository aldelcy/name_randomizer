import io
import random
import os

cwd = os.getcwd()+"/"+os.path.basename(os.path.dirname(os.path.realpath(__file__)))

file_path = cwd+"/students.txt"

with open(file_path, 'r') as file:
    data = file.readlines()

student_list = "Steven Barkley, Anthony Becerra, Jahaziel Ben Israel, Moises Castano, Lasaly Changkachith, Stephanie Cherubin, Ant-quanique  Dancy, Evelyn Feristin, Zico Fremont, Brandon Gant, Maruschka Germain, Jonathan Guerrero Nunez, Jasmine Harris, Peter Hernandez, Jason Hesch, Maximo Hinojosa, Juan Hurtado, Julie Hutchinson, Gloria Jimenez, Malcolm Jordan, Laquandra Lane, Christian Leon, Nicholas Montanino, Danny Neira, Raymond Pache, Edward Pache, Timothy Paulk, Adler Pierre, Judy Rincon, Kitiara Rivera, Mike Rosbrough, Diego Sanchez, Neil Vilain"


print("\n\n --------------------- \n\n")

if len(data) != 0:
    students = data[0].split(', ')
    random_stud = random.choice(students)

    print('\033[93m \033[1m \033[4m' + random_stud + '\033[0m')
        
    print("\n\n ---------------------")

    
    contin = False
    while contin!=True :
        action = input("what would you like to do?  [ \033[93m rs \033[0m (remove student) / \033[93m rl \033[0m (reset list) / \033[93m dn \033[0m ( do nothing )   /  exit ]:  \n")
        if action == 'rs':
            students.remove(random_stud)
            contin = True
            print("\n \033[93m ", random_stud, "\033[0m has been \033[31m removed \033[0m from the list. \n")
            data[0] = ', '.join(students)
            print("\n \n >>", len(students), "students left to come up.\n \n ")

        elif action == "rl":
            data = student_list
            contin = True
            print("\n \033[32m The list has been reset :) \033[0m \n")

        elif action == "dn":
            contin = True
            print("\n Nothing has been done to the list :)\n")
        
        elif action == "exit": break
        else :
            print("\n Please choose ( rs, rl, dn or exit )\n")
            contin = False


else:
    print('\n No More students, Reseting the list')
    data = student_list

    print("\n\n ---------------------")







with open(file_path, 'w') as file:
    file.writelines( data )