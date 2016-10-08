GradeComment Documentation
==========================

GC reads a file with grade comments for multiple students and writes files that contain grade comments pertaining to each specific student.

Usage: py gradeComments.py filename [nowrap]

Where filename is a local file or a relative path to a file. If the nowrap argument is included, then any multiline grade comments will be made into a single line in the output files.

Example
-------

Input file:
    (-5) Late submission
        -Archer

	Implementation (90)
	===================
	(-50) Program is terrible
		-Archer
		-Figgis
	(-10) Main function not written
		+	very well
		-Archer
		-Poovey
	(+5) Program is good
		-Kane

	Style (10)
	==========
	(-5) No comments
		-Archer
	(-0) Name submitted files correctly
		-Kane

Output file "Archer.txt":
    (-5) Late submission

	Implementation (90)
	===================
	(-50) Program is terrible
	(-10) Main function not written
		very well

	Style (10)
	==========
	(-5) No comments

	Total: 30

Input File
----------

GC checks the first non-whitespace character to determine what the current line is. Allowed characters are any alphabetic character, "(", "-", "+", and "=". Lines that contain only whitespace are ignored. Lines that begin with any character other than those specified will cause the script to print a warning, but will not stop execution.

- Category: A grading category is a group of grade comments. They are all lines that begin with an alphabetic character. Categories are optional and the script will work fine if you do not include any. If the grading categories have a number surrounded by parentheses, it will be added to the total grade from which the grade comments of individual students will be subtracted or added to in order to find their total score. If the total grade feature is not used, the total for each student will be the points lost rather than their earned grade.

- Grade Comment: Start with "(". The suggested format for grade comments is "(-n) Comment" where n is any integer and the minus sign can also be a plus sign. If your comments are in that format, the script will be able to print the student's total number of points lost or gained at the end of their output file.

- Multi-line Grade Comment: If the line after a grade comment begins with "+", that line minus the plus sign will be appended to the current grade comment with a newline inbetween. This allows multi-line grade comments. Their is no limit to the number of lines a grade comment can have. If the script is called with "nowrap" as the argument after the filename, then the multiline grade comments will be made into a single line in the output files, with erroneous whitespace removed.

- Student Name: Start with "-" followed by the student's name. Output files will be written for each unique student name (not including the beginning dash). After all grade comments, there should be at least one student name, otherwise the script will print a warning and continue execution.

- Comment: Any line that starts with "=" will be ignored. Starting lines with a character not in the list of acceptable characters is not recommended due to the possibility of future additions to this program.

Output File
-----------

Output files will be written for each unique student name found in the input file, and each output file will have the name "studentname.txt". The output files will contain all grade comments associated with each individual student and the comments will be grouped into categories if there are any.
