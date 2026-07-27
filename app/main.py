import sys
import os
import shutil

def main():
    # TODO: Uncomment the code below to pass the first stage

    builtin_commands=["type","echo","exit"]
    
    while True:
        sys.stdout.write("$ ")
        
        command=input()
        cmd = command[5:]
        # print(command[5:])
        if command=="exit":
                break

       #Rnning External prg
        elif command.startswith("echo"):
             print(" ".join(command.split()[1:]))

        elif command.startswith("type"):
             for b in builtin_commands:
                  if command[5:]==b:
                    print(f"{command[5:]} is a shell builtin")
                    break
                  #else  is of for loop 
             else:
                  #PATH env variable
                  path =os.environ.get("PATH").split(os.pathsep)
                  for dictionary in path:
                       filePath=os.path.join(dictionary,command[5:])
                       if os.access(filePath, os.X_OK):
                            print(f"{command[5:]} is {filePath}")
                            break

# this all process can be replaced by shutil.which(cmd)
      #    bcz internally it do all this like 
 # shutil.which(command) internally does something very similar to:

#  Reads the PATH environment variable.
#  Splits it using the correct separator (: on Linux/macOS, ; on Windows).
#  Looks in each directory for the command.
#  Checks if the file exists and is executable.
#  Returns the full path (e.g., /bin/cat) if found, otherwise returns None.

                  else: print(f"{command[5:]}: not found")
                                               
                 
        else:
             #RUNNING External prg
             if file:=shutil.which(cmd):
                  file.subprocess()


    
    

if __name__ == "__main__":
    main()
