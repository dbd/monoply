from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Discover():

    """Connector to Discover Student Loans"""

    def __init__(self, username, password,
                 url=('https://www.discoverstudentloans.com'
                      '/MFA/EnterUsername.aspx')):
        """Create a new class with the default url for login

        :username: discover account username
        :password: discover account password
        :url: login url to use

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
        username = driver.find_element_by_id('userId')
        username.clear()
        username.send_keys(self.username)
        password = driver.find_element_by_id('password')
        password.clear()
        password.send_keys(self.password)
        driver.find_element_by_id('logInButton').click()
        elems = driver.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            if 'AccountDetail' in elem.get_attribute("href"):
                driver.get(elem.get_attribute("href"))
                break
        balance = driver.find_element_by_id('accountBalance').text
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
