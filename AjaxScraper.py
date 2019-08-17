
from __future__ import print_function
import httplib2
import os
import pprint
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import mechanize
import re
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import threading
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'

found_counter = 0
def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1cYrhzVauv62x6fk2S04hjAymFDF2CVueCub9ywPm624'

    def ret(range): #returns values given range
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheetId, range=rangeName).execute()
        vals = result.get('values', [])
        return vals;

    print("Gathering price data...")

    def eval_val(trade):
    #----------return value of trade-----------------
        des = []
        array = []
        item = ''
        color = ''
        array = trade.split()
        item = array[len(array)-1] # last element
        if len(array) > 1:
            color = array[len(array)-2]
        des.append(item)
        des.append(color)
        return des
        '''if re.search('xkey', trade):
            val=int(trade.split("x")[0])
            return val
        else:
            for i in range(wheels[0]):
                if re.search(trade, wheels[0][i], re.IGNORECASE):
                '''




    s = 'asdf=5;iwantthis123jasd'
    result = re.search('asdf=5;(.*)123jasd', s)
    print (result.group(1))
    result#------------------------------Wheels------------------------------
    wheels = []
    print("loading wheels")
    #print('C%d:Z%d' % (g,g))

    x=22
    while x < 38:
        rangeName = ('C%d:Z%d' % (x,x))
        if x == 22:
            x = 24
        x+=1
        wheel = ret(rangeName)
        # lateral cells are returned as a list with 1 long string - STUPID
        wheel_str = str(wheel[0]) #have to split the string into elements
        my_list = wheel_str.split(",")
        wheels.append(my_list)
        #wheels[color(14)][wheel(24)]


#---------------------------BM Decals-------------------------------
    bm_decals = []
    print("loading BM decals")

    rangeName = ('B42:B51')
    decal = ret(rangeName)
    bm_decals.append(decal)

    rangeName = ('D42:D51')
    price = ret(rangeName)
    bm_decals.append(price)

    #bm_decals[decal/price(2)][index(10)]

#--------------------------Import Bodies----------------------------
    bodies = []
    print("loading bodies")

    x = 55
    while x < 61:
        rangeName = ('C%d:P%d' % (x, x))
        if x == 55:
            x = 56
        x += 1
        body = ret(rangeName)
        # lateral cells are returned as a list with 1 long string - STUPID
        body_str = str(body[0])  # have to split the string into elements
        my_list = body_str.split(",")
        bodies.append(my_list)
        # bodies[body(4)][color(14)]
#-----------------------------Boost---------------------------------
    boosts = []
    print("loading boosts")

    x = 65
    while x < 72:
        rangeName = ('C%d:P%d' % (x, x))
        if x == 65:
            x = 66
        x += 1
        boost = ret(rangeName)
        # lateral cells are returned as a list with 1 long string - STUPID
        boost_str = str(boost[0])  # have to split the string into elements
        my_list = boost_str.split(",")
        boosts.append(my_list)
        # boosts[boost(6)][color(14)]

#--------------------Trade Data------------------------------------
    print("Launching browser...")

    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_refresh(False)
    br.addheaders = [('User-agent', 'Firefox')]

    browser = webdriver.Firefox()
    browser.get('https://rl-trades.com')
    end_loop = False


    def collect_data():
        #code
        #print("Getting Trades")
        trades_text = []
        trades = browser.find_elements_by_xpath('//*[@id="trade_results"]/tr[@class="new"]/td')
        for i in range(len(trades)):
            try:
                trades_text.append(trades[i].text) # collects all text data first
            except StaleElementReferenceException:
                pass
        # handling href links separately
        links_text = []
        links = browser.find_elements_by_xpath('//*[@id="trade_results"]/tr[@class="new"]/td/a')
        for i in range(len(links)):
            try:
                links_text.append(links[i].get_attribute("href")) # collects all text data first
            except StaleElementReferenceException:
                pass
        # print len(trades)  # list of new trade elements
        have = []
        want = []
        site = []
        #print(len(links)) #error 16
        #print(len(trades_text)/4) #error 22

        for i in range(len(trades_text)):
            if i % 4 == 0:
                site.append(trades_text[i])


        #Gather all h/w offers
        for i in range(len(trades_text)):
            if i % 4 == 1:
                have.append(trades_text[i])
                want.append(trades_text[i + 1]) #error index out of range
         #Filter out discord,steam,reddit
        f_index = []

        for i in range(len(site)):
            if site[i] == "DISCORD" or site[i] == "STEAM" or site[i] == "REDDIT":
               f_index.append(i)

        #removes filtered trades from lists AFTER traversing to avoid out of range
        i = len(f_index)-1
        while i >= 0:
            del have[f_index[i]]
            del want[f_index[i]]
            del site[f_index[i]]
            del links_text[f_index[i]]
            i-=1




        ''' Handling discord user names
        if links[i].get_attribute("data-user") is not None:
            print(links[i].get_attribute("data-user"))
            end_loop = True
        '''
        s_ex = [] #single exchange trade indexes

        # Only 1:1 item trades (no commas)
        for i in range(len(have)):
            if "," not in have[i] and "," not in want[i]:
                s_ex.append(i)
                #print("[H] " + have[i] + "(Item: " + eval_val(have[i])[0] + " Color: " + eval_val(have[i])[1] + ") " + " [W] " + want[i] + "(Item: " + eval_val(want[i])[0] + " Color: " + eval_val(want[i])[1] + ") ")
                #print(links_text[i])
                #print('')

            if "," not in want[i]:
                if re.search('fireworks', want[i], re.IGNORECASE) or re.search('type-s', want[i], re.IGNORECASE) or re.search('gt', want[i], re.IGNORECASE): #probably more efficient way to filter this
                    global found_counter
                    found_counter +=1
                    print (found_counter)
                    print("[H] " + have[i] + "(Item: " + eval_val(have[i])[0] + " Color: " + eval_val(have[i])[
                        1] + ") " + " [W] " + want[i] + "(Item: " + eval_val(want[i])[0] + " Color: " +
                          eval_val(want[i])[1] + ") ")
                    print(links_text[i])
                    print('')
        #for i in range(len(s_ex)):
            #if eval_val(have[i]) !=0 and eval_val(want[i])!=0:



        #threading.Timer(10, collect_data).start()
    data_tim = '' #string holder
 #waits for first new update before starting collection
    while True: #Replaces recursion to avoid max recursion limit
        try:
            top_element = browser.find_element_by_xpath('//*[@id="trade_results"]/tr[@class="new"]').get_attribute(
                "data-tim")
            if data_tim != top_element:
                collect_data()
                data_tim = top_element
        except (NoSuchElementException, StaleElementReferenceException):
            pass
    #threading.Timer(10, collect_data).start()
    #while (end_loop == False):
        #time.sleep(10)  # wait for new elements to load






if __name__ == '__main__':
    main()
