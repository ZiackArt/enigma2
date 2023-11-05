import string, getopt, sys, bcrypt
from tqdm import tqdm
from time import perf_counter
from colorama import Fore, Back, Style


module_name = "ENIGMA2"
__version__ = "0.1"

def hash_check(pwd_hash,Output_file_name):
    try:
        # opening the file in read mode 
        my_file = open("pwd.txt", "r") 
        pwd_datas = my_file.read()  
        pwd_datas = pwd_datas.split("\n") 
        my_file.close()
    except:
        sys.exit("Reading file error")
    encode_pwd_datas = []
    [encode_pwd_datas.append(pwd.encode("utf-8")) for pwd in pwd_datas]
    # [print(Fore.BLUE +"\n"+str()) for pwd in  if bcrypt.checkpw(pwd, pwd_hash) ]

    for pwd in tqdm(encode_pwd_datas,desc=f"Wating..."):
        if bcrypt.checkpw(pwd, pwd_hash):
            print(Fore.GREEN + f"\n[ {str(pwd.decode('utf-8'))} => {pwd_hash.decode('utf-8')} ]")
            print(Fore.WHITE)
            break

def list_hash_check(Output_file,Output_file_name):
    try:
        # opening the file in read mode 
        my_file = open(Output_file, "r") 
        h_pwd_file = my_file.read()  
        h_pwd_file = h_pwd_file.split("\n") 
        my_file.close()

        my_file = open("passwords.txt", "r") 
        pwd_datas = my_file.read()  
        pwd_datas = pwd_datas.split("\n") 
        my_file.close()

    except:
        sys.exit("Reading file error")
    encode_pwd_datas = []
    [encode_pwd_datas.append(pwd.encode("utf-8")) for pwd in pwd_datas]

    encode_h_pwd_file = []
    [encode_h_pwd_file.append(h.encode("utf-8")) for h in h_pwd_file]
    for h in tqdm(encode_h_pwd_file,desc=f"Hashs Wating..."):
        for pwd in tqdm(encode_pwd_datas,desc=f"Passwords checking...") :
            if bcrypt.checkpw(pwd, h):
                print(Fore.GREEN + f"\n[ {str(pwd.decode('utf-8'))} => {h.decode('utf-8')} ]"+Fore.BLUE)
                outputs = f"{str(pwd.decode('utf-8'))} => {h.decode('utf-8')}\n"
                Output_f(outputs=outputs,filename=Output_file_name)    
                break

def Output_f(outputs,filename="enigma2.txt"):
    try:
        file = open(filename,"a")
        file.write(outputs)
        file.close()
    except:
        sys.exit("=======Opening file error=======")

def main():
    begin_perf = perf_counter()
    Hash= Output_file_name= File_name =""
    Is_file = False
    argumentList = sys.argv[1:]
    # Remove 1st argument from the
    # list of command line arguments
    argumentList = sys.argv[1:]

    if len(argumentList) == 0:
        print(f"{module_name} \nVersion: {__version__}")
        sys.exit()

    # Options
    options = "Hh:f:o:v"
    long_options = ["Help", "Hash", "File","Output","Version"]

    try: 
        # Parsing argument
        arguments, values = getopt.getopt(argumentList,options,long_options)
    
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))
        sys.exit() 
    try:
        for currentArgument, currentValue in arguments:
            if currentArgument in ('-H',"--Help"):
                print("helps menu")
            elif currentArgument in ("-h","--Hash"):
                Hash = currentValue.encode("utf-8")
            elif currentArgument in ("-f","--Combinaition"):
                Is_file = True
                File_name = str(currentValue)
            elif currentArgument in ("-o", "--Output"):
                Output_file_name = str(currentValue)
                if len(Output_file_name) < 4:
                    Output_file_name = "enigma2.txt"
            elif currentArgument in ("-v", "Version"):
                print(Fore.BLUE + f"{module_name} \nVersion: {__version__}")
                sys.exit()
        
        if Is_file:
            list_hash_check(File_name,Output_file_name)
        else:
            hash_check(Hash,Output_file_name)
            
    except getopt.error as err:
        if err:
            print(str(err))
        else:
            print("Unknown error")
    
    delta = perf_counter() - begin_perf
    print(Fore.BLUE + f"Exécution time: {delta:.2f}s")


if __name__ == "__main__":
    main()