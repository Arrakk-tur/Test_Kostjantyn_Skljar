# -*- coding: utf-8 -*-


class Sites:
    site = "http://safebreach-qa-test.dev.sbops.com/"

    class Pages:
        login = "scp/login.php"


class Credentional:

    class OsTicket:
        login = "devops"
        pswd = "123456a"

    class MySQL:
        login = "root"
        pswd = "123456a"

    class User:
        email = "traylen.jarian@lnvoke.org"     # temporary email (pswd: tqfbb9M@) (https://www.tempmailaddress.com/)
        name = "QA Tester"
        topic = "12"
        issue_summary = "Test issue Skljar K "
        description = "Description for Test issue created by Skljar K"


class Pages:

    class Main_page:            # by CSS_selector
        header_new_ticket = "a.new"
        header_status = "a.status"
        content_title = "h1"
        content_title_text = "Welcome to the Support Center"

    class New_Ticket_page:
        content_title = "h1"
        content_title_text = "Open a New Ticket"

        thankYou_msg = "#msg_notice"
        thankYou_msg_text = "Support ticket request created"

        class Form:
            email_input = "#ticketForm > table > tbody:nth-child(1) > tr:nth-child(2) > td > label > input"
            full_name = "#ticketForm > table > tbody:nth-child(1) > tr:nth-child(3) > td > label > input"
            topic_dropdown = "#topicId"
            ticket_details = "#dynamic-form > tr:nth-child(1) > td > div.form-header > h3"
            ticket_details_text = "Ticket Details"
            issue_summary = "#dynamic-form > tr:nth-child(2) > td > label > input"
            description = "div.redactor-editor.redactor-linebreaks.redactor-placeholder"
            submit_button = '#ticketForm > p > input[type="submit"]:nth-child(1)'

    class Status_page:
        content_title = "h1"
        content_title_text = "Check Ticket Status"

    class OsTicket:

        class Login_Form:
            name = "#name"
            pswd = "#pass"
            loginBtn = "#login > fieldset > button"

        class Tickets_page:
            logOut = "#info > a:nth-child(4)"
            logOut_text = "Log Out"

            row_first = "tbody > tr:nth-of-type(1) > td:nth-of-type(4)"
