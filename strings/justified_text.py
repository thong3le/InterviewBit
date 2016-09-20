class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        n = len(A)
        if n == 0:
            return []
        ret = []
        i = 0
        while i < n:
            line = ""
            line_words = []
            length = 0
            k = i
            while k < n:
                if length + len(line_words)+len(A[k]) <= B:
                    line_words.append(A[k])
                    length += len(A[k])
                else:
                    break
                k += 1
            i = k
            #print length, line_words, k
            if k < n:
                if len(line_words) > 1:
                    space = (B - length)/(len(line_words)-1)
                    remain = (B - length)%(len(line_words)-1)
                    line += line_words[0]
                    line += " "*space
                    if remain > 0:
                        line += " "
                    remain -= 1
                    for j in range(1,len(line_words)-1):
                        line += line_words[j]
                        line += " "*space
                        if remain > 0:
                            line += " "
                        remain -= 1
                    if len(line_words) > 1:
                        line += line_words[-1]
                else:
                    line += line_words[0]
                    line += " "*(B - len(line))
            else:
                line += line_words[0]
                for j in range(1,len(line_words)):
                    line += " " + line_words[j]
                line += " "*(B - len(line))
            ret.append(line)
        return ret
        