import requests, threading
from bs4 import BeautifulSoup


class Spider:

	def __init__(self, domain):
		self._domain = domain
		self._urls = []
		self._includes = ['html']

	def get_urls(self):
		self._fetch_urls_recursivly(self._domain)
		return self._urls


	def set_includes(self, includes):
		if not isinstance(lst, includes):
			raise Exception("Includes should be a list.")

		self._includes = includes

	def _fetch_urls_recursivly(self, url):
		resp = requests.get(url)
		html = BeautifulSoup(resp.text, 'html.parser')

		if resp.status_code != 200:
			return

		for include in self._includes:
			if not include in resp.headers.get('content-type'):
				return

		self._urls.append(url)

		links = html.find_all('a')
		for link in links:
			href = link.get('href')

			if not self._domain in href:
				continue

			if href in self._urls:
				continue

			t = threading.Thread(target=self._fetch_urls_recursivly, args=(href,))
			t.start()




if __name__ == "__main__":
	spider = Spider('http://test.se')
	urls = spider.get_urls()
	print(urls)