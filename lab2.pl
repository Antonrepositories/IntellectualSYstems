% Родова-видові зв'язки (is_a)
is_a(vertebrate, animal).
is_a(invertebrate, animal).

is_a(mammal, vertebrate).
is_a(reptile, vertebrate).

is_a(spider, invertebrate).
is_a(insect, invertebrate).



is_a(dog, mammal)
is_a(antilopa, mammal).

is_a(turtle, reptile).
is_a(snake, reptile).


is_a(scorpion, spider).
is_a(black_widow, spider).

is_a(bee, insect).
is_a(ant, insect).


is_a(X, Z) :- is_a(X, Y), is_a(Y, Z).

% Зв'язки частина-ціле
part_of(paw, dog).
part_of(horn, antilopa).
part_of(hoof, antilopa).

part_of(shell, turtle).
part_of(poison, snake).

part_of(poisonous_tail, scorpion).
part_of(web, black_widow).

part_of(geniculate_tendrils, ant).
part_of(wings, bee).
part_of(sting, bee).


part_of(X, Z) :- part_of(X, Y), is_a(Y, Z).

