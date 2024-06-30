from abc import ABC, abstractmethod

# Шаг 1: Создаем абстрактный класс Weapon, используя модуль abc для реализации концепции абстрактных классов.
class Weapon(ABC):
    @abstractmethod  # Декоратор, который указывает, что метод должен быть реализован в дочерних классах.
    def attack(self):
        pass  # Пустое тело метода, так как реализация будет в конкретных классах оружия.

# Шаг 2: Реализуем конкретные типы оружия.
class Sword(Weapon):
    def attack(self):
        # Реализуем метод attack() для меча.
        print("Боец наносит удар мечом.")

class Bow(Weapon):
    def attack(self):
        # Реализуем метод attack() для лука.
        print("Боец наносит удар из лука.")

# Шаг 3: Модифицируем класс Fighter, чтобы он поддерживал использование различных типов оружия.
class Fighter:
    def __init__(self, weapon: Weapon):
        # Инициализируем бойца с определенным оружием.
        self.weapon = weapon

    def changeWeapon(self, weapon: Weapon):
        # Метод для изменения оружия бойца.
        self.weapon = weapon

    def attack(self):
        # Метод для атаки, который вызывает метод attack() текущего оружия.
        self.weapon.attack()

# Класс Monster для представления монстра.
class Monster:
    def __init__(self, health: int):
        # Инициализируем монстра с определенным количеством здоровья.
        self.health = health

    def take_damage(self):
        # Метод, который уменьшает здоровье монстра при получении урона.
        self.health -= 1
        if self.health <= 0:
            # Если здоровье монстра меньше или равно нулю, выводим сообщение о его поражении.
            print("Монстр побежден!")

# Шаг 4: Реализация демонстрации работы программы.
if __name__ == "__main__":
    # Создаем меч как начальное оружие бойца.
    sword = Sword()
    # Создаем бойца с мечом.
    fighter = Fighter(sword)

    # Создаем монстра с 1 единицей здоровья.
    monster = Monster(1)

    # Боец атакует монстра с использованием меча.
    print("Боец выбирает меч.")
    fighter.attack()
    monster.take_damage()

    # Меняем оружие бойца на лук.
    bow = Bow()
    fighter.changeWeapon(bow)

    # Боец снова атакует монстра с использованием лука.
    print("\nБоец выбирает лук.")
    fighter.attack()
    monster.take_damage()
