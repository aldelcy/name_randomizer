import io
import random
import os

cwd = os.getcwd()

file_path = cwd+"/students.txt"

with open(file_path, "r") as file:
    data = file.readlines()

student_list = "Steven Barkley, Anthony Becerra, Jahaziel Ben Israel, Moises Castano, Lasaly Changkachith, Stephanie Cherubin, Ant-quanique  Dancy, Evelyn Feristin, Zico Fremont, Brandon Gant, Maruschka Germain, Jonathan Guerrero Nunez, Jasmine Harris, Peter Hernandez, Jason Hesch, Maximo Hinojosa, Juan Hurtado, Julie Hutchinson, Gloria Jimenez, Malcolm Jordan, Laquandra Lane, Christian Leon, Nicholas Montanino, Danny Neira, Raymond Pache, Edward Pache, Timothy Paulk, Adler Pierre, Judy Rincon, Kitiara Rivera, Mike Rosbrough, Diego Sanchez, Neil Vilain"




if len(data) != 0:
    students = data[0].split(", ")
    
    roll=True

    while roll:

        random_stud = random.choice(students)
        print("\n\n --------------------- \n\n")
        print("\033[93m \033[1m \033[4m" + random_stud + "\033[0m")
        print("\n\n ---------------------")

        
        contin = False
        while contin!=True :
            try:
                action = input("what would you like to do? \n [ 1) \033[93mrs\033[0m (remove student) ]\n [ 2) \033[93mrl\033[0m (reset list) ] \n [ 3) \033[93mroll\033[0m (roll again) ] \n [ exit ]:  \n")
            except SyntaxError:
                print(' you entered nothing ')

            if action == "rs":
                
                confirm = input("Are you sure you want to remove \033[93m"+random_stud+"\033[0m ? [yes(y)/no(n)] ")

                if confirm == "yes" | confirm == "y":
                    students.remove(random_stud)
                    print("\n \033[93m ", random_stud, "\033[0m has been \033[31m removed \033[0m from the list. \n")
                elif confirm == "no" | confirm == "n":
                    print("\n \033[93m ", random_stud, "\033[0m  \033[32m remains \033[0m in the list. \n")
                    
                roll=True
                contin=True
                data[0] = ", ".join(students)
                print("\n \n >>", len(students), "students left to come up.\n \n ")

            elif action == "rl":
                data = student_list
                contin=True
                roll=False
                print("\n \033[32m The list has been reset :) \033[0m \n")

            elif action=="roll" or None:
                contin=True
                roll=True
                print("\n ROOOOOLIN...")
                print("...")
                print("...")
            
            elif action == "exit":
                roll=False
                print("\n\n Nothing has been done to the list... Bye \n\n")
                break
            
            else :
                contin=True
                roll=False
                print("\n Sorry, could not unerstand what you typed... :(  ")


else:
    print("\n\n --------------------- \n\n")
    print("\n No More students, Reseting the list")
    print("\n\n ---------------------")
    data = student_list







with open(file_path, "w") as file:
    file.writelines( data )