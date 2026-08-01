
import sys
import os
import shutil
import subprocess
from pathlib import Path
class Shell:
    # builtin_commands=["type","echo","exit"]  
    def __init__(self,command):
        self.command=command
        self.__path=os.environ.get("PATH","").split(os.pathsep)
        self.builtin_commands=["type","echo","pwd","exit"] 

    def validate_cmd(self,parts):
         return len(parts)>=2
    def execute(self,parts):
        #  parts = self.command.split()
        #  if not parts:return 
         cmd= parts[0] 

         start_Methods={
                "echo":self.echo,
                "type":self.type_m,
                "pwd":lambda:print(os.getcwd()),
                "cd":self.cd,
                "exit":lambda:sys.exit(0)
            }

         select_method=start_Methods.get(cmd,self.External)
         select_method()


    def echo(self):
         parts=self.command
         single_Qoutes=False
         tokens=[]
         current_token = ""

         for p in parts[5:]:
              if p=="'" :single_Qoutes=not single_Qoutes

              if p==" " and not single_Qoutes:
                   tokens.append(current_token)
                   current_token=""
              else:
                   current_token+=p

         if current_token:
          tokens.append(current_token)

         print(" ".join(tokens))
    
              
              

        #  List=[]
        #  word
        #  s_word

        #  for p in parts[5:]:
        #       if single_Qoutes:
        #            if p=="'":
        #             single_Qoutes=False
        #             List.append(s_word)
        #             continue
        #            s_word+=p

        #       if p != " ":word += p
        #       else:List.append(word)
        #       if p=="'":single_Qoutes=True
    
        #  print(" ".join(List))

    def pwd(self):
         sys.stdout.write(os.getcwd() + "\n")
         sys.stdout.flush()

    def cd(self):
         path=self.command.split()
         if len(path) > 0 and path[1].startswith('~'):
            # home_path=Path.home()-- it gives string cant apply path methods here
             #better way
            target=Path(path[1]).expanduser() # it gives path obj can apply path methods like path.exists() etc 
            os.chdir(target)
            return
         
         if os.path.isdir(path[1]): os.chdir(path[1]) 
         else:print(f"{path[0]}: {path[1]}: No such file or directory")
         

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
        parts=command.split()
        s=Shell(command)
        s.validate_cmd(parts)
        s.execute(parts)

if __name__ == "__main__":
    main()
