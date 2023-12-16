# Method 2 (BETTER) - Make the python itself run from shell:

# Modify your script hello.py and add this as the first line

# #!/usr/bin/env python

# mark it executable using

# $ chmod +x hello.py

# then run it

# $ ./hello.py
"""Ideas for this backup program... 
   Ask for input within the ~ directory"""


# Simple script to backup and save files from a certain directory 
# TODO Prompt user for desired copy space before copying. Yes or no, are you sure you want to copy x space?
import subprocess
import os 
import sys 

class Backup:
    def __init__(self, destination: str):
        """
        self.destination = where the backup will copy the file too
        self.__source_paths = the paths of the sources that will be backed up
        """
        self.destination = destination


    def run(self):
        homeDirDict = self.getHomeDirLookup()
        selections = self.askUserDirSelection(homeDirDict)
        source_paths = self.grabSelectedHomePaths(selections, homeDirDict)
        self.confirmBackupDownload(source_paths)
        self.download(source_paths)


    def getHomeDirLookup(self):
        """Lists all potential source directories in the home directory and 
           returns a dictionary of home directory options"""
        # Lists all files in the home directory, pipe standard output to text
        home_directory = os.path.expanduser('~')
        homedirs = subprocess.run(['ls', home_directory], stdout=subprocess.PIPE, text=True)
        # Create a list of dirs in home, exclude empty string at end
        homeList = homedirs.stdout.split('\n')[:-1]
        # Create a dictionary of dirs with coresponding index codes
        home_dir_lookup = {index: value for index, value in enumerate(homeList)}
        return home_dir_lookup


    def askUserDirSelection(self, directory: dict) -> list[int]:
        """Given a dictionary of dirs, returns user specified indexs of desired dirs"""
        print("Please Make A Selection(s) by typing in a number(s) seperated by spaces")
        for key, value in directory.items():
            print(f"{key} : {value}")
        while True:
            try:
               """ Takes in multiple inputs sep by spaces and converts 
                    them to int values and returns a list"""
               selection = input("Selection: ")
               selection = selection.split()
               selections = list(map(lambda x : int(x), selection))
               break
            except Exception:
                print("Exception. Please select a valid input")
        return selections
    

    def grabSelectedHomePaths(self, selections: int, selectionDictionary: dict):
        """Grabs the paths of the home directories that the user selected 
            and return a list of full paths
        """
        paths = []
        homePath = os.path.expanduser('~') 
        for index, path in selectionDictionary.items():
            if index in selections:
                path = os.path.join(homePath, path)
                paths.append(path)
        return paths 
        

    def confirmBackupDownload(self, source_paths):
        """Confirms to the user the dirs to be saved, and the save destination"""
        print("\nPlease verify source paths:")
        for path in source_paths:
            print(path)
        confirmation = input("Is this correct? (y/n) ")
        if confirmation.lower() == 'y':
            pass
        else:
            print('Operation Cancelled')
            sys.exit()


    def download(self, paths):
        """for each path in __soure_paths, download them to self.destination"""
        for path in paths:
            print(f"Copying files in the directory now... {path}", end=' ')
            #subprocess.run(['cp', '-rui', path, self.destination])
            print("DONE")


def main():
    print('File Backup Program, Created by Karl, Version 0.5')
    print('Press Ctrl+c to exit')
    try:
        # Gets the folder that the script path is in, "backupTesting"
        parent_folder = os.path.dirname(os.path.abspath(__file__))
        destination = os.path.join(parent_folder, 'backup')

        backup = Backup(destination)
        backup.run()
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":
    main()

