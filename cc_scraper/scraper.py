#   Copyright [2022] Chris J Daly (github user cjdaly)
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import requests, bs4

URL = "https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2"

rsp = requests.get(URL, timeout=10)
soup = bs4.BeautifulSoup(rsp.content, "html.parser")
tables = soup.find_all('table')
for t in tables:
    ths = t.find_all('th')
    if (len(ths) > 1) and ths[0].text.startswith("Code") and ths[1].text.startswith("Country name"):
        print("# generated from scraper.py")
        print("CC_to_Name = {")
        trs = t.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            if (len(tds) > 1):
                print('  "{}":"{}",'.format(tds[0].text, tds[1].text))
        print("}")
