from question import Question
question_prompts = [
    "Какая компания продает больше всего игрушек в мире?\n(a) TaDa\n(b) Na-Na\n(c) McDonald's\n\n",
    "Почему белые медведи не едят пингвинов?\n(a) Они живут в разных полушариях\n(b) Они друзья\n(c) Пингвины вредны для их здоровья\n\n",
    "Какое из этих чисел является наименшим простым числом?\n(a) 1\n(b) 2\n(c) 3\n\n",
    "Какой материк омывается 4 океанами?\n(a) Евразия\n(b) Африка\n(c) Австралия\n\n",
    "Электрон меньше атома?\n(a) Нет\n(b) Да\n\n",
    "В каком году люди высадились на луну?\n(a) 1972\n(b) 1969\n(c) 1958\n\n",
    "Антибиотики убивают не только бактерии, но и вирусы?\n(a) да\n(b) Нет\n\n",
    "Сколько законов Ньютона существует?\n(a) 5\n(b) 3\n(c) 6\n\n",
    "Что обозначает О3 в химии?\n(a) Водород\n(b) Кислород\n(c) Озон\n\n",
    "Какой город является столицей Австралии?\n(a) Канберра\n(b) Сидней\n(c) Мельбурн\n\n",
    "Сколько лошадиных сил в лошади?\n(a) 0,3\n(b) 0,7\n(c) 1\n\n",
    "Сколько костей в теле взрослого человека?\n(a) 206\n(b) 215\n(c) 195\n\n",
]

answers = [
		'c', 'a', 'b', 'a', 'a', 'b', 'b', 'b', 'c', 'a', 'a', 'a',
		
	]
	
questions = []
for prompt_num, ans in enumerate(answers):
	questions.append(
			Question(question_prompts[prompt_num], ans)
		)

def run_test(questions):
    score = 0
    for question in questions:
        otvet = input(question.vopros)
        score += otvet == question.otvet
    print(f"У вас {score} ответов из {len(questions)} верны")


run_test(questions)
