import sys

# Demonstration of sys.argv for command-line arguments

def main():
    # sys.argv[0] is always the script name
    script_name = sys.argv[0]
    
    # Arguments start from index 1
    arguments = sys.argv[1:]
    
    print(f"Script: {script_name}")
    print(f"Total arguments: {len(arguments)}")
    
    if arguments:
        for i, arg in enumerate(arguments, 1):
            print(f"Arg {i}: {arg}")
    else:
        print("No arguments provided. Try running: python sys_argv_demo.py hello world")

if __name__ == "__main__":
    main()
