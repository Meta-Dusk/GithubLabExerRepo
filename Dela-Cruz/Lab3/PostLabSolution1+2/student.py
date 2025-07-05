"""
File: student.py
(Currently modified)
Resources to manage a student's name and test scores.
"""
import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
    
    def __eq__(self, other):
        """Tests if two students have the same name."""
        return self.name == other.name
    
    def __lt__(self, other):
        """Tests if this student's name is less than another's."""
        return self.name < other.name
    
    def __ge__(self, other):
        """Tests if this student's name is greater than or equal to another's."""
        return self.name >= other.name

def main():
    """Tests the comparison operators and sorting of Student objects."""
    # Create a list of students with different names
    students = [
        Student("Ken", 5),
        Student("Alice", 5),
        Student("Bob", 5),
        Student("Diana", 5),
        Student("Charlie", 5)
    ]
    
    # Set some sample scores
    for student in students:
        for i in range(1, 6):
            student.setScore(i, random.randint(70, 100))
    
    # Test comparison operators
    print("Testing comparison operators:")
    print(f"Ken == Alice: {students[0] == students[1]}")
    print(f"Alice < Bob: {students[1] < students[2]}")
    print(f"Bob >= Alice: {students[2] >= students[1]}")
    print(f"Diana >= Diana: {students[3] >= students[3]}")
    print()
    
    # Print original list
    print("Original student list:")
    for student in students:
        print(student)
    print()
    
    # Shuffle and print
    random.shuffle(students)
    print("Shuffled student list:")
    for student in students:
        print(student)
    print()
    
    # Sort and print
    students.sort()
    print("Sorted student list (by name):")
    for student in students:
        print(student)

if __name__ == "__main__":
    main()