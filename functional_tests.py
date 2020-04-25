from selenium import webdriver
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_homepage_and_test_login_pass(self):  # หน้า HomePage แรก
        # เอิร์ธได้ยินมาว่ามีเว็บในการคำนวณเกรดและอยากจะใช้งาน
        # จึงเข้าเว็บไปที่หน้า index.html
        self.browser.get('http://localhost:8000')
        '''Test Only Index'''
        time.sleep(3)
        #เขาสังเกตุว่ามีลิงค์ GRADGUIDE FLOW ABOUT HELP SIGNUP LOGIN
        homepage_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('GRADEGUIDE', homepage_link)

        signup_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('SIGNUP', signup_link)

        login_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('LOGIN', login_link)

        FLOW_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('FLOW', FLOW_link)

        ABOUT_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('ABOUT', ABOUT_link)

        HELP_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('HELP', HELP_link)
        time.sleep(3)
        #และเขาสังเกตุว่ามีข้อความ Welcome to GradeGuide !
        welcome_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Welcome to GradeGuide !', welcome_text)
        #เขาสังเกตุว่ามีข้อความ Total users registered: และจำนวน user
        totaluser_text = self.browser.find_element_by_tag_name('p').text
        self.assertIn('Total users registered:', totaluser_text)

        # เขาเข้าไปที่หน้า login
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        # เขาสังเกตุเห็นลิงค์ GRADGUIDE SIGNUP LOGIN FLOW ABOUT HELP
        homepage_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('GRADGUIDE', homepage_link)
        signup_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('SIGNUP', signup_link)
        login_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('LOGIN', login_link)
        FLOW_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('FLOW', FLOW_link)
        ABOUT_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('ABOUT', ABOUT_link)
        HELP_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('HELP', HELP_link)
        time.sleep(3)

        # เขาสังเกตุเห็นข้อความ Username:
        username_label = self.browser.find_element_by_xpath("//label[@for='id_username']").text
        self.assertIn('Username:', username_label)
        # เขาสังเกตุเห็นช่องให้กรอก Username
        username_box = self.browser.find_element_by_id("id_username")
        self.assertEqual(
            username_box.get_attribute('type'),
            'text'
        )
        # เขาสังเกตุเห็นข้อความ Password:
        password_label = self.browser.find_element_by_xpath("//label[@for='id_password']").text
        self.assertIn('Password:', password_label)
        # เขาสังเกตุเห็นช่องให้กรอก Password
        password_box = self.browser.find_element_by_id("id_password")
        self.assertEqual(
            password_box.get_attribute('type'),
            'password'
        )
        # เขาสังเกตุเห็นปุ่ม Log in
        login_button = self.browser.find_element_by_id("Login_button")
        self.assertEqual(
            login_button.get_attribute('type'),
            'submit'
        )

        # เขากรอก Username และ Password
        username_box.send_keys('loginpass')
        password_box.send_keys('test123456')
        time.sleep(3)

        # เขากดปุ่ม Log in
        login_button.click()
        time.sleep(3)

        # เมื่อ Log in เข้ามาแล้วเขาสังเกตุเห็น  GRADGUIDE LOGOUT FLOW ABOUT GRAPH RESULT GRADECALCULATOR HELP
        homepage_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('GRADGUIDE', homepage_link)
        login_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('LOGOUT', login_link)
        FLOW_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('FLOW', FLOW_link)
        ABOUT_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('ABOUT', ABOUT_link)
        GRAPH_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('GRAPH', GRAPH_link)
        RESULT_Dropdow = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('RESULT', RESULT_Dropdow)
        GRADE_CALUATOR_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('GRADECAL CULATOR', GRADE_CALUATOR_link)
        HELP_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('HELP', HELP_link)
        time.sleep(3)
    def test_login_fail(self):
        self.browser.get('http://localhost:8000')
        time.sleep(3)
        # เขาเข้าไปที่หน้า login
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        time.sleep(3)
        # เขาสังเกตุว่ามีลิงค์ GRADGUIDE FLOW ABOUT HELP SIGNUP และ LOGIN ที่เขาได้กดเข้ามา
        homepage_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('GRADGUIDE', homepage_link)

        signup_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('SIGNUP', signup_link)

        login_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('LOGIN', login_link)

        FLOW_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('FLOW', FLOW_link)

        ABOUT_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('ABOUT', ABOUT_link)

        HELP_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('HELP', HELP_link)
        time.sleep(3)
        # เขาเห็นข้อความ Username
        username_label = self.browser.find_element_by_xpath("//label[@for='id_username']").text
        self.assertIn('Username:', username_label)

        # และเขาเห็น ช่องให้กรอก Username
        username_box = self.browser.find_element_by_id("id_username")
        self.assertEqual(
            username_box.get_attribute('type'),
            'text'
        )

        # และเขาเห็นข้อความ Password
        password_label = self.browser.find_element_by_xpath("//label[@for='id_password']").text
        self.assertIn('Password:', password_label)
        # และเขาเห็น ช่องให้กรอก password
        password_box = self.browser.find_element_by_id("id_password")
        self.assertEqual(
            password_box.get_attribute('type'),
            'password'
        )
        # และเห็นปุ่ม login
        login_button = self.browser.find_element_by_id("Login_button")
        self.assertEqual(
            login_button.get_attribute('type'),
            'submit'
        )
        time.sleep(3)
        # เขากรอก username และ password
        username_box.send_keys('testloginfail')
        password_box.send_keys('testloginfail123456')
        time.sleep(3)
        # เขากดปุ่ม login
        login_button.click()
        error_message = self.browser.find_element_by_tag_name('tag_error').text
        # เขาสังเกตุเห็นข้อความ Please enter a correct username and password. Note that both fields may be case-sensitive.
        self.assertIn('Please enter a correct username and password. Note that both fields may be case-sensitive.',
                      error_message)
        time.sleep(3)

    def test_signup_test_calculateGrade_and_test_Button_search_Picture_in_Flowpage(self):
        self.browser.get('http://localhost:8000')
        time.sleep(3)
        # เมื่อเขากดเข้าไปที่หน้า SIGNUP
        self.browser.get('http://localhost:8000/signup')
        # เขาสังเกตุว่ามีลิงค์ GRADGUIDE FLOW ABOUT HELP LOGIN SIGNUP
        homepage_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('GRADGUIDE', homepage_link)
        signup_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('SIGNUP', signup_link)
        login_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('LOGIN', login_link)
        FLOW_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('FLOW', FLOW_link)
        ABOUT_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('ABOUT', ABOUT_link)
        HELP_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('HELP', HELP_link)
        time.sleep(3)
        username_box =self.browser.find_element_by_id("id_username")
        password_box =self.browser.find_element_by_id("id_password1")
        password_box2 =self.browser.find_element_by_id("id_password2")

        # เขาทำการสมัคร username kistamet1998
        # password kistamet123456
        # password2 kistamet123456
        username_box.send_keys('kistamet1998')
        password_box.send_keys('kistamet123456')
        password_box2.send_keys('kistamet123456')
        time.sleep(3)

        # เขาทำการกดปุ่ม signup
        signup_button = self.browser.find_element_by_id("SignUp_button")
        self.assertEqual(
            signup_button.get_attribute('type'),
            'submit'
        )
        signup_button.click()

        #เมื่อเขากดปุ่ม SIGNUP แล้วจะเข้ามาที่หน้า GRADECALCULATOR
        #เขามาแล้วเขาสังเกตุเห็น  GRADGUIDE LOGOUT FLOW ABOUT GRAPH RESULT GRADECALCULATOR HELP
        homepage_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('GRADGUIDE', homepage_link)
        logout_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('LOGOUT', logout_link)
        FLOW_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('FLOW', FLOW_link)
        ABOUT_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('ABOUT', ABOUT_link)
        GRAPH_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('GRAPH', GRAPH_link)
        RESULT_Dropdow = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('RESULT', RESULT_Dropdow)
        GRADE_CALUATOR_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('GRADECAL CULATOR', GRADE_CALUATOR_link)
        HELP_link = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('HELP', HELP_link)
        time.sleep(5)




        #การกรอกข้อมูลเข้าไปที่หน้า Gradecalculator
        #เขาเลือกเทอม
        Term_text = self.browser.find_element_by_id('subjectTermid')
        Term_text.send_keys('Term: 1')
        # เขาใส่ unit
        unit1_text = self.browser.find_element_by_id('subject1Unitid')
        unit1_text.send_keys('Unit: 1')
        # เขาใส่ Grade
        Grade1_text = self.browser.find_element_by_id('subject1Gradeid')
        Grade1_text.send_keys("Grade: 3.5&nbsp; (B+)")
        time.sleep(5)
        # เขาใส่ unit ตัวที่2
        unit2_text = self.browser.find_element_by_id('subject2Unitid')
        unit2_text.send_keys('Unit: 1')
        # เขาใส่ Grade ตัวที่2
        Grade2_text = self.browser.find_element_by_id('subject2Gradeid')
        Grade2_text.send_keys("Grade: 4&nbsp; (A)")
        time.sleep(5)
        # เขาเห็นเกรดแสดงขึ้นมา
        submit_button = self.browser.find_element_by_id("submit_button")
        submit_button.click()
        time.sleep(3)
        submit_text = self.browser.find_element_by_id('gradeshow').text
        self.assertIn('3.75', submit_text)
        time.sleep(6)
        # เขาเห็นสาถานะนักศึกษาของเขา
        State_text = self.browser.find_element_by_id('showStatus').text
        self.assertIn('Normal State', State_text)




        # เขาคลิกเข้ามาที่ link flow
        self.browser.get('http://localhost:8000/flow.html')
        time.sleep(3)

        # test Flow H1 text
        # เขาเห็นคำว่า Flow ซึ่งเป็นหัวข้อใหญ่
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual('Flow', header_text)

        # เขาเห็นประโยคที่อยู่ก่อนหน้าปุ่ม subjects
        defination = self.browser.find_element_by_tag_name('p1').text
        self.assertEqual("If you can't remember the subject's name , The Subjects button will help you. :)", defination)

        # test subjects button
        # เขาจำชื่อวิชาไม่ได้
        # เขาจึงคลิกไปที่ปุ่ม subjects เพื่อที่เขาจะได้ดูชื่อวิชา
        subject_button = self.browser.find_element_by_id("subject_button")
        subject_button.click()
        time.sleep(3)

        # เขาคลิกเข้ามาที่ link flow
        self.browser.get('http://localhost:8000/flow.html')

        self.assertIn('', self.browser.title)

        # test search box
        # เขาเห็นช่องสำหรับใส่ชื่อวิชาเพื่อค้นหาวิชาที่เป็นตัวต่อกัน
        # เขาจึงพิมพ์วิชา Programming Fundamental ลงไป
        subject_placeholder = self.browser.find_element_by_id("search_placeholder")
        self.assertEqual(
            subject_placeholder.get_attribute('type'),
            'text'
        )

        subject_placeholder.send_keys('Programming Fundamental')
        time.sleep(3)

        # test submit button
        # เขาจึงกดปุ่ม search เพื่อทำการหาตัวต่อของวิชา Programming Fundamental
        submit_button = self.browser.find_element_by_id("submit_button")
        self.assertEqual(
            submit_button.get_attribute('type'),
            'submit'
        )
        submit_button.click()
        time.sleep(3)

        # test input Search text
        # เขาเห็นหัวข้อ subject
        # หลังจากที่เขากด search แล้ว เขาพบว่าวิชาที่เขา search ไปปรากฏอยู่หลังหัวข้อ subject
        subject_head = self.browser.find_element_by_tag_name('h2').text
        self.assertEqual('subject : Programming Fundamental', subject_head)

        # test search result
        # เขาเห็นผลของการ search ของเขา หลังจากที่กดปุ่ม search ไป
        result_search = self.browser.find_element_by_tag_name('p2').text
        self.assertEqual("Semister2 : Algorithms and Data Structures\nSemister5 : Operating Systems", result_search)

        # test Note
        # เขาเห็นประโยคด้านล่างเกี่ยวกับวิชาเลือก
        note = self.browser.find_element_by_tag_name('p3').text
        self.assertEqual(
            "Note : Elective Subjects don't connect to each other but I want to show how many elective subjects are in this flow.",
            note)

        # เขาคลิกเข้ามาที่ link flow
        self.browser.get('http://localhost:8000/flow.html')
        time.sleep(3)

        # test fullflow button
        # เขาอยากดูภาพรวมของวิชาทั้งหมดที่เขาต้องเรียน
        # เขาจึงคลิกไปที่ปุ่ม Full Flow เพื่อไปยังรูป flow
        flow_button = self.browser.find_element_by_id("fullflow_button")
        flow_button.click()

        # test can find the flow picture
        # เขาเห็นภาพวิชาตัวต่อทั้งหมด
        flow_image = self.browser.find_element_by_id("image")
        self.assertEqual(
            flow_image.get_attribute('id'),
            'image'
        )
        time.sleep(3)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
