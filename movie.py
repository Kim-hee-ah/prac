import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'movie.naver.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'iframe',
    'referer': 'https://movie.naver.com/movie/bi/mi/point.nhn?code=189069',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NNB=5AFCSLXTGECV6; nx_ssl=2; ASID=731711c9000001732eb515f900000053; MM_NEW=1; NFS=2; MM_NOW_COACH=1; _ga=GA1.2.39785719.1595920887; _fbp=fb.1.1595945619295.1551079798; NDARK=N; NRTK=ag#20s_gr#0_ma#-2_si#2_en#-2_sp#-2; page_uid=UyXNydprvmZssvZ/gOKssssstsG-018278; BMR=s=1596693748623&r=https%3A%2F%2Fm.post.naver.com%2Fviewer%2FpostView.nhn%3FvolumeNo%3D28995336%26memberNo%3D21959512%26vType%3DVERTICAL&r2=https%3A%2F%2Fsearch.naver.com%2Fsearch.naver%3Fwhere%3Dnexearch%26sm%3Dtab_lve.ag20sgr0mamsipenmspm%26ie%3Dutf8%26query%3D%25EB%25A7%2588%25EC%2597%2590%25EB%258B%25A4%2B%25EC%258A%258C; csrf_token=10d4b399-fb73-4e7e-a387-756a99442a98',
}

params = (
    ('code', '189069'),
    ('type', 'after'),
    ('isActualPointWriteExecute', 'false'),
    ('isMileageSubscriptionAlready', 'false'),
    ('isMileageSubscriptionReject', 'false'),
)

response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)
soup = BeautifulSoup(response.text, 'html.parser')

movies_list = soup.select('div.score_result')

final_movie_data =[]

for movie in movies_list:
    score = movie.select('div.star_score>em')
    reple = movie.select('div.score_reple>p>span')[1::2]

for sc, rp in zip(score, reple):
    movie_data = {
        'score' : sc.string,
        'reple' : rp.string.replace('\n','').replace('\t','').replace('\r','')
    }
    
    final_movie_data.append(movie_data)

print(final_movie_data)