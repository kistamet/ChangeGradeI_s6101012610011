from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_index(self): #หน้า HomePage แรก
        #เอิร์ธได้ยินมาว่ามีเว็บในการคำนวณเกรดและอยากจะใช้งาน
        #จึงเข้าเว็บไปที่หน้า Homepage

        self.browser.get('http://localhost:8000')
        '''Test Only Index'''
        #เขาสังเกตุว่าชื่อเว็บจะมีคำว่า grade guide
        # She notices the page title and header mention to-do lists
        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        #Check HomePage, Sign Up and Log in Link
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        welcome_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Welcome to GradeGuide !', welcome_text)

        totaluser_text = self.browser.find_element_by_tag_name('p').text
        self.assertIn('Total users registered:', totaluser_text)

        #Check User Loging in
        login_click = self.browser.find_element_by_link_text('Log in')
        login_click.click()

        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        login_h2 = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Log in', login_h2)
        #check Label Username:
        username_label = self.browser.find_element_by_xpath("//label[@for='id_username']").text
        self.assertIn('Username:', username_label)
        #check Label Input Box
        username_box = self.browser.find_element_by_id("id_username")
        self.assertEqual(
            username_box.get_attribute('type'),
            'text'
        )
        #check Label Password:
        password_label = self.browser.find_element_by_xpath("//label[@for='id_password']").text
        self.assertIn('Password:', password_label)
        #check Label Input Pasword Box
        password_box = self.browser.find_element_by_id("id_password")
        self.assertEqual(
            password_box.get_attribute('type'),
            'password'
        )

        #check button
        login_button = self.browser.find_element_by_tag_name("button")
        self.assertEqual(
            login_button.get_attribute('type'),
            'submit'
        )

    def test_login_fail(self):#หน้า login เมื่อกรอกข้อมูลไม่ถูกต้อง
        #BASIC TEST
        self.browser.get('http://localhost:8000')
        '''Test Only Index'''
		# เขาสังเกตุว่าชื่อเว็บจะมีคำว่า grade guide
        # She notices the page title and header mention to-do lists
        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        welcome_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Welcome to GradeGuide !', welcome_text)

        totaluser_text = self.browser.find_element_by_tag_name('p').text
        self.assertIn('Total users registered:', totaluser_text)

        # Check User Loging in
        login_click = self.browser.find_element_by_link_text('Log in')
        login_click.click()

        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        login_h2 = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Log in', login_h2)
        # check Label Username:
        username_label = self.browser.find_element_by_xpath("//label[@for='id_username']").text
        self.assertIn('Username:', username_label)
        # check Label Input Box
        username_box = self.browser.find_element_by_id("id_username")
        self.assertEqual(
            username_box.get_attribute('type'),
            'text'
        )
        # check Label Password:
        password_label = self.browser.find_element_by_xpath("//label[@for='id_password']").text
        self.assertIn('Password:', password_label)
        # check Label Input Pasword Box
        password_box = self.browser.find_element_by_id("id_password")
        self.assertEqual(
            password_box.get_attribute('type'),
            'password'
        )

        # check button
        login_button = self.browser.find_element_by_tag_name("button")
        self.assertEqual(
            login_button.get_attribute('type'),
            'submit'
        )
        #END BASIC TEST
        error_message = self.browser.find_element_by_tag_name('ul').text
        self.assertIn('Please enter a correct username and password. Note that both fields may be case-sensitive.',
                      error_message)

        time.sleep(20)
        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        error_message = self.browser.find_elements_by_xpath("//ul[@class='errorlist nonfield']").text
        self.assertIn('Please enter a correct username and password. Note that both fields may be case-sensitive.', error_message)

    def test_login_pass(self):#หน้า login เมื่อกรอกข้อมูลผ่าน
        #basic test
        self.browser.get('http://localhost:8000')
        '''Test Only Index'''
        # เขาสังเกตุว่าชื่อเว็บจะมีคำว่า grade guide
        # She notices the page title and header mention to-do lists
        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        welcome_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Welcome to GradeGuide !', welcome_text)

        totaluser_text = self.browser.find_element_by_tag_name('p').text
        self.assertIn('Total users registered:', totaluser_text)

        # Check User Loging in
        login_click = self.browser.find_element_by_link_text('Log in')
        login_click.click()

        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        login_h2 = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Log in', login_h2)
        # check Label Username:
        username_label = self.browser.find_element_by_xpath("//label[@for='id_username']").text
        self.assertIn('Username:', username_label)
        # check Label Input Box
        username_box = self.browser.find_element_by_id("id_username")
        self.assertEqual(
            username_box.get_attribute('type'),
            'text'
        )
        # check Label Password:
        password_label = self.browser.find_element_by_xpath("//label[@for='id_password']").text
        self.assertIn('Password:', password_label)
        # check Label Input Pasword Box
        password_box = self.browser.find_element_by_id("id_password")
        self.assertEqual(
            password_box.get_attribute('type'),
            'password'
        )

        # check button
        login_button = self.browser.find_element_by_tag_name("button")
        self.assertEqual(
            login_button.get_attribute('type'),
            'submit'
        )
        #end basic test

        # Check Type Username Pass RIGHT !
        username_box.send_keys('jesselingard')
        password_box.send_keys('lingard123456789')
        # username_box.send_keys('tamtong007')
        # password_box.send_keys('o87525o135')
        login_button.click()
        # Check Redirect !!!!!

        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        logout_link = self.browser.find_element_by_link_text('Log out').text
        self.assertIn('Log out', logout_link)

        id_text = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('ID : jesselingard', id_text)

        '''Check Click Link
        homepage_click = self.browser.find_element_by_link_text('Home page')
        homepage_click.click()
        time.sleep(2)'''

        '''End of Checking Login'''

    def test_subjects_button_flow(self):#หน้า flow
        # เธอคลิกเข้ามาที่ link flow
        self.browser.get('http://localhost:8000/flow.html')
        time.sleep(5)

        # test Flow H1 text
        # เธอเห็นคำว่า Flow ซึ่งเป็นหัวข้อใหญ่
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual('Flow', header_text)

        # เธอเห็นประโยคที่อยู่ก่อนหน้าปุ่ม subjects
        defination = self.browser.find_element_by_tag_name('p1').text
        self.assertEqual("If you can't remember the subject's name , The Subjects button will help you. :)",defination)

        # test subjects button
        # เธอจำชื่อวิชาไม่ได้
        # เธอจึงคลิกไปที่ปุ่ม subjects เพื่อที่เธอจะได้ดูชื่อวิชา
        subject_button = self.browser.find_element_by_id("subject_button")
        subject_button.click()
        time.sleep(5)

        self.fail('Finish the test!')

    def test_search_flow(self):#ช่อง search หน้า flow
        # เธอคลิกเข้ามาที่ link flow
        self.browser.get('http://localhost:8000/flow.html')

        self.assertIn('', self.browser.title)

        # test search box
        # เธอเห็นช่องสำหรับใส่ชื่อวิชาเพื่อค้นหาวิชาที่เป็นตัวต่อกัน
        # เธอจึงพิมพ์วิชา Programming Fundamental ลงไป
        subject_placeholder = self.browser.find_element_by_id("search_placeholder")
        self.assertEqual(
            subject_placeholder.get_attribute('type'),
            'text'
        )

        subject_placeholder.send_keys('Programming Fundamental')
        time.sleep(5)

        # test submit button
        # เธอจึงกดปุ่ม search เพื่อทำการหาตัวต่อของวิชา Programming Fundamental
        submit_button = self.browser.find_element_by_id("submit_button")
        self.assertEqual(
            submit_button.get_attribute('type'),
            'submit'
        )
        submit_button.click()
        time.sleep(10)

        # test input Search text
        # เธอเห็นหัวข้อ subject
        # หลังจากที่เธอกด search แล้ว เธอพบว่าวิชาที่เธฮ search ไปปรากฏอยู่หลังหัวข้อ subject
        subject_head = self.browser.find_element_by_tag_name('h2').text
        self.assertEqual('subject : Programming Fundamental', subject_head)

        # test search result
        # เธอเห็นผลของการ search ของเธอ หลังจากที่กดปุ่ม search ไป
        result_search = self.browser.find_element_by_tag_name('p2').text
        self.assertEqual("Semister2 : Algorithms and Data Structures\nSemister5 : Operating Systems",result_search)

        # test Note
        # เธอเห็นประโยคด้านล่างเกี่ยวกับวิชาเลือก
        note = self.browser.find_element_by_tag_name('p3').text
        self.assertEqual("Note : Elective Subjects don't connect to each other but I want to show how many elective subjects are in this flow.", note)

        self.fail('Finish the test!')
        
    def test_flow_pic(self):# link หน้า flow
        # เธอคลิกเข้ามาที่ link flow
        self.browser.get('http://localhost:8000/flow.html')
        time.sleep(5)

        # test fullflow button
        # เธออยากดูภาพรวมของวิชาทั้งหมดที่เธอต้องเรียน
        # เธอจึงคลิกไปที่ปุ่ม Full Flow เพื่อไปยังรูป flow
        flow_button = self.browser.find_element_by_id("fullflow_button")
        flow_button.click()

        # test can find the flow picture
        # เธอเห็นภาพวิชาตัวต่อทั้งหมด
        flow_image = self.browser.find_element_by_id("image")
        self.assertEqual(
            flow_image.get_attribute('id'),
            'image'
        )
        time.sleep(10)

        self.fail('Finish the test!')
    def test_home(self):#การ signup และ login และการกรอกข้อมูลเข้าไปที่หน้า Gradecalculator
        # เมื่อเขากดเข้าไปที่หน้า signup
        self.browser.get('http://localhost:8000/signup')

        username_box = self.browser.find_element_by_id("id_username")

        password_box = self.browser.find_element_by_id("id_password1")

        password_box2 = self.browser.find_element_by_id("id_password2")

        # เขาทำการสมัคร username jesselingard
        # password lingard123456789
        # password2 lingard123456789
        username_box.send_keys('jesselingard')
        password_box.send_keys('lingard123456789')
        password_box2.send_keys('lingard123456789')
        # เขาทำการกดปุ่ม signup
        signup_button = self.browser.find_element_by_tag_name("button")
        signup_button.click()
        time.sleep(2)
        # เขาเข้าไปที่หน้า login
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Log in', header_text)

        username_login_box = self.browser.find_element_by_id("id_username")

        password_login_box = self.browser.find_element_by_id("id_password")
        # เขาใส่ id password
        username_login_box.send_keys('jesselingard')
        password_login_box.send_keys('lingard123456789')
        # เขากดปุ่ม login
        login_button = self.browser.find_element_by_tag_name("button")
        login_button.click()
        time.sleep(2)
        # เขาเข้าไปที่หน้า homepage
        self.browser.get('http://127.0.0.1:8000/home')
        id_user = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('jesselingard', id_user)
        # เขาใส่ unit
        unit_text = self.browser.find_element_by_id('subject1Unitid')
        unit_text.send_keys('Unit: 1')
        # เขาใส่ Grade
        unit_text = self.browser.find_element_by_id('subject1Gradeid')
        unit_text.send_keys('Grade: 2.5&nbsp; (C+)')
        time.sleep(3)
        # เขาเห็นเกรดแสดงขึ้นมา
        submit_button = self.browser.find_element_by_id("submit")
        submit_button.click()
        time.sleep(3)
        submit_text = self.browser.find_element_by_id('gradeshow').text
        self.assertIn('2.5', submit_text)
        time.sleep(6)
        # เขาเห็นสาถานะนักศึกษาของเขา
        self.assertIn('Normal State', submit_text)

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
