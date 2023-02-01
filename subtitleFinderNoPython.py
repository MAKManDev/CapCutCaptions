####################################################################################################
# 
#   Author: MAKDev
#           http://www.youtube.com/@MAKDev
#
#
#   Description: This program is designed specifically for getting captions from capcut (Desktop)
#                The user will need to replace the text in the text variable string
#                When the program is ran, it will use the text variable and find the subtitles
#                This program can be ran in any python comp
#
#   Disclaimer: You are free to use, share, and distribute this code as long as you do not change it
#               DO NOT CLAIM THIS AS YOUR OWN
#               Copyright of this code belongs to MAKDev 
#               You are not allowed to sell this code
#               If you bought this code, please contact MAKDev
#
#   Date: 1-28-23
#
###################################################################################################



text = """Paste your json text here"""

def find_subtitles(text):
    # Searches the code for "</size></color></font>"
    # It then sets the end variable to be equal to how many times it found it
    end = text.find("</size></color></font>")
    print("Here is your subtitles---")
    while end != -1:
        # It will then find the ">" before "</size></color></font>"
        # Anything inbetween these two will be subtitles
        start = text[:end].rfind(">") + 1
        print(text[start:end])
        # It then updates the end variable
        # Eventually the end variable will be equal to -1 exiting this loop
        # and giving you the subtitles
        text = text[end + len("</size></color></font>"):]
        end = text.find("</size></color></font>")
    print("---END OF SUBTITLES")

find_subtitles(text)