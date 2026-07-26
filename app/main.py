import sys


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
                  if command[5:]==b:return print(f"{command[5:]} is a shell builtin")

             else:print(f"{command}: not found")
                       
                 
        else:
             print(f"{command}: command not found")

    
    

if __name__ == "__main__":
    main()
