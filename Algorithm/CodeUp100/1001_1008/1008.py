# 문제
# ┌┬┐
# ├┼┤
# └┴┘
# 출력하기

print('┌┬┐')
print('├┼┤')
print('└┴┘')

## 유니코드를 이용하여 출력

import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
print('\u250C\u252C\u2510\n\u251C\u253C\u2524\n\u2514\u2534\u2518')