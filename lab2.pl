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

is_a(X, Z) :- is_a(X, Y), is_a(Y, Z).

% Зв'язки частина-ціле
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

part_of(X, Z) :- part_of(X, Y), is_a(Y, Z).

% Якщо X є ссавцем, то у нього є шерсть
has_fur(X) :- is_a(X, mammal).

% Якщо X є птахом, то у нього є пір'я
has_feathers(X) :- is_a(X, bird).

% Якщо X є рептилією, то у нього є луска
has_scales(X) :- is_a(X, reptile).