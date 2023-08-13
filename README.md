# AirBnB_clone

## About

    The goal of the project is to deploy on your server a simple copy of the AirBnB website.
    Not all the featires of the website are implemented, only some so as to cover all fundamental 
    concepts of the higher level programming track.
    On completetion, we will have a complete web application composed by:

        . A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
        . A website (the front-end) that shows the final product to everybody: static and dynamic
        . A database or files that store data (data = objects)
        . An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

### The Console

    This is the command interpreter. It is the first step towards building the full web application: the AirBnB clone.
    From the console we will be able to:

        . Create a new object (ex: a new User or a new Place)
        . Retrieve an object from a file, a database etc…
        . Do operations on objects (count, compute stats, etc…)
        . Update attributes of an object
        . Destroy an object

#### Starting the console

    You start the console by typing the command below:
        $ ./console.py


#### Using the console

Commands	Sample Usage	            Functionality
help	    help	                    displays all commands available
create	    create <class>	            creates new object of type class
update	    User.update	                updates attribute of an object
destroy	    User.destroy('123')	        destroys specified object
show	    User.show('123')	        retrieve an object from a file, a database
all	        User.all()	                display all objects in class
count	    User.count()	            returns count of objects in specified class
quit	    quit	                    exits

#### Examples

    $ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  all  count  create  destroy  help  quit  show  update

    (hbnb)
    (hbnb)
    (hbnb) create User
    0068a8e3-e8e3-4a65-90c8-0bcd639edbed
    (hbnb) all
    ["[User] (f9694ebe-3b7f-4db6-b4ba-3f252c71d482) {'id': 'f9694ebe-3b7f-4db6-b4ba-3f252c71d482', 'created_at': datetime.datetime(2023, 8, 14, 1, 37, 31, 944987), 'updated_at': datetime.datetime(2023, 8, 14, 1, 37, 31, 945011)}", "[User] (0068a8e3-e8e3-4a65-90c8-0bcd639edbed) {'id': '0068a8e3-e8e3-4a65-90c8-0bcd639edbed', 'created_at': datetime.datetime(2023, 8, 14, 2, 1, 12, 599768), 'updated_at': datetime.datetime(2023, 8, 14, 2, 1, 12, 599821)}"]
    (hbnb) create City
    accb9445-673d-4fc6-973a-2fe3f942c2a3
    (hbnb) show City accb9445-673d-4fc6-973a-2fe3f942c2a3
    [City] (accb9445-673d-4fc6-973a-2fe3f942c2a3) {'id': 'accb9445-673d-4fc6-973a-2fe3f942c2a3', 'created_at': datetime.datetime(2023, 8, 14, 2, 1, 40, 931089), 'updated_at': datetime.datetime(2023, 8, 14, 2, 1, 40, 931163)}
    (hbnb) 
    (hbnb) 
    (hbnb) help update
    update <class name> <id> <attribute name> "<attribute value>"
    (hbnb) quit
    $


## Description of files and directories

    . generate_authors.sh - generates all the contributors to this project repo
    . console.py - entry point to the command interpreter
    . models - this directory contains all classes used for the entire project
    . tests - this directory contains all unit tests
