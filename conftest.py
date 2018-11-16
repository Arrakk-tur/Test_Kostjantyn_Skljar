# -*- coding: utf-8 -*-
import pytest, allure, os
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture(scope="module")    # scope='session')
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd

@pytest.mark.tryfirst
def pytest_runtest_makereport(item, call, __multicall__):
    rep = __multicall__.execute()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def screenshot_on_failure(request, driver):
    def fin():
        attach = WebDriver.get_screenshot_as_png(driver)
        if request.node.rep_setup.failed:
            allure.attach(attach, request.function.__name__, allure.attachment_type.PNG)
        elif request.node.rep_setup.passed:
            if request.node.rep_call.failed:
                allure.attach(attach, request.function.__name__, allure.attachment_type.PNG)
    request.addfinalizer(fin)


