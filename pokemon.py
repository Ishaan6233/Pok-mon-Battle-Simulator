'''
Read Pokémon from a file and randomly select two Pokémon to battle, and simulate a battle
Author: Ishaan Meena
When: 25/11/22
'''

import random


class Pokemon:
    """
     An object in this class represents a single pokemon
     """

    def __init__(self, name, attack, defense, max_health, current_health):
        """
        Creates and returns a pokemon object with attributes: name, attack, defense, max_health, current_health
        """
        self.name = name
        self.attack = attack
        self.defense = defense
        self.max_health = max_health
        self.current_health = current_health

    def __str__(self) -> str:
        """
        Return a string representation of the Pokemon.
        Returns Pokemon name, current_health and max_health
        """
        return (f"{self.name} (health: {self.current_health}/{self.max_health})")

    def lose_health(self, amount: int) -> None:
        """
        Lose health from the Pokemon.
        Decrements the Pokemons health
        """
        if amount > 0:
            if amount < self.current_health:
                self.current_health = self.current_health - amount
            elif amount >= self.current_health:
                self.current_health = 0

    def is_alive(self) -> bool:
        """
        Return True if the Pokemon has health remaining.
        """
        return self.current_health != 0

    def revive(self) -> None:
        """
        Revive the Pokemon.
        """
        self.current_health = self.max_health

    def attempt_attack(self, other: "Pokemon") -> bool:
        """
        Attempt an attack on another Pokemon.
        This method can either return a bool, or return nothing
        (depends on your implementation)
        """
        luck_array = [i / 10 for i in range(7, 13, 1)]
        coefficient_of_luck = random.choice(luck_array)
        damage = round(self.attack * coefficient_of_luck)
        print(f"{self.name} attacks {other.name} for {damage} damage!")
        if damage > other.defense:
            other.lose_health(damage)
            return True
        else:
            return False


def read_pokemon_from_file(filename: str) -> list[Pokemon]:
    """
    Read a list of Pokemon from a file.
    """
    with open(filename, 'r') as all_pokemon_file:
        file_data = all_pokemon_file.readlines()[1:]  # Skipping the first line
        pokemon_list = []
        for pokemon_data in file_data:
            pokemon_list.append(pokemon_data[:-1])

    rand_num = random.randint(0, len(pokemon_list) - 1)
    pokemon1_list = pokemon_list[rand_num - 1].split('|')
    pokemon1 = Pokemon(pokemon1_list[0], int(pokemon1_list[1]), int(pokemon1_list[2]), int(pokemon1_list[3]),
                       int(pokemon1_list[3]))

    rand_num = random.randint(0, len(pokemon_list) - 1)
    pokemon2_list = pokemon_list[rand_num].split('|')
    pokemon2 = Pokemon(pokemon2_list[0], int(pokemon2_list[1]), int(pokemon2_list[2]), int(pokemon2_list[3]),
                       int(pokemon2_list[3]))
    if pokemon1 != pokemon2:
        return [pokemon1, pokemon2]


def main():
    """
    Battle of two Pokemon
    """
    pokemon_list = read_pokemon_from_file('all_pokemon.txt')
    pokemon1 = pokemon_list[0]
    pokemon2 = pokemon_list[1]
    print(f"Welcome, {pokemon1} and {pokemon2}!")

    round_counter = 1
    while True:
        print(f"Round {round_counter} begins! {pokemon1} and {pokemon2}")
        if pokemon1.attempt_attack(pokemon2):
            print(f"Attack is successful! {pokemon2.name} has {pokemon2.current_health} remaining!")
            if not (pokemon2.is_alive()):
                chance = random.choice(['revive', 'die'])
                if chance == 'revive':
                    pokemon2.revive()
                    print(f"{pokemon2.name} has been revived!")
                else:
                    print(f"{pokemon1} has won in {round_counter} rounds!")
                    break
        else:
            print("Attack is blocked")

        if pokemon2.attempt_attack(pokemon1):
            print(f"Attack is successful! {pokemon1.name} has {pokemon1.current_health} remaining!")
            if not (pokemon1.is_alive()):
                chance = random.choice(['revive', 'die'])
                if chance == 'revive':
                    pokemon1.revive()
                    print(f"{pokemon2.name} has been revived!")
                else:
                    print(f"{pokemon2} has won in {round_counter} rounds!")
                    break
        else:
            print("Attack is blocked")

        if round_counter < 10:
            round_counter += 1
        else:
            print(f"It's a tie between {pokemon1} and {pokemon2}")
        print()  # Add a line at the end of each round


if __name__ == '__main__':
    main()
