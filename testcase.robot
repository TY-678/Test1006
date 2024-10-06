*** Settings ***
Library    ./TestMath.py



*** Variables ***



*** Test Cases ***
Test 1
    ${a}=    Evaluate    int(100)
    ${b}=    Evaluate    int(100)

    ${sum}=    Get Sum    ${a}    ${b}
    ${check_result}=    Evaluate    int(200)

    Should Be Equal    ${sum}    ${check_result}

Test Fail
    Fail    msg=for test parse

Test 2
    ${a}=    Evaluate    int(0)
    ${b}=    Evaluate    int(-10)

    ${sum}=    Get Sum    ${a}    ${b}
    ${check_result}=    Evaluate    int(-10)

    Should Be Equal    ${sum}    ${check_result}