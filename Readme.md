# Valfred - Valorant Game Assistant :

Get Visual data statistics report of your played Competitive matches. The statistics report is formatted in pdf and it will ask if the user wants it to be sent via email. It scrapes the data from dak.gg using Selenium and Beautiful Soup. For Data Storage I am using MongoDB with the Pymongo library, other libraries used in the program are Matplotlib, Numpy, Pandas for data visualization, Fpdf2 for generating pdf files, Os & Shutil for Opening and deletion of files, Smtplib for formatting and sending emails.

## Screenshots 
![alt text](https://github.com/saifkwik/Valfred-Valorant-Game-Assistant/blob/main/screenshots/bar_charts.png)
![alt text](https://github.com/saifkwik/Valfred-Valorant-Game-Assistant/blob/main/screenshots/pie_chart.png)
![alt text](https://github.com/saifkwik/Valfred-Valorant-Game-Assistant/blob/main/screenshots/match_history.png)
![alt text](https://github.com/saifkwik/Valfred-Valorant-Game-Assistant/blob/main/screenshots/email.png)
## Installation

Clone the repo and install the requirements of the program.

```bash
pip install requirements.txt
```

## Usage
* Enter your game username with the hashtag (like ~ peacemaker#dceu)
* If your account is private, the riot authentication page will auto open in browser. After signing in your account information is made public and the browser will autoclose.
![alt text](https://github.com/saifkwik/Valfred-Valorant-Game-Assistant/blob/main/screenshots/riot_authentication.png)
* report.pdf will auto-open after the program is executed.
* program will ask if you want the report.pdf sent to you via email type(y/n) and enter your email id. Email may take 2-3 minutes to appear in your inbox.

## Program Workflow
 ![alt text](https://github.com/saifkwik/Valfred-Valorant-Game-Assistant/blob/main/screenshots/valfred.png)

## MongoDB player Database Design
 ![alt text](https://github.com/saifkwik/Valfred-Valorant-Game-Assistant/blob/main/screenshots/player_db1.png)
 ![alt text](https://github.com/saifkwik/Valfred-Valorant-Game-Assistant/blob/main/screenshots/player_db2.png)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)