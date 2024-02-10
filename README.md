# Trycode-Programming-Language-Compiler
Project of the Programming Paradigms course, National University of Costa Rica.

TryCode is a project developed as a compiler of a simple programming language with its own syntax and semantics.
TryCode has a graphical interface built with Tkinter, allowing users to write code and view results. 
The parsing and execution structure of the code is defined using the Python [SLY](https://sly.readthedocs.io/en/latest/sly.html) library, ensuring consistent operation of the TryCode language.

The analysis and execution of the code is given by using two sections corresponding the Syntax section in: Lexer and Parser, plus the Semantics section with Interpreter.
The TryCode code is composed of expressions ending in the ';' character, without taking into account spaces and identation.

##Examples Syntax:

####Comments:
    #a=5;

####Variable assignment:
    a=2;
    b =” Hola Mundo”;
    c=TRUE;

####Show variable content:
    a;
    PRINT(a);


####Show Character String:
    PRINT(“hello”);

####Arithmetic Operations:
    2+2;
    3-3;
    4/4;
    5*5;

####Comparators:
    a==3;
    b!=4;
    c<=3;
    v>=4;
    k<9;
    k>6;


####Logical Comparators:
    a==3 AND b==4;
    a==3 OR b==4;
    NOT a==3 AND b==4;

####IF Syntax:
Example 1:
    a=1;
    IF a==1 THEN
    a
    ELSE
    a=a+2;

Example 2:
    a=2;
    b=2;
    IF a==2 AND b==2 THEN
    3
    ELSE
    4;

####FOR Syntax:
    FOR a=0 TO 5 THEN a;

####WHILE syntax:
    a=1;
    WHILE a<3 THEN
    a
    a=a+1;

####Function Syntax:
    FUN prueba()-> PRINT("HOLA");
    prueba();


####ILLUSTRATIVE IMAGE:

[![TryCode.png](https://i.postimg.cc/LXh7sX74/TryCode.png)](https://postimg.cc/CBTJPFS9)

### Authors

- [Ronald Blanco Navarro](rblanconavarro@gmail.com)
- [Sergio Villanueva Ríos]()
- [Esteban Altamirano Granados]()

Language:Spanish
