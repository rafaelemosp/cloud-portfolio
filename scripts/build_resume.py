from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas

OUTPUT = "output/pdf/Rafael-Lemos-Resume.pdf"

NAVY = HexColor("#0D1117")
SURFACE = HexColor("#161B22")
BLUE = HexColor("#58A6FF")
GREEN = HexColor("#7EE787")
TEXT = HexColor("#E6EDF3")
MUTED = HexColor("#8B949E")
LINE = HexColor("#30363D")
WHITE = HexColor("#FFFFFF")


def wrap(text, font, size, width):
    words = text.split()
    lines, current = [], ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if stringWidth(candidate, font, size) <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def paragraph(c, text, x, y, width, size=8.2, leading=11, color=TEXT, font="Helvetica"):
    c.setFillColor(color)
    c.setFont(font, size)
    for line in wrap(text, font, size, width):
        c.drawString(x, y, line)
        y -= leading
    return y


def heading(c, text, x, y, width):
    c.setFillColor(BLUE)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x, y, text.upper())
    c.setStrokeColor(LINE)
    c.setLineWidth(0.7)
    c.line(x, y - 5, x + width, y - 5)
    return y - 18


def role(c, title, organisation, dates, x, y, width, bullets):
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 9.2)
    c.drawString(x, y, title)
    c.setFillColor(GREEN)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawRightString(x + width, y, dates)
    y -= 12
    c.setFillColor(MUTED)
    c.setFont("Helvetica-Oblique", 7.7)
    c.drawString(x, y, organisation)
    y -= 12
    for bullet in bullets:
        c.setFillColor(BLUE)
        c.circle(x + 2, y + 3, 1.4, fill=1, stroke=0)
        y = paragraph(c, bullet, x + 10, y + 6, width - 10, size=8, leading=10.2)
        y -= 3
    return y - 5


c = canvas.Canvas(OUTPUT, pagesize=A4)
page_w, page_h = A4
c.setTitle("Rafael Lemos - Cloud Engineering and Customer Success Resume")
c.setAuthor("Rafael Lemos")
c.setSubject("Cloud Engineering, Customer Success, Infrastructure and IT Support Resume")

c.setFillColor(NAVY)
c.rect(0, 0, page_w, page_h, fill=1, stroke=0)
c.setFillColor(SURFACE)
c.rect(0, 0, 190, page_h, fill=1, stroke=0)
c.setFillColor(BLUE)
c.rect(0, page_h - 8, page_w, 8, fill=1, stroke=0)

# Header
c.setFillColor(WHITE)
c.setFont("Helvetica-Bold", 25)
c.drawString(220, page_h - 54, "Rafael Lemos")
c.setFillColor(GREEN)
c.setFont("Helvetica-Bold", 11)
c.drawString(220, page_h - 74, "CLOUD ENGINEERING · CUSTOMER SUCCESS")
c.setFillColor(MUTED)
c.setFont("Helvetica", 8.5)
c.drawString(220, page_h - 90, "AWS · Infrastructure · Technical Support · Customer Care")
c.setStrokeColor(LINE)
c.line(220, page_h - 102, page_w - 34, page_h - 102)

# Left column
lx, lw, ly = 28, 134, page_h - 45
ly = heading(c, "Contact", lx, ly, lw)
ly = paragraph(c, "Gold Coast, Queensland", lx, ly, lw, 8.2, 11)
ly = paragraph(c, "rafaelemosp@gmail.com", lx, ly - 3, lw, 7.8, 10, GREEN)
ly = paragraph(c, "linkedin.com/in/rafael-lemos-pereira-5443aa358", lx, ly - 3, lw, 7.1, 9, BLUE)
ly = paragraph(c, "rafaellemos.cloud", lx, ly - 3, lw, 7.5, 9, BLUE)

ly = heading(c, "Technical Skills", lx, ly - 16, lw)
for label, value in [
    ("Cloud", "AWS fundamentals, Amazon S3, IAM, GitHub Actions, OIDC"),
    ("Servers", "Windows Server 2022, Ubuntu, Active Directory, DNS, DHCP"),
    ("Virtualisation", "Hyper-V, failover clustering, TrueNAS"),
    ("Networking", "TCP/IP, OSPF, Cisco Packet Tracer, routing"),
    ("Platforms", "Nextcloud, hMailServer, SMTP, IMAP"),
    ("Security", "Risk assessment, security awareness, access control"),
]:
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 7.8)
    c.drawString(lx, ly, label)
    ly = paragraph(c, value, lx, ly - 11, lw, 7.3, 9, MUTED)
    ly -= 5

