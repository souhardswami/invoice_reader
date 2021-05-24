#!d:\python\code\invoice\invoice_reader\myenv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'invoice2data==0.3.5','console_scripts','invoice2data'
__requires__ = 'invoice2data==0.3.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('invoice2data==0.3.5', 'console_scripts', 'invoice2data')()
    )
