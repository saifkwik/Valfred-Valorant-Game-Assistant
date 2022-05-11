import os
import shutil

from PIL import Image
from fpdf import FPDF

from database import collection, get_player_name

pdf = FPDF()


def table_column(player):
    document = collection.find({'player_name': player})
    for info in document:
        match_history = list(info['match_history'][0].keys())
        return match_history


def table_data(player):
    document = collection.find({'player_name': player})
    match_data = []
    for info in document:
        try:
            for x in range(30):
                match_info = list(info['match_history'][x].values())
                match_info = [str(y) for y in match_info]
                match_data.append(match_info)
        except IndexError:
            pass

    return match_data


def render_table_header(TABLE_COL_NAMES):
    # pdf.add_page()
    # pdf.set_font("helvetica", "B", 8)
    # pdf.cell(40, 10, "Competitive Match history from Last 30 matches played :", ln=True)
    line_height = pdf.font_size * 2.9
    col_width = pdf.epw / len(TABLE_COL_NAMES)  # distribute content evenly
    pdf.set_font("helvetica", "B", 7)  # enabling bold text
    for col_name in TABLE_COL_NAMES:
        if len(col_name) > 7:
            pdf.cell(col_width, line_height, col_name, border=1)
        elif len(col_name) <= 7:
            pdf.cell(col_width, line_height, col_name, border=1)
    pdf.ln(line_height)
    pdf.set_font(style="")  # disabling bold text


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
    for x in range(3):
        pdf.cell(40, 10, text[x], ln=True)
        pdf.cell(40, 10, ln=True)
        try:
            img = Image.open(images[x])
        except IndexError:
            break
        pdf.image(img, h=pdf.eph / 2.5, w=pdf.epw)
        pdf.cell(40, 10, ln=True)


def delete_files():
    folder = 'C:\\Users\\Rango\\PycharmProjects\\valorant-stats-tracker\\images'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def generate_pdf(username):
    print('Generating Pdf Report')
    player = get_player_name(username)[0]
    pdf.add_page()
    pdf.set_font("helvetica", "B", 12)
    pdf.cell(40, 10, "Competitive Match history from Last 30 matches played :", ln=True)
    TABLE_COL_NAMES = table_column(player)
    TABLE_DATA = table_data(player)
    render_table_header(TABLE_COL_NAMES)
    line_height = pdf.font_size * 2.9
    col_width = pdf.epw / len(TABLE_COL_NAMES)  # distribute content evenly
    for _ in range(1):  # repeat data rows
        pdf.set_font("helvetica", "", 7)
        for row in TABLE_DATA:
            if pdf.will_page_break(line_height):
                render_table_header(TABLE_COL_NAMES)
            for datum in row:
                pdf.cell(col_width, line_height, datum, border=1)
            pdf.ln(line_height)
    add_graphics()
    pdf.output("report.pdf")
    file_path = 'C:\\Users\\Rango\\PycharmProjects\\valorant-stats-tracker\\images'
    delete_files()
    print('Report successfully generated')


# generate_pdf('peacemaker#dceu')

