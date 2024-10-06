import xml.etree.ElementTree as ET
import sys

tree = ET.parse('results/output.xml')
root = tree.getroot()

total_tests = int(root.attrib['tests'])
failed_tests = int(root.attrib['failures'])

if failed_tests > 0:
    print(f'Total Tests: {total_tests}, Failed Tests: {failed_tests}')
    sys.exit(1)
else:
    print('All tests passed!')
