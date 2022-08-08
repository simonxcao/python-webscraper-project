import csv
from bs4 import BeautifulSoup
import json
import requests
import urllib.request
import urllib.error
import urllib.parse

lat = 37.25
long = -121.91
url = f"https://www.mcdonalds.com/googleappsv2/geolocation?latitude={lat}&longitude={long}&radius=8.045&maxResults=30&country=us&language=en-us"


payload = {}
headers = {
    'Cookie': '_abck=BDEF69BF50C2700A4B43FF03D986C9CF~-1~YAAQVfs7FysWImSCAQAAMpEtdgj/Ir211xEGHyNJtpMvGGF3S480FwSRxcxmspEelW05egJR7UfBJig27U2IaDi1UhcTfKnwtjRJ1S+A/V0zuXhIR3t/IeBnwHODbNdYjD2LOJNHaW2uWLmj8Tji/+AdBzxBxvf8VTpY56+IbDJ1S5VdJw+iQ+YDlVkeF+LxBK+c07SNV1U1HqCKW/cxsjfpzu/1DcbdZd7O8uh3X0LDPeW1K5ad4eWas8A2lie7jp70rFOxCqRL8Z8q6Mapy8tQUHMXpwKOCA9jzEzIyrWfNYJ0z+8qHZrxsHXNHSLCVKSflRChDL+AQkJzwZ3oUXj54FtjKiIrXiGVQPwNxrjIPLXCs0W5jf6aU70=~-1~-1~-1; ak_bmsc=DBED88E2ADF470221232035D9CBEA813~000000000000000000000000000000~YAAQVfs7FywWImSCAQAAMpEtdhCmtpnziSWjW0HQqTU2G3m7Te4tqZIE9GLzot6eILbboZLG8pZPdNng9LWAuR3FXEV4e488AQN/RyJQ1ddpls92uuXiay9D5O5N5VSUbZ1H3wMrNdsMjy2/tIhVstyYMPpG/KoNSIjDYfibFkaLl0MQAGYpeaKtPY7Mc9tFpxgv3ZEZBRBVhPqCGsdRyxq5jXe9UW8U7TBTSELuO47zXbAo7c36C55gxGXL4NrGR2XVNjYhZjkr3FgzSUMoWpDM518ff4DWeE9asQE3rUiXFOB0HptpbV3BHeh0JFBvk52/EIeqp4w+6ps8sJL078pEqJUVNZnflgjMyjwiBAa6MocpF/jYSdeV2R6pPQcx; bm_sv=BCED1FB59F7BDCF545BCE4C777D5E891~YAAQROstFyI7vjmCAQAAJ5ItdhC9rnLO84rCObaSAoyyexTlRNHzrDRnEw2CW+qzxkLIiGdXpJwFRIcEFMGuYwhQUi3LZtETDo3Wv2ga+u3xpuFvtPdavRd1sXmf4RW7aGZcdYRzYQ559NfspYcOE89GOoC5mJJf2I8HJed7+ZTchg3b36QxCRd52WIPpr07Sj7vYtyiO5uIc0ShqYxlbrASM/I/XDNmnpHuf7m+6EpcJEs+VF5safBejfi0+1DJC4ET~1; bm_sz=D2845D1978D4FD4AFA8A2E5ACE876EC3~YAAQVfs7Fy0WImSCAQAAMpEtdhBaUDUSGY2rMcIHvB9kMLk2nXfZcO+gKX3K8HfWOwFVavldA84+huWEds8Elj3UfKTaEkCDs7VjLHxfHc+1050slFZAtVdxovEbtSxjnA9IpmyHDXH1Ll1PmGAeLXTB7m62LO207xBormE1VzuWMMqQsrcoE1IUrB76c6NcRa0z9JOtWwiFhPBC5hHl5ozJa7QcUC0tch+lKLZWornalQTKUfMYrQBrpkG4gRef49CLwrIXadXrB4IBqR7Z3rK89a/8N5f51N13T7Q8dXCsOnD1bqQ=~3683893~3485751; MCDCountry_code=US; affinity="fee556b908c3eea5"'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
print(url)

# lat = 37.25
# long = -121.91
# url = f"https://www.mcdonalds.com/googleappsv2/geolocation?latitude={lat}&longitude={long}&radius=8.045&maxResults=30&country=us&language=en-us"

# user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
# headers = {'User-Agent': user_agent}
# req = urllib.request.Request(url, None, headers)
# response = urllib.request.urlopen(req)
# html = response.read()
# print(html)
# response.close()
