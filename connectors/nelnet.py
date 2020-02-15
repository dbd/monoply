import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Nelnet():

    """Connector to Nelnet"""

    def __init__(self, username, password,
                 url='https://www.nelnet.com/Account/Login?ReturnUrl=%2Fhome%2Findex'):
        """Create a new class with the default url for login

        :username: Username of user
        :password: Password of user
        :url: default login url

        """

        self.username = username
        self.password = password
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
        time.sleep(2)
        username = driver.find_element_by_id('username')
        username.clear()
        username.send_keys(self.username)
        driver.find_element_by_id('submit-username').click()
        time.sleep(2)
        password = driver.find_element_by_id('Password')
        password.clear()
        password.send_keys(self.password)
        driver.find_element_by_id('submit-password').click()
        time.sleep(2)
        driver.get('https://www.nelnet.com/Loan/Details')
        time.sleep(2)
        balance_table = driver.find_element_by_css_selector("table[summary='Balance Table']")
        balance = balance_table.find_element_by_css_selector("td[class='ng-binding']").text
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

