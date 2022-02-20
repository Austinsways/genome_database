import sqlite3

#this is a connection to he databse. its an object that holds functions that allow us to interact with it.
connection = sqlite3.connect("genetics.db")
#this is a cursor that executes SQL commands.
cursor = connection.cursor()

#This creates the database if it doesnt exist within the folder the program is run inside of.
cursor.execute('''CREATE TABLE IF NOT EXISTS Genomes (Entity_name TEXT, Input_traits INT, Output_traits INT)''')
connection.commit


#user interface here.
quit = True
#This allows us to quit out of the program.
while quit:
    #If the user enters a string instead of an integer or vice/versa this allows the program to continue running.
    try:
        choice = int(input("Please select an option: \n 1) show entitys in the database \n 2) add an entity to the database \n 3) remove an entity from the database\n 4) Change entitys information \n 5) Quit\n"))
        #this ensures that the user enters a valid option.
        if choice > 5 or choice < 1:
            raise ValueError
        
        #this statement carries out the process of showing all the entities
        elif choice == 1:
            #This statement "cursor.execute" sends the contained string as SQL command and exectues it. 
            cursor.execute("SELECT * FROM Genomes;")
            counter = 1
            print("Entitys within the database: ")
            print("")
            #cursor.fetchall() grabs all the items the query returns and puts them into a list of lists we can index by row then column
            for entity in cursor.fetchall():
                print(f"{counter}) Entity_name: {entity[0]}, Input_trait: {entity[1]}, Output_trait: {entity[2]}\n")
                counter += 1

        #This statement allows the user to add an entity into the table. 
        elif choice == 2:
            entity_name = input("Please enter the entitys name: ")
            input_trait = int(input("Please enter the input_traits as numbers: "))
            output_trait = int(input("Please enter the output_traits as a number: "))
            genome = (entity_name, input_trait, output_trait)
            #The execute command can take variables by using questions marks, and inserts them in order from a tuple given as a second parameter.
            cursor.execute("INSERT INTO Genomes VALUES (?, ?, ?)", genome)
            connection.commit()

        #this statement allows the user to remove an entity from the database.
        elif choice == 3:
            removal = input("Enter the name of the entity you would like to remove: ")
            cursor.execute("Select * FROM Genomes;")
            for entity in cursor.fetchall():
                if removal == entity[0]:
                    value = (removal,)
                    #This command deletes the given entity
                    cursor.execute("DELETE FROM Genomes WHERE Entity_name = ?", value)
                    connection.commit()
                    print(f"\nremoved {removal} from the database.\n")
                #if the entity doesnt exist nothing happens.

        #This statement allows the user to alter the attributes of the entity
        elif choice == 4:
            choice = input("What is the entity name of the entity you would like to alter?: ")
            cursor.execute("SELECT * FROM Genomes;")
            for entity in cursor.fetchall():
                #This if statement ensures that nothing happens if the entity doesnt exist within the table.
                if entity[0] == choice:
                    choice2 = int(input("What Would you like to change? \n 1) Entity_name \n 2) Input_trait \n 3) Output_trait \n 4) None, I messed up.\n"))
                    
                    #this alters the entity_name
                    if choice2 == 1:
                        new_value = input("What would you like the new name to be?: ")
                        set_values = (new_value,entity[0])
                        cursor.execute("UPDATE Genomes SET Entity_name = ? WHERE Entity_name = ?;",set_values)
                        connection.commit()
                        print(f"Changed {choice} to {new_value}")
                    
                    #this alters the input_traits
                    elif choice2 == 2:
                        new_value = int(input("What would you like the new Input_traits to be?: "))
                        set_values = (new_value,entity[0])
                        cursor.execute("UPDATE Genomes SET Input_traits = ? WHERE Entity_name = ?;",set_values)
                        connection.commit()
                        print(f"Changed {choice}'s Input_trait to {new_value}.")

                    #this alters the output_traits
                    elif choice2 == 3:
                        new_value = input("What would you like the new Output_traits to be?: ")
                        set_values = (new_value,entity[0])
                        cursor.execute("UPDATE Genomes SET Output_traits = ? WHERE Entity_name = ?;",set_values)
                        connection.commit()
                        print(f"Changed {choice} to {new_value}")
                    
                    else:
                        pass
        
        #This quits the program
        elif choice == 5:
            quit = False
            print("Exiting...")

    #This handles the case of the user entering an incorrect data type
    except ValueError:
        print("please enter an integer, 1-5")

#When the user ends the program this saves there changes and closes the connection.
connection.commit()
connection.close()






