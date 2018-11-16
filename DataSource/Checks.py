# -*- coding: utf-8 -*-

import Variables as Va, Actions as Ac
import pytest, allure
from selenium.webdriver.support import expected_conditions as Ec


class Main_page(object):

    @allure.step("Check that Main page is loaded")
    def check_Welcome_text_is_present(self, driver):
        driver.find_element_by_css_selector(Va.Pages.Main_page.content_title)
        assert Ec.text_to_be_present_in_element(driver.find_element_by_css_selector(Va.Pages.Main_page.content_title),
                                                Va.Pages.Main_page.content_title_text)


class New_Ticket_page(object):

    @allure.step("Check that 'Open a New Ticket page' is loaded")
    def check_Page_Title_is_present(self, driver):
        driver.find_element_by_css_selector(Va.Pages.New_Ticket_page.content_title)
        assert Ec.text_to_be_present_in_element(driver.find_element_by_css_selector(Va.Pages.New_Ticket_page.content_title),
                                                Va.Pages.New_Ticket_page.content_title_text)

    @allure.step("Check that Thank you message is shown")
    def check_ThankYou_msg(self, driver):
        driver.find_element_by_css_selector(Va.Pages.New_Ticket_page.thankYou_msg)
        assert Ec.text_to_be_present_in_element(driver.find_element_by_css_selector(Va.Pages.New_Ticket_page.thankYou_msg),
                                                Va.Pages.New_Ticket_page.thankYou_msg_text)


class Status_page(object):

    @allure.step("Check that 'Ticket Status page' is loaded")
    def check_Page_Title_is_present(self, driver):
        driver.find_element_by_css_selector(Va.Pages.Status_page.content_title)
        assert Ec.text_to_be_present_in_element(driver.find_element_by_css_selector(Va.Pages.Status_page.content_title),
                                                Va.Pages.Status_page.content_title_text)


class Tickets_page(object):

    @allure.step("Check that 'osTicket page' is loaded")
    def check_LogOut_is_present(self, driver):
        driver.find_element_by_css_selector(Va.Pages.OsTicket.Tickets_page.logOut)
        assert Ec.text_to_be_present_in_element(driver.find_element_by_css_selector(Va.Pages.OsTicket.Tickets_page.logOut),
                                                Va.Pages.OsTicket.Tickets_page.logOut_text)

    @allure.step("Find ticket by subject")
    def find_ticket_by_subject(self, driver):
        driver.find_element_by_css_selector(Va.Pages.OsTicket.Tickets_page.row_first)
        assert Ec.text_to_be_present_in_element(driver.find_element_by_css_selector(Va.Pages.OsTicket.Tickets_page.row_first),
                                                Ac.New_Ticket_page.issue_summary)
