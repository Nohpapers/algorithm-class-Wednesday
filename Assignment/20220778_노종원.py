class Node:  # 단순 연결 리스트를 위한 노드 클래스
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next    
    def append(self, new):  # 현재 노드 다음에 new 노드를 삽입
        if new is not None:
            new.link = self.link
            self.link = new
    def popNext(self):  # 현재 노드의 다음 노드를 삭제한 후 반환
        deleted_node = self.link
        if deleted_node is not None: self.link = deleted_node.link
        return deleted_node
    
class Book: # 도서 정보 저장
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

# 단순 연결 리스트
class LinkedList:
    def __init__(self):
        self.head = None # 비어있는 리스트의 초기 상태

    # 주요 기본 연산
    def isEmpty(self):
        # 리스트의 빈 상태 검사
        return self.head == None
    
    def isFull(self):
        # 리스트의 포화 상태 검사
        return False # 동적 노드 할당
    
    def getNode(self, pos): # pos 기반 연산
        # pos 위치에 있는 노드를 반환 
        # pos는 리스트의 인덱스 0부터 고려
        if pos < 0 : return None # pos는 유효하지않은 위치
        if self.head == None: # 리스트가 빈 상태 
            return None
        else :
            ptr = self.head
            for _ in range(pos):
                if ptr == None : # pos가 리스트보다 크기가 큰 경우(유효하지 않는 위치)
                    return None
                ptr = ptr.link
            return ptr
        
    def getEntry(self, pos): # 인덱스 기반 연산
        # 리스트의 pos 위치에 있는 노드를 찾아 데이터값을 반환
        node = self.getNode(pos) # 1. 해당 위치의 노드를 탐색
        if node == None : # 해당 노드가 없는 경우
            return None
        else: # 있는 경우
            return node.data
        
    def insert(self, pos, elem) : # 인덱스 기반 연산 
        # pos 위치에서 새노드(elem) 삽입 연산
        if pos < 0: 
            raise ValueError("잘못된 위치 값!")
        
        new = Node(elem) # 1. 새 노드 생성
        before = self.getNode(pos-1) # 2. pos -1 위치의 노드 탐색
        # 3. before 노드의 위치에 따라 구분
        if before is None :
            if pos == 0: # 1) 머리 노드로 삽입
                new.link = self.head 
                self.head = new 
                return 
            else: # 2) pos가 리스트 범위에서 벗어남
                raise IndexError("삽입할 위치가 유효하지 않음!")
        else:  # 3) 중간 노드로 삽입
            before.append(new)

    def delete(self, pos) : # 인덱스 기반 연산
        # pos 위치에서 해당 노드 삭제한 후 그 노드 반환
        if pos < 0 : 
            raise ValueError("잘못된 위치 값!")
        
        before = self.getNode(pos-1) # 1. 삭제 노드 이전의 노드 탐색
        # 2. before 노드의 위치에 따라 구분
        if before == None :
            if pos == 0: # 1) 머리 노드로 삭제
                deleted = self.head
                self.head = deleted.link
                deleted.link = None # 연결 해제
                return deleted
            else: # 2)pos가 리스트 범위에서 벗어남
                raise IndexError("삽입할 위치가 유효하지 않음!")
        else: # 3) 중간 노드로 삭제
            return before.popNext()
        
    def size(self):
        # 리스트의 전체 노드의 개수
        if self.head == None: # 현재 리스트가 공백이면
            return 0
        else :
            ptr = self.head
            count = 0
            while ptr is not None: 
                count += 1
                ptr = ptr.link
            return count
    
    def display(self, msg = "LinkedList:"):
        # 리스트의 내용을 출력
        print(msg, end = ' ')
        if self.head == None: # 현재 리스트가 공백이면
            return None
        else :
            ptr = self.head
            while ptr is not None: 
                print(ptr.data, end = " -> ")
                ptr = ptr.link
            print('None')

    def replace(self,pos,elem): # 인덱스 기반 연산
        # 리스트의 pos 위치에 있는 노드의 데이터 필드를 수정
        node = self.getNode(pos)
        if node != None: # 해당 노드가 있는 경우
            node.data =  elem   
        

    def find_by_title(self, title): # 책 제목으로 리스트에서 도서 찾기 
        ptr = self.head
        while ptr is not None:
            if ptr.data.title == title:
                return ptr.data
            ptr = ptr.link
        return None 

    def find_pos_by_title(self, title): # 책 제목으로 리스트에서 도서의 위치를 찾기 
        ptr = self.head
        pos = 0
        while ptr is not None:
            if ptr.data.title == title:
                return pos
            ptr = ptr.link
            pos += 1
        return None

