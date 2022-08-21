from konlpy.tag import Komoran
komoran = Komoran()

text = "나는 한국을 사랑한다. 오늘 전공 과제 최악이다."
lst = komoran.pos(text)
print(lst)