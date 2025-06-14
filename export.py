import csv
from db import get_all_tasks
from fpdf import FPDF

def export_to_csv(filename="tasks_export.csv"):
    tasks = get_all_tasks()
    with open(filename, mode="w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Title", "Category", "Date", "Time", "Notes"])
        writer.writerows(tasks)

def export_to_pdf(filename="tasks_export.pdf"):
    tasks = get_all_tasks()
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)

    pdf.cell(200, 10, txt="Task List", ln=True, align='C')
    pdf.ln(10)

    for task in tasks:
        text = f"{task[1]} | {task[2]} | {task[3]} {task[4]} | {task[5]}"
        pdf.cell(0, 10, txt=text, ln=True)

    pdf.output(filename)
