# This script uses the corrected files in the Translations/ directory to create a .CSV file that
# can be easily imported into Anki.
# @info Another alternative was to use anki-connect, but I believe a CSV is better since both Anki Desktop 
# and Mobile (AnkiDroid, but I assume the rest do as well) support importing it where as anki-connect
# only works on the Desktop. 

from os import walk

corrected_files = []

for (path, _, files) in walk("Translations/"):
    for f in files:
        translated_file = path + f
        # print(f"'{tag}'")
        anki_file = "Anki/" + f
        with open(translated_file, 'r', encoding="utf-8") as open_file, open(anki_file, 'w', encoding="utf-8") as output_file:
            all_lines = open_file.readlines()

            # Tag: languages involved in the card. Three possibilities: short, long, short + watermark
            # tag = f.split(".")[0] # Short. Example: is-en, de-en, no-en
            tag = "LangMaster " + f.split(".")[0] # Short with Watermark
            # tag = ''.join('-'.join(all_lines[0].split(",")).split()) # Long: Icelandic-English, 
            # German-English, Norwegian-English. 
            # @info: This only works if the translated CSV has as its first item the names of the
            # two languages used.

            all_lines = all_lines[1:] # The first line is not useful in Anki
            all_lines = [f"{l.strip()}, {tag}\n" for l in all_lines]
            output_file.writelines(all_lines)
        # END
        print(translated_file, anki_file)
    # END
# END
print("Done")
