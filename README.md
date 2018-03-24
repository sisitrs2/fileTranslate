# fileTranslate
This will allow you to translate large files using google translate.

Google translate translations service allow users to translate text within 5k characters
or documents, but there's a bug (or some kind of limitation) that ends you up with a partially
translated file and partially untranslated.

Here's an example of a victim to this problem: https://productforums.google.com/forum/#!topic/docs/pMeiE1pxyAQ

using this tool is realy simple but probably not the best way XD
just run
```
$ python devideFile.py
```
you'll get this output:
```
Enter file path:
```
Enter your file path:
```file.txt```
you'll get parts of your file as so:
```
ls:
file(1).txt file(2).txt
```
now go to: https://translate.google.com/?tr=f
Enter your file(1).txt, copy result to the same file.
do the same for the rest of your files.
then run
```
$ python combineFile.py
```
you'll get this output:
```
Enter file path: 
```
Enter your file path:
```file.txt```
and you'll have your single translated file.txt
