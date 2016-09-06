#coding:utf-8
#import codecs
from urllib import request

def read_text():
    quotes = open(r"C:\Users\frank.li\Desktop\Python\takeAbreak\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = request.urlopen('www.wdyl.com/profanity?q'+text_to_check)
    output = connection.read()
    print(output)
    connection.request.urlclose()
    if 'true' in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("There is not curse words in document")
    else:
        print("We can't scan the text properly")

read_text()
