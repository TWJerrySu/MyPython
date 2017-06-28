*** Settings ***
Library    Remote    http://10.1.214.181:8270    WITH NAME    Web_UI
Library    Collections
Library    OperatingSystem
Suite Setup    Login KKbox player         

*** Variables ***

${kk_url}         https://www.kkbox.com/play/
${kk_account}     0932208xxx
${kk_password}    xxxxx


          
    
*** Test Cases ***
    
    
Search specific keyword
    [Tags]      1
    Web_UI.input_search_bar    清平調
    sleep    5 
    
Goto radio play and unlike
    [Tags]      2
    Web_UI.goto_radio
    Web_UI.choose_first_radio
    web_UI.unlike

*** Keywords ***

Login KKbox player
    Web_UI.start    ${kk_url}
    Web_UI.login    ${kk_account}    ${kk_password}
