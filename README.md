# Overview

This is a Python program written to interact and change a database created to hold the genomes of neural networks created within the neural net program. It stores the entitys name, input traits and output traits.

This software will allow me to hold data for surviving entities and put them against eachother to compete for resources to find the most resilient genome possible. It also holds dating showing which genomes do the best within there given environment.

[Software Demo Video](https://www.youtube.com/watch?v=VrF79ZdAoJ4)

# Relational Database

The relationsal database I'm using is called genetics.db, it currently holds only one table.

The Genomes table hold each entity and its input and output traits.

# Development Environment

This program was written in VScode, SQlite and was better visualized using SQliteStudio.

This program is written in Python and requires the sqlite3 library to be used. The language used within SQlite is SQL.

# Useful Websites

* [sqlitetutorial](https://www.sqlitetutorial.net/)
* [w3schools, SQL tutorial](https://www.w3schools.com/sql/default.asp)

# Future Work
* Integrate the databse to work in tadem with the Neural Network without the need for user input.
* Create a variable or table for different developement environment the genome has been tested inside of or came from.
* Place error handling within the program to better handle SQlite SQL syntax errors.
