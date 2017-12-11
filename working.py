from selenium import webdriver

# Init webdriver
br = webdriver.Chrome()
user = "username_goes_here"
pw = "password_goes_here"

# Log in
br.get('https://www.mathxlforschool.com/login_school.htm')
login_user = br.find_element_by_xpath('//*[@id="userName"]').send_keys(user)
login_pw = br.find_element_by_xpath('//*[@id="password"]').send_keys(pw)
sign_in_btn = br.find_element_by_xpath('/html/body/section[1]/div/div/fieldset/form[2]/button').click()

# Get average
avg = br.find_element_by_xpath('//*[@id="overallScore"]/p/span[1]').text
print(avg)
