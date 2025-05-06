*** Settings ***
Library             SeleniumLibrary
Library             ../Library/ExtractPage.py



*** Variables ***
${link}                                        https://widgets.scorenco.com/old/61237b1e4a5cf15b5874d8d4
${page_html}                                   ""              
@{DATAS}                                       @{EMPTY}




*** Test Cases ***
Open Google Search Page  
    Open Browser                               ${link}                                            chrome
    Maximize Browser Window
    Wait Until Element Is Visible              xpath=//div[@id="simple-tabpanel-0"]               60s
    Click Element                              xpath=//*[text()="Calendrier"]
    Sleep                                      10s
    ${page_html}                               Get Source
    ${DATAS}                                   Extract Page                                       ${page_html}
    Log To Console                             ${DATAS}    
    Close Browser





*** Keywords ***

