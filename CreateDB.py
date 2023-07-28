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
    


#createDB()


