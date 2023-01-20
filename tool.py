from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Flashcards():
    Base = declarative_base()
    class MyClass(Base):
        __tablename__ = 'flashcard.db'
        id = Column(Integer, primary_key=True)
        first_column = Column(String)
        second_column = Column(String)
        box = Column(Integer)

    engine = create_engine('sqlite:///flashcard.db?check_same_thread=False')
    Base.metadata.create_all(engine)

    def print_menu(self):
        while True:
            try:
                choice = input("""\n1. Add flashcards\n2. Practice flashcards\n3. Exit\n""")
                if choice not in ["1","2","3"]:
                    raise ValueError
                elif choice == "1":
                    self.add_flashcards() # ADD FLASHCARDS
                elif choice == "2":
                    self.practice_flashcards() # PRACTICE FLASHCARDS
                else:
                    print("\nBye!")
                    break
            except (ValueError):
                    print("\n" + choice + " is not an option\n")
                    continue
            break

    def get_question_answer(self):
        while True:
            try:
                question = input("\nQuestion:\n")
                if len(question) == 0 or question == " ":
                    raise ValueError
            except(ValueError):
                print("Cannot be empty!")
                continue
            break
        while True:
            try:
                answer = input("\nAnswer:\n")
                if len(answer) == 0 or answer == " ":
                    raise ValueError
                Session = sessionmaker(bind=self.engine)
                session = Session()
                new_data = self.MyClass(first_column=question, second_column=answer, box=1)
                session.add(new_data)
                session.commit()
            except(ValueError):
                print("Cannot be empty!")
                continue
            break

    def practice_flashcards(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        result_list = session.query(self.MyClass).all()

        if result_list == []:
            print("There is no flashcard to practice!")
            self.print_menu()
        else:
            n = len(result_list)
            for i in range(0, n):
                print("\nQuestion: " + result_list[i].first_column)
                response = input('press "y" to see the answer:\npress "n" to skip:\npress "u" to update: ')
                if response == "y":
                    print("\nAnswer: " + result_list[i].second_column + "\n")
                    self.right_or_wrong(result_list[i].id)
                elif response == "u":
                    self.update_flashcard(str(result_list[i].id))
                else:
                    continue
        self.print_menu()

    def right_or_wrong(self, id):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        query = session.query(self.MyClass)
        while True:
            try:
                decision = input('press "y" if your answer is correct:\npress "n" if your answer is wrong:\n')
                if decision not in ["y", "n"]:
                    raise ValueError
            except (ValueError):
                    print("\n" + decision + " is not an option\n")
                    continue
            if decision == "y":
                box_query = query.filter(self.MyClass.id == id)
                session.commit()
                if box_query[0].box == 1:
#                    print("box_query[0].box")  #debug
#                    print(box_query[0].box)  #debug
                    box_query.update({"box": 2})
                    session.commit()
#                    break
                elif box_query[0].box == 2:
#                    print("box_query[0].box")  #debug
#                    print(box_query[0].box)  #debug
                    box_query.update({"box": 3})
                    session.commit()
#                    break
                elif box_query[0].box == 3:
#                    print("box_query[0].box")  #debug
#                    print(box_query[0].box)  #debug
                    self.delete_flashcard(box_query[0].id)
                    session.commit()
#                    break
                else:
                    print("something went wrong")
            else:
                box_query = query.filter(self.MyClass.id == id)
                session.commit()
#                print("THIS IS THE BOX\n")
#                print(box_query[0].box)
                box_query.update({"box": 1})
                session.commit()
            break

    def delete_flashcard(self, id):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        query = session.query(self.MyClass)
        query.filter(self.MyClass.id == id).delete()
        session.commit()
        self.practice_flashcards()

    def edit_flashcard(self, id):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        result_list = session.query(self.MyClass).filter(
            self.MyClass.id.like(id)
        )
        query = session.query(self.MyClass)
        current_filter = query.filter(self.MyClass.id == id)
        c_q = result_list[0].first_column
        print("current question: " + c_q)
        while True:
            new_question = input('please write a new question: ')
            if len(new_question) == 0 or new_question == " ":
                break
            else:
                current_filter.update({"first_column": new_question})
                session.commit()
                break
        print("current answer: " + result_list[0].second_column)
        while True:
            new_answer = input('please write a new answer: ')
            if len(new_answer) == 0 or new_answer == " ":
                break
            else:
                current_filter.update({"second_column": new_answer})
                session.commit()
                break
        self.print_menu()

    def update_flashcard(self, id):
        while True:
            try:
                update = input('\npress "d" to delete the flashcard:\npress "e" to edit the flashcard: \n')
                if update not in ["d","e"]:
                    raise ValueError
                elif update == "d":
                    self.delete_flashcard(id)
                else:
                    self.edit_flashcard(id)
            except(ValueError):
                print(update + " is not an option")
                continue
    def add_flashcards(self):

        decision = 0
        while decision != "2":
            try:
                decision = input("""\n1. Add a new flashcard\n2. Exit\n""")
                if decision not in ["1","2"]:
                    raise ValueError
                if decision == "1":
                    self.get_question_answer() # GET QUESTION ANSWER
                if decision == "2":
                    self.print_menu()
            except (ValueError):
                print(decision + " is not an option")

def main():
    fc = Flashcards()
    fc.print_menu()

if __name__ == '__main__':
    main()