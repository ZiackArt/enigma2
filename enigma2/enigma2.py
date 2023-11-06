#! /usr/bin/env python3
"""
ENIGMA2: Find a password from a hash password

This module allows you to retrieve a password from its hash
"""

import string, getopt, sys, bcrypt
from tqdm import tqdm
from time import perf_counter
from colorama import Fore
from hash_checker  import hash_check, list_hash_check

helps =  """
    ENIGMA2 allows you to retrieve a password from its hash
        >py enigma2
    Parameters
    ----------
    `-H`  : to display Helps
    `-v`  : to have a runing version of enigma2
    `-h`  : to give a single hash value
    `-f`  : to give a txt file with a list of hash
    `-o`  : to give a output file name (write nan if your want to use a default output file name)
    `-p`  : (Optional) to give a txt passwords file name
    
    Good use
    ----------
    Author : ZiackArt
    GitHub : https://github.com/ZiackArt
"""

module_name = "ENIGMA2"
__version__ = "1.0"



def main():
    begin_perf = perf_counter()
    Hash=password=output_file_name=file_name=""
    is_file = False
    # Remove 1st argument from the
    argumentList = sys.argv[1:]
    # list of command line arguments
    if len(argumentList) == 0:
        sys.exit(Fore.GREEN + f"{module_name} \nVersion: {__version__}")

    # Options
    options = "Hh:f:o:vp:"
    long_options = ["Help", "Hash", "File","Output","Version","Password"]

    try: 
        # Parsing argument
        arguments, values = getopt.getopt(argumentList,options,long_options)
    
    except getopt.error as err:
        # output error, and return with an error code
        sys.exit(Fore.RED+"(╬▔皿▔)╯ "+str(err))

    try:
        for currentArgument, currentValue in arguments:
            if currentArgument in ('-H',"--Help"):
                sys.exit(Fore.GREEN + helps)
            elif currentArgument in ("-h","--Hash"):
                Hash = currentValue.encode("utf-8")
            elif currentArgument in ("-f","--Combinaition"):
                is_file = True
                file_name = str(currentValue)
            elif currentArgument in ("-o", "--Output"):
                output_file_name = str(currentValue)
                if len(output_file_name) < 4:
                    output_file_name = "enigma2.txt"
            elif currentArgument in ("-v", "Version"):
                print(Fore.BLUE + f"{module_name} \nVersion: {__version__}")
                sys.exit()
            elif currentArgument in ("-p", "--Password"):
                password = str(currentValue)
        
        if is_file:
            if len(password) > 4:
                list_hash_check(file_name,output_file_name,data_file=password)
            else:
                list_hash_check(file_name,output_file_name)
        else:
            if len(password) > 4:
                list_hash_check(file_name,output_file_name,data_file=password)
            else:
                list_hash_check(file_name,output_file_name)
            
    except getopt.error as err:
        if err:
            sys.exit(Fore.RED+"(╬▔皿▔)╯ "+str(err))
        else:
            sys.exit(Fore.RED+"＞︿＜ Unknown error"+str(err))

    delta = perf_counter() - begin_perf
    print(Fore.BLUE + f"Exécution time: {delta:.2f}s")


if __name__ == "__main__":
    main()