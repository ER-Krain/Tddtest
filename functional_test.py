from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest
import time

class NewVisitorTest(unittest.TestCase):  #(1)
    
    def setUp(self):  #(3)
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()  #(3)

    def test_can_start_a_list_and_retrieve_it_later(self):  #(2)
        #edith has heard about a cool new online to-do app. She goes
        #to check out its homepage
        self.browser.get('http://localhost:8000')

        #She notice the page title and header mention to-do lists
        self.assertIn('To-Do',self.browser.title)  #(4)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)  #(5)

        #She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
            )
        
        #She types "Buy peacock feathers" into a text box (Edith's hobby
        #is trying fly-fishing luers)
        inputbox.send_keys('Buy peacock feather')

        #when she hits enter, the page updates, and now the page lists
        #"1:Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tage_name('tr')
        self.assertTrue(
            any(row.text == '1:Buy peacock feathers' for row in rows)
            )

        #There is still a text box inviting her to add another item. She
        #enters "Use peacock feathers to make a fly" (Edith is very methodical)
        self.fail('Finish the test')

if __name__ == '__main__':  #(6)
    unittest.main(warnings='ignore')  #(7)

#browser = webdriver.Firefox()      #(2)











#The page updates again, and now shows both items on her list

#Edith wonders whether the site will remember her list. Then she sees
#that the site has generated a unique URL for her -- there is some
#explanatory text to that effect

#She visits that URL - her to-do list is still there.

#Satisfied, she goes back to sleep

browser.quit()
