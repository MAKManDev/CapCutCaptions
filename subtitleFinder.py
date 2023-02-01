####################################
# 
#   Author: MAKDev
#
#   Description:
#
####################################

import json

import os


def find_text_between_tags_in_txt(filepath):
    with open(str(filepath), 'r') as f:
        text = f.read()
        end = text.find("</size></color></font>")
        output_file = filepath.split(".")[0] + "_subtitles.txt"
        with open(output_file, "w") as new_file:
            while end != -1:
                start = text[:end].rfind(">") + 1
                new_file.write(text[start:end] + "\n")
                text = text[end + len("</size></color></font>"):]
                end = text.find("</size></color></font>")




def json_to_txt(json_file_path, txt_file_path):
    # Open the json file
    with open(json_file_path, 'r') as json_file:
        # Load the json data
        data = json.load(json_file)
        
    # Write the json data to a text file
    with open(txt_file_path, 'w') as txt_file:
        json.dump(data, txt_file)



def main():
    file_path = input("Enter the file path: ")
    file_path = file_path.strip('"')
    file_extension = os.path.splitext(file_path)[1].lower()
    output_file_path = os.path.splitext(file_path)[0] + "_output.txt"
    print("Output file will be saved at:", output_file_path)

    if file_extension == ".txt":
        find_text_between_tags_in_txt(file_path, output_file_path)
    elif file_extension == ".json":
        json_to_txt(file_path, output_file_path)
        find_text_between_tags_in_txt(output_file_path)
    else:
        print("Invalid file format.")
        
main()