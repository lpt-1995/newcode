import appium.webdriver.extensions.android.gsm.GsmCallActions
def test_mobile(self):
    self.driver.make_gsm_call('18202991488', GsmCallActions.CALL)
    self.driver.send_sms('18202991488','erdfderfewsfsd')
    self.driver.set_network_connection(1)

    self.driver.set_network_connection()
