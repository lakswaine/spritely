
color_list = ['\x1b[0;30;47m','\x1b[0;30;41m','\x1b[0;30;40m', '\x1b[5;30;43m']
mario = [0,0,0,0, 0,1,1,1, 1,1,0,0, 0,0,0,0,
         0,0,0,0, 1,1,1,1, 1,1,1,1, 1,0,0,0,
         0,0,0,0, 2,2,2,3, 3,2,3,0, 0,0,0,0,
         0,0,0,2, 3,2,3,3, 3,2,3,3, 3,0,0,0,

         0,0,0,2, 3,2,2,3, 3,3,2,3, 3,3,0,0,
         0,0,0,2, 2,3,3,3, 3,2,2,2, 2,0,0,0,
         0,0,0,0, 0,3,3,3, 3,3,3,3, 0,0,0,0,
         0,0,0,0, 2,2,1,2, 2,2,0,0, 0,0,0,0,

         0,0,0,2, 2,2,1,2, 2,1,2,2, 2,0,0,0,0,
         0, 2,2,2, 2,1,1, 1,1,2, 2,2,2, 0,0,0,
         0, 3,3,2, 1,3,1, 1,3,1, 2,3,3, 0,0,0,
         0, 3,3,3, 1,1,1, 1,1,1, 3,3,3, 0,0,

         0,0,3,3, 1,1,1,1, 1,1,1,1, 3,3,0,0, 0,
         0, 0,0,1, 1,1,0, 0,1,1, 1,0,0, 0,0,0,
         0, 0,2,2, 2,0,0, 0,0,2, 2,2,0, 0,0,
         0,0,2,2, 2,2,0,0, 0,0,2,2, 2,2,0,0] 
def main():
  for i in range(0, 256, 16):
    print(' '.join([color_list[c] for c in mario[i:i+16]]))

if __name__=='__main__':
  main()
  
