# fileTranslate
This will allow you to translate file from any language to english.

Google translate translations service allow users to translate text within 5k characters
or documents with a limit of 15k characters that ends you up with a partially
translated file and partially untranslated.

Here's an example of a victim to this problem: https://productforums.google.com/forum/#!topic/docs/pMeiE1pxyAQ

using this tool is realy simple
first make sure you install
```
$ sudo pip install googletrans
```
and
```
$ sudo pip install requests
```
After that all you got to do is run
```
$ python translate.py
```
## further explanation
you'll get this output:
```
Enter file path:
```
Enter your file path:
```file.txt```

Now check in the file directory you will find a ```translated-english``` directory
which will contain the translated file.
