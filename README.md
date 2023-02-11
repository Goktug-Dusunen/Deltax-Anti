#[]deltax-icon.png
# Deltax-Anti
Hello, I am trying to make my own antivirus in this project, an anti virus based on artificial intelligence.

# ➤ :heavy_exclamation_mark: What does it do ?
```
This code aims to scan all files in a directory to determine if they contain viruses.
The code scans files and obtains their hashes using file hashes from the given databases.
The resulting hashes are used as feature vectors of the files.
A SVM (Support Vector Machine) model is then trained using these feature 
vectors and tags that identify whether the files contain viruses
(1 with virus, 0 without virus). The trained model is used to predict whether
the files contain viruses. If a file contains a virus, it is deleted and a message is given to the user about this situation.

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
