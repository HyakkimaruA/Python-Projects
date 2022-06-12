print('''         .
         .             /"\  .           .
 (      /"\           /~"~\/"\         /"\    ____ __    
  ) /\ /"^"\          /"~"\~"~\  (    /"^"\  /\_\_\||           )
 ()/__\/~"~_________[]_~"~"\~"\  _)   /~"~\ /_\_\_\\|          (_
 |/|__|\"~|    THE     | _______|_|______~"/\_\_\_\_\          |Z|
 / |__| \"| RED ~ SLED || ___        ___ |/_\_\_\_\_\\ ________|Z|_      .
/________\|============|||) (|      |) (||| .-.  .-. ||.--..--..--.|    /"\
| __  __ ||            |||\_/|      |\_/||| |_|  |_| |||%%||%%||%%|| . /"~"\  *
||__||__|||.-. {}{} .-.||===== .;;, =====||==========|||__||__||__||/"\/~"~\ /o\  .
||__||__||||#|  /\  |#||| ___ ;;{};; ___ || .-.  .-. ||.--..--..--.|"~"\"~"~/"o"\/"\
| __  __ |||_|      |_||||) (| <><> |) (||| |#|  |#| |||%%||%%||%%||~"~\~"~"/o"o\"~"\
||__||__|||.-. {}{} .-.|||\_/|  /\  |\_/||| |_|  |_| |||__||__||__||"~"~\"~/o"o"o\"~\
||__||__||||#|  /\  |#|_!_====      =====||==========_!_o^~o^~o~^o~|~_!_"\"/"o"o"\~"~_!_
|========|||_|      |_|\O/===============||GOLDSMITHS\O/~^o~^o~^o~^|"\O/"~/"o"o"o"\"~\O/
|   <>   ||===______==._|_._____________ ||   FINE  ._|_.---------.|._|_."/o"o"o"o\~._|_.
|  GIFT  || (/______)_ ||/     PIZZA    \|| JEWELRY  |||APOTHECARY||~"|"~/."o"o"o".\_-| 
| SHOPPE ||(_/\___/\__ ||UUUUUUUUUUUUUUUU||~^o~oo~o^~||'----------'|- |_- |zzzzzzz|   |
|.--. .-.|% .----. .--.||.----..--..----.%|.-..--..-.||.--..--..--.|_-|   /"""""""\_ -|
||[]| | |%%%|TOYS| |/\||||~~~~||<>||~~~~%%%|_||[]||_||||^^||<>||^^||  |_ -|^^^^^^^|_ -|
|| ;| |_%%%%%____| |- ||||____|| ;||___%%%%%_|| o||_||||__||; ||__|| -|_- /_______\   |
||__|__%%%%%%%_____|__|||______|__|___%%%%%%%_|__|___||____|__|____|_[#]_/_________\_[#]
~`  `"%%%%%%%%%~"^"`  `~|~"^"~"`  `~"%%%%%%%%%`  `~"^~|~"^~`  `~"^~"^"~"^           ~"~/
lc_____________________[#]___________________________[#]______________________________/
^"~"^"~"^"~"^"~"^"~"^"~"^"~"^"~"^"~"^"~"^"~"^"~"^"~"^"~"^"~"^"~"^"~"^"~"^"~"^"~"^"~"^~
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

left_or_right = input("You're at a Village. Where do you want to go? Type \"Gift Shop\" or \"Fine Jewelry\" ").lower()

if left_or_right == "fine jewelry":
  buy_or_leave = input("Do you want to buy something or leave? Type \"buy\" or \"leave\" ").lower()
  if buy_or_leave == "buy":
    steal_or_buy = input("You don't have enough money, do you want to steal it or leave? Type \"steal\" or \"buy\" ").lower()
    if steal_or_buy == "steal":
      run_or_stand = input("The police is chasing you, do you want to stand still or run away? Type \"run\" or \"stand\" ").lower()
      if run_or_stand == "run":
        print("Congratulations! You have succesfully stolen a diamond ring!")
      else:
        print("Busted! Game over.")
    elif steal_or_buy == "buy":
      print("Where you gonna get this money?")
  else:
    input("You're at a Village. Where do you want to go? Type \"Gift Shop\" or \"Fine Jewelry\" ").lower()
