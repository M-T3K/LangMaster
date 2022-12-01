# @info This Script combines already existing language translations according to the meaning of words.

import argparse
import os
import csv
from collections import defaultdict


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-f", "--files", required=True, type=argparse.FileType('r', encoding='utf-8'), nargs='+', help="Include the list of files to be parsed and combined")
    argparser.add_argument("-v", "--verbosity", help="Enables/Disables verbose.", action="store_true")
    argparser.add_argument("-d", "--dir", help="Directory where the combined file will be stored. Must include trailing slash '/'", type=str)
    args = argparser.parse_args()

    if args.verbosity:
        print("Verbose Option Selected")
    n_files = len(args.files)
    print("Storage Directory:", args.dir)
    if not os.path.exists(os.path.dirname(args.dir)):
        print("Storage directory doesn't exist. Creating.")
        try:
            os.makedirs(os.path.dirname(args.dir))
        except OSError: 
            raise
    # END IF
    # Get languages from file name
    f_num = 0
    file_data = []
    trans_lang = os.path.basename(args.files[0].name)[3:5] # Translated language must be the same, otherwise it makes no sense
    target_file_name = args.dir + "translation_combo"
    while f_num < n_files:
        lang = os.path.basename(args.files[f_num].name)[0:2] # Get the language code
        target_file_name += "-" + lang
        file_data.append(args.files[f_num])
        f_num += 1
    target_file_name += "@" + trans_lang + ".csv"
    print(target_file_name)

    # Iterate through files contents and create dictionaries of the words associated to each
    dict_trans = defaultdict(list)
    full_language_names = []
    full_trans_lang_name = ""
    f_num = 0
    for _file in file_data:
        print(_file.name)
        csv_reader = csv.reader(_file, delimiter=',')
        file_line_count = 1
        for row in csv_reader:
            # print(row[0], row[1])
            ori_row = row[0].strip()
            trans_row = row[1].strip()
            if file_line_count == 1:
                full_language_names.append(ori_row)
                if full_trans_lang_name == "":
                    full_trans_lang_name = trans_row
            # End if
            else:
                print(ori_row, trans_row)
                trans_row_len = len(dict_trans[trans_row])
                if trans_row_len < f_num + 1:
                    while trans_row_len < f_num:
                        dict_trans[trans_row].append("")
                        trans_row_len += 1
                    dict_trans[trans_row].append("[ " + ori_row + " ]")
                else:
                    print(f_num, "f_num", dict_trans[trans_row])
                    dict_trans[trans_row][f_num] = dict_trans[trans_row][f_num][0:-2] + ";" + ori_row + " ]" 
                print(dict_trans[trans_row])
            # Loop Ending
            file_line_count += 1
        f_num += 1
    print(full_trans_lang_name, full_language_names)
    # print(dict_trans)
    # End For

    with open(target_file_name,'w', encoding='utf-8') as output_file:
        row1 = full_trans_lang_name
        for lang in full_language_names:
            row1 += "," + lang
        rows = [row1]
        for x in dict_trans:
            print(x, dict_trans[x])
            new_row = x
            for word in dict_trans[x]:
                new_row += "," + word
            rows.append('\n' + new_row)
        output_file.writelines(rows)
# END