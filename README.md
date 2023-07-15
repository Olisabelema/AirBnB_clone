AirBnB clone - The console

Description of the project: The goal of the project is to deploy on your server a simple copy of the AirBnB website.
First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine.

Description of the command interpreter:
A command interpreter, also known as a command-line interpreter, shell, or command prompt, is a program that interprets and executes commands entered by a user in a text-based interface. It is typically found in operating systems like Unix/Linux, macOS, and Windows.

The command interpreter allows users to interact with the computer system by typing commands as text strings and receiving output or performing actions based on those commands. Here are some key characteristics and functionalities of a command interpreter:

Prompt: The command interpreter displays a prompt, typically a text string like "$" or ">", indicating that it is ready to accept user input.

Command input: Users enter commands by typing them at the prompt. Commands are typically a combination of executable program names, options, and arguments, entered in a specific format and syntax.

Command execution: Once the user enters a command, the command interpreter interprets and executes it. It locates the appropriate executable program, passes the necessary arguments, and initiates its execution.

File system navigation: The command interpreter allows users to navigate the file system hierarchy by using commands such as "cd" (change directory) or "ls" (list directory contents) to move between directories, view file and folder listings, and perform other file management operations.

Command line editing: Most command interpreters provide basic editing capabilities, such as cursor movement, deletion, and command recall, allowing users to modify or reuse previously entered commands.

Environment variables: The command interpreter often supports environment variables, which are named values that can be set, modified, and accessed by the user or scripts. Environment variables provide a way to store and retrieve information relevant to the user's session or the system configuration.

Redirection and piping: Command interpreters often support input/output redirection and piping. Redirection allows users to redirect the input or output of a command to or from files, while piping enables users to chain multiple commands together, using the output of one command as the input to another.

Command scripting: Command interpreters can interpret and execute scripts—sequences of commands stored in a file. Scripts allow users to automate repetitive tasks by writing a series of commands that the interpreter executes in order.

These are some general features and functionalities of a command interpreter. Different operating systems may have variations in specific commands, syntax, and additional capabilities provided by their respective command interpreters.

To use a command interpreter, follow these general steps:

Open the command interpreter: Depending on your operating system, you can open the command interpreter by searching for "Command Prompt" or "Terminal" in the applications menu, or by pressing specific keyboard shortcuts (e.g., Windows key + R, then type "cmd" and press Enter for Command Prompt in Windows).

Navigate the file system (optional): If you need to navigate to a specific directory, use the appropriate command. For example, in Windows, you can use the "cd" (change directory) command to move between folders, while in Unix/Linux/macOS, you can use the "cd" command as well.

Enter commands: Once you're in the desired directory, enter the commands you want to execute. Commands typically consist of the program name, followed by any options or arguments. For example, to list the files in a directory, you would use the "ls" command in Unix/Linux/macOS or the "dir" command in Windows.

Press Enter: After entering a command, press the Enter or Return key to execute it. The command interpreter will interpret the command and perform the requested action.

Review the output: The command interpreter will provide output based on the executed command. This output may be informational, error messages, or the result of the command's execution.

Repeat as needed: You can enter additional commands, navigate directories, or perform other actions within the command interpreter as required.
