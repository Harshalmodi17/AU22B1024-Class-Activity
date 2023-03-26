Problem 1:

Suppose you are buying something online on amazon.com 

On the website, you get
a 15% discount if you are a prime member. Additionally, you are also getting a discount of 8% on the item because it's black Friday sales.

Write a function that takes as input the amount of the asset that you are buying and a logical variable indicating whether you are a prime member applies the discount offered appropriately and returns the result.

Problem 2:

Chit Chat Application - Function:

(a) In few chit-chat programs, there is a limitation on the number of letters that you can send to your family and friends.

Write a function that takes as input the,

message and checks whether the number of letters is less than 200 or above. If the length of the information is less than 200, the chat should be returned.


If the length of the chat is greater than 200, data consisting of only the first 200 characters should be returned.


(b) How one can check if the restriction is on a number of words rather than letters?
Write a function that allows a message with only 30 words.


#Problem 1
class shoping:
    def __init__(self,pn,price,quantity,mem):
        self.pn = pn
        self.price = price
        self.quantity = quantity
        self.mem = mem
    def dis(self):
        if self.mem == "Prime":
            s = (self.price - 0.23*self.price)*self.quantity
            return s
        if self.mem == "Non Prime":
            s = (self.price - 0.08*self.price)*self.quantity
            return s
C1 = shoping("Shoes",2500,3,"Non Prime")
C1.dis()

#Problem 2(a)
n = list(input())
if len(n)<=200:
    print(*n,end = "")
if len(n) > 200:
    print(*n[0:200],end = "")

#Problem 2(b)
i = input()

words = []
c = ""

for ch in i:
    if ch != "," and ch != " ":
        c = c + ch
    else:
        words.append(c)
        c = ""
words.append(c)
if len(words) < 30:
    print(*words, end=" ")
else:
    print("Word Limit Exceeded!!!")
