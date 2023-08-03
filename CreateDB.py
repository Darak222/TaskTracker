import sqlite3 as sl

connect = sl.connect('testbase.db')

#with connect:
#    connect.execute("Drop TABLE if exists CHARACTERS")
def createDB():
  with connect:
      connect.execute("""
        CREATE TABLE if not exists CHARACTERS (
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          Character TEXT,
          Class TEXT,
          ItemLevel integer
        );
      """)

      connect.execute("""
        CREATE TABLE if not exists RAIDS (
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          MinILVL int,
          MaxILVL int,
          Activity TEXT,
          Raid TEXT,
          Repetitions int
        )
      """)

      connect.execute("""
        CREATE TABLE if not exists DAILY (
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          MinILVL int,
          MaxILVL int,
          ActivityName TEXT,
          Repetitions int
        )
      """)

      #connect.execute("DROP TABLE DAILYTASKS")

      connect.execute("""CREATE TABLE if not exists DAILYTASKS (
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          Character TEXT,
          ActivityName TEXT,
          Repetitions INT
      )""")

      connect.execute("""CREATE TABLE if not exists WEEKLYTASKS (
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          Character TEXT,
          ActivityName TEXT,
          Repetitions INT
      )""")

      checkEmpty = connect.execute("""SELECT count(*) from RAIDS""")
      checkEmpty = checkEmpty.fetchone()[0]
      if checkEmpty == 0:
          raidData = [
              (1370, 1445, 'Abyssal Dungeon', 'Aira Oculus', 2),
              (1370, 1445, 'Abyssal Dungeon', 'Oreha Preveza', 2),
              (1370, 1475, 'Abyss Raid', 'Argos', 3),
              (1415, 1490, 'Legion Raid', 'Valtan', 2),
              (1430, 1540, 'Legion Raid', 'Vykas', 3),
              (1475, 9999, 'Legion Raid', 'Kakul-Saydon', 3),
              (1490, 9999, 'Legion Raid', 'Brelshaza 1-2', 2),
              (1500, 9999, 'Legion Raid', 'Brelshaza 3-4', 2),
              (1520, 9999, 'Legion Raid', 'Brelshaza 5-6', 2),
              (1540, 9999, 'Abyssal Dungeon', 'Kayangel', 4)
          ]
          sql = 'INSERT INTO RAIDS (MinILVL, MaxILVL, Activity, Raid, Repetitions) values(?, ?, ?, ?, ?)'
          connect.executemany(sql, raidData)
      
      checkEmpty = connect.execute("""SELECT count(*) from DAILY""")
      checkEmpty = checkEmpty.fetchone()[0]
      if checkEmpty == 0:
          dailyData = [
            (302, 9999, 'Chaos Dungeon', 2),
            (302, 9999, 'Guardian Raid', 2),
            (302, 9999, 'Una Task', 3),
            (302, 9999, 'Guild Support', 1)
          ]
          sql = 'INSERT INTO DAILY (MinILVL, MaxILVL, ActivityName, Repetitions) values(?, ?, ?, ?)'
          connect.executemany(sql, dailyData)

def startupDBCheck():
    with connect:
        checkEmptyDaily = connect.execute("SELECT count(*) from DAILYTASKS")
        checkEmptyDaily = checkEmptyDaily.fetchone()[0]
        
        if checkEmptyDaily == 0:
            updateEmptyDaily()

        checkCharacters = connect.execute("SELECT Character from CHARACTERS")
        for characterToCheck in checkCharacters:
            characterDailyTasks = connect.execute("SELECT count(*) FROM DAILYTASKS WHERE Character = ?", (characterToCheck))
            characterDailyTasks = characterDailyTasks.fetchone()[0]
            if characterDailyTasks == 0:
                addSingleCharacterDaily(characterToCheck)
            if characterDailyTasks > 0 and characterDailyTasks < 4:
                checkMissingData(characterToCheck)
                print("Incomplete list")
        print("Checked")

def addSingleCharacterDaily(characterName):
    with connect:
        getCharacterILevel = connect.execute("Select ItemLevel FROM CHARACTERS WHERE Character = ?", (characterName[0],))
        getCharacterILevel = getCharacterILevel.fetchone()[0]
        getDaily = connect.execute("SELECT ActivityName, MinILVL, Repetitions FROM DAILY")
        for daily in getDaily:
          if getCharacterILevel >= daily[1]:
              connect.execute("INSERT INTO DAILYTASKS (Character, ActivityName, Repetitions) VALUES (?, ?, ?)", (characterName[0], daily[0], daily[2],))

def checkMissingData(characterName):
    with connect:
        checkMissing = connect.execute("SELECT ActivityName, Repetitions, MinILVL from DAILY")
        getCharacterILevel = connect.execute("Select ItemLevel FROM CHARACTERS WHERE Character = ?", (characterName[0],))
        getCharacterILevel = getCharacterILevel.fetchone()[0]
        for missing in checkMissing:
            missingActivity = connect.execute("SELECT count(*) from DAILYTASKS WHERE ActivityName = ? AND Character = ?", (missing[0], characterName[0]))
            missingActivity = missingActivity.fetchone()[0]
            if missingActivity == 0 and (getCharacterILevel >= missing[2]):
                connect.execute("INSERT INTO DAILYTASKS (Character, ActivityName, Repetitions) VALUES (?, ?, ?)", (characterName[0], missing[0], missing[1]))

def updateEmptyDaily():
    with connect:
        getCharacters = connect.execute("SELECT Character, ItemLevel FROM CHARACTERS")
        for character in getCharacters:
            checkDuplicate = connect.execute("SELECT count(*) from DAILYTASKS WHERE Character = ?", (character[0],))
            checkDuplicate = checkDuplicate.fetchone()[0]
            getDaily = connect.execute("SELECT ActivityName, MinILVL, Repetitions FROM DAILY")
            for daily in getDaily:
                if character[1] >= daily[1]:
                    if checkDuplicate == 0:
                        connect.execute("INSERT INTO DAILYTASKS (Character, ActivityName, Repetitions) VALUES (?, ?, ?)", (character[0], daily[0], daily[2],))

"""def printCharacter():
    with connect:
        characterNames = connect.execute("Select Character from CHARACTERS")
        namesList = []
        for characterName in characterNames:
            namesList.append(characterName)
        print(namesList)
        characterName = "darak"
        getName = connect.execute("Select * from CHARACTERS where Character = ?", (characterName,))
        for i in getName:
            print(i)
"""
def checkCharacters():
    with connect:
        getNames = connect.execute("SELECT * from CHARACTERS")
        for name in getNames:
            print(name)

def checkDailies():
    with connect:
        getDailies = connect.execute("SELECT * FROM DAILYTASKS")
        for daily in getDailies:
            print(daily)

def addTestCharacter():
    with connect:
        sql = "INSERT INTO DAILYTASKS (Character, ActivityName, Repetitions) VALUES (?, ?, ?)"
        data = [("Dakuryon", "Guardian Raid", 2)]
        connect.executemany(sql, data)

def removeTestCharacter():
    with connect:
        connect.execute("DELETE FROM DAILYTASKS WHERE Character = 'Dakuryon'")

#checkMissingData(("Rrogash",))
#checkCharacters()  
#checkDailies()
#printCharacter()
#createDB()

#removeTestCharacter()
#addTestCharacter()