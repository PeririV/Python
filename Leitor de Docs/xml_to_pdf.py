import xml.etree.ElementTree as ET
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import datetime
import os


def register_russian_fonts():
    """
    Registra fontes que suportam caracteres cirílicos
    """
    try:
        # Tenta usar fontes comuns que suportam russo
        font_paths = [
            # Windows
            "C:/Windows/Fonts/arial.ttf",
            "C:/Windows/Fonts/times.ttf",
            # Linux
            "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            # macOS
            "/Library/Fonts/Arial.ttf",
            "/System/Library/Fonts/Arial.ttf"
        ]

        for font_path in font_paths:
            if os.path.exists(font_path):
                pdfmetrics.registerFont(TTFont('ArialUnicode', font_path))
                print(f"Fonte registrada: {font_path}")
                return True

        # Se não encontrar fontes do sistema, usa as padrão do ReportLab
        pdfmetrics.registerFont(TTFont('ArialUnicode', 'arial.ttf'))
        return True

    except:
        print("Usando fontes padrão do ReportLab")
        return False


def parse_xml_to_pdf(xml_file_path, pdf_file_path):
    """
    Converte arquivo XML do Gosuslugi para PDF formatado com suporte a russo
    """
    try:
        # Registrar fontes russas
        register_russian_fonts()

        # Parse do XML com encoding correto
        with open(xml_file_path, 'r', encoding='utf-8') as file:
            xml_content = file.read()

        root = ET.fromstring(xml_content)

        # Namespaces para buscar os elementos
        namespaces = {
            'ns2': 'http://umms.fms.gov.ru/integration/epgu/migration/staying/arrivalsheet/notice/2.0.8',
            'ns3': 'urn://mvd/gismu/mig/MigrUchet_EPGU/alt/core/2.0.8',
            'ns4': 'urn://mvd/gismu/mig/MigrUchet_EPGU/alt/migration/2.0.8'
        }

        # Extrair dados
        data = extract_data(root, namespaces)

        # Criar PDF
        create_pdf(data, pdf_file_path)

        print(f"PDF criado com sucesso: {pdf_file_path}")

    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")
        import traceback
        traceback.print_exc()


