def maxVowels( s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o','u']
        countMax = 0
        for i in range(0, len(s)):
            count = 0
            print(s[i:i+k])
            for vowel in vowels:
                count += s[i:i+k].count(vowel)
            if count > countMax:
                countMax = count
        return countMax
    
print(maxVowels("weallloveyou", 7))