import os

length_file = 0
files = []
listdir = r'C:\Users\Max Hao\Desktop\npm_Package\Test\maths'
gotodir = r'C:\Users\Max Hao\Desktop\npm_Package\Test\docs\source'


listofdir = os.listdir(listdir)

# To add files to the folder and their last filename
for eachone in listofdir:
    filepath_prefix = rf'{listdir}\{eachone}'
    files.append([filepath_prefix, eachone])



for file_path in files:
    line_index = 0
    line_switch = 0
    comments= []

    with open(file_path[0], 'r') as file:
        lines = file.readlines()

    for line in lines:

        line_index += 1

        line = line.strip()
        if line.startswith('#'):  # Assumes single-line comments start with #
            comments.append(line[:].strip())

        # Assumes multi-line comments start with ''' or """
        if line.startswith("'''") or line.startswith('"""'):

            if line_switch < 2:
                line_switch += 1
                print(line_switch)

        if line_switch == 1:
            comments.append(line[:].strip())
        elif line_switch == 0:
            continue
        else:
            comments.append(line[:].strip())
            line_switch = 0

    rst_postfix = files[length_file][1]
    rst_postfix = rst_postfix[:-2] + 'rst'
    filename = rf'{gotodir}/{rst_postfix}'
    print(filename)

    with open(filename, 'a') as md_file:

            for i in range(len(comments)):
                md_file.write(comments[i] + '\n')

    
    
    length_file += 1


