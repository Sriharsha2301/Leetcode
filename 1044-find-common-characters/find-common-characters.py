class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result=[]
         # Initialize common_character_counts with the characters from the first word
        common_char_count=Counter(words[0])
         # Count characters in the current word

        for i in range(1,len(words)):
            current_char_count=Counter(words[i])

        # Update the common character counts to keep the minimum counts

            for letter in common_char_count.keys():
                common_char_count[letter]=min(common_char_count[letter],current_char_count[letter]
                )
        for letter,count in common_char_count.items():
            for _ in range(count):
                result.append(letter)
        return result








        