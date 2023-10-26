# Лабораторні роботи з дисципліни "Алгоритмів і структур даних"

## Виконала: Бігун Марія Ігорівна(Група ІР-25)

### Лабораторна робота №1 (Варіант 2 Рівень 2)

Масив вважається монотонним, якщо всі його елементи розташовані в зростаючому або спадаючому порядку.
​
Завдання: Напишіть функцію, яка перевіряє, чи є заданий масив монотонним. Функція повинна повертати логічне значення True, якщо масив є монотонним, і False, якщо масив не є монотонним.
​
Приклад вхідних даних і результатів:
​
1. Для масиву [1, 2, 3, 4, 5] функція повертає True, оскільки всі елементи зростають монотонно.
2. Для масиву [5, 4, 3, 2, 1] функція повертає True, оскільки всі елементи спадають монотонно.
3. Для масиву [1, 2, 2, 3, 2, 4] функція повертає False, оскільки масив не є строго монотонним.
​
Зверніть увагу, що масив із однаковими значеннями наступного елемента вважається монотонним.
​

***
### Лабораторна робота №2 (Варіант 2 Рівень 1)

Припустимо, компанія, в якій ви працюєте, розробляє електронний календар. У календарі є функція, що показує, коли різні команди програмістів будуть зайняті протягом будь-якої зустрічі.
Ті періоди, коли команда зайнята, на календарі позначені як діапазони часу, наприклад, з 10:00 до 12:30 або з 12:30 до 13:00. У вашій програмі проміжок часу представлений у вигляді пари з двох цілих чисел. Число означає номер 30-хвилинного блоку, який йде після 9:00 ранку. Наприклад, кортеж (2, 4) означає діапазон з 10:00 до 11:00, а (0, 1) - це проміжок 9:00-9:30.
Вам потрібно написати функцію, яка повинна спростити вивід інформації таким чином, що якщо команда зайнята в проміжках з 10:00 до 12:30 і з 12:30 до 13:00, то це має відображатись  як 10: 00-13: 00. 

Приклад: 
на вході вашої функції невпорядкований масив з кортежів [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)], 

Результат:
Ваша функція має повернути впорядкований масив  [(0, 1), (3, 8), (9, 12)].  
  
Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку unittest та перевірити роботу вашої функції на прикладах, наведених вище

***

### Лабораторна робота №3 (Варіант 2 Рівень 2)


Для бінарного дерева знайдіть суму всіх глибин усіх вузлів. Глибина вузла - це кількість ребер, які потрібно пройти від кореня дерева, щоб досягти цього вузла.

Ваше завдання полягає в написанні функції, яка обчислює та повертає суми глибин для всіх вузлів у бінарному дереві

Приклад: Розглянемо таке бінарне дерево:

    1
   / \
  2   3
 / \
4   5


Глибина вузла 1 -0, глибина вузла 2 та 3 становить 1, а глибина вузлів 4 та 5 - 2. Сума глибин всіх вузлів дорівнює 0 + 1 + 1 + 2 + 2 = 6.

Функція отримує на вхід корінь бінарного дерева, який має наступний вигляд:

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

 Ваша функція має мати такий вигляд:  

def sum_of_depths(root: TreeNode) -> int:
    # ваш код
Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з бінарного дерева. У тесті ви можете створити достатню кількість елементів класу TreeNode наступним чином:

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
