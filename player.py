import random

class player:

    def __init__(self,deck=[],race='race',hitpts=50):
        random.shuffle(deck)
        self.hand = []
        self.deck = deck
        self.hitpts = hitpts
        self.energy = 1
        self.race = race
        self.discard = []
        self.in_play = []

    def discard(self,card):
        if card not in self.hand:
            raise Exception('Select a card in your hand to discard')
        self.hand.remove(card)
        self.discard.append(card)

    def draw(self):
        new_card = self.deck.pop()
        self.hand.append(new_card)
        if len(self.hand) > 10:
            print('Hand limit is 10. Choose a card from your hand to discard')
            card = input()
            self.discard(card)

    def get_playable_cards(self):
        playable = []
        for card in self.hand:
            if card.cost <= self.energy:
                playable.append(card)
        return playable

    def is_playable_done(self,opt_out=False):
        if len(get_playable_cards(self)) == 0 or opt_out==True:
            return True
        return False

    def get_tapable_cards(self):
        tapable = []
        for card in self.in_play:
            if card.tap == False:
                tapable.append(card)
        return tapable

    def get_immediates(self):
        imm = []
        for card in self.hand:
            if card.immediate == True:
                imm.append(card)
        return imm

    def is_action_done(self,opt_out=False):
        actions = self.get_immediates + self.get_tapable
        if len(actions) == 0 or opt_out == True:
            return True
        return False

    def add_card_to_in_play(self,card):
        while card not in self.hand:
            print('Card must come from your hand')
            card = input()
        if card.cost >= self.energy:
            self.energy -= card.cost
            self.in_play.append(card)
        else:
            print('Cannot afford to play this card')


