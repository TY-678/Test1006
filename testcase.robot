*** Settings ***
Library    ./TestMath.py



*** Variables ***



*** Test Cases ***
Test 1
    ${a}=    Evaluate    int(1)
    ${b}=    Evaluate    int(100)

    ${sum}=    Get Sum    ${a}    ${b}
    ${check_result}=    Evaluate    int(101)

    Should Be Equal    ${sum}    ${check_result}