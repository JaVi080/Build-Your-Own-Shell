
import sys
import os
import shutil
import subprocess
class Shell:
    # builtin_commands=["type","echo","exit"]  
    def __init__(self,command):
        self.command=command
        self.__path=os.environ.get("PATH","").split(os.pathsep)
        self.builtin_commands=["type","echo","exit"] 
        

    def execute(self):
         parts = self.command.split()
         if not parts:return 
         cmd= parts[0] 

         start_Methods={
                "echo":lambda:self.echo,
                "type":lambda:self.type_m,
                "exit":lambda:sys.exit(0)
               
            }

         select_method=start_Methods.get(cmd,lambda:self.External)

         select_method()


    def echo(self):print(" ".join(self.command.split()[1:]))

    def type_m(self)->None:
        parts = self.command.split()

        if parts[1] in self.builtin_commands:
                print(f"{parts[1]} is a shell builtin")
                return

                     #PATH env variable
            # path =os.environ.get("PATH").split(os.pathsep)
        for dictionary in self.__path:
                filePath=os.path.join(dictionary,parts[1])
                if os.access(filePath, os.X_OK):                
                    print(f"{parts[1]} is {filePath}")
                    return

        print(f"{parts[1]}: not found")

    def External(self):
         if file:=shutil.which(self.command.split()[0]):
                            #subprocess.run() expects the command and its arguments as separate items.
            subprocess.run(self.command.split())
        
         else:  print(f"{self.command}: not found")


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
        s.execute()

if __name__ == "__main__":
    main()
