# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 01:31:02 2025

@author: duidu， MCHIGM
"""


# %%
class FileTransfer:
    
    def __init__(self, folder_path, zip_name): # Initialize class
            
        self.folder_path = folder_path
        self.zip_name = zip_name
        self.default_path = r"C:\/\/Program Files\/CHATu\/temp\/Files"

    # This code provides a class to create a zip archive from a file/folder.
    
    class ZipFolder:
    
        def create_zip1(self): # Zip file for small files
            
            import shutil
    
            shutil.make_archive(self.zip_name, 'zip', self.folder_path)
            
            return 1
        
        def create_zip2(self): # Zip file for large folders
            
            import zipfile
            import os
            
            with zipfile.ZipFile(self.zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(self.folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, self.folder_path)
                        zipf.write(file_path, arcname)
                        
            return 1
    
    ZF = ZipFolder # This is to make things eazier
    ### DO NOT MESS UP WITH zipfile.Zipfile since that has low compress rate ###
    
    # This code provides a class to get file size f
    
    class FileSize:
        
        def filesize(self): # Get file size for small file
            
            from pathlib import Path
    
            p = Path(self.zip_name)
            size_bytes = p.stat().st_size
            
            return f"Size: {size_bytes} bytes"
        
        def folder_size(self): # Get folder size
            
            import os
    
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(self.folder_path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    total_size += os.path.getsize(fp)
                    
            return total_size
        
        def zip_suffle(self): # Get all file size in a folder
            
            import os
            l = []
            
            for root, dirs, files in os.walk(self.folder_path):
                for file_name in files: l.append(os.path.getsize(os.path.join(root, file_name)))
                
            return l
    
    # This code provides a class to unzip file sizes
    
    class UnzipFolder:
        
        def __init__(): # Check selected PATH existance
            pass
        
        def extract(self): # Take out specific files
            
            from zipfile import Zipfile  
            
            with Zipfile(self.file_path) as zf:
                zf.extract(self.zip_name, self.default_path)
                
            return 1
        
        def unpack(self): # Unzpi all files&folders
            
            import os
            import shutil
            
            shutil.unpack_archive(os.path.join(self.file_path, self.zip_name), self.default_path)
            
            return 1
    
    UF = UnzipFolder # This is to make things eazier

# Gerneral settings

class Settings:
    
    class general:
        pass
    
    class safty:
        
        import warnings, re
        
        def check(self, check=bool('TRUE'), **ListOfPrograms):
            
            import os
            
            current = ListOfPrograms
            while check:
# =============
# Tutorial: Using the BugChecker 129-139
# =============
                try:
                    ''' # Basically: Call -> verify -> run -> feedback -> output
                    Let say: Unzip a file from zip
                    '''
                    # Then
                    FileTransfer.__init__("PATH", "path") # Call initialize object
                    pass
                except IndentationError(): #Example error case
                    pass
                finally:
                    responce = FileTransfer.UF.extract() # Run the command
                Settings.safty.log.Problem(current) if responce != 0 else os.exit(1)
                current = current()
            
            pass
        
        class ERROR:
            
            pass
        
        class WARNING:
            
            pass

        class log:
            
            pass
            
            def Problem():
                
                pass
            
            def Exit():
                
                pass
            
            def NoResponce():
                
                pass
# %%