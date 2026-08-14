#!/usr/bin/env python3

print("Hello World!")

# cat hello.py  ---> shows the contents of that file

# touch hello.py  ---> creates a file 'hello.py'

# python3 hello.py  ---> executes 'hello.py' with python3 interpreter

# we can add an extra line in file called 'shebang' which can tell OS which command is used to execute the script, to do that :
    # 1. type "nano file_name.py"
    # 2. #!/usr/bin/env python3
    # 3. ctrl+x to save, then press enter to save the file with name.
    # 4. now in terminal, type "chmod +x file_name.py"  to save it as executable file
    # 4. now run command "./hello.py"  -->  and will see the code is executed 
