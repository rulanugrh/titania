import sys
import subprocess

def main(args: str):
    if args == "ogive":
        subprocess.run(["python", "./ogive/histogram-ogive.py"])
    elif args == "table-ogive":
        subprocess.run(["python", "./ogive/table-frequently.py"])
    elif args == "offclose":
        subprocess.run(["python", "./offclose/main.py"])
    else:
        print("Command Not Found")

if __name__ == "__main__":
    args = sys.argv[1]
    main(args=args)