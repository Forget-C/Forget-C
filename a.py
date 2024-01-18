import datetime
import requests
import bs4

if __name__ == '__main__':
    url = 'https://blog.csdn.net/q1403539144'
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTHL, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    }
    html_file = requests.get(url, headers=headers)
    obj_soup = bs4.BeautifulSoup(html_file.text, 'lxml')

    result = []
    names = obj_soup.select('div .user-profile-statistics-name')
    numbers = obj_soup.select('div .user-profile-statistics-num')
    for i in range(len(numbers)):
      result.append("{}: {}".format(names[i].text, numbers[i].text))

    now_time = datetime.datetime.now()
    year = now_time.year
    month = now_time.month
    day = now_time.day
    hour = now_time.hour
    minute = now_time.minute
    second = now_time.second

    output = "\n{}_{}_{}_{}_{}_{}\t {}".format(year, month, day, hour, minute, second, result)
    with open("./csdn_data.txt", mode="a") as f:
      f.write(output)

