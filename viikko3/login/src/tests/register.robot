*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username    newuser
    Set Password    secret123
    Set Password Confirmation    secret123
    Click    button >> text=Register
    Get Title    ==    Welcome to Ohtu Application!

Register Accepts Password Containing Digits
    Register User With Password    kalle123
    Get Title    ==    Welcome to Ohtu Application!

Register Accepts Password Containing Special Character
    Register User With Password    kalle#abc
    Get Title    ==    Welcome to Ohtu Application!

Register Accepts Matching Password And Confirmation
    Register User With Password    matching123
    Get Title    ==    Welcome to Ohtu Application!

Register Rejects Different Password And Confirmation
    Set Username    newuser
    Set Password    secret123
    Set Password Confirmation    different123
    Click    button >> text=Register
    Registration Should Fail With Message    Passwords do not match

Register Accepts Uppercase Password Containing Digits
    Register User With Password    KALLE123
    Get Title    ==    Welcome to Ohtu Application!

Register Accepts Uppercase Password Containing Special Character
    Register User With Password    KALLE#ABC
    Get Title    ==    Welcome to Ohtu Application!

Register Rejects Password Containing Only Lowercase Letters
    Register User With Password    kallekalle
    Registration Should Fail With Message    Password must contain at least one non-letter character

Register Rejects Password Containing Only Uppercase And Lowercase Letters
    Register User With Password    KalleKalle
    Registration Should Fail With Message    Password must contain at least one non-letter character

Register Rejects Password Containing Only Uppercase Letters
    Register User With Password    KALLEKALLE
    Registration Should Fail With Message    Password must contain at least one non-letter character

Register Without Username
    Set Password    secret123
    Set Password Confirmation    secret123
    Click    button >> text=Register
    Registration Should Fail With Message    Username and password are required

Register Without Password
    Set Username    newuser
    Click    button >> text=Register
    Registration Should Fail With Message    Username and password are required

Register With Username That Is Already In Use
    Set Username    kalle
    Set Password    kalle123
    Set Password Confirmation    kalle123
    Click    button >> text=Register
    Registration Should Fail With Message    User with username kalle already exists

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User    kalle    kalle123
    Go To Register Page

Register User With Password
    [Arguments]    ${password}
    Set Username    newuser
    Set Password    ${password}
    Set Password Confirmation    ${password}
    Click    button >> text=Register

Set Password Confirmation
    [Arguments]    ${password}
    Fill Secret    id=password_confirmation    $password

Registration Should Fail With Message
    [Arguments]    ${message}
    Register Page Should Be Open
    Get Text    body    *=    ${message}