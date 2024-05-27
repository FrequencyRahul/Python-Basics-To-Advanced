#Kaun Banega Crorepati (KBC)

#create a program capable of displaying questions to user like KBC.
#use list data type to store questions and their correct answers.
#Display the total amount the person is taking after playing the game.

questions=[
"""1. The enzyme pepsin convert?

(A) Carbohydrates to sugars
(B) Proteins to amino acids
(C) Protein to peptones
(D) Fats to fatty acids and glycerol
""",

"""2. Which of these does not generate energy but are still essential for body?

(A) Fats
(B) Proteins
(C) Vitamins
(D) Carbohydrates
""",

"""3. Nitrogen

(A) is essential to the body
(B) dilutes oxygen which, other wise is very active in the pure form
(C) makes oxygen soluble in blood
(D) decreases the density of air
""",

"""4. The leading coffee producing State of India is?

(A) Andhra Pradesh
(B) Kerala
(C) Karnataka
(D) Tamil Nadu
""",

"""5. Tides in the sea have stored in them


(A) Hydraulic energy
(B) Kinetic energy
(C) Gravitational potential energy
(D) a combination of all the above three forms of energy
""",

"""6. The largest petroleum reserves are found in?

(A) Iran
(B) Russia
(C) Saudi Arabia
(D) Venezuela
""",

"""7. Port Diamond is located in?

(A) Australia
(B) Sri Lanka
(C) South Africa
(D) Zaire
""",

"""8. The headquarters of UNEP are located at?

(A)Berne
(B) Nairobi
(C) New York
(D) Vienna
""",

"""9. Which one of the following countries has the largest population?
(A) Brazil
(B) Bangladesh
(C) Indonesia
(D) Pakistan
""",

"""10. The Indus Valley Civilization was non-Aryan because?
(A) it was urban
(B) it had a pictographic script
(C) it had an agricultural economy
(D) it extended upto the Narmada Valley
"""
]

solutions=["A","C","C","C","D","C","C","C","C","C"]
winnings=[1000,2000,5000,10000,20000,120000,240000,1000000,5000000,10000000]
m=0
for i in questions:
    print(i)
    b=input("Enter your choice A/B/C/D:")
    if(b==solutions[m]):
        print("Congratulations you won:",winnings[m])
    else:
        print("Sorry you lost")
        break
    m=m+1




"""
1. The enzyme pepsin convert?

(A) Carbohydrates to sugars
(B) Proteins to amino acids
(C) Protein to peptones
(D) Fats to fatty acids and glycerol

ANS : A


2. Which of these does not generate energy but are still essential for body?


(A) Fats
(B) Proteins
(C) Vitamins
(D) Carbohydrates

ANS : C


3. Nitrogen
(A) is essential to the body
(B) dilutes oxygen which, other wise is very active in the pure form
(C) makes oxygen soluble in blood
(D) decreases the density of air

ANS : C


4. The leading coffee producing State of India is?


(A) Andhra Pradesh
(B) Kerala
(C) Karnataka
(D) Tamil Nadu

ANS : C


5. Tides in the sea have stored in them


(A) Hydraulic energy
(B) Kinetic energy
(C) Gravitational potential energy
(D) a combination of all the above three forms of energy


Ans : (D)


6. The largest petroleum reserves are found in?


(A) Iran
(B) Russia
(C) Saudi Arabia
(D) Venezuela

ANS : C

7. Port Diamond is located in?


(A) Australia
(B) Sri Lanka
(C) South Africa
(D) Zaire
ANS : C

8. The headquarters of UNEP are located at?
(A)Berne
(B) Nairobi
(C) New York
(D) Vienna
ANS : C

9. Which one of the following countries has the largest population?
(A) Brazil
(B) Bangladesh
(C) Indonesia
(D) Pakistan
ANS : C

10. The Indus Valley Civilization was non-Aryan because?
(A) it was urban
(B) it had a pictographic script
(C) it had an agricultural economy
(D) it extended upto the Narmada Valley
ANS : C

11. The greatest Pratihar King was?
(A) Dharampal
(B) Harsha
(C) Mihir Bhoj
(D) Mahendrapal
ANS : C

12. The Permanent Settlement was introduced by
(A) Lord Hastings
(B) Lord Cornawallis
(C) Lord Curzon
(D) Lord William Bentinck
ANS : C

13. Which of the following is known as the man’s most useful tree?
(A) Walnut
(B) Teak
(C) Mango
(D) Coconut
Ans : (A)

14. Who of the following is associated with football?
(A) Diego Maradona
(B) Forest Hills
(C) Target
(D) Jeev Milkha Singh
ANS : A

15. Who said “India is a quasi federal State”?
(A) Harold Laski
(B) Ivor Jennings
(C) Lord Bryee
(D) K. C. Wheare
ANS : C

16. Human Poverty Index was developed in the year?
(A)1991
(B) 1995
(C)1997
(D) 2001
ANS : C

17. Ram travels 7 km to the north. Then he turns to the right and walks 3 km. Now, he turns to the right and walks 7km. How many kilometres is he away from the starting point?
(A) 3km
(B) 7km
(C) 10km
(D) 14km
ANS :A

18. Which of the following is a cold blooded animal?
(A) Penguin
(B) Whale
(C) Otter
(D) Tortoise
Ans : (B)

19. A narrow strip of land bordered on both sides by water, connecting two large bodies of land is known as
(A) An isthmus
(B) A lagoon
(C) A peninsula
(D) A strait
Ans : (D)

20. The oldest mountain system of India is?
(A) Aravallis
(B) Himalayas
(C) Shiwaliks
(D) Vindhyas
ANS : C

21. Radioactivity is measured b?
(A) Hydrometer
(B) Geiger Counter
(C) Seismometer
(D) Ammeter
ANS : C

22. Interferon is used for the control of?
(A)Cancer
(B) Diabetes
(C)T. B.
(D) Typhoid
ANS : C

23. Oil spreads on water surface because?
(A) oil is denser than water
(B) oil is less dense than water
(C) surface tension of oil is more than water
(D) surface tension of oil is less than water
ANS : C D


24. Which country has produced the first transgenic glowing pigs that are all green from inside out?

(A) Korea
(B) Japan
(C) Singapore
(D) Taiwan
ANS : C

25 Tipu Sultan ruled from
(A) Srirangapatnam
(B) Mysore
(C) Madras
(D) Belur

Ans:A 
"""