import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def test_mail(self):
    
        stu_1 = Student('Robin', 'Wills', 25000)
        stu_2 = Student('Mark', 'Smith', 28000)
        
        self.assertEqual(stu_1.mail, 'Robin.Wills@xyz.com')
        self.assertEqual(stu_2.mail, 'Mark.Smith@xyz.com')

        stu_1.first = 'Jenifer'
        stu_2.first = 'Graham'

        self.assertEqual(stu_1.mail, 'Jenifer.Wills@xyz.com')
        self.assertEqual(stu_2.mail, 'Graham.Smith@xyz.com')

    def test_fullname(self):
    
        stu_1 = Student('Robin', 'Wills', 25000)
        stu_2 = Student('Mark', 'Smith', 28000)

        self.assertEqual(stu_1.fullname, 'Robin Wills')
        self.assertEqual(stu_2.fullname, 'Mark Smith')

        stu_1.first = 'Jenifer'
        stu_2.first = 'Graham'

        self.assertEqual(stu_1.fullname, 'Jenifer Wills')
        self.assertEqual(stu_2.fullname, 'Graham Smith')

    def test_stipend_hike(self):
     
        stu_1 = Student('Robin', 'Wills', 25000)
        stu_2 = Student('Mark', 'Smith', 28000)
     
        stu_1.apply_hike()
        stu_2.apply_hike()

        self.assertEqual(stu_1.stipend, 26250)
        self.assertEqual(stu_2.stipend, 29400)

if __name__ == '__main__':
    unittest.main()







































