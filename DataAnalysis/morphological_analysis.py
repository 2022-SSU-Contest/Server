from konlpy.tag import Komoran
komoran = Komoran()

text = "나는 한국을 사랑한다. 나는 오늘 너무 행복하다."
lst = komoran.pos(text)
print(lst)