def extract_data(root, namespaces):
    """Extrai todos os dados do XML"""

    data = {}

    try:
        # Informações básicas
        notification_number = root.find('.//ns2:notificationNumber', namespaces)
        data['notification_number'] = notification_number.text if notification_number is not None else "Не указано"

        notification_received = root.find('.//ns2:notificationReceived', namespaces)
        data[
            'notification_received'] = notification_received.text if notification_received is not None else "Не указано"

        # Período de estada
        stay_period = root.find('.//ns2:stayPeriod', namespaces)
        if stay_period is not None:
            date_from = stay_period.find('.//ns3:dateFrom', namespaces)
            date_to = stay_period.find('.//ns3:dateTo', namespaces)
            data['date_from'] = date_from.text if date_from is not None else "Не указано"
            data['date_to'] = date_to.text if date_to is not None else "Не указано"
        else:
            data['date_from'] = "Не указано"
            data['date_to'] = "Не указано"

        # Dados da pessoa
        person_data = root.find('.//ns2:personDataDocument', namespaces)
        if person_data is not None:
            person = person_data.find('.//ns3:person', namespaces)
            if person is not None:
                data['last_name'] = person.find('.//ns3:lastName', namespaces).text or "Не указано"
                data['last_name_lat'] = person.find('.//ns3:lastNameLat', namespaces).text or "Не указано"
                data['first_name'] = person.find('.//ns3:firstName', namespaces).text or "Не указано"
                data['first_name_lat'] = person.find('.//ns3:firstNameLat', namespaces).text or "Не указано"
                data['birth_date'] = person.find('.//ns3:birthDate', namespaces).text or "Не указано"
                data['citizenship'] = person.find('.//ns3:citizenship', namespaces).text or "Не указано"

                # Local de nascimento
                birth_place = person.find('.//ns3:birthPlace', namespaces)
                if birth_place is not None:
                    birth_country = birth_place.find('.//ns3:country', namespaces)
                    birth_place_city = birth_place.find('.//ns3:place', namespaces)
                    data['birth_country'] = birth_country.text if birth_country is not None else "Не указано"
                    data['birth_place'] = birth_place_city.text if birth_place_city is not None else "Не указано"
                else:
                    data['birth_country'] = "Не указано"
                    data['birth_place'] = "Не указано"

            # Documento
            document = person_data.find('.//ns3:document', namespaces)
            if document is not None:
                data['doc_type'] = document.find('.//ns3:type', namespaces).text or "Не указано"
                data['doc_series'] = document.find('.//ns3:series', namespaces).text or "Не указано"
                data['doc_number'] = document.find('.//ns3:number', namespaces).text or "Не указано"
                data['doc_authority'] = document.find('.//ns3:authority', namespaces).text or "Не указано"
                data['doc_issued'] = document.find('.//ns3:issued', namespaces).text or "Не указано"
                data['doc_valid_to'] = document.find('.//ns3:validTo', namespaces).text or "Не указано"

        # Endereço
        stay_place = root.find('.//ns2:stayPlace', namespaces)
        if stay_place is not None:
            address = stay_place.find('.//ns3:address', namespaces)
            if address is not None:
                postal_code = address.find('.//ns3:postalCode', namespaces)
                address_str = address.find('.//ns3:addressStr', namespaces)
                full_address = address.find('.//ns3:fullAddress', namespaces)

                data['postal_code'] = postal_code.text if postal_code is not None else "Не указано"
                data['address_str'] = address_str.text if address_str is not None else "Не указано"
                data['full_address'] = full_address.text if full_address is not None else "Не указано"

        # Dados do anfitrião
        host = root.find('.//ns2:host', namespaces)
        if host is not None:
            host_person = host.find('.//ns3:person', namespaces)
            if host_person is not None:
                data['host_last_name'] = host_person.find('.//ns3:lastName', namespaces).text or "Не указано"
                data['host_first_name'] = host_person.find('.//ns3:firstName', namespaces).text or "Не указано"
                data['host_middle_name'] = host_person.find('.//ns3:middleName', namespaces).text or "Не указано"
                data['host_birth_date'] = host_person.find('.//ns3:birthDate', namespaces).text or "Не указано"
                data['host_citizenship'] = host_person.find('.//ns3:citizenship', namespaces).text or "Не указано"

            host_document = host.find('.//ns3:document', namespaces)
            if host_document is not None:
                data['host_doc_type'] = host_document.find('.//ns3:type', namespaces).text or "Не указано"
                data['host_doc_series'] = host_document.find('.//ns3:series', namespaces).text or "Не указано"
                data['host_doc_number'] = host_document.find('.//ns3:number', namespaces).text or "Не указано"
                data['host_doc_authority'] = host_document.find('.//ns3:authority', namespaces).text or "Не указано"
                data['host_doc_issued'] = host_document.find('.//ns3:issued', namespaces).text or "Не указано"

        responsible = root.find('.//ns2:responsible', namespaces)
        data['responsible'] = responsible.text if responsible is not None else "Не указано"

    except Exception as e:
        print(f"Erro ao extrair dados: {e}")
        import traceback
        traceback.print_exc()

    return data


