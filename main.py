from hawk_scanner.internals import system
import os
output = os.system("mkdir hello")
print(output)

pii = system.scan_file("/Users/kumarohit/Downloads/credential_file.json", {
   "fingerprint": {
     "Email": '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}',
  }}
)
print(pii)

pii2 = system.read_match_strings({}, "/Users/kumarohit/Downloads/credential_file.json", "jira")
print(pii2)

test = system.print_alert("Hello")
print(test)



test3 = system.test_fn("Hello")
print(test3)
