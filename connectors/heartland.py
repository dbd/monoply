import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Heartland():

    """Connector to Discover Student Loans"""

    def __init__(self, username, password, security_questions,
                 url=('https://heartland.ecsi.net'
                      '/index.main.html#/access/signIn')):

        """Create a new class with the default url for login

        :username: discover account username
        :password: discover account password
        :url: login url to use

        """

        self.username = username
        self.password = password
        self.security_questions = security_questions
        self.url = url

    def getBalance(self):
        """Get the balance for the Discover Loan
        :returns: decimal of loan balance

        """
        opts = Options()

        user_agent = ('user-agent=Mozilla/5.0 '
                      '(Macintosh; Intel Mac OS X 10_15_3) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.131 Safari/537.36')

        opts.add_argument(user_agent)

        driver = webdriver.Chrome(options=opts)
        driver.get(self.url)
        time.sleep(1)
        username = driver.find_element_by_id('signInUserName')
        username.clear()
        username.send_keys(self.username)
        password = driver.find_element_by_id('signInPassword')
        password.clear()
        password.send_keys(self.password)
        driver.find_element_by_id('signInFormSubmit').click()
        time.sleep(1)
        question = driver.find_element_by_css_selector("h2[ng-bind='secNo.question']").text
        answer = self.security_questions[question]
        sec = driver.find_element_by_id('inputSecAns')
        sec.clear()
        sec.send_keys(answer)
        driver.find_element_by_css_selector("button[ng-click='secNo.transit(secNo.securityAnswer)']").click()
        driver.get('https://heartland.ecsi.net/index.main.html#/app/page/accountoverview')
        time.sleep(5)
        driver.find_element_by_css_selector("p[ng-bind='campus.institutionName']").click()
        time.sleep(3)
        elements = driver.find_element_by_css_selector("div[class='col-md-5 col-sm-5 col-xs-5']")
        balance = elements.find_element_by_css_selector("h2[class='school-feature-set-content-heading ng-binding']").text
        return self._parse_balance(balance)

    @staticmethod
    def _parse_balance(balance):
        """Converts the string balance into a decimal

        :balance: String representation of string
        :returns: decimal

        """
        balance = balance.replace('$', '')
        balance = balance.replace(',', '')
        balance = float(balance)
        return balance
