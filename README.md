# gs-autograder-template
Template for Gradescope autograder, using a mock version of vpython

This repository is a template for a Gradescope autograder capable of correctly grading a student-provided program utilizing the vPython package. A mock version of most vPython objects are stored in a file 'vpython.py' contained in the test folder. All calculations are carried out using vector objects, so these are a separate class in vpython.py, with appropriate mathematical operations defined.

If the students either submit a file downloaded from Glowscript.org, or else create their own, the autograder will use the local version of vpython.py. Then, no graphics display will occur, but all calculations these would require still take place using vector objects. These can then be used for unittest purposes.

The design of this autograder template was inspired by a more involved version by Geoff Schmit ([repository link](https://github.com/gcschmit/vpython-physics)), called physutil.py.
