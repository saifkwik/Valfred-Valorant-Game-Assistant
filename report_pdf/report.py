from fpdf import FPDF
from database import collection, get_player_name

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
pdf.cell(40, 10, "Last 30 Match history", ln=True)
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

pdf.output("report.pdf")