def create_pdf(data, pdf_path):
    """Cria o PDF com suporte a caracteres russos"""

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        rightMargin=20 * mm,
        leftMargin=20 * mm,
        topMargin=20 * mm,
        bottomMargin=20 * mm
    )

    styles = getSampleStyleSheet()

    # Estilos com fontes que suportam russo
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontName='ArialUnicode',
        fontSize=16,
        spaceAfter=30,
        alignment=1,
        textColor=colors.darkblue
    )

    section_style = ParagraphStyle(
        'SectionStyle',
        parent=styles['Heading2'],
        fontName='ArialUnicode',
        fontSize=12,
        spaceAfter=12,
        spaceBefore=12,
        textColor=colors.darkblue
    )

    normal_style = ParagraphStyle(
        'NormalStyle',
        parent=styles['Normal'],
        fontName='ArialUnicode',
        fontSize=10,
        spaceAfter=6
    )

    story = []

    # Título principal
    title = Paragraph("УВЕДОМЛЕНИЕ О ПРИБЫТИИ", title_style)
    story.append(title)
    story.append(Spacer(1, 10))

    # Informações básicas
    story.append(Paragraph("ОСНОВНЫЕ ДАННЫЕ", section_style))
    basic_data = [
        ["Номер уведомления:", data.get('notification_number', 'Не указано')],
        ["Дата получения:", data.get('notification_received', 'Не указано')],
        ["Период пребывания:", f"{data.get('date_from', 'Не указано')} - {data.get('date_to', 'Не указано')}"],
        ["Ответственный:", data.get('responsible', 'Не указано')]
    ]

    basic_table = Table(basic_data, colWidths=[80 * mm, 100 * mm])
    basic_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'ArialUnicode', 9),
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
    ]))
    story.append(basic_table)
    story.append(Spacer(1, 15))

    # Dados do estrangeiro
    story.append(Paragraph("ДАННЫЕ ИНОСТРАННОГО ГРАЖДАНИНА", section_style))
    foreigner_data = [
        ["Фамилия (рус):", data.get('last_name', 'Не указано')],
        ["Фамилия (лат):", data.get('last_name_lat', 'Не указано')],
        ["Имя (рус):", data.get('first_name', 'Не указано')],
        ["Имя (лат):", data.get('first_name_lat', 'Не указано')],
        ["Дата рождения:", data.get('birth_date', 'Не указано')],
        ["Гражданство:", data.get('citizenship', 'Не указано')],
        ["Место рождения:", f"{data.get('birth_place', 'Не указано')}, {data.get('birth_country', 'Не указано')}"]
    ]

    foreigner_table = Table(foreigner_data, colWidths=[60 * mm, 120 * mm])
    foreigner_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'ArialUnicode', 9),
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
    ]))
    story.append(foreigner_table)
    story.append(Spacer(1, 15))

    # Documento do estrangeiro
    story.append(Paragraph("ДОКУМЕНТ, УДОСТОВЕРЯЮЩИЙ ЛИЧНОСТЬ", section_style))
    doc_data = [
        ["Тип документа:", data.get('doc_type', 'Не указано')],
        ["Серия:", data.get('doc_series', 'Не указано')],
        ["Номер:", data.get('doc_number', 'Не указано')],
        ["Орган выдачи:", data.get('doc_authority', 'Не указано')],
        ["Дата выдачи:", data.get('doc_issued', 'Не указано')],
        ["Действителен до:", data.get('doc_valid_to', 'Не указано')]
    ]

    doc_table = Table(doc_data, colWidths=[50 * mm, 130 * mm])
    doc_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'ArialUnicode', 9),
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
    ]))
    story.append(doc_table)
    story.append(Spacer(1, 15))

    # Endereço
    story.append(Paragraph("АДРЕС ПРЕБЫВАНИЯ", section_style))
    address_data = [
        ["Почтовый индекс:", data.get('postal_code', 'Не указано')],
        ["Адрес:", data.get('address_str', 'Не указано')],
        ["Полный адрес:", data.get('full_address', 'Не указано')]
    ]

    address_table = Table(address_data, colWidths=[50 * mm, 130 * mm])
    address_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'ArialUnicode', 9),
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
    ]))
    story.append(address_table)
    story.append(Spacer(1, 15))

    # Dados do anfitrião
    story.append(Paragraph("ДАННЫЕ ПРИНИМАЮЩЕЙ СТОРОНЫ", section_style))
    host_data = [
        ["ФИО:",
         f"{data.get('host_last_name', '')} {data.get('host_first_name', '')} {data.get('host_middle_name', '')}"],
        ["Дата рождения:", data.get('host_birth_date', 'Не указано')],
        ["Гражданство:", data.get('host_citizenship', 'Не указано')],
        ["Тип документа:", data.get('host_doc_type', 'Не указано')],
        ["Серия и номер:", f"{data.get('host_doc_series', '')} {data.get('host_doc_number', '')}"],
        ["Орган выдачи:", data.get('host_doc_authority', 'Не указано')],
        ["Дата выдачи:", data.get('host_doc_issued', 'Не указано')]
    ]

    host_table = Table(host_data, colWidths=[50 * mm, 130 * mm])
    host_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'ArialUnicode', 9),
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
    ]))
    story.append(host_table)

    # Data de geração
    story.append(Spacer(1, 20))
    generation_date = Paragraph(
        f"Документ сгенерирован: {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')}",
        ParagraphStyle('DateStyle', parent=styles['Normal'], fontName='ArialUnicode', fontSize=8, textColor=colors.grey)
    )
    story.append(generation_date)

    # Construir PDF
    doc.build(story)


# USO DO CÓDIGO
if __name__ == "__main__":
    xml_file = "SheetNoticeSignedPo.xml"
    pdf_file = "Registro_Migratorio_Russo.pdf"

    parse_xml_to_pdf(xml_file, pdf_file)