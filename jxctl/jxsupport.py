"""
jxsupport support module jxctl
"""
import pprint
from tabulate import tabulate


class JxSupport():
    """
    JxSupport class for support opertions like display
    """

    @staticmethod
    def print_table(source, count=False):
        """
        Display the dictionary in table format
        :param `source`: source dictionary `dict`
        :param `count`: count flag `bool`
        """
        table_value = []
        table_header = []
        for source_key, source_value in source.items():
            for item in source_value:
                table_value.append([v for v in item.values()])
                table_header.append([k for k in item.keys()])
            if not count:
                print(tabulate(table_value,
                               headers=table_header[0],
                               tablefmt='orgtbl'))
            else:
                print(tabulate([[len(source_value)]],
                               headers=[source_key],
                               tablefmt='orgtbl'))

    @staticmethod
    def print_json(source, count=False):
        """
        Display the dictionary in json format
        :param `source`: source dictionary `dict`
        :param `count`: count flag `bool`
        """
        if not count:
            pprint.pprint(source)
        else:
            source_count = {}
            for key, value in source.items():
                source_count.update({key: len(value)})
                pprint.pprint(source_count)

    def print(self, source, format_display="json", count=False):
        """
        Print method to display result
        :param `source`: source dictionary `dict`
        :param `format_display`: displat format by `json` is default format `str`
        :param `count`: count flag `bool`
        """
        if format_display == "table":
            self.print_table(source, count)
        else:
            self.print_json(source, count)
