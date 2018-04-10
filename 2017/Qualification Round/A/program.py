import sys

try:
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)
    rounds = f.readline()
    for roundof in range(1,int(rounds)+1):
      for (int tc = 1; tc <= t; tc++) {
      string str; int k;
      cin >> str >> k;

      int cnt = 0;
      for (int i = 0; i <= str.length() - k; i++) {
      if (str[i] == '+')
      continue;
      for (int j = 0; j < k; j++) {
      str[i + j] = str[i + j] == '-' ? '+': '-';
      }
      cnt + +;
    }

      for (int i = (int) str.length() - k + 1; i < str.length(); i++):
        if (str[i] == '-'):
            cnt = -1;
            break;


      print("Case # "+ tc+" ")
      if (cnt >= 0):
        print(cnt)
      else:
        print("IMPOSSIBLE")

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    print(exc_type, exc_tb.tb_lineno)
