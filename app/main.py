
import sys
import os
import shutil
import subprocess
class Shell:
    # builtin_commands=["type","echo","exit"]  
    def __init__(self,command):
        self.command=command
        self.__path=os.environ.get("PATH").split(os.pathsep)
        self.builtin_commands=["type","echo","exit"] 

    def echo(self):print(" ".join(self.command.split()[1:]))

    def type_m(self,command)->None:
        for b in self.builtin_commands:
            if command[5:]==b:
                print(f"{command[5:]} is a shell builtin")
                break
                #else  is of for loop 
        else:

                          #PATH env variable
            # path =os.environ.get("PATH").split(os.pathsep)
            for dictionary in self.__path:
                filePath=os.path.join(dictionary,self.command[5:])
                if os.access(filePath, os.X_OK):                
                    print(f"{command[5:]} is {filePath}")
                    break

            else:
                print(f"{command[5:]}: not found")

    def External():
         if file:=shutil.which(command.split()[0]):
                            #subprocess.run() expects the command and its arguments as separate items.
            subprocess.run(command.split())
        
         else:  print(f"{command}: not found")




    start_Methods={
        "echo":lambda:echo(self.comman),
        "type":lambda:type_m(self.comman),
        "exit":lambda:sys.exit(0)
       
    }
    cmd=command.split()[0] if command.split()>0 else ""
    select_method=start_Methods.get(cmd,External())
# this all process can be replaced by shutil.which(cmd)
      #    bcz internally it do all this like 
 # shutil.which(command) internally does something very similar to:

#  Reads the PATH environment variable.
#  Splits it using the correct separator (: on Linux/macOS, ; on Windows).
#  Looks in each directory for the command.
#  Checks if the file exists and is executable.
#  Returns the full path (e.g., /bin/cat) if found, otherwise returns None.



def main():
    # TODO: Uncomment the code below to pass the first stage


    while True:
        sys.stdout.write("$ ")
        
        command=input()
        s=Shell(command)



if __name__ == "__main__":
    main()
