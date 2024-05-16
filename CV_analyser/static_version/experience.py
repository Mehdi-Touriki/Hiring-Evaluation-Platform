from datetime import datetime
import re
def find_experience_paragraph(resume_text: str):
    exp_pattern = r"(?s)(?:experience|work history)(?!d|s)(.*?)(?:Skills|Education|Achievements)"
    matches = re.findall(exp_pattern, resume_text, re.I)
    if len(matches) == 0:
        exp_pattern = r"(?s)(?:experience|work history)(?!d).*"
        matches = re.findall(exp_pattern, resume_text, re.I)
    if len(matches) == 0:
        return [""]
    result = ""
    for match in matches:
        result += match
    result = result.replace("\n", " ")
    matches[0] = result
    return matches
def calc_total_months(date: dict) -> int:
    """
    Une fonction qui calcule la durée en mois entre les dates entrées comme dictionnaire :param date: elle peut avoir
    3 formes. Exemples:{"fmonth":"May","fyear":"2001","lmonth":"sept","lyear":"2004"},{"fmonth":"sept",
    "lmonth":"oct"};{"fyear":"2004","lyear":"2005"}

    :return: la durée en mois entre ces deux dates
    """
    current_year = datetime.now().year
    current_month = datetime.now().month
    months_numbers = {
        'jan': '01',
        'feb': '02',
        'mar': '03',
        'apr': '04',
        'may': '05',
        'jun': '06',
        'jul': '07',
        'aug': '08',
        'sep': '09',
        'oct': '10',
        'nov': '11',
        'dec': '12'
    }
    total = 0
    try:
        if len(date) == 4:

            if date['fmonth'].isnumeric():
                if date['lmonth'] in ["present", "current", "now", "date"]:
                    total += 12 - int(date['fmonth']) + 12 * (
                            current_year - int(date['fyear']) - 1) + current_month
                else:
                    total += 12 - int(date['fmonth']) + 12 * (
                            int(date['lyear']) - int(date['fyear']) - 1) + int(
                        date['lmonth'])
            else:
                if date['lmonth'] in ["present", "current", "now", "date"]:
                    total += 12 - int(months_numbers[date['fmonth'][:3]]) + 12 * (
                            current_year - int(date['fyear']) - 1) + current_month
                else:
                    total += 12 - int(months_numbers[date['fmonth'][:3]]) + 12 * (
                            int(date['lyear']) - int(date['fyear']) - 1) + int(
                        months_numbers[date['lmonth'][:3]])
        elif len(date) == 2:
            if 'fyear' in date and 'lyear' in date:
                if date['lyear'] in ["present", "current", "now", "date"]:
                    date['lyear'] = str(current_year)
                total += 12 * (int(date['lyear']) - int(date['fyear']))
            elif 'fmonth' in date and 'lmonth' in date:
                if date['lmonth'] == "present":
                    total += 12 - int(months_numbers[date['fmonth'][:3]])
                else:
                    total += int(months_numbers[date['lmonth'][:3]]) - int(months_numbers[date['fmonth'][:3]])
    except KeyError:
        return 0
    return total

def find_total_months(exp_list: list[str]) -> int:
    """
    Une fonction qui trouve la duree totale dans une liste d'experiences
    :param exp_list:
    :return:
    """
    dates = []
    lines = exp_list[0].split(".")
    for line in lines:
        line = line.lower()
        # dates in the form 2015 - 2020
        experience = re.search(
            r"(?P<fyear>\d{4})\s*(\s|-|to)\s*(?P<lyear>\d{4}|present|date|now|current)",
            line,
        )
        if experience:
            d = experience.groupdict()
            # exemple d = {"fyear":"2004","lyear":"2005"}
            dates.append(d)
            continue
        # dates in the form (sept - oct [2012])
        experience = re.search(
            r"(?s)\((?P<fmonth>\w+)\s*(-|to)\s*(?P<lmonth>\w+|present|date|now|current).*\)",
            line,
        )
        if experience:
            d = experience.groupdict()
            # exemple d = {"fmonth":"sept","lmonth":"oct"}
            dates.append(d)
            continue
        # dates in the form May 2001 to sept 2004
        experience = re.search(
            r"(?P<fmonth>\w+)\s*/*(?P<fyear>\d+)\s*(-|to)\s*((?P<lmonth>\w+)\s*/*("
            r"?P<lyear>\d+)|present|date|now|current)",
            line,
        )
        if experience:
            d = experience.groupdict()
            # exemple d = {"fmonth":"May","fyear":"2001","lmonth":"sept","lyear":"2004"}
            dates.append(d)
            continue
            # dates in the form 07/2019 to current
        experience = re.search(
            r"(?P<fmonth>\w+)\s*/(?P<fyear>\d+)\s*(-|to)\s*((?P<lmonth>\w+)\s*/("
            r"?P<lyear>\d+)|present|date|now|current)",
            line,
        )
        if experience:
            d = experience.groupdict()
            # exemple d = {"fmonth":"May","fyear":"2001","lmonth":"sept","lyear":"2004"}
            dates.append(d)
            continue
    results = []
    for date in dates:
        total = calc_total_months(date)
        if total > 1200 or total < 0:
            continue
        results.append(calc_total_months(date))

    return sum(results)
