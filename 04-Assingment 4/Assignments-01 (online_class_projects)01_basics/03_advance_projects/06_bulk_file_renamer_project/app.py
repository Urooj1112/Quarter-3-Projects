import os

def main():
    i = 0
    path = r"C:\Users\hp\Desktop\New folder"

    for filename in os.listdir(path):
        if filename.endswith(".txt"): # only txt files will rename
            new_name = f"text{i}.txt" 
            old_path = os.path.join(path,filename)
            new_path = os.path.join(path, new_name)
            os.rename(old_path, new_path)
            i += 1

if __name__ == '__main__':
    main()