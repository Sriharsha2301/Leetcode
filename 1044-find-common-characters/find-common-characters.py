class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result=[]
        common_character_count=Counter(words[0])

        for i in range(1,len(words)):
            current_character_count=Counter(words[i])

            for letter in common_character_count.keys():
                common_character_count[letter]=min(common_character_count[letter],current_character_count[letter])
        
        for letter,count in common_character_count.items():
            for _ in range(count):
                result.append(letter)
        return result








        