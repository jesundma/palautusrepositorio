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
    Go To    ${REGISTER_URL}

Set Username
    [Arguments]    ${username}
    Fill Text    id=username    ${username}

Set Password
    [Arguments]    ${password}
    Fill Secret    id=password    $password

Set Password Confirmation
    [Arguments]    ${password}
    Fill Secret    id=password_confirmation    $password

Registration Should Fail With Message
    [Arguments]    ${message}
    Register Page Should Be Open
    Get Text    body    *=    ${message}