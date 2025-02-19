import os 
import subprocess  # Add this import at the top
from tinyDSL import *
from demoInteractionCLI import *

class File:
        
    def __init__(self, name, content = "", extension = ".txt"): # constructor takes 3 parameters: name, content and extension
        self.extensions = [".html", ".css", ".js", ".txt"] # list of authorized extensions
        self.name = name
        self.content = content
        if extension not in self.extensions: # if the extension is not in the list of authorized extensions, raise an error
            raise ValueError(f"Extension {extension} is not valid, authorized extensions are {self.extensions}")
        self.extension = extension
    
    @staticmethod 
    def fromFileName(file_name: str): # function that takes a file name and returns a File object
        if "." not in file_name: # if the file name does not contain an extension, raise an error
            raise ValueError("The file name must contain an extension")
        name, extension = file_name.split(".") # split the file name and the extension
        # if file file_name exists, we can get the content
        if os.path.exists(file_name):
            content = "" 
            with open(file_name, "r") as file: # open the file and read the content
                content = file.read() 
            return File(name, content, "."+extension) 
        return File(name, "", "."+extension) # return a File object
    
    def full_name(self) -> str: # function that returns the full name of the file
        return self.name + self.extension
        
    def informations(self) -> str: # function that returns the informations of the file
        return f"Name: {self.name}, Content: {self.content}, Extension: {self.extension}"

# Classe FileManager
class FileManager:

    def __init__(self): # constructor
        pass
    
    def create_file(self, file_name, content = "", extension = ".txt") -> File: # function that creates a file
        
        myFile = File(file_name, content, extension) # create a File object
        
        with open(myFile.full_name(), "w", encoding="utf-8") as file: # open the file and write the content   
            file.write(content)
        return myFile # return the File object


    def delete_file(self, file:File) -> bool: # function that deletes a file
        print("Deleting file", file.full_name())
        if os.path.exists(file.full_name()): # if the file exists, delete 
            os.remove(file.full_name()) 
            return True
        return False
        
    def delete_file_from_file_name(self, file_name:str) -> bool: # function that deletes a file from a file name
        file_to_delete = File.fromFileName(file_name) # get the file to delete
        self.delete_file(file_to_delete) # delete the file
    
    
    def update_file(self, file: File, content) -> bool: # function that updates a file
        with open(file.full_name(), "a", encoding="utf-8") as f: # open the file and append the content
            f.write(content)
        return True
    
    def update_file_from_file(self, file_name: str, content) -> bool: # function that updates a file from a file name
        file_to_update = File.fromFileName(file_name) # get the file to update
        return self.update_file(file_to_update, content) # update the file
    
    
class ProjectGenerator:
    
    def __init__(self, type = "web"):
        self.type = type.lower()  # Convert to lowercase for case-insensitive comparison
        self.fileManager = FileManager()

    def generate_project(self, folder_name):
        if self.type == "web":
            if not os.path.exists(folder_name):
                # Create main directories
                os.makedirs(folder_name + "/assets/img/png") 
                os.makedirs(folder_name + "/assets/img/svg")
                os.makedirs(folder_name + "/assets/fonts")
                os.makedirs(folder_name + "/assets/audio")
                os.makedirs(folder_name + "/assets/video")
                # Create styles directory
                os.makedirs(folder_name + "/styles") 

                # Create HTML file in root
                self.fileManager.create_file(folder_name + "/index", questionner.buildHTML(), ".html")
                
                # Create CSS files in styles folder
                self.fileManager.create_file(folder_name + "/styles/" + style, questionner.buildCSS(), ".css")
                self.fileManager.create_file(folder_name + "/styles/reset", questionner.buildResetCSS(), ".css")
                
                # Create JS file in root
                self.fileManager.create_file(folder_name + "/script", questionner.buildJS(), ".js")
            else:
                print("The project already exists")
        elif self.type == "next":
            if not os.path.exists(folder_name):
                print("Creating Next.js project...")
                try:
                    # Run create-next-app command with shell=True
                    subprocess.run("npx create-next-app@latest " + folder_name, 
                                 shell=True, 
                                 check=True) 
                    print(f"Next.js project '{folder_name}' created successfully!") 
                except subprocess.CalledProcessError as e:
                    print(f"Error creating Next.js project: {e}") # if the command fails, print the error
                    exit(1)
                except FileNotFoundError:
                    print("Error: 'npx' command not found. Please make sure Node.js and npm are installed.") # if the command is not found, print the error
                    exit(1)
            else:
                print("The project already exists")
        elif self.type == "vue":
            if not os.path.exists(folder_name):
                print("Creating Vue project...")
                try:
                    # Run create-vue command with shell=True
                    subprocess.run("npx create-vue@latest " + folder_name, 
                                 shell=True, 
                                 check=True) 
                    print(f"Vue project '{folder_name}' created successfully!") 
                except subprocess.CalledProcessError as e:
                    print(f"Error creating Vue project: {e}") # if the command fails, print the error
                    exit(1)
        else:
            print("The project type is not valid. Available types: 'web', 'next'") # if the project type is not valid, print the error
            exit()
        
    
    
webProject = ProjectGenerator(type) # create a ProjectGenerator object
webProject.generate_project(name) # generate the project
print(f"A {type} project named '{name}' has been created") # print the success message




