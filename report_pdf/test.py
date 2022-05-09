from fpdf import FPDF
from database import collection, get_player_name
from PIL import Image
import os

player = get_player_name()[0]
print(player)


def table_column():
    document = collection.find({'player_name': player})
    for info in document:
        match_history = list(info['match_history'][0].keys())
        return match_history


TABLE_COL_NAMES = table_column()
print(TABLE_COL_NAMES)


def table_data():
    document = collection.find({'player_name': player})
    match_data = []
    for info in document:
        try:
            for x in range(30):
                # pprint.pprint(info)
                match_info = list(info['match_history'][x].values())
                match_info = [str(y) for y in match_info]
                # print(match_info)

                # print(match_info)
                match_data.append(match_info)
        except IndexError:
            pass

    return match_data


TABLE_DATA = table_data()

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 8)
pdf.cell(40, 10, "Competitive Match history from Last 30 matches played :", ln=True)
line_height = pdf.font_size * 2.9
col_width = pdf.epw / len(TABLE_COL_NAMES)  # distribute content evenly


def render_table_header():
    pdf.set_font("helvetica", "B", 7)  # enabling bold text
    for col_name in TABLE_COL_NAMES:
        # print(len(col_name))
        if len(col_name) > 7:
            # col_name = col_name.replace('-', '\n')
            pdf.cell(col_width, line_height, col_name, border=1)
        elif len(col_name) <= 7:
            pdf.cell(col_width, line_height, col_name, border=1)
    pdf.ln(line_height)
    pdf.set_font(style="")  # disabling bold text


render_table_header()
for _ in range(1):  # repeat data rows
    pdf.set_font("helvetica", "", 7)
    for row in TABLE_DATA:
        if pdf.will_page_break(line_height):
            render_table_header()
        for datum in row:
            pdf.cell(col_width, line_height, datum, border=1)
        pdf.ln(line_height)


def add_graphics():
    pdf.add_page()
    pdf.set_font("helvetica", "B", 12)
    text = ['Average Damage | Headshot Percentage | Last 15 or less Competitive Matches :',
            'Kill vs Deaths | Last 10 or less Competitive Matches :',
            'Map frequency and Win Percentage | Last 30 or less Competitive Matches :']
    path = "C:\\Users\\Rango\\PycharmProjects\\valorant-stats-tracker\\images"
    dir_list = os.listdir(path)
    images = []
    for files in dir_list:
        file = f'{path}\\{files}'
        images.append(file)
    # print(images)
    for x in range(3):
        pdf.cell(40, 10, text[x], ln=True)
        pdf.cell(40, 10, ln=True)
        try:
            img = Image.open(images[x])
        except IndexError :
            break
        # img = img.resize((720, 900))
        pdf.image(img, h=pdf.eph / 2.5, w=pdf.epw)
        pdf.cell(40, 10, ln=True)


add_graphics()
pdf.output("report.pdf")