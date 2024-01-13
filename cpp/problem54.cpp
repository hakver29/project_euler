#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <iterator>

class Card {
    public:
        Card(int value, char suit) : value(value), suit(suit) {}

        int getValue() const { return value; }
        char getSuit() const { return suit; }

        friend std::ostream& operator<<(std::ostream& os, const Card& card);
        friend bool operator<(const Card& card1, const Card& card2);
        friend bool operator==(const Card& card1, const Card& card2);
        friend bool operator!=(const Card& card1, const Card& card2);


private:
        int value;
        char suit;
};

bool operator<(const Card& card1, const Card& card2) {
    // Compare based on value first, and if values are equal, compare based on suit
    if (card1.getValue() == card2.getValue()) {
        return card1.getSuit() < card2.getSuit();
    }
    return card1.getValue() < card2.getValue();
}
bool operator==(const Card& card1, const Card& card2) {
    // Compare based on value first, and if values are equal, compare based on suit
    return card1.getValue() == card2.getValue();
}

bool operator!=(const Card& card1, const Card& card2) {
    // Compare based on value first, and if values are equal, compare based on suit
    return card1.getValue() != card2.getValue();
}


std::ostream& operator<<(std::ostream& os, const Card& card) {
    os << card.value << card.suit;
    return os;
}

class PokerHand {
    public:
        PokerHand(const std::vector<Card>& cards) : cards(cards) {}

        bool operator <(PokerHand const& rhs) const {
            return this->isFlush();
        }

        std::vector<Card> cards;

        friend std::ostream& operator<<(std::ostream& os, const Card& card);

        int handStrength(){
            if(this->isRoyalStraightFlush()) return 8;
            if(this->isStraightFlush()) return 7;
            if(this->isFourOfAKind()) return 6;
            if(this->isFullHouse()) return 5;
            if(this->isFlush()) return 4;
            if(this->isStraight()) return 3;
            if(this->isThreeOfAKind()) return 2;
            if(this->isTwoPairs()) return 1;
            if(this->isOnePair()) return 0;
            return -1;
        }

        bool isFlush() const;
        bool isStraight() const;
        bool isOnePair() const;
        bool isTwoPairs() const;
        bool isThreeOfAKind() const;
        bool isStraightFlush() const;
        bool isFullHouse() const;
        bool isFourOfAKind() const;
        bool isRoyalStraightFlush() const;
};

std::ostream& operator<<(std::ostream& os, const PokerHand& hand) {
    for (int i = 0; i < hand.cards.size(); i++){
        os << hand.cards[i] << " ";
    }
    return os;
}

bool PokerHand::isFlush() const {
    int i;
    char suit = cards[0].getSuit();
    for (i = 1; i < 5; ++i) if (cards[i].getSuit() != suit) return false;
    return true;
}

bool PokerHand::isOnePair() const {
    if(cards[0] == cards[1]) return true;
    if(cards[1] == cards[2]) return true;
    if(cards[2] == cards[3]) return true;
    if(cards[3] == cards[4]) return true;
    return false;
}

bool PokerHand::isTwoPairs() const {
    if(cards[0] == cards[1] && cards[2] == cards[3] && cards[1] != cards[2]) return true;
    if(cards[0] == cards[1] && cards[2] == cards[4] && cards[1] != cards[2]) return true;
    if(cards[0] == cards[1] && cards[3] == cards[4] && cards[1] != cards[3]) return true;
    if(cards[0] == cards[2] && cards[3] == cards[4] && cards[2] != cards[3]) return true;
    if(cards[1] == cards[2] && cards[3] == cards[4] && cards[2] != cards[3]) return true;
    return false;
}

bool PokerHand::isFullHouse() const {
    if(this->isThreeOfAKind() && this->isTwoPairs()) return true;
    return false;
}

bool PokerHand::isStraightFlush() const {
    if(this->isStraight() && this->isFlush()) return true;
    return false;
}

bool PokerHand::isRoyalStraightFlush() const {
    if(this->isStraight() && this->isFlush() && cards[0].getValue() == 10) return true;
    return false;
}

bool PokerHand::isFourOfAKind() const {
    if(cards[0] == cards[1] && cards[1] == cards[2] && cards[2] == cards[3]) return true;
    if(cards[0] == cards[1] && cards[1] == cards[2] && cards[2] == cards[4]) return true;
    if(cards[0] == cards[1] && cards[1] == cards[3] && cards[3] == cards[4]) return true;
    if(cards[0] == cards[1] && cards[2] == cards[3] && cards[3] == cards[4]) return true;
    if(cards[1] == cards[2] && cards[2] == cards[3] && cards[3] == cards[4]) return true;
    return false;
}

bool PokerHand::isThreeOfAKind() const {
    if(cards[0] == cards[1] && cards[1] == cards[2]) return true;
    if(cards[1] == cards[2] && cards[2] == cards[3]) return true;
    if(cards[2] == cards[3] && cards[3] == cards[4]) return true;
    return false;
}

bool PokerHand::isStraight() const {
    if(cards[0].getValue() + 1 == cards[1].getValue() &&
        cards[1].getValue() + 1 == cards[2].getValue() &&
        cards[2].getValue() + 1 == cards[3].getValue() &&
        cards[3].getValue() + 1 == cards[4].getValue()) return true;
    if(cards[0].getValue() + 12 == cards[4].getValue() &&
       cards[0].getValue() + 1 == cards[1].getValue() &&
       cards[1].getValue() + 1 == cards[2].getValue() &&
       cards[2].getValue() + 1 == cards[3].getValue()) return true;
    return false;
}

int convertValue(char value)  {
    switch(value){
        case 'A':
            return 14;
        case 'K':
            return 13;
        case 'Q':
            return 12;
        case 'J':
            return 11;
        case 'T':
            return 10;
        default:
            return value - '0';
    }
}

int main() {
    std::ifstream file("cpp/problem54poker.txt");
    std::string line;

    int numberOfTimesPlayer1Wins = 0;


    while (std::getline(file, line)) {
        int a = 0;
        std::string word;
        std::istringstream iss(line);
        std::vector<Card> firstHand;
        std::vector<Card> secondHand;
        while (iss >> word) {
            int val = convertValue(word[0]);
            Card card = Card(val,word[1]);
            if(a < 5){
                firstHand.push_back(card);
            } else{
                secondHand.push_back(card);
            }
            a++;
        }
        std::sort(firstHand.begin(), firstHand.end());
        std::sort(secondHand.begin(), secondHand.end());
        PokerHand firstPokerHand = PokerHand(firstHand);
        PokerHand secondPokerHand = PokerHand(secondHand);
        if(firstPokerHand.handStrength() == secondPokerHand.handStrength()){
            numberOfTimesPlayer1Wins++;
            std::cout << firstPokerHand << secondPokerHand << std::endl;
        }
    }
    std::cout << numberOfTimesPlayer1Wins << std::endl;



    // Close the file
    file.close();

    return 0;
}