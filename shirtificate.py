from fpdf import FPDF


def main():
    name = get_name()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", size=30)
    pdf.image("shirtificate.png", x=10, y=60, w=190, keep_aspect_ratio=True)
    pdf.cell(text="CS50 Shirtificate", border=0, align="C", center=True)
    pdf.ln(100)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(text=f"{name} took CS50", w=105, h=20, border=0, align="C", center=True, new_x="CENTER", new_y="NEXT")
    pdf.output("shirtificate.pdf")


def get_name():
    return input("Name: ")


if __name__ == "__main__":
    main()
