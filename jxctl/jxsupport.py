"""
jxsupport
"""
import pprint
from tabulate import tabulate


class JxSupport():
    """
    JxSupport
    """

    @staticmethod
    def print_table(source, count=False):
        """
        Display the result in list to Table format.
        Having the special param count_flag,
        If true will display the count of the list in table.
        :param name: OutputList display_list ``list``
        :param name: HeaderList display_header ``list``
        :param name: Count count_flag ``bool``

        Example::
            >>> self.display_table(list_item, list_header)
            >>> self.display_table(list_item, list_header, count_flag=True)
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
        Display JSON in human readable format
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
        Print method
        """
        if format_display == "table":
            self.print_table(source, count)
        else:
            self.print_json(source, count)
