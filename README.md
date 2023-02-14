# HBNB
Welcome to the AirBnB clone project:Before starting, please read the AirBnB
This is the console /command interpreter for the alx  Airbnb clone project. The console can be used to store objects in and retrieve objects from a JSON.

### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions/documentation  of commands

To start th program, you need to navigate to the project folder and enter `./console.py` in the shell.

#### Create
`create <class name>`
Example:
`create BaseModel`

#### Show
`show <class name> <object id>`
Example:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`
Example:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`
Example:
`all` or `all State`

#### Quit
`quit` or `EOF`

#### Help
`help` or `help <command>`
Example:
`help` or `help quit`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Example:
`City.show(my_city_id)`

## Resources
* [cmd module](https://docs.python.org/3.8/library/cmd.html)
* [cmd module in depth](https://pymotw.com/2/cmd/)
* [uuid module](https://docs.python.org/3.8/library/uuid.html)
* [datetime](https://docs.python.org/3.8/library/datetime.html)
* [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
* [Testing Your Code with the unittest Module](https://www.youtube.com/watch?v=6tNS--WetLI)
* [Making a command line prompt program in Python](https://www.youtube.com/watch?v=lffgNFRLF9M&t=16s)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
* [cmd module wiki page](https://wiki.python.org/moin/CmdModule)
* [python unittest](https://realpython.com/python-testing/)

