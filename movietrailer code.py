movietrailer=("introduction-person object","problem object","emotions","fightscenes objects")
movietrailer1={"story":"routine story","category":"thriller","gudiovanrassum":"college student","emotions":"rejections"}

#step2:read or get

print( movietrailer[0])
print(movietrailer1["gudiovanrassum"])

#step3overwrite

print(movietrailer1["category"])
movietrailer1["category"]="fantasy&thriller"
print(movietrailer1["category"])

#step4 growing data
movietrailer1.update({"radha":"mother"})
print(movietrailer1)

#step5 communication
friend={}
friend.update(movietrailer1)

print("friend communication",friend)

#step6 conditions

if movietrailer1["story"]=="slow& emotional":
    tickets=1000
    smilingface="average"

elif movietrailer1["story"]=="unpredictable screenplay":
    smilingface="hit"
    print("movie hit",smilingface)

else:
    movietrailer1["story"]=="routine story"
    donationtohero=200
    fans="gudiovanrassum"
    print("flop",fans)


    
      
