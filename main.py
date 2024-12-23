import csv
import re


with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    for row in contacts_list[1:]:
        name_parts = " ".join(row[:3]).split()
        if len(name_parts) == 3:
            row[0] = name_parts[0]
            row[1] = name_parts[1]
            row[2] = name_parts[2]
        elif len(name_parts) == 2:
            row[0] = name_parts[0]
            row[1] = name_parts[1]
            row[2] = ''
        elif len(name_parts) == 1:
            row[0] = name_parts[0]
            row[1] = ''
            row[2] = ''

    phone_pattern = re.compile(
        r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})[-\s+]?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    phone_exchenge = r'+7(\2)\3-\4-\5\7\8\9'

    for contact in contacts_list:
        contact[5] = phone_pattern.sub(phone_exchenge, contact[5])

    contacts_list_updated = []
    new_contact_list = {}
    for contacts in contacts_list:
        last_name = contacts[0]
        if last_name not in new_contact_list:
            new_contact_list[last_name] = contacts
        else:
            for id, item in enumerate(new_contact_list[last_name]):
                if item == '':
                    new_contact_list[last_name][id] = contacts[id]

    for last_name, contact in new_contact_list.items():
        for contacts in contact:
            if contact not in contacts_list_updated:
                contacts_list_updated.append(contact)


with open("phonebook.csv", "w", encoding="utf-8") as out_file:
    datawriter = csv.writer(out_file, delimiter=',')
    datawriter.writerows(contacts_list_updated)