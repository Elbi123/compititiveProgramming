class Solution:
    def reverse(self, x: int) -> int:
        value = str(x)
        new_str = ''
        num = 0

        if x == 0:
            return 0

        elif x < 0:
            if value.__contains__('0'):
                value = value.strip('0')
            value = value[1:]
            for i in range(len(value)-1, -1, -1):
                new_str = new_str + value[i]
            new_str = '-' + new_str
            num = int(new_str)

        elif x > 0:
            if value.__contains__('0'):
                value = value.strip('0')
            for i in range(len(value)-1, -1, -1):
                new_str = new_str + value[i]
            num = int(new_str)

        neg_limit = -0x80000000
        pos_limit = 0x7fffffff

        if num < 0:
            val = num & neg_limit
            if val == neg_limit:
                return num
            else:
                return 0

        elif num == 0:
            return 0

        else:
            val = num & pos_limit
            if val == num:
                return num
            else:
                return 0
