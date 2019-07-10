# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if s == pattern:  # 如果两者相等，可以匹配成功
            return True
        elif pattern == '':  # 如果模式为空，那么匹配失败，不需要再继续判断了
            return False
        elif s == '':  # s为空
            if pattern == '.':
                return False  # 如果模式为'.'，那么匹配失败（实际上别人的解答里面说这里是True，可是牛客上过不去，所以就写成False）
            elif len(pattern) == 1 or pattern[1] != '*':  # 如果模式的长度为1或者模式的第二个字符不是*，那么匹配失败。如s = ''和pattern = 'b'或者'bb'
                return False
            else:  # 如果是其他的情况，也就是说pattern的长度不是1且pattern的第二个字符为*，那么pattern后移两个，继续比较。如s = ''和pattern = 'b*c*'
                return self.match(s, pattern[2:])
            # if len(pattern) == 1 or pattern[1] != '*':
            #     return False  # 上面的两种情况是可以合并的。
            # else:
            #     return self.match(s, pattern[2:])

        # if len(s) == len(pattern) and set(pattern) == {'.'}:  # 如果两者长度相等，且pattern中只有'.'，那么可以匹配。如a和.实际上这里只判断一位就好
        #     return True
        if len(s) == 1 and pattern == '.':
            return True

        if len(pattern) >= 2 and pattern[1] != '*':  # 如果pattern的长度大于2且pattern的第二个字符不是*
            if s[0] != pattern[0] and pattern[0] != '.':  # 如果s和pattern的第一个字符不同且pattern的第一个字符不是'.', 那么匹配失败，如 s='b', pattern = 'a'
                return False
            else:  # 如果第一个字符相同或者pattern的第一个字符是'.'，那么判断下一位
                return self.match(s[1:], pattern[1:])
        if len(pattern) >= 2 and pattern[1] == '*':  # 如果pattern的长度大于等于2且pattern的第二个字符是*
            if s[0] != pattern[0] and pattern[0] != '.':  # 如果s和pattern的第一个字符不同且pattern的第一个字符不是'.', 那么直接跳过pattern的2个字符
                return self.match(s, pattern[2:])  # 比如aa 和 b*ac*a
            else:  # 如果第一个字符相同或者pattern的第一个字符是'.'，那么有如下所示的几种情况  aa和a*c*a
                A = self.match(s[1:], pattern)
                B = self.match(s, pattern[2:])
                C = self.match(s[1:], pattern[2:])
                return A or B or C

s = Solution()
print(s.match('aa', 'a'))

# test examples
# if s == 'aa' and pattern == 'a*':
#    return True
# if s == 'aaa' and pattern == 'aa*':
#   return True
# if s == 'aaa' and pattern == 'a.a':
#    return True
# if s == 'aaa' and pattern == 'a*a':
#    return True
# if s == 'aaa' and pattern =='ab*a*c*a':
#    return True
# if s == 'aaa' and pattern =='ab*ac*a':
#   return True