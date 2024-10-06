:- discontiguous is_a/2.
:- discontiguous part_of/2.
% Родова-видові зв'язки (is_a)
is_a(cat, mammal).
is_a(dog, mammal).
is_a(elephant, mammal).
is_a(mammal, animal).
is_a(bird, animal).
is_a(eagle, bird).
is_a(sparrow, bird).
is_a(fish, animal).
is_a(shark, fish).
is_a(salmon, fish).
is_a(reptile, animal).
is_a(snake, reptile).
is_a(crocodile, reptile).

% Зв'язки частина-ціле (part_of)
part_of(wing, eagle).
part_of(beak, eagle).
part_of(wing, sparrow).
part_of(beak, sparrow).

part_of(tail, cat).
part_of(paw, cat).
part_of(tail, dog).
part_of(paw, dog).

part_of(fin, shark).
part_of(gill, shark).
part_of(fin, salmon).
part_of(gill, salmon).

part_of(trunk, elephant).
part_of(tusk, elephant).

part_of(poison, snake).
part_of(tail, crocodile).
% Транзитивні зв'язки
part_of(cat, mammal).
part_of(dog, mammal).
part_of(elephant, mammal).

part_of(eagle, bird).
part_of(sparrow, bird).

part_of(shark, fish).
part_of(salmon, fish).

part_of(snake, reptile).
part_of(crocodile, reptile).

part_of(mammal, animal).
part_of(reptile, animal).
part_of(bird, animal).
part_of(fish, animal).

% Правило транзитивності для родо-видових зв'язків (is_a)
is_a(X, Z) :- is_a(X, Y), is_a(Y, Z).

% Правило транзитивності для зв'язків частина-ціле (part_of)
part_of(X, Z) :- part_of(X, Y), part_of(Y, Z).

% Якщо X є ссавцем, то у нього є шерсть
has_fur(X) :- is_a(X, mammal).

% Якщо X є птахом, то у нього є пір'я
has_feathers(X) :- is_a(X, bird).

% Якщо X є рептилією, то у нього є луска
has_scales(X) :- is_a(X, reptile).