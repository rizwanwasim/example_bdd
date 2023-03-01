Feature: Orange hrm 
    Scenario: Logo Present on Homepage
        Given launch chrome browser
        When Open ornagehrm Homepage
        Then verify that the logo is Present
        # When Enter username as "Admin" and Enter password as "admin123"
        # And click on the login button
        # Then User must successfully login to the Dashboard Page
        And close the browser