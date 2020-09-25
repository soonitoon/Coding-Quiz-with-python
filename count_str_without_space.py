string = """나보기가 역겨워 가실 때에는
죽어도 아니 눈물 흘리오리다
영변에 약산 진달래꽃
아름따다 가실 길에 뿌리오리다"""

def countString(string):
    result = string.replace(" ", "").replace("\n", "")
    print(len(result))

countString(string)
