# LangMaster

Language Master or LangMaster for short is a set of scripts and tools whose objective is to help you in the process of learning a new language. Particularly, it will be useful for you if you want to learn a new language but do not know how to start or find starting out the most difficult.

Currently it has hardcoded .csv files that come from analyzing subtitles from opensubtitles.org, which can be obtained from [The OpenSubtitles 2018 dataset](https://opus.nlpl.eu/OpenSubtitles-v2018.php). They are lists of the most used words of a language. 

These files can be parsed with `translate.py`. It uses [deep-translator](https://github.com/nidhaloff/deep-translator) to generate a CSV file with the words and their respective translation. It will also perform simple error checking: if the translated text and the original text are the same, an additional column `ERROR` will appear in the CSV file, warning the user of a possible error. This is particularly useful in lesser known languages such as icelandic or to remove english words that are relatively common in subtitles.



Furthermore, it attempts to obtain the basics of the alphabet of said language, including phonetic information.

## Current Status

It is currently being used with Icelandic, Norwegian, and German. A preset of 1000 common words (according to the subtitles) is generated, and manually corrected after the process of automatic translation. 

## Further Updates

- [ ] Automatically download, parse and analyze the subtitle dataset for a specific language: currently not being done for lack of disk space.
- [ ] Add an index of the best automatic translators for each language: `deep-translator` allows the usage of multiple websites, and to improve the efficiency of the process, reducing the amount of errors (which can be very high) is key.
- [ ] Improve the Readme so that it contains more useful information.

## Usage

LangMaster allows for multiple arguments. @TODO: Explain them. This is a usage example: 

```
λ python translate.py -f data_test/icelandic.csv data_test\norwegian.csv data_test\german.csv -l is no de -t en -v -fl 1000 -d Storage/
```
