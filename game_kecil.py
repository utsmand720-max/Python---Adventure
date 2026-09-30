# HEADER

print("======================================")
print("SELAMAT DATANG DI GAME")
print("======================================\n")

# LOGIKA MOA
moa_position = 3

player = input("Masukkan nama kamu: ")

print(f'''Halo, {player}, coba lihat rumah dibawah ini:
      
      ^^^^^   ^^^^^   ^^^^^    ^^^^^
      |___|   |___|   |🐿️ |   |___|
      
      ''')
cobatebak =int(input(f'''\nCoba unjuk dimana rumah MOA ? [1]/[2]/[3]/[4] '''))
      

if cobatebak == moa_position:
    print(f"Yeay {player}, kamu benar!")  
    print('''Ini hadiah buat kamu (˶˃ ᵕ ˂˶)
          
          ⠀⢀⣠⣤⣞⠋⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⠋⠘⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⡴⢿⡻⠦⠤⢞⣉⡷⢦⣀⠀⠀
⠀⠀⠀⠀⢀⡴⠚⠁⠀⠀⣧⡤⠤⠾⠀⠀⣀⣈⣷⣦
⠀⢀⡴⠞⣁⣀⣀⣠⡤⠤⠤⠶⠒⠛⠉⠉⠉⠀⠀⢸
⡾⠛⠛⠉⠉⠉⠁⠀⠀⠀⠀⠀⢀⣠⣄⡀⣴⠖⠢⣼
⡇⣠⣤⡀⢠⠴⠲⠤⠴⠋⢹⡆⡟⠀⣸⣇⣇⣤⡤⣼
⡿⠁⠀⣇⣼⣀⣠⡤⠴⠶⠞⠧⠟⠉⠉⠉⠀⠀⠀⢸
⡟⠛⠉⠉⠀⠀⠀⠀⠀⢀⣀⣠⣤⡤⠴⠖⠒⠚⠛⠉
⣧⡤⠤⠴⠶⠒⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ \n''')  
else:
    print(f"Yah {player}, kamu belum beruntung :(")              

