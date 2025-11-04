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
    def __init__(self, bookID, title, author, year):
        self.bookID = bookID
        self.title = title
        self.author = author
        self.year = year

# 단순 연결 리스트
class LinkedList:
    def __init__(self):
        self.head = None  # 비어있는 리스트의 초기 상태
        
    # 주요 기본 연산
    def isEmpty(self):
        return self.head == None
    
    def isFull(self):
        return False  
    
    def getNode(self, pos):  # pos번째 노드 반환
        if pos < 0: 
            return None 
        if self.head == None: 
            return None
        else:
            ptr = self.head 
            for _ in range(pos):
                if ptr == None: 
                    return None
                ptr = ptr.link
            return ptr 

    def getEntry(self, pos): # pos 번째 노드 데이터 반환 
        node = self.getNode(pos)
        if node == None: 
            return None
        else:
            return node.data

    def insert(self, pos, elem): # pos 위치에 삽입
        if pos < 0:
            raise ValueError("잘못된 위치 값!")
        new = Node(elem)
        before = self.getNode(pos-1)
        if before is None:
            if pos == 0: 
                new.link = self.head
                self.head = new
                return
            else: 
                raise IndexError("삽입할 위치가 유효하지 않습니다")
        else:
            before.append(new)

    def delete(self, pos): # pos 위치 삭제
        if pos < 0:
            raise ValueError("잘못된 위치 값!")
        before = self.getNode(pos-1)
        if before == None:
            if pos == 0:
                deleted = self.head
                self.head = deleted.link
                deleted.link = None
                return deleted
            else:
                raise IndexError("삭제할 위치가 유효하지 않습니다")
        else:
            return before.popNext()

    def size(self): # 전체 노드 개수 
        if self.head == None:
            return 0
        else:
            ptr = self.head
            count = 0
            while ptr is not None:
                count += 1
                ptr = ptr.link
            return count

    def display(self):
        if self.head == None:
            print("None")
        else:
            ptr = self.head
            while ptr is not None:
                print(ptr.data, end=' -> ')
                ptr = ptr.link
            print("None")


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

    def duplicated_bookID(self, book_id): # 책 번호 중복 확인
        ptr = self.book.head
        while ptr is not None:
            if ptr.data.bookID == book_id:
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
    
    def add_book(self, book_id, title, author, year): # 도서 추가 
        pos = self.book.size()
        self.book.insert(pos,Book(book_id, title, author, year))
        print(f"도서 {title}가 추가되었습니다")
     
    def remove_book(self,title): #도서 삭제
        pos = self.book.find_pos_by_title(title)
        if pos is None:
            print("도서를 찾을 수 없습니다")
            return
        deleted_Node = self.book.delete(pos)
        print(f"도서 {deleted_Node.data.title}가 삭제되었습니다")

    def search_book(self,title): # 도서 조회
        book = self.book.find_by_title(title)
        if book is None:
            print("해당 도서를 찾을 수 없습니다")
            return
        print(f"[책 번호: {book.bookID}, 제목: {book.title}, 저자: {book.author}, 출판 연도: {book.year}]")

    def display_books(self): # 전체 도서 목록 출력
        if self.book.isEmpty():
            print("현재 등록된 도서가 없습니다")
            return
        print("현재 등록된 도서 목록:")
        ptr = self.book.head
        while ptr is not None:
            a = ptr.data
            print(f"[책 번호: {a.bookID}, 제목: {a.title}, 저자: {a.author}, 출판 연도: {a.year}]")
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
                        bookID = int(input("책 번호를 입력하세요: ").strip())
                        if self.duplicated_bookID(bookID):
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
                    self.add_book(bookID,title,author,year)
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