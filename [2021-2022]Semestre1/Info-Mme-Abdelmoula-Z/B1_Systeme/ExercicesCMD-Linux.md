# Linux -> Cheatsheet
#### [Gwendal PRUNY](mailto:gwendal.pruny@gmail.com), ESIEE-IT
#### Cours Bloc1 Système (BTS - SIO) - 20/01/2022


<details><summary>Linux command</summary>

| command | Description |
| ------- | ----------- |
| ls | Lists all files and directories in the present working directory |
| ls-R | Lists all files and directories in the present working directory |
| ls-a | Lists hidden files as well |
| ls-al | Lists files and directories with detailed information like permissions,size, owner, etc. |
| cd or cd ~| Navigate to HOME directory |
| cd .. | Move one level up |
| cd To | change to a particular directory |
| cd / Move | to the root directory |
| cat > filename  | Creates a new file |
| cat filename | Displays the file content |
| cat file1 file2 > file3 | Joins two files (file1, file2) and stores the output in a new file (file3) |
| mv file "new file path" | Moves the files to the new location |
| mv filename new_file_name | Renames the file to a new filename |
| sudo | Allows regular users to run programs with the security privileges of the superuser or root |
| rm | filename Deletes a file |
| man | Gives help information on a command |
| history | Gives a list of all past commands typed in the current terminal session |
| clear | Clears the terminal |
| mkdir directoryname | Creates a new directory in the present working directory or a at the specified path |
| rmdir | Deletes a directory |
| mv | Renames a directory |
| pr -x | Divides the file into x columns |
| pr -h | Assigns a header to the file |
| pr -n | Denotes the file with Line Numbers |
| apt-get | Command used to install and update packages
| ls-l | to show file type and access permission |
| r | read permission |
| w | write permission |
| x | execute permission |
| x | no permission |
| -= | no permission |
| Chown user | For changing the ownership of a file/directory |
|  Chown user:group filename | change the user as well as group for a file or directory |
| echo $VARIABLE  |  To display value of a variable |
| env |  Displays all environment variables |
| VARIABLE_NAME= variable_value | Create a new variable |
| export Variable=value | o set value of an environment variable |
| sudo adduser username | To add a new user |
| sudo passwd -l 'username'  | To change the password of a user |
| sudo userdel -r 'username'  | To remove a newly created user |
</details>


<details><summary>Exercices</summary>
Exercice 1:

    /home/bob/music/rock/track1.mp3
    music/rock/track1.mp3
    ../music/rock/track1.mp3
    ../../music/rock/track1.mp3
    cd rock
    cd ../tmp/tests
    cd ..
    cd ; cd etc

Exercice 2 :

cd ; ls
mkdir .gitingore
ls -al
ls -a -al
cp Index1.html Index2.html
cd monsite ; mkdir archive
cp -v *.html archive
mv style.css monsite.css
rm monsite/Index.html monsite/Index2.html
rm -fr monsite

Exercice 3 :

mkdir exo3
cd exo3
touch moi.txt
echo Je suis en BTS SIO
echo Et j’aime ça ! >> moi.txt



rm rois.txt roisFrance.txt
mv !(roi.txt) ~/home/personal
cd 
find ~/home* -ctime +60 -exec rm {} \;
rm exo3
clear


Exercice 4:

cd personal
mkdir bin
printenv
whoami
export PATH=$PATH:/bin
aliase ll='ls -al'
</details>