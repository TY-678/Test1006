import xml.etree.ElementTree as ET
import sys

tree = ET.parse("results/output.xml")
root = tree.getroot()


total_stat = root.find(".//total/stat")
total_tests = int(total_stat.attrib["pass"]) + int(
    total_stat.attrib["fail"]
)  # 总测试数为通过和失败的总和
failed_tests = int(total_stat.attrib["fail"])


if failed_tests > 0:
    print(f"Total Tests: {total_tests}, Failed Tests: {failed_tests}")
    sys.exit(1)
else:
    print("All tests passed!")
