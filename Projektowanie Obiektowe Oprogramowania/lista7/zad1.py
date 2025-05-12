import sys
from typing import Callable, Dict, List, Optional, Type, Union

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QPushButton, QLabel, QLineEdit, QDialog, QHBoxLayout,
    QStackedWidget, QListWidget, QListWidgetItem, QFormLayout
)
from PyQt5.QtCore import Qt


class EventAggregator:
    def __init__(self) -> None:
        self._subs: Dict[Type, List[Callable]] = {}

    def subscribe(self, typ: Type, fn: Callable) -> None:
        self._subs.setdefault(typ, []).append(fn)

    def publish(self, ev: object) -> None:
        for fn in self._subs.get(type(ev), []):
            fn(ev)


event = EventAggregator()


class CategorySelectedNotification:
    def __init__(self, cat: str) -> None:
        self.cat: str = cat


class UserSelectedNotification:
    def __init__(self, user: 'User') -> None:
        self.user: User = user


class UserAddedNotification:
    def __init__(self, user: 'User') -> None:
        self.user: User = user


class UserUpdatedNotification:
    def __init__(self, user: 'User') -> None:
        self.user: User = user


class User:
    def __init__(self, first: str, last: str, email: str, cat: str) -> None:
        self.first: str = first
        self.last: str = last
        self.email: str = email
        self.cat: str = cat

    def __str__(self) -> str:
        return f"{self.first} {self.last}"


class UserDialog(QDialog):
    def __init__(self, user: Optional[User] = None) -> None:
        super().__init__()
        self.user: Optional[User] = user
        self.inputs: List[QLineEdit] = [QLineEdit() for _ in range(4)]
        self.setWindowTitle("Dodaj" if not user else "Zmień")

        if user:
            self.inputs[0].setText(user.first)
            self.inputs[1].setText(user.last)
            self.inputs[2].setText(user.email)
            self.inputs[3].setText(user.cat)

        layout = QFormLayout()
        for label, inp in zip(["Imię", "Nazwisko", "Email", "Kategoria"], self.inputs):
            layout.addRow(label, inp)

        save_btn = QPushButton("Zapisz")
        save_btn.clicked.connect(self.save)
        layout.addWidget(save_btn)
        self.setLayout(layout)

    def save(self) -> None:
        first, last, email, cat = [i.text() for i in self.inputs]
        if self.user:
            self.user.first, self.user.last = first, last
            self.user.email, self.user.cat = email, cat
            event.publish(UserUpdatedNotification(self.user))
        else:
            event.publish(UserAddedNotification(User(first, last, email, cat)))
        self.accept()


class Tree(QTreeWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setHeaderLabel("Kategorie")
        self.cats: Dict[str, QTreeWidgetItem] = {}
        self.itemClicked.connect(self.on_click)
        event.subscribe(UserAddedNotification, self.add_user)
        event.subscribe(UserUpdatedNotification, self.update_user)

    def on_click(self, item: QTreeWidgetItem, _: int) -> None:
        data: Union[str, User] = item.data(0, Qt.UserRole)
        if isinstance(data, str):
            event.publish(CategorySelectedNotification(data))
        else:
            event.publish(UserSelectedNotification(data))

    def add_user(self, ev: UserAddedNotification) -> None:
        u = ev.user
        if u.cat not in self.cats:
            cat = QTreeWidgetItem([u.cat])
            cat.setData(0, Qt.UserRole, u.cat)
            self.addTopLevelItem(cat)
            self.cats[u.cat] = cat

        item = QTreeWidgetItem([str(u)])
        item.setData(0, Qt.UserRole, u)
        self.cats[u.cat].addChild(item)

    def update_user(self, ev: UserUpdatedNotification) -> None:
        u = ev.user
        for cat in self.cats.values():
            for i in range(cat.childCount()):
                item = cat.child(i)
                if item.data(0, Qt.UserRole) == u:
                    item.setText(0, str(u))


class UserList(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.cat: str = ""
        self.users: List[User] = []
        self.list: QListWidget = QListWidget()

        btn = QPushButton("Dodaj")
        btn.clicked.connect(lambda: UserDialog().exec_())

        layout = QVBoxLayout()
        layout.addWidget(self.list)
        layout.addWidget(btn)
        self.setLayout(layout)

        event.subscribe(CategorySelectedNotification, self.load)
        event.subscribe(UserAddedNotification, self.add_user)

    def load(self, ev: CategorySelectedNotification) -> None:
        self.cat = ev.cat
        self.refresh()

    def add_user(self, ev: UserAddedNotification) -> None:
        self.users.append(ev.user)
        self.refresh()

    def refresh(self) -> None:
        self.list.clear()
        for u in self.users:
            if u.cat == self.cat:
                item = QListWidgetItem(str(u))
                item.setData(Qt.UserRole, u)
                self.list.addItem(item)

        self.list.itemClicked.connect(
            lambda i: event.publish(UserSelectedNotification(i.data(Qt.UserRole)))
        )


class Profile(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.user: Optional[User] = None
        self.label: QLabel = QLabel("Brak danych")
        btn = QPushButton("Zmień")
        btn.clicked.connect(lambda: UserDialog(self.user).exec_())

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(btn)
        self.setLayout(layout)

        event.subscribe(UserSelectedNotification, self.show_user)
        event.subscribe(UserUpdatedNotification, self.show_user)

    def show_user(self, ev: Union[UserSelectedNotification, UserUpdatedNotification]) -> None:
        self.user = ev.user
        self.label.setText(
            f"{self.user.first} {self.user.last}\n{self.user.email}\n{self.user.cat}"
        )


class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Rejestr użytkowników")

        tree = Tree()
        self.stack: QStackedWidget = QStackedWidget()
        self.list: UserList = UserList()
        self.profile: Profile = Profile()

        self.stack.addWidget(self.list)
        self.stack.addWidget(self.profile)

        layout = QHBoxLayout()
        layout.addWidget(tree, 1)
        layout.addWidget(self.stack, 3)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        event.subscribe(CategorySelectedNotification, lambda _: self.stack.setCurrentWidget(self.list))
        event.subscribe(UserSelectedNotification, lambda _: self.stack.setCurrentWidget(self.profile))


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    win: Main = Main()
    win.resize(800, 500)
    win.show()
    sys.exit(app.exec_())
