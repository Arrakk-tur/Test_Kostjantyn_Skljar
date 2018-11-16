# -*- coding: utf-8 -*-

import Variables as Va
import pytest, allure
from datetime import datetime
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

currentTime = datetime.now().strftime('%Y-%m-%d %H:%M')

# Actions
main_page = Va.Pages.Main_page()
new_ticket_form = Va.Pages.New_Ticket_page.Form()
osTickets_login = Va.Pages.OsTicket.Login_Form()
osTickets_ticket = Va.Pages.OsTicket.Tickets_page()


#credentionals
credentionals_User = Va.Credentional.User
credentionals_Login = Va.Credentional.OsTicket()


class Global(object):

    @allure.step("Start browser")
    def start_browser(self, driver, site=Va.Sites.site):
        driver.get(site)


class Main_page(object):

    @allure.step("Click 'Open a New Ticket' button")
    def click_new_ticket(self, driver):
        driver.find_element_by_css_selector(main_page.header_new_ticket).click()

    @allure.step("Click 'Check Ticket Status' button")
    def click_status(self, driver):
        driver.find_element_by_css_selector(main_page.header_status).click()


class New_Ticket_page(object):

    issue_summary = credentionals_User.issue_summary + currentTime

    @allure.step("Filling in form")
    def filling_form(self, driver):
        driver.find_element_by_css_selector(new_ticket_form.email_input).send_keys(credentionals_User.email)
        driver.find_element_by_css_selector(new_ticket_form.full_name).send_keys(credentionals_User.name)
        Select(driver.find_element_by_css_selector(new_ticket_form.topic_dropdown)).select_by_value(credentionals_User.topic)
        driver.find_element_by_css_selector(new_ticket_form.issue_summary).send_keys(New_Ticket_page.issue_summary)
        driver.find_element_by_css_selector(new_ticket_form.description).click()
        driver.find_element_by_css_selector(new_ticket_form.description).send_keys(credentionals_User.description)
        driver.find_element_by_css_selector(new_ticket_form.submit_button).click()


class Tickets_page(object):

    @allure.step("Login")
    def login(self, driver):
        driver.find_element_by_css_selector(osTickets_login.name).send_keys(credentionals_Login.login)
        driver.find_element_by_css_selector(osTickets_login.pswd).send_keys(credentionals_Login.pswd)
        driver.find_element_by_css_selector(osTickets_login.loginBtn).click()

