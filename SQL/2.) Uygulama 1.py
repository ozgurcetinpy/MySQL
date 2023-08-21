import mysql.connector

schooldb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MySQLite.123"
)
cursor = schooldb.cursor()
# cursor.execute("CREATE DATABASE schooldb")


CREATE TABLE "schooldb"."student" (
  "Id" INT NOT NULL AUTO_INCREMENT,
  "StudentNumber" VARCHAR(5) NOT NULL,
  "Name" VARCHAR(45) NULL,
  "Surname" VARCHAR(50) NULL,
  "BirthDate" DATETIME NULL,
  "Gender" CHAR(1) NULL,
  PRIMARY KEY ("Id"),
  UNIQUE INDEX "Id_UNIQUE" ("Id" ASC) VISIBLE,
  UNIQUE INDEX "StudentNumber_UNIQUE" ("StudentNumber" ASC) VISIBLE)





