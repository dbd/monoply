from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class GreatLakes():

    """Connector to Great Lakes Borrowers"""

    def __init__(self, username, password, pin,
                 url='https://mygreatlakes.org/educate/login.html'):
        """Create a new class with the default url for login

        :username: Username of user
        :password: Password of user
        :pin: Pin of user
        :url: default login url

        """

        self.username = username
        self.password = password
        self.pin = pin
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
        username = driver.find_element_by_id('userid')
        username.clear()
        username.send_keys(self.username)
        driver.find_element_by_id('authenticate').click()
        try:
            pin = driver.find_element_by_id('pinNumber')
            pin.clear()
            pin.send_keys(self.pin)
            driver.find_element_by_id('authenticate').click()
        except Exception as err:
            _ = err
            print(f'Didnt need pin for GreatLakes: {err}')
        password = driver.find_element_by_id('password')
        password.clear()
        password.send_keys(self.password)
        driver.find_element_by_id('authenticate').click()
        balance = driver.find_element_by_class_name(
                    'card-account-giant-text').text
        while balance == '':
            balance = driver.find_element_by_class_name(
                        'card-account-giant-text').text
        return self._parse_balance(balance)

    @staticmethod
    def _parse_balance(balance):
        """Converts the string balance into a decimal

        :balance: String representation of string
        :returns: decimal

        """
        print(balance)
        balance = balance.replace('$', '')
        balance = balance.replace(',', '')
        balance = float(balance)
        return balance
