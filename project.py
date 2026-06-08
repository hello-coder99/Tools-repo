#PROJECT
import requests
from bs4 import BeautifulSoup
import csv
csv_file=input("Enter csv filename :")
#BASE_URL = "http://www.howstat.com/cricket/Statistics/Matches/MatchList.asp?A="
#BASE_URL="http://www.howstat.com/cricket/Statistics/Matches/MatchScorecard.asp?MatchCode=2631"
#BASE_URL="https://www.howstat.com/cricket/Statistics/Matches/MatchScorecard.asp?MatchCode=2640"
#                                                            MatchScorecard_ODI.asp?MatchCode=5105
data = {
        "Match Date": "N/A",
        "Team 1": "N/A",
        "Team 2": "N/A",
        "Venue": "N/A",
        "Match Result": "N/A",
        "Top Scorer": "N/A",
        "Top Score": 0
        }

BASE_URL="https://www.howstat.com/Cricket/Statistics/Matches/MatchListCountry_ODI.asp"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
    "Cookie": "cf_chl_rc_ni=1; cf_clearance=rb8xum6qaG.MEQYAKH8u3y2oJjpW37Lz8dZxPFEyDRQ-1780623481-1.2.1.1-5FPtHASZUPcFO0Vo41doxxbYpY6q1kVtNL_.rzagGgABy036X3SwpWyPWOnFHJwyehaG3pxlmJWVT27DM8lSIDxgpNPlhmJJH8Jh8NRP2vKo0bpn3I0i3lONszYrOAz.aRnknb_7ji9HWQEZ.UWbij2Q.DgDZe_C5wpToBmTki7gmz.oCM7y.sFhIrtvO4qJtASoOMbUQOfIo7ssBGCJDuztxRqcXW71ji197NIFZDY8OPFNkpCHC0OU35.Vf47GpKjez8yo7xuNghJ8rJmXNOczbrkB8WeMJp4Ys5aBkWTAo1Qod8SK0o5NPdQgW5geLPfqs3N0kty9_FBiySzoZEuzh21XSplySAre1JvRuGvOvw8ntlQfPBxuqiopxyZNjY5PXcOHBSvGSPn3nnTo24C8SRiuZMtgqRjekZ261C8",
    "Origin": "https://www.howstat.com",
    "Sec-Fetch-Site": "same-origin"
}
#=================================
def extract_match_data(html_content):

    #with open(html_file, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(html_content, "html.parser")

    # ==========================
    # Extract title information
    # ==========================

    if soup.title:

        title = soup.title.text.strip()

        # Example:
        # Scorecard - 2022-2023 India v Australia - 1st ODI
        # - 17/03/2023 - Wankhede Stadium, Mumbai

        parts = title.split(" - ")

        if len(parts) >= 5:

            teams = parts[1]

            if " v " in teams:

                team1, team2 = teams.split(" v ")

                data["Team 1"] = team1.strip()
                data["Team 2"] = team2.strip()

            data["Match Date"] = parts[3].strip()
            data["Venue"] = parts[4].strip()

    # ==========================
    # Extract match result
    # ==========================

    page_text = soup.get_text("\n")

    lines = page_text.split("\n")

    for line in lines:

        line = line.strip()

        if "won by" in line.lower():
            data["Match Result"] = line
            break


#=================================
def page_parse(h_url):
    url="https://www.howstat.com/cricket/Statistics/Matches/"+h_url
    runs_list=[]
    # Replace this string with your method of loading the file, e.g., open("scorecard.html").read()
    response= requests.get(url=url,headers=HEADERS)
    html_content=response.text
    extract_match_data(html_content)
    soup = BeautifulSoup(html_content, "html.parser")
    ##addd function
    # Find all table rows in the document
    rows = soup.find_all("tr")

    print("=========================cricket match status==============================")
    player_data=dict()
    for row in rows:
        # Player profiles are linked via URLs containing 'PlayerOverview_ODI.asp'
        player_link = row.find("a", href=lambda href: href and "PlayerOverview_ODI.asp" in href)

        if player_link:
            player_name = player_link.text.strip()

            # The runs column is typically the next explicit text block highlighted with <b>
            runs_element = row.find("b")

            if runs_element:
                runs = runs_element.text.strip()
                if "/" not in runs and runs.isdigit():
                    player_data[player_name]=runs
    m_p=""
    m_r=0
    for player in player_data:
        runs=int(player_data[player])
        if m_r<runs:
            m_p=player
            m_r=runs
    data['Top Scorer']=m_p
    data['Top Score']=m_r
    save_to_csv(csv_file)    


#================================================
def save_to_csv(csv_file):

    with open(csv_file,
              "a",
              newline="",
              encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Match Date",
                "Team 1",
                "Team 2",
                "Venue",
                "Match Result",
                "Top Scorer",
                "Top Score"
            ]
        )
        writer.writeheader()
        for key in data:
            print(key," : ",data[key])
            writer.writerow(data)
        print("Data successfully updated in csv file......")
##main function ==============not scrore card======================
def parse_link(text):
    #with open("page.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(text, "html.parser")
    links = soup.find_all("a", class_="LinkTable")
    count=0
    limit=int(input("Enter the limit of records(default 10) :"))
    if(limit<=0 or limit>20):
        limit=10
    for link in links:
        #print(link["href"])
        page_parse(link["href"])
        if count==limit:
            return 
        count+=1

def main():
    f=open(csv_file,"w",newline="",encoding="utf-8")
    f.close()
    res=requests.get(url=BASE_URL,headers=HEADERS)
    parse_link(res.text)
if __name__ == "__main__":
    main()
