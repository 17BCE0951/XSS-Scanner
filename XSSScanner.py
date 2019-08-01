import selenium
from selenium import webdriver 
from selenium.common.exceptions
import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException profile = webdriver.FirefoxProfile('/home/fake_batman_/.mozilla/firefox/x2n55od1.default') webdriver.DesiredCapabilities.FIREFOX["unexpectedAlertBehaviour"] = "accept" 
 
driver = webdriver.Firefox(firefox_profile=profile) 
 # url = 'http://testphp.vulnweb.com/' 
 # url = 'https://www.woodlandworldwide.com/' destination_url = 'https://www.woodlandworldwide.com/' url = 'https://www.lenovo.com/in/en/laptops/c/LAPTOPS' driver.get(url) 
html = driver.page_source input_counter = 0 text_counter = 0 button_counter = 0 id_name_counter = 0 reflected_counter = 0 reflected_tester = "I am batman" 
 # [text, 'id', number] 
list_of_input_tags = []
def XSS_checker(list_of_names_, button_name):
    with open("payloads") as file:
        payloads = file.read().split("\n")
        number = 0
        for payload in payloads:
            driver.get(url)
            try:
                for mName in list_of_names_:
                    if id_name_counter == 1:
                        name_field =  driver.find_element_by_id(mName)
                    else:  name_field = driver.find_element_by_name(mName)
                    if driver.current_url == destination_url:
                        driver.find_element_by_xpath('/html/body/nav/div/form/div').click()
                        name_field.send_keys(payload)

                        if id_name_counter == 1:
                            button_field = driver.find_element_by_id(button_name)
                        else:
                            button_field =  driver.find_element_by_name(button_name)
                            button_field.click() number += 1
                            try:
                                driver.switch_to.alert.accept()
                                print("Payload number: {}\tStatus:  {}".format(number, "Success"))
                                except NoAlertPresentException:
                                    print("Payload number: {}\tStatus:  {}".format(number, "Not success"))
                                except Exception:
                                    continue  

 
 
while True:
    if html.find('<input') != -1:
        input_tags = html[html.find('<input'):html.find('>', html.find('<input') + 1)]
        if input_tags.find("search") != -1 and input_tags.find("text") != -1:
            search_id = input_tags.find("name")
            search_text = input_tags[search_id:]
            id = search_text[search_text.find("\"") + 1:]
            id = id[:id.find("\"")]
            if id == '':
                id_name_counter = 1
                if id_name_counter == 1:
                    search_id = input_tags.find("id")
                    search_text = input_tags[search_id:]
                    id = search_text[search_text.find("\"") + 1:]
                    id = id[:id.find("\"")]
                list_of_input_tags.append([input_counter, 'search', id, button_counter])
                button_counter = 0
                text_counter += 1
                input_counter += 1
                print("Search field found...")
                elif input_tags.find("text") != -1:
                    text_id = input_tags.find("name")
                    field_text = input_tags[text_id:]
                    id = field_text[field_text.find("\"") + 1:]
                    id = id[:id.find("\"")]
                    if id == '':
                        id_name_counter = 1
                        if id_name_counter == 1:
                            search_id = input_tags.find("id")
                            search_text = input_tags[search_id:]
                        id = search_text[search_text.find("\"") + 1:]
                        id = id[:id.find("\"")]
                    list_of_input_tags.append([input_counter, 'text', id, button_counter])
                    button_counter = 0
                    text_counter += 1
                    input_counter += 1
                    print("Text field found...")
                elif input_tags.find("button") != -1 and input_tags.find("clear") != -1:
                    continue
                elif input_tags.find("button") != -1 or input_tags.find("submit") != -1:
                    button_id = input_tags.find("name")
                    button_text = input_tags[button_id:]
                    id = button_text[button_text.find("\"") + 1:]
                    id = id[:id.find("\"")]
                    if id == '':
                        id_name_counter = 1
                        if id_name_counter == 1:
                            search_id = input_tags.find("id")
                            search_text = input_tags[search_id:]
                            id = search_text[search_text.find("\"") + 1:]
                            id = id[:id.find("\"")]
                        list_of_input_tags.append([input_counter, 'button', id, text_counter])
                        button_counter += 1
                        text_counter = 0
                        input_counter += 1
                        print("Button field found...")
                        html = html[html.find('<input') + 1:]
                    else:
                        if input_counter == 0:
                            print("No input fields found!")
                            break
                        print(list_of_input_tags)
                        counter_www = 0
                        text_field_counter = 0
                        list_of_names = []
                        for input_tag in list_of_input_tags:
                            if input_tag[1] == 'search' or input_tag[1] == 'text':
                                id = input_tag[0] name = input_tag[2]
                                if id_name_counter ==1:
                                    nameField = driver.find_element_by_id(name)
                                else:
                                    nameField = driver.find_element_by_name(name)
                                text_field_counter += 1
                                if driver.current_url == destination_url and counter_www == 0:
                                    driver.find_element_by_xpath('/html/body/nav/div/form/div').click()
                                    counter_www = 1
                                    nameField.send_keys(reflected_tester) l
                                    ist_of_names.append(name)
                elif input_tag[1] == 'button':
                    name = input_tag[2]
                    if id_name_counter ==1:
                        buttonField = driver.find_element_by_id(name)
                    else:  buttonField = driver.find_element_by_name(name)
                    if text_field_counter == input_tag[3]:
                        text_field_counter = 0
                        buttonField.click()
                        if driver.page_source.find(reflected_tester) != - 1:
                            print("The value has been reflected...")  
 # Check for XSS reflected_counter = 1  if XSS_checker(list_of_names, name): break else:  list_of_names.clear() continue else:  driver.get(url) else:  print("Wrong button please check...")  # TODO: Implement spidering and go to other pages and implement the same 
 
 
