# ExpressionTree.py
from binary_tree_Wed import BTNode

# 모스코드 결정트리
# 1. 모스 코드 테이블 (A~Z) 
MORSE_TABLE = [
    ('A', '.-'),   ('B', '-...'), ('C', '-.-.'), ('D', '-..'),  ('E', '.'),
    ('F', '..-.'), ('G', '--.'),  ('H', '....'), ('I', '..'),   ('J', '.---'),
    ('K', '-.-'),  ('L', '.-..'), ('M', '--'),   ('N', '-.'),   ('O', '---'),
    ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),  ('S', '...'),  ('T', '-'),
    ('U', '..-'),  ('V', '...-'), ('W', '.--'),  ('X', '-..-'), ('Y', '-.--'),
    ('Z', '--..'),
]

# 2. encoding : 문자+{공백} -> 모스 부호
def encode(ch):
   ch = ch.upper()
   if ch == ' ':
      return '/' # 단어 구분
   elif 'A'<= ch <= 'Z':
      idx = ord(ch)- ord('A')
      return MORSE_TABLE[idx][1] # 해당 문자 ch의 모스 부호 반환
   else :
      return '?' 
   
# 3. decoding : 부호 -> 문자 변환 : 결정트리 기반
def decode(root, code):
   if code == '/':
      return ' '
   node = root
   for c in code :
      if c == '.':
         node = node.left
      if c == '-':
         node = node.right
      if node is None:
         return "?"
      
   if node and node.data :
      return node.data
   else:
      return '?'
   
# 4. 결정트리 생성
def make_morse_tree():
   root = BTNode(None, None, None) 
   for ch, code in MORSE_TABLE:
      cur = root
      for c in code:
         if c == '.':
            if cur.left is None:
               cur.left = BTNode(None, None, None) 
            cur = cur.left
         else:
            if cur.right is None:
               cur.right = BTNode(None, None, None) 
            cur = cur.right
      cur.data = ch
   return root
   


#===================================================
# 테스트 프로그램 : 결정 트리(이진 트리) 기반 모스 코드 트리
#===================================================   
if __name__ == "__main__":
    morseCodeTree = make_morse_tree()
    s = input("입력 문장 : ").strip() # GAMEOVER, DATA

    print("Encoding: ", s)
    mlist = [ ]
    for ch in s:
      code = encode(ch) 
      mlist.append(code)
    print("Morse Code:", mlist)

    print("Decoding: ", end='')
    for code in mlist:
        print(decode(morseCodeTree, code), end='')
    print()
   