# 도서 관리 클래스 
class BookManagement:
    def __init__(self):
        self.book = LinkedList()

    def duplicated_book_id(self, book_id): # 책 번호 중복 확인
        ptr = self.book.head
        while ptr is not None:
            if ptr.data.book_id == book_id:
                return True
            ptr = ptr.link
        return False
    
    def duplicated_title(self,title): # 책 이름 중복 확인 
        ptr = self.book.head
        while ptr is not None:
            if ptr.data.title == title:
                return True
            ptr = ptr.link
        return False
    
    def add_book(self, book_id, title, author, year): # 도서 추가 코드 
        pos = self.book.size()
        self.book.insert(pos,Book(book_id, title, author, year))
        print(f"도서 {title}가 추가되었습니다")
     
    def remove_book(self,title): #도서 삭제 코드 
        pos = self.book.find_pos_by_title(title)
        if pos is None:
            print("도서를 찾을 수 없습니다")
            return
        deleted_Node = self.book.delete(pos)
        print(f"도서 {deleted_Node.data.title}가 삭제되었습니다")

    def search_book(self,title): # 도서 조회 코드
        book = self.book.find_by_title(title)
        if book is None:
            print("해당 도서를 찾을 수 없습니다")
            return
        print(f"[책 번호: {book.book_id}, 제목: {book.title}, 저자: {book.author}, 출판 연도: {book.year}]")

    def display_books(self): # 전체 도서 목록 출력
        if self.book.isEmpty():
            print("현재 등록된 도서가 없습니다")
            return
        print("현재 등록된 도서 목록:")
        ptr = self.book.head
        while ptr is not None:
            dis = ptr.data
            print(f"[책 번호: {dis.book_id}, 제목: {dis.title}, 저자: {dis.author}, 출판 연도: {dis.year}]")
            ptr = ptr.link

    def run(self):
        while True:
            print("\n===== 도서 관리 프로그램 =====")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로 삭제)")
            print("3. 도서 조회 (책 제목으로 조회)")
            print("4. 전체 도서 목록 출력")
            print("5. 종료")

            chose = input("메뉴를 선택하세요: ").strip()
            if chose == '1':
                try:

                    while True:
                        book_id = int(input("책 번호를 입력하세요: ").strip())
                        if self.duplicated_book_id(book_id):
                            print("이미 존재하는 책 번호입니다. 다시 입력하세요.")
                        else:
                            break
                    while True:
                        title = input("책 제목을 입력하세요: ").strip()
                        if self.duplicated_title(title):
                            print("이미 존재하는 책입니다. 다시 입력하세요")
                        else:
                            break
                    author = input("저자를 입력하세요: ").strip()
                    year = int(input("출판 연도를 입력하세요: ").strip())
                    self.add_book(book_id,title,author,year)
                except ValueError:
                    print("도서 추가 실패하였습니다. 다시 입력하세요.")
            elif chose == '2':
                title = input("삭제할 책 제목: ").strip()
                self.remove_book(title)
            elif chose == '3':
                title = input("조회할 책 제목을 입력하세요: ").strip()
                self.search_book(title)
            elif chose == '4':
                self.display_books()
            elif chose == '5':
                print("종료합니다")
                break
            else:
                print("올바른 번호를 입력하세요.")

if __name__ == "__main__":
    bookmanager = BookManagement()
    bookmanager.run()