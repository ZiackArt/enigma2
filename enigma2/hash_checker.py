import bcrypt, sys
from tqdm import tqdm
from colorama import Fore

def hash_check(pwd_hash, output_file_name="", data_file="./enigma2/resources/pwds.txt"):
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.

    Parameters
    ----------
    `Pwd_hash`  : iterable, not optional
        is the password hach that we will try to find.
    `Output_file_name`  : str, optional
        Name of de output file. the ouput won't be save in a file if
        this paremeter is absent
    `data_file`  : str, optional
        the file with a list of password, if absent, we will user our 
        password database
    """

    try:
        my_file = open(data_file, "r")
        pwd_datas = my_file.read().split("\n")
        my_file.close()
        encode_pwd_datas = []
        [encode_pwd_datas.append(pwd.encode("utf-8")) for pwd in pwd_datas]
        pwd_datas.clear()
    except FileNotFoundError as err:
        sys.exit(Fore.RED + ".·´¯`(>▂<)´¯`·. "+ str(err))

    for pwd in tqdm(encode_pwd_datas,desc=Fore.BLUE+"Searching...."):
        if bcrypt.checkpw(pwd, pwd_hash):
            print(Fore.GREEN + f"\n(づ￣ 3￣)づ [ {str(pwd.decode('utf-8'))} => {pwd_hash.decode('utf-8')} ]" + Fore.WHITE + "\n")
            if len(output_file_name) > 5:
                save(output=f"[ {str(pwd.decode('utf-8'))} => {pwd_hash.decode('utf-8')} ]",filename=output_file_name)
            break

def list_hash_check(output_file, output_file_name="", data_file="./enigma2/resources/pwds.txt"):
    try:
        my_file = open(output_file, "r") 
        h_pwd_file = my_file.read().split("\n")
        my_file.close()

        my_file = open(data_file, "r") 
        pwd_datas = my_file.read().split("\n")  
        my_file.close()

        encode_pwd_datas = []
        [encode_pwd_datas.append(pwd.encode("utf-8")) for pwd in pwd_datas]
        pwd_datas.clear()

        encode_h_pwd_file = []
        [encode_h_pwd_file.append(h.encode("utf-8")) for h in h_pwd_file]
        h_pwd_file.clear()
    except FileNotFoundError as err:
        sys.exit(".·´¯`(>▂<)´¯`·. "+str(err))
    
    size = len(encode_h_pwd_file)
    for i, h in enumerate(encode_h_pwd_file):
        for pwd in tqdm(encode_pwd_datas,desc=Fore.CYAN+"Passwords checking...") :
            if bcrypt.checkpw(pwd, h):
                print(Fore.GREEN + f"\n{i+1}/{size} (づ￣ 3￣)づ [ {str(pwd.decode('utf-8'))} => {h.decode('utf-8')} ]\n")
                if len(output_file_name) > 5:
                    save(output=f"{str(pwd.decode('utf-8'))} => {h.decode('utf-8')}\n",filename=output_file_name)  
                break

def save(output,filename="enigma2.txt"):
    try:
        file = open(filename,"a")
        file.write(output)
        file.close()
    except FileNotFoundError as err:
        sys.exit(Fore.RED + ".·´¯`(>▂<)´¯`·. Saving file error :"+ str(err))