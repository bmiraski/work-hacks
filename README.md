# work-hacks
A set of scripts to optimize some troublesome tasks at work

compareproperties.py: 
This will take two properties files and compare the list of keys in each one. This is helpful when seeing what might be missing from a new language, now that the properties files are insanely long for the project we are accomplishing..
A couple of things to note:
* This does not like Chinese characters (and I assume the same is true for Japanese). You will need to convert the file into ANSI, which will change any non-standard character into a "?", for the comparison to work.
* This isn't fully automated, so you need to edit the script with the file names, which need to either be full paths on your machine, or reside in the same directory as the script. Future enhancement to remove that dependency.
* The output is a results.txt file with the missing items grouped by file. If you plan to run this multiple times, you will want to make sure to rename the files. Yes, this could be done as a future enhancement.
* I am sure this isn't the most optimized code to do this (for example, I would have like to have been able to strip the property values immediately, but that was causing headaches), but it works, and for the file sizes we are dealing with it is fast, and especially so compared to the time it takes to do this in Excel.
* This is fungible to compare other lists of items in two files. The data clean would just be different.
