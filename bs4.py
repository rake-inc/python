import requests
import BeautifulSoup
def main():
	a=requests.get("http://www.cricbuzz.com/cricket-match/live-scores")
	s=BeautifulSoup.BeautifulSoup(a.content)
	span[]
	for i in s.findAll('div',{'class':'cb-lv-scrs-col cb-font-12 text-black'}):
		span.append(i.get_text('span',{'class':'text-bold'}))
	print(span[0])
if __name__=="__main__":
	main()