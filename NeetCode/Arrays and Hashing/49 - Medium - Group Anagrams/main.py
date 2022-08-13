class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        length_dict = {i : [] for i in range(101)}
        for string in strs:
            length_dict[len(string)].append(string)
        final = []
        for words in length_dict.values():
            result = []
            i = 0
            while words:
                word_to_compare = words.pop()
                result.append([word_to_compare])
                j = 0
                for word in words[:]:
                    if sorted(word) == sorted(word_to_compare):
                        result[i].append(word)
                        del words[j]
                        j -= 1
                    j += 1
                i += 1
            final += result
        return final

