from robot.api.deco import keyword
from bs4 import BeautifulSoup
from toolkits.bs4_extension import ( 
                        extract_element_by_locator, 
                        get_element_by_locator,
                        get_all_element_by_locator)
from toolkits.loggers import show_message
from toolkits.file_manager import get_json_file_content, save_json_data
from datetime import datetime


months_fr_short = {
    'jan': '01',
    'fév': '02',
    'mar': '03',
    'avr': '04',
    'mai': '05',
    'jun': '06',
    'jui': '07',
    'aoû': '08',
    'sep': '09',
    'oct': '10',
    'nov': '11',
    'déc': '12'
}


def extract_page(page_html:str) -> list:
    def clean_text(text) -> str:
        return text.strip().replace('\u00e9', 'é')
    
    def format_date(unformated_date:str, unformated_time:str) -> str:
        show_message("INFO", f"{unformated_date} {unformated_time}")
        unformated_date = unformated_date.split(' ')
        date = f"{datetime.now().year}-{months_fr_short[unformated_date[1][:3]]}-{unformated_date[0]}"
        return f"{date} {unformated_time}"
    cleaned_data = []
    selectors = get_json_file_content("/home/keller/Documents/Jobdev/G2A/SOC/selectors.json")
    page_html = BeautifulSoup(page_html, 'html.parser')
    container = get_element_by_locator(page_html, selectors.get('container')[0])
    print(container)
    datas = get_all_element_by_locator(container, selectors.get('datas')[0])
    # name = extract_element_by_locator(page_html, selectors.get('match_name')[0])
    for data in datas:
        new_data = {}
        divs = data.find('div', {'class':"event-content"}).find_all('div')
        print(len(divs))
        new_data['id'] = ""
        new_data['team1'] = clean_text(divs[0].text)
        new_data['team2'] = clean_text(divs[-1].text)
        new_data['name'] = f"{clean_text(divs[0].text)} - {clean_text(divs[-1].text)}"
        date = divs[1].find_all('div')[0].text
        time = divs[1].find_all('div')[1].text
        new_data['date'] = format_date(date, time)
        new_data['type'] = "match"
        new_data['address'] = extract_element_by_locator(data, selectors.get('adress')[0])
        new_data["zipcode"] = ""
        new_data["city"] = ""
        new_data["gps"] = ""
        print(new_data)
        cleaned_data.append(new_data)
    return cleaned_data