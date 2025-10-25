<p align=center>
  <br>
   <img src="https://github.com/ZiackArt/enigma2/blob/main/enigma2/resources/enigma2.png"/></a>
  <br>
  <span>ENIGMA2: Find a password from a hash password</span>
  <br>
</p>

<p align="center">
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#usage">Usage</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>

<p align="center">
<img width="70%" height="70%" src="https://github.com/ZiackArt/enigma2/blob/main/enigma2/resources/test.png?raw=true"/>
</a>
</p>

## Installation

```console
# clone the repo
$ git clone https://github.com/ZiackArt/enigma2.git

# change the working directory to enigma2
$ cd enigma2

# install the requirements
$ pip install -r requirements.txt (Install dependencies one by one if you encounter a problem)
```

## ⚠️ Legal Disclaimer

```console
Enigma2 is meant strictly for ethical and authorized use — such as testing your own systems, cybersecurity research, or educational projects. Using this tool to crack or access data without permission is illegal and unethical.
```

## Usage

```console
$ python3 enigma2 -H
with the terminal make sure you are in the first ENIGMA2 folder
Parameters
----------
    `-H`  : to display Helps
    `-v`  : to have a runing version of enigma2
    `-h`  : to give a single hash value
    `-f`  : to give a txt file with a list of hash
    `-o`  : to give a output file name (write nan if your want to use a default output file name)
    `-p`  : (Optional) to give your own txt passwords list file

Good use
----------
Author : ZiackArt
GitHub : https://github.com/ZiackArt
```

To search for only one hash:

```
python3 enigma2 -h 'hash_password'
```

To search for more than one, file list:

```
python3 enigma2 -f file.txt -o output_file_name.txt
```

To use your own password database list

```
python3 enigma2 -f file.txt -o output_file_name.txt -p my_pwd_database.txt
```

go to enigma2\hash_checker.py and Uncomment this line "Data_file='./enigma2/resources/pwd.txt'" to have a larger database

## License

Enigma2 Project<br/>
Original Creator - [Ziack Art](https://github.com/ZiackArt)
