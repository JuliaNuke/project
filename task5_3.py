tutors = [
'Иван', 'Анастасия', 'Петр', 'Сергей',
'Дмитрий', 'Борис', 'Елена'
]
klasses = [
'9А', '7В', '9Б', '9В', '8Б' #, '10А', '10Б', '9А'
]


def tutor_class_generator():
    klass_gen = (k for k in klasses)
    for i,t in enumerate(tutors):
        kls = None
        if i <= len(klasses) - 1:
            kls = next(klass_gen)
        yield (t, kls)


print(list(tutor_class_generator()))