from fpdf import FPDF
import webbrowser

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)

# Save top coordinate
top = pdf.y

# Calculate x position of next cell
offset = pdf.x + 40

pdf.multi_cell(40, 10, 'Hello World!,how are you today', 1)

# Reset y coordinate
pdf.y = top

# Move to computed offset
pdf.x = offset

pdf.multi_cell(40, 20,'This cell needs to beside the other', 1)

pdf.output('tuto1.pdf', 'F')

webbrowser.open_new('tuto1.pdf')
