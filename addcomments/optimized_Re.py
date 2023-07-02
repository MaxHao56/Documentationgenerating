import os 
import re


# Class to initize the self and filepath and filename for python
class File:
    def __init__(self,filepath,filename):
        self.filepath = filepath
        self.filename = filename
        self.comments =  []

    # defult functions for adding comments
    def add_comments(self,commnets):
        self.comments.append(commnets)
    # default functions for converting python to rst_get filename
    def get_rst_filename(self):
        sp_rst_filpostfix = self.filename[:-2]+'rst'
        return os.path.join(goal_folder_dir,sp_rst_filpostfix)


file_index = 0
files = []
python_folder_dir = r'C:\Users\Max Hao\Desktop\npm_Package\Test\maths'
goal_folder_dir = r'C:\Users\Max Hao\Desktop\npm_Package\Test\docs\source'

python_file_dir = os.listdir(python_folder_dir)

# Add each python file to become rst file and push SPHINX FOR USES
for each_postfix in python_file_dir:
    filepath_forcomments = os.path.join(python_folder_dir,each_postfix)
    files.append(File(filepath_forcomments,each_postfix))


comment_pattern = r"#.*$|'''[\s\S]*?'''|\"\"\"[\s\S]*?\"\"\""




for file_obj in files:
    line_index = 0
    line_switch = 0

    with open(file_obj.filepath,'r') as file:
        content = file.read()
        

    comments = re.findall(comment_pattern, content,re.MULTILINE)
    
    file_obj.comments.extend(comments)

    filename = file_obj.get_rst_filename()

    with open(filename, 'a') as md_file:
        for comment in file_obj.comments:
            md_file.write(comment.strip() + '\n')

 