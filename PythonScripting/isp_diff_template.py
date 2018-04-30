"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """

    list1 = line1.split()
    list2 = line2.split()
    #len1 = len(list1)
    #len2 = len(list2)
    #print(len(list1), len(list2))
    pos2 = 0
    if not line1:
        if line2:
            return 0
    elif not line2:
        if line1:
            return 0

    for word1, word2 in zip(list1, list2):
        if word1 != word2:
            pos1 = line1.find(word1)
            #print("pos1 ",pos1)
            if len(word1) < len(word2):
                for letter1,letter2 in zip(word1,word2):
                    pos2 = pos2 + 1
                    #print(pos2,letter1)
                    if letter1 != letter2:
                        return pos1 +pos2
                if pos1 == 0:
                    return pos1 +pos2
                else:
                    return pos1 + pos2

            if len(word2) < len(word1):
                for letter1,letter2 in zip(word1,word2):
                    pos2 = pos2 + 1
                    #print(pos2,letter1)
                    if letter1 != letter2:
                        return pos1 +pos2
                return pos1 +pos2
            for letter1, letter2 in zip(word1,word2):
                pos2 = pos2 + 1
                #print(pos2,letter1)
                if letter1 != letter2:
                    return pos1 +pos2-1
    return IDENTICAL

#print(singleline_diff('Python i  fun!', 'Python is fun!!!')); # Done
#print(singleline_diff('Python abcd  fun!', 'Python abc fun!!!')); # Done
#print(singleline_diff('abc', 'abb'));
#print(singleline_diff('abc', 'abcd')); # DONE
#print(singleline_diff('abcd', 'abc')); # Done
#print(singleline_diff('abcd', 'abcd'));
#print(singleline_diff('Python is  fun!', 'Python is fun!'));
#print(singleline_diff('', 'a'));
#print(singleline_diff('a', ''));

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    eq_str = ""
    for _ in range(idx):
        eq_str = eq_str + "="
    eq_str = eq_str + "^"
    diff_format = line1 +"\n"+eq_str+'\n'+line2+'\n'

    return diff_format

#print(singleline_diff_format('abc', 'abd', 2))

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    return (IDENTICAL, IDENTICAL)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    return []


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    return ""
