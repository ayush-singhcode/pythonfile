import os
def create_file(file_name):
    try:
         with open(file_name,'x') as f:
              print(f"file nme{file_name}:is successfully created")
    except FileExistsError :
         print(f"file name{file_name};already exists")    

    except Exception as E:
         print("an error occured")    

def view_all_files() :
     files=os.listdir
     if not files :
          print("no file found")
     else :
          print("files in directory")
          for file in files :
               print(file)

def delete_file(file_name) :
    try :
          os.remove(file_name)
          print(f"file{file_name} has deleted successfully")

    except FileNotFoundError :
         print(f"file {file_name} does not found")

    except Exception as E :
         print("an arror occured")

def read_files(file_name) :
     try:
          with open()
    
    except FileNotFoundError :
         print(f"file {file_name} does not exist")

    except Exception as E :
         print("an arror occured")
