from bs4 import BeautifulSoup
import requests


def url_finder(starting_url):    #generates URL for all 10 pages of bobs burger scripts
    list_of_links = [starting_url]
    counter = 0
    while counter != 225:
        counter += 25
        new_link = starting_url + '&start=' + f'{counter}'
        list_of_links.append(new_link)
    return list_of_links


def script_writer(list_of_links):  #finds URL of each individual script and then writes the contents of each script to a text file to be parsed later

    script_links = []

    for link in list_of_links:
        html_text = requests.get(link).text
        soup = BeautifulSoup(html_text, 'lxml')
        table = soup.find_all("td", "a", class_ = 'topic-titles row2')
        for item in table:
            temp = 'https://transcripts.foreverdreaming.org' + f'{item.h3.a["href"][1:]}'
            script_links.append(temp)

    for index, link in enumerate(script_links):
        html_text = requests.get(link).text
        soup = BeautifulSoup(html_text, 'lxml')
        text = soup.find("div", class_ = 'postbody')
        fin_text = text.find_all('p')
        name = soup.find('div', class_ = 't-header clearfix')
        fin_name = name.find('div', class_ = 'pull-left').a.string
        rid = 'Updates: (07/01/22) Summer Challenge & Censorship'
        if fin_name != rid:
            with open(f'Scripts\Episode {index}.txt', 'w', encoding = "utf-8") as f:
                for line in fin_text:
                    no_p = str(line)
                    end = no_p.replace("<p>", "").replace("</p>", "").replace("<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>", "").replace("♪ ♪", "").replace("<br/>", "").replace("<strong>", "")
                    f.write(f'{end}')
                    f.write('\n')
            f.close()


def note_finder():
    counter = 1
    total_lines = 0
    music_lines = 0
    while counter != 247:
        with open(f'Scripts\Episode {counter}.txt', 'r', encoding = 'utf-8') as f:
            counter += 1
            for line in f:
                total_lines += 1
                if "♪" in line:
                    music_lines += 1
    percent = round((music_lines / total_lines), 4) * 100
    print(f"{percent}% of the show Bob's Burger's contains singing")
    print('Liam Was Right!')



def corrector():    #removing summer challenges post
    html_text = requests.get('https://transcripts.foreverdreaming.org/viewtopic.php?f=428&t=20934&sid=2dd02a8649d3a017496c9a6e35c2c36a').text
    soup = BeautifulSoup(html_text, 'lxml')
    text = soup.find("div", class_='postbody')
    fin_text = text.find_all('p')
    counter = 26
    while counter <= 234:
        with open(f'Scripts\Episode {counter}.txt', 'w', encoding="utf-8") as f:
            counter += 26
            for line in fin_text:
                no_p = str(line)
                end = no_p.replace("<p>", "").replace("</p>", "").replace(
                    "<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>", "").replace("♪ ♪", "").replace(
                    "<br/>", "").replace("<strong>", "")
                f.write(f'{end}')
                f.write('\n')
        f.close()


note_finder()