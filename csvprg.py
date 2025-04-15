from fpdf import FPDF
import csv

# Read CSV and compute average of "Score"
with open("data.csv") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    scores = [int(row["Score"]) for row in rows]
    avg_score = sum(scores) / len(scores)

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, "Simple Report", ln=True, align='C')
pdf.ln(10)
pdf.cell(200, 10, f"Average Score: {avg_score:.2f}", ln=True)

pdf.output("easy_report.pdf")
print("PDF generated: easy_report.pdf")
