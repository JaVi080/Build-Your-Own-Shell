import sys
import os

def main():
    # TODO: Uncomment the code below to pass the first stage

    builtin_commands=["type","echo","exit"]
    
    while True:
        sys.stdout.write("$ ")
        
        command=input()
        # print(command[5:])
        if command=="exit":
                break

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
                  path =os.environ.get["PATH"].split(os.pathsep)
                  for dictionary in path:
                       filePath=os.path.join(dictionary,command[5:])
                       if os.access(filePath, os.X_OK):
                            print(f"{command[5:]} is {filePath}")

                  else: print(f"{command[5:]}: not found")
                                               
                 
        else:
             print(f"{command}: command not found")

    
    

if __name__ == "__main__":
    main()
