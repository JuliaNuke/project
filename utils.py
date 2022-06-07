import requests


def currency_rates(currency_code):
    currency_code = currency_code.upper()
    char_code_tag = "<CharCode>"
    value_start_tag = "<Value>"
    value_end_tag = "</Value>"
    cbr = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    html = cbr.text
    start_search_index = 0
    while True:
        curr_idx = html.find(char_code_tag, start_search_index)
        if curr_idx == -1:
            break
        curr_code = html[curr_idx + len(char_code_tag): curr_idx + len(char_code_tag) + 3]
        value_start_idx = html.find(value_start_tag, curr_idx)
        if value_start_idx >= 0 and curr_code == currency_code:
            value_end_index = html.find(value_end_tag, value_start_idx)
            value = float(html[value_start_idx + len(value_start_tag):value_end_index].replace(",", "."))
            return value
        start_search_index = curr_idx + 2*len(char_code_tag) + 3
    return None


if __name__ == '__main__':
    print(currency_rates('usd'))
    print(currency_rates('xxx'))
