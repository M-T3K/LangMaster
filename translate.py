# TODO

# [X] Input: CSV file with one column of words from a specific language
# [X] Output: CSV file with two columns of words from the original language, and the target translation language.
# Optional: Additional column in which words from other preselected languages that have the same target translation stay in the same row. 
# Optional: On top of comparing against the target translation language, it also compares by translating them to the other preselected languages, 
#           and checking which ones have the same meaning in that way.

# @info There can be an error with the translations if a lot of translation requests are performed

# from googletrans import Translator
# from google_trans_new import google_translator
from deep_translator import GoogleTranslator
import csv
import os
import argparse
import time



if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-f", "--files", required=True, type=argparse.FileType('r', encoding='utf-8'), nargs='+', help="Include the list of files to be parsed and translated")
    argparser.add_argument("-l", "--langs", nargs="+", help="For a faster and better translation you can include the languages used in the files.")
    argparser.add_argument("-t", "--target", help="Select a target language for the translation.")
    argparser.add_argument("-v", "--verbosity", help="Enables/Disables verbose.", action="store_true")
    argparser.add_argument("-fl", "--file_length", help="Determines the maximum length to be read from a file", type=int)
    argparser.add_argument("-d", "--dir", help="Directory where the translation files will be stored. Must include trailing slash '/'", type=str)
    args = argparser.parse_args()

    if args.verbosity:
        print("Verbose Option Selected")
    print("Target Language: ", args.target)
    n_files = len(args.files)
    n_langs = len(args.langs)
    max_file_length = int(args.file_length)
    print("Maximum File Length: ", max_file_length)
    print("Storage Directory:", args.dir)
    if not os.path.exists(os.path.dirname(args.dir)):
        print("Storage directory doesn't exist. Creating.")
        try:
            os.makedirs(os.path.dirname(args.dir))
        except OSError: 
            raise

    # END IF
    f_num = 0
    file_data = []
    while f_num < n_files:
        if n_langs > f_num:
            print("File: ", args.files[f_num], "Language:", args.langs[f_num])
            tup = (args.files[f_num], args.langs[f_num])
        else:
            print("File: ", args.files[f_num], "Language:", "auto")
            tup = (args.files[f_num], "auto")
        file_data.append(tup)
        f_num += 1
    # END WHILE
    # END IF
    # @info Breaking point for now
    # exit(0)

    # Read the files
    # translator = Translator()
    # translator = google_translator()

    dict_trans = {} # We create a translation dictionary
    translation_lists = []
    curr = 0
    for _file,_lang in file_data:
        translator = GoogleTranslator(source=_lang, target=args.target)
        print("File Name: ", _file.name, "Language: ", _lang)
        csv_reader = csv.reader(_file, delimiter=',')
        file_line_count = 1
        # Translating to the same language is a waste of time and resources
        if _lang == args.target:
            continue 

        translate_queue = []
        for row in csv_reader:
            if file_line_count > max_file_length:
                break
            translate_queue.append(row[0])
            file_line_count += 1
        # END FOR

        trans = translator.translate_batch(translate_queue)
        print(trans)
        # if _lang != "auto":
            # trans = translator.translate(translate_queue, dest=args.target, src=_lang)
            # trans = translator.translate(translate_queue, lang_tgt=args.target, lang_src=_lang, pronounce=True)
        # else:
            # trans = translator.translate(translate_queue, dest=args.target)
            # trans = translator.translate(translate_queue, lang_tgt=args.target, pronounce=True)
            # _lang = trans[0].src
            # END IF
        # END IF

        # Writing to CSV File
        count_err = 0
        filename = args.dir + "" + _lang + "-" + args.target + ".csv"
        with open(filename,'w', encoding='utf-16') as output_file:
            csv_out=csv.writer(output_file)
            # csv_out.writerow([_lang, args.target])
            # From 0..len(trans)==len(translate_queue)
            for i in range(len(trans)):
                t_origin = translate_queue[i]
                t_trans  = trans[i]
                # print(f'{t.origin} -> {t.text}')
                print(f' At index {i}: {t_origin} -> {t_trans}')

                # If there is no difference between the original text 
                # and its translation, we indicate there could be an
                # error in the translation

                if t_origin == t_trans:
                    count_err +=1
                    csv_out.writerow([t_origin, t_trans, "ERROR"])
                else:
                    csv_out.writerow([t_origin, t_trans])
            # END FOR
        # Reset
        print("ESTIMATED ERROR PERCENTAGE = ", count_err / len(trans) * 100, "%")
        count_err = 0
        # END WITH
        translation_lists.append(trans)
        trans = []
        translate_queue = []
# END FOR


    

