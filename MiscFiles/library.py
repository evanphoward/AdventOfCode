import requests

def get_input(year, day):
    try:
        return open("input").read()
    except FileNotFoundError:
        target_url = 'https://www.adventofcode.com/' + str(year) + '/day/' + str(day) + '/input'
        session_key = open("../../MiscFiles/session-key").read().strip()
        response = requests.get(target_url, cookies={'session':session_key}).text.strip()
        open("input", "w").write(response)
        return response

