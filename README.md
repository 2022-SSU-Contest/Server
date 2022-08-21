# 서버

nlp / textmining

### API

+ Method : GET
+ URI : `/video?sentence={sentence}`
+ Query String 
    - Name : sentence
    - Type : String
    - Description : 수어로 번역할 문장
+ 설명 : 입력 문장을 자연어 처리 과정을 거친 뒤 해당하는 수어 영상 목록을 리턴
+ Response Parameter
    - Name : result
    - Type : Array
    