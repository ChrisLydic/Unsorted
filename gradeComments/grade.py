import sys


class GradeText:
    def __init__( self, fileName, lineWrap ):
        self.gradeCategories = []
        self.dict = {}
        self.lineWrap = lineWrap
        self.gradeCap = 0

        try:
            with open( fileName ) as file:
                self.readFile( file )
        except IOError:
            exit( "Error: File not found" )
        
        for student in self.dict.keys():
            self.writeGrades( student )
        
    def readFile( self, file ):
        lineCount = 1
        gradeCategory = "none"
        gradeComment = ""
        gradeValue = 0

        for line in file:
            line = line.strip()
            
            # skip empty lines and lines that are only whitespace
            if len( line ) == 0:
                continue
            
            startChar = line[0]

            # marks category
            if startChar.isalpha():
                gradeCategory = line
                
                self.gradeCap += self.getNum( gradeCategory )
                self.gradeCategories.append( gradeCategory )
                
                if gradeCategory == "totalGrade" or gradeCategory == "none":
                    exit( "Error: Grading category named " + gradeCategory
                         + " is invalid" )

            # marks a new grade comment
            elif startChar == "(":
                gradeComment = line
                gradeValue = self.getNum( line )

            # marks grade comment continued on new line
            elif startChar == "+":
                if gradeComment == "":
                    print( "Error: '+' symbol before grading comment at "
                        + " line " + str(lineCount), file=sys.stderr )

                if self.lineWrap:
                    gradeComment += "\n" + line[1:]
                else:
                    gradeComment += " " + line[1:].strip()
            
            # marks a student name (should always be after a grade comment) 
            elif startChar == "-":
                student = line[1:].strip()

                if student in self.dict.keys() and gradeCategory in self.dict[student]:
                    if not gradeComment in self.dict[student][gradeCategory]:
                        self.dict[student][gradeCategory].append( gradeComment )

                        self.dict[student]["totalGrade"] += gradeValue

                elif student in self.dict.keys():
                    self.dict[student].update( { gradeCategory: [gradeComment] } )
                
                    self.dict[student]["totalGrade"] += gradeValue

                else:
                    self.dict.update(
                        { student: {
                            gradeCategory: [gradeComment],
                            "totalGrade": gradeValue 
                        } } )

            # marks a comment, so do nothing
            elif startChar == "=":
                pass

            else:
                print( "Error: Unknown char '" + startChar + "' at line "
                    + str(lineCount), file=sys.stderr )

            lineCount += 1
    
    def getNum( self, line ):
        sign = "+"
        number = ""

        for char in line:
            # todo: avoid other chars on line from breaking this!!!
            if char == "-":
                sign = "-"
            elif char == "+":
                sign = "+"
            elif char.isdigit():
                number += char
            elif char == ")":
                break
        
        if number == "":
            return 0
        
        if sign == "-":
            return int(number) * -1
        else:
            return int(number)
    
    def writeGrades( self, student ):
        stuGrades = self.dict[student]
        stuTotal = stuGrades["totalGrade"]
        del stuGrades["totalGrade"]

        with open( student + ".txt", mode="w" ) as file:
            if "none" in stuGrades.keys():
                for gradeComment in stuGrades["none"]:
                    file.write( gradeComment + "\n" )
            
            for category in self.gradeCategories:
                file.write( category + "\n" )
                file.write( "=" * len( category ) + "\n" )
                
                if category in stuGrades.keys():
                    for gradeComment in stuGrades[category]:
                        file.write( gradeComment + "\n" )

                file.write( "\n" )

            file.write( "Total: " + str( self.gradeCap + stuTotal ) )


if __name__ == "__main__":
    if len( sys.argv ) == 2:
        GradeText( sys.argv[1], True )

    elif len( sys.argv ) > 2:
        if sys.argv[2] != "nowrap":
            exit( "Error: Argument '" + sys.argv[2] + "' invalid" )

        GradeText( sys.argv[1], False )
    else:
        print( "usage: py grade.py filename [nowrap]" )
