# -*- coding: utf-8 -*-
import pytest, allure
from DataSource import Actions as Ac, Checks as Ch, Variables as Va


@allure.story("New ticket creating")
@allure.description("Creating a new ticket, start from Main page")
class Test_Create_ticket():

    @allure.title("Start browser")
    def test_start(self, driver):
        Ac.Global().start_browser(driver)

    @allure.title("Creating a new ticket")
    def test_Create_ticket(self, driver, screenshot_on_failure):

        Ch.Main_page().check_Welcome_text_is_present(driver)

        Ac.Main_page().click_new_ticket(driver)

        Ch.New_Ticket_page().check_Page_Title_is_present(driver)

        Ac.New_Ticket_page().filling_form(driver)

        Ch.New_Ticket_page().check_ThankYou_msg(driver)

    @allure.title("Checking that ticket is created")
    def test_Check_ticket(self, driver, screenshot_on_failure):

        Ac.Global().start_browser(driver, Va.Sites.site + Va.Sites.Pages.login)

        Ac.Tickets_page().login(driver)

        Ch.Tickets_page().check_LogOut_is_present(driver)

        Ch.Tickets_page().find_ticket_by_subject(driver)