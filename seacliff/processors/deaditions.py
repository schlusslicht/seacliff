from typing import Any, List

from xlsxwriter import Workbook

from seacliff.processors._processor import _processor
from seacliff.utilities import concretemethod


class deaditions(_processor):

  @concretemethod
  def process(self, items: List[Any]) -> None:
    workbook = Workbook('deaditions.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.set_column(0, 9, 15)

    bold = workbook.add_format({ 'bold': 1 })
    date = workbook.add_format({ 'num_format': 'dd.mm.yyyy HH:ss' })
    ranking = workbook.add_format({ 'num_format': '#.##' })

    worksheet.write('A1', 'Name', bold)
    worksheet.write('B1', 'Link', bold)
    worksheet.write('C1', 'Available', bold)
    worksheet.write('D1', 'Description', bold)
    worksheet.write('E1', 'Editors', bold)
    worksheet.write('F1', 'Ranking', bold)
    worksheet.write('G1', 'Published (manual)', bold)
    worksheet.write('H1', 'Lastseen (manual)', bold)
    worksheet.write('I1', 'Published (wayback)', bold)
    worksheet.write('J1', 'Lastseen (wayback)', bold)

    row = 0
    for item in items:
      row += 1

      worksheet.write_string(row, 0, item.name)
      worksheet.write_url(row, 1, item.href, string = 'Link')
      worksheet.write_string(row, 2, str(item.meta.available))
      worksheet.write_string(row, 3, item.meta.description)
      worksheet.write_string(row, 4, item.meta.editors or '')
      worksheet.write_number(row, 5, item.meta.ranking, ranking)

      if item.meta.published.man:
        worksheet.write_number(row, 6, item.meta.published.man)

      if item.meta.lastseen.man:
        worksheet.write_number(row, 7, item.meta.lastseen.man)

      if item.meta.published.ia:
        worksheet.write_datetime(row, 8, item.meta.published.ia, date)

      if item.meta.lastseen.ia:
        worksheet.write_datetime(row, 9, item.meta.lastseen.ia, date)

    worksheet.write(row + 1, 0, 'Deaditions', bold)
    worksheet.write(row + 1, 9, '=ROW()-1', bold)

    workbook.close()
