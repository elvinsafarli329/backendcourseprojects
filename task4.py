# inheritance

# class chess():
#     def __init__(self, name, elo, age, country):
#         self.name = name
#         self.elo = elo
#         self.age = age
#         self.country = country
    
#     def title(self):
#         if self.elo > 3000:
#             return "GM"
#         elif 2000 < self.elo < 3000:
#             return "IM"
#         else:
#             return "FM"
    
# player1 = chess("Hikaru", 3300, 30, "Vietnam")

# print(f"{player1.name} is a famous chess player in {player1.country}, who has {player1.elo} elo in chess.com")

# class fisher(chess):
#     def __init__(self, name, elo, age, country):
#         super().__init__(name, elo, age, country)
#         super().title()
#     def legend(self):
#         print("Bobby Fisher is a legend")
        
#     def wins(self):
#         print("Bobby Fisher won 300 games during his life")

# bobby_fisher = fisher("Bobby Fisher", 2900, 64, "USA")
# print(f"{bobby_fisher.name} is a famous chess player in {bobby_fisher.country}, who has {bobby_fisher.elo} elo in chess.com")

# print(f"{bobby_fisher.name} is {bobby_fisher.title()}")

# bobby_fisher.legend()
# bobby_fisher.wins()

# polymorphism

# class chess():
#     def __init__(self, name, elo, age, country):
#         self.name = name
#         self.elo = elo
#         self.age = age
#         self.country = country
    
#     def title(self):
#         if self.elo > 3000:
#             return "GM"
#         elif 2000 < self.elo < 3000:
#             return "IM"
#         else:
#             return "FM"

# class fisher(chess):
#     def __init__(self, name, elo, age, country):
#         super().__init__(name, elo, age, country)
#         super().title()
        
#     def legend(self):
#         return "Bobby Fisher is a legend"
        
#     def wins(self):
#         return "Bobby Fisher won 300 games during his life"

# class magnus(chess):
#     def __init__(self, name, elo, age, country):
#         super().__init__(name, elo, age, country)
#         super().title()

#     def legend(self):
#         return "Magnus Carlsen is a legend"
    
#     def wins(self):
#         return "Magnus Carlsen won 500 games during his life"
    
#     def champion(self):
#         print("Magnus is a world champion")

# Magnus = magnus("Magnus Carlsen", 2850, 30, "Norway")
# print(f"{Magnus.name} is a young chess player with {Magnus.elo} elo. For me, {Magnus.legend()}")
# Magnus.champion()