####################################################################################################
# 
#   Author: MAKDev
#           http://www.youtube.com/@MAKDev
#
#
#   Description: This program is designed specifically for getting captions from capcut (Desktop)
#                The user will be asked to provide the location 
#                of a file with the name draft_content.json
#                the program then turns this file to a text file and reads the text file
#                Once the file has found all of the necessary text it creates a txt file
#                The text file will include the subtitles and will be saved in the same spot 
#                that the draft_content.json file was found.
#
#   Disclaimer: This only works if you have python and an IDE to run python on your desktop.
#               You are free to use, share, and distribute this code as long as you do not change it
#               DO NOT CLAIM THIS AS YOUR OWN
#               Copyright of this code belongs to MAKDev 
#               You are not allowed to sell this code
#               If you bought this code, please contact MAKDev
#
#   Date: 1-28-23
#
###################################################################################################

# Imports necessary libraries
# These libraries often times cannot be ran on an online compiler
import json
import os


def find_subtitles(filepath):
    # Opens the txt file and reads from it
    with open(str(filepath), 'r') as f:
        text = f.read()
        # The main indicator of subtitles is "</size></color></font>"
        # The script searches for any case of that and splits the file into chunks
        end = text.find("</size></color></font>")
        output_file = filepath.split(".")[0] + "_subtitles.txt"
        with open(output_file, "w") as new_file:
            # If the script doesn't find any cases as above, end will be negative one
            # Otherwise it should enter this while loop
            while end != -1:
                # It will then find the ">" before "</size></color></font>"
                # Anything inbetween these two will be subtitles
                start = text[:end].rfind(">") + 1
                # Once it finds the subtitles it writes it to a new line in the txt file
                new_file.write(text[start:end] + "\n")
                # These two lines update how much more subtitles need to be found
                # Eventually end will be equal to negative one and the while loop will be broken
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
    # This will ask the user to imput the location of the file
    # Make sure that the file ends in draft_content.json
    # EX: "C:\Users\user\Capcut\Drafts\draft_content.json"
    file_path = input("Enter the file path: ")
    file_path = file_path.strip('"')
    file_extension = os.path.splitext(file_path)[1].lower()
    output_file_path = os.path.splitext(file_path)[0] + "_output.txt"
    print("Output file will be saved at:", output_file_path)
    
    # If the user has already converted the json file to text it skips the json_to_txt function
    if file_extension == ".txt":
        find_subtitles(file_path, output_file_path)
    # If the user provides the file as the regular json file
    # The script will make a txt file and find the subtitles in that text file
    elif file_extension == ".json":
        json_to_txt(file_path, output_file_path)
        find_subtitles(output_file_path)
    else:
    # If the user did not provide a txt or json file it will let them know
        print("Invalid file format.")
        
main()
