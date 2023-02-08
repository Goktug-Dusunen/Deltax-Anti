# Deltax-Anti
Hello, I am trying to make my own antivirus in this project, an anti virus based on artificial intelligence.

# ➤ :heavy_exclamation_mark: What does it do ?
```
This code appears to be part of an antivirus application that is 
used to recognize viruses by scanning files in a directory. 
The feature vectors of the files are calculated based on the MD5
hash value of each file and this hash value is compared to the virus 
hash values in a database. If a file matches a virus, that file tag is set as virus.
Feature vectors and tags of scanned files are used as training data,
and a model is created using the Support Vector Classification (SVC) algorithm.
If no match is found with one of the virus hash values in the database,
the message "No virus was found [✓]" is displayed. The found infected 
files are deleted and the message "Removed <file_path> as it was infected. [x]" is displayed.

This code is intended to detect viruses,
but unfortunately may not provide a reliable solution for virus detection.
Virus detection is a very difficult and rapidly changing field,
and viruses can constantly change and hide themselves. Therefore,
antivirus software needs to be constantly updated and improved.
Also, virus hashes in the database must be up-to-date, otherwise new viruses may not be detected.

This code uses an approach based on the hashes of viruses,
but such an approach may not be sufficient as viruses can easily replace 
themselves and invalidate this approach.
This code should only be used as part of an antivirus software 
and should be used in conjunction with other antivirus tools and techniques.
```
