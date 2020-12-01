class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lst = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
        final_lst = []
        for word in words:
            temp = ""
            for letter in word:
                temp += lst[letter]
            
            final_lst += [temp]
            
        res = len(set(final_lst))
        return res