ly = heading(c, "Education", lx, ly - 4, lw)
c.setFillColor(WHITE)
c.setFont("Helvetica-Bold", 8.2)
c.drawString(lx, ly, "Diploma of Information Technology")
ly -= 11
ly = paragraph(c, "Advanced Networking / Cloud Engineering", lx, ly, lw, 7.5, 9, GREEN)
ly = paragraph(c, "TAFE Queensland · 2026-current", lx, ly - 3, lw, 7.3, 9, MUTED)
ly = paragraph(c, "Expected completion: Dec 2026", lx, ly - 2, lw, 7.3, 9, MUTED)
ly -= 8
c.setFillColor(WHITE)
c.setFont("Helvetica-Bold", 8.2)
c.drawString(lx, ly, "Pathology Collection")
ly = paragraph(c, "TAFE Queensland · 2022", lx, ly - 12, lw, 7.3, 9, MUTED)
ly -= 8
c.setFillColor(WHITE)
c.setFont("Helvetica-Bold", 8.2)
c.drawString(lx, ly, "Bachelor of Physiotherapy")
ly = paragraph(c, "UNIJORGE (Centro Universitário Jorge Amado) · Salvador, Brazil · 2014", lx, ly - 12, lw, 7.3, 9, MUTED)

ly = heading(c, "Professional", lx, ly - 14, lw)
ly = paragraph(c, "Customer success · Relationship building · Clear communication · Problem resolution · Leadership · Multidisciplinary teamwork", lx, ly, lw, 7.4, 9.3, TEXT)

ly = heading(c, "Languages", lx, ly - 12, lw)
ly = paragraph(c, "English · Portuguese", lx, ly, lw, 8, 10, TEXT)

# Main column
mx, mw, my = 220, page_w - 254, page_h - 126
my = heading(c, "Profile", mx, my, mw)
profile = ("Qualified physiotherapist and customer-focused professional transitioning into cloud engineering and technology. "
           "Combines healthcare, team leadership and technical-support experience with clear communication, relationship building and calm problem-solving. "
           "Develops practical AWS, infrastructure, Linux, Windows Server and networking capability through hands-on projects.")
my = paragraph(c, profile, mx, my, mw, 8.3, 11.2, TEXT)

my = heading(c, "Experience", mx, my - 12, mw)
my = role(c, "Specialist", "Apple · Upcoming position", "STARTING 27 JUL 2026", mx, my, mw, [
    "Joining Apple in a customer-focused Specialist role while continuing Cloud Engineering studies."
])
my = role(c, "Hospital Pathology Collector", "Sullivan Nicolaides Pathology", "2023-2025", mx, my, mw, [
    "Managed sensitive patient data and specimens with strict privacy, accuracy and regulatory compliance.",
    "Used hospital information systems to track collection and testing workflows accurately.",
    "Collaborated with multidisciplinary teams and communicated clearly in high-pressure environments."
])
my = role(c, "Hospital Pathology Collector", "QML Pathology", "2023", mx, my, mw, [
    "Delivered professional patient care while maintaining accurate records and timely information exchange.",
    "Applied attention to detail, organisation and confidentiality across daily clinical workflows."
])
my = role(c, "Team Leader / Detailer", "Cranks Carbon", "2019-2022", mx, my, mw, [
    "Led staffing, recruitment, onboarding and training while coordinating workload, safety and quality standards.",
    "Allocated team members according to job size and operational requirements.",
    "Monitored performance and improved processes in a fast-paced operational environment."
])

my = heading(c, "Selected Technical Projects", mx, my - 3, mw)
projects = [
    ("AWS Cloud Portfolio", "Deployed S3, CloudFront, Route 53, HTTPS, GitHub OIDC CI/CD and a Lambda-DynamoDB visitor counter."),
    ("Enterprise Server Lab", "Windows Server, Ubuntu, AD, DNS, DHCP, TrueNAS and two-node failover clustering."),
    ("Cisco OSPF Lab", "Configured and troubleshot multi-router dynamic routing and end-to-end connectivity."),
    ("Communication Platform", "Integrated Nextcloud, hMailServer, Thunderbird, SMTP and IMAP in a virtual lab."),
    ("Cybersecurity Program", "Assessed workplace risks and developed prioritised awareness and training controls."),
]
for title, detail in projects:
    c.setFillColor(GREEN)
    c.setFont("Helvetica-Bold", 7.8)
    c.drawString(mx, my, title)
    my = paragraph(c, detail, mx + 12, my - 12, mw - 12, 7.4, 9, MUTED)
    my -= 4

c.setFillColor(MUTED)
c.setFont("Helvetica", 6.8)
c.drawRightString(page_w - 34, 24, "https://rafaellemos.cloud")
c.save()
print(OUTPUT)
