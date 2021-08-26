# LangMaster

Language Master or LangMaster for short is a set of scripts and tools whose objective is to help you in the process of learning a new language. Particularly, it will be useful for you if you want to learn a new language but do not know how to start or find starting out the most difficult.

Currently it has hardcoded .csv files that come from analyzing subtitles from opensubtitles.org, which can be obtained from [The OpenSubtitles 2018 dataset](https://opus.nlpl.eu/OpenSubtitles-v2018.php). They are lists of the most used words of a language. 

These files can be parsed with `translate.py`. It uses [deep-translator](https://github.com/nidhaloff/deep-translator) to generate a CSV file with the words and their respective translation. It will also perform simple error checking: if the translated text and the original text are the same, an additional column `ERROR` will appear in the CSV file, warning the user of a possible error. This is particularly useful in lesser known languages such as icelandic or to remove english words that are relatively common in subtitles.

- [LangMaster](#langmaster)
  - [Current Status](#current-status)
  - [Further Updates](#further-updates)
  - [Usage](#usage)
  - [Directories](#directories)
    - [Translations](#translations)
    - [Resources](#resources)
    - [Anki](#anki)
      - [Switching Tags](#switching-tags)
      - [Precompiled Decks](#precompiled-decks)
  - [Information on Typical Errors Found in Subtitles and their Translations](#information-on-typical-errors-found-in-subtitles-and-their-translations)
    - [German](#german)
    - [Icelandic](#icelandic)
    - [Norwegian](#norwegian)
  - [Contribution Guidelines](#contribution-guidelines)

## Current Status

It is currently being used with Icelandic, Norwegian, and German. A preset of 1000 common words (according to the subtitles) is generated, and manually corrected after the process of automatic translation. 

## Further Updates

- [ ] Automatically download, parse and analyze the subtitle dataset for a specific language: currently not being done for lack of disk space.
- [ ] Add an index of the best automatic translators for each language: `deep-translator` allows the usage of multiple websites, and to improve the efficiency of the process, reducing the amount of errors (which can be very high) is key.
- [ ] Improve the Readme so that it contains more useful information.
- [ ] Add Anki Support to make flashcards.
- [ ] Furthermore, obtain the basics of the alphabet of the selected language, including relevant phonetic information.
- [ ] Normalize the corrected files. As of now, they don't have a clear/standard nomenclature for manually added translations. This happens when there is more information than a simple translation in the CSV file.

## Usage

LangMaster allows for multiple arguments. @TODO: Explain them. This is a usage example: 

```
λ python translate.py -f data_test/icelandic.csv data_test\norwegian.csv data_test\german.csv -l is no de -t en -v -fl 1000 -d Storage/
```

## Directories
### Translations

The `Translations` folder is where manually translated files should go. That is, when all errors in a file are corrected, you move it to this folder instead of the folder where they are temporarily stored.

### Resources

Specific resources for each language can be found in the `Resources` folder. However, the [Wiktionary](https://en.wiktionary.org) stands out as possibly the greatest resource there is for translation of individual words, acting as a very complete dictionary for most languages. It is useful to use it alongside another dictionary of your choice to ensure maximum coverage of the language (since both dictionaries may be missing some words).

### Anki

The `Anki` folder is the designated folder to export everything to [Anki](https://apps.ankiweb.net/), a popular open source software for flashcards. Once you run `to_anki.py` with your python distribution, files will appear in the directory. 
To import the files just press import on Anki's menu and then select the file.  Default import settings should suffice, but feel free to tinker around with them. You may want to create a new Deck or import the cards into another one that isn't the default deck.

#### Switching Tags
Tags are not really relevant. By default, the script adds an extra field to the CSV file that represents the tag of the card in the following format: `LangMaster [language_code]-[language_code]`. To change this, either modify the CSV file or change the script. There are a couple of premade tags in the script that you can choose from by simply commenting and uncommenting lines.

#### Precompiled Decks

You can access precompiled decks for Anki from the `Precompiled` subfolder within the `Anki` directory in the Anki Deck Package Format. These decks are preconfigured with the following settings:

- Maximum of New Cards per day: 50
- Maximum of Reviews per day: 500
- Show Answer Timer: ON

Once imported, these settings can be changed from within Anki.

## Information on Typical Errors Found in Subtitles and their Translations

In this section I will go over the most common errors that I have found in the subtitles dataset for the different languages to which I am applying LangMaster. These errors must be corrected manually: as far as I know, there's no reliable way of fixing them automatically. This is specially true of lesser known languages such as Icelandic or Norwegian, where as in German it seems more plausible (a querry to identify nouns and apply modifications should suffice).

### German

- [X] Not capitalizing nouns. For example: Writing `art` instead of `Art` (which makes a huge difference in German since the word doesn't have the same meaning as in English).

### Icelandic

- [X] Not using the correct letters. For example: Writing `við` as `vio`, `pér` instead of `þér` or even `pao` instead of `það`. This seems to be a simplification used by lazy subtitle writers who can't be bothered to write their language properly. Especially common with the letters `þ` and `ð`. Identifying these errors is a matter of trial and error until you understand enough of the orthography of the language to detect them efficiently.
- [X] Words like `vi` are used instead of the appropriate `við` for simplification. These words are often times valid in other nordic languages such as Swedish, but not in Icelandic. This creates issues with automatic translators, since they will attempt to translate anyways and often complete with a "similar" language when they can't find an approrpriate match.

### Norwegian

- [X] Not using the correct letters and/or accents. For example: Writing `å` as `a`.

## Contribution Guidelines

If you have the time/interest to do the work it takes to support another language and manually correct any errors found in the translating process, please, do so. I'd be very happy to merge your pull request, as it would be of great help to all those who want to learn the language.

There's no specific pull request format as of yet, as I don't think it is necessary in this kind of project. Just include basic information like the language that you are adding or the error that you are correcting, and ensure that you add proper resources to the `Resources` folder if you've used any.

Thanks =D

