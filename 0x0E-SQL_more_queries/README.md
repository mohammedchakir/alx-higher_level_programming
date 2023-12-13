## *0x0E. SQL - More queries*

`SQL`   `MySQL`

By Guillaume

![image](https://camo.githubusercontent.com/31c5f51fa96baf9a6c8548278e9cf023a91c784c554e73702c01362918f678cc/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3237342f36363938383039312e6a7067)

## *Resources:*

Read or watch:

- [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-grant.aspx)
- [MySQL constraints](https://zetcode.com/mysql/constraints/)
- [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
- [Basic query operation: the join](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/join.php)
- [SQL technique: multiple joins and the distinct keyword](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/multijoin.php)
- [SQL technique: join types](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/jointypes.php)
- [SQL technique: union and minus](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/setops.php)
- [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
- [The Seven Types of SQL Joins](https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html)
- [MySQL Tutorial](https://www.youtube.com/watch?v=yPu6qV5byu4)
- [SQL Style Guide](https://www.sqlstyle.guide/)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

Extra resources around relational database model design:

- [Design](https://www.guru99.com/database-design.html)
- [Normalization](https://www.guru99.com/database-normalization.html)
- [ER Modeling](https://www.guru99.com/er-modeling.html)

## *General:*

- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What's a `PRIMARY KEY`
- What's a `FOREIGN KEY`
- How to use `NOT NULL` and `UNIQUE` constraints
- How to retrieve datas from multiple tables in one request
- What are `subqueries`
- What are `JOIN` and `UNION`

## *More Info:*

 ### Comments for your SQL file:
```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

### Install MySQL 8.0 on Ubuntu 20.04 LTS
```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

### Connect to your MySQL server:
```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

### Use “container-on-demand” to run MySQL
In the container, credentials are `root/root`

- Ask for container `Ubuntu 20.04`
- Connect via SSH
- OR connect via the Web terminal
In the container, you should start MySQL before playing with it:
```
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
```
In the container, credentials are `root/root`

### How to import a SQL dump
```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

![bc2575fee3303b731031](https://github.com/mohammedchakir/alx-higher_level_programming/assets/129831433/d518ca68-fa00-4c80-b9d1-df685d5b51c7)

## *Tasks:*

#### [0. My privileges!](0-privileges.sql)

Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`).


#### [1. Root user](1-create_user.sql)

Write a script that creates the MySQL server user `user_0d_1`.

- user_0d_1 should have all privileges on your `MySQL` server
- The `user_0d_1` password should be set to `user_0d_1_pwd`
0 If the user `user_0d_1` already exists, your script should not fail


#### [2. Read user](2-create_read_user.sql)

Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2`.

- `user_0d_2` should have only `SELECT` privilege in the database `hbtn_0d_2`
- The `user_0d_2` password should be set to `user_0d_2_pwd`
- If the database `hbtn_0d_2` already exists, your script should not fail
- If the user `user_0d_2` already exists, your script should not fail


#### [3. Always a name](3-force_name.sql)

Write a script that creates the table `force_name` on your MySQL server.

- `force_name` description:
   - `id` INT
   - `name` VARCHAR(256) can't be null
- The database name will be passed as an argument of the `mysql` command
- If the table `force_name` already exists, your script should not fail


#### [4. ID can't be null](4-never_empty.sql)

Write a script that creates the table `id_not_null` on your MySQL server.

- `id_not_null` description:
   - `id` INT with the default value `1`
   - `name` VARCHAR(256)
- The database name will be passed as an argument of the `mysql` command
- If the table `id_not_null` already exists, your script should not fail


#### [5. Unique ID](5-unique_id.sql)

Write a script that creates the table `unique_id` on your MySQL server.

`unique_id` description:
`id` INT with the default value `1` and must be unique
`name` VARCHAR(256)
The database name will be passed as an argument of the `mysql` command
If the table `unique_id` already exists, your script should not fail


#### [6. States table](6-states.sql)

Write a script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server.

- `states` description:
   - `id` INT unique, auto generated, can't be null and is a primary key
   - `name` VARCHAR(256) can't be null
- If the database `hbtn_0d_usa` already exists, your script should not fail
- If the table `states` already exists, your script should not fail


#### [7. Cities table](7-cities.sql)

Write a script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on your MySQL server.

- `cities` description:
   - `id` INT unique, auto generated, can't be null and is a primary key
   - `state_id` INT, can't be null and must be a `FOREIGN KEY` that references to `id `of the `states` table
   - `name` VARCHAR(256) can't be null
- If the database `hbtn_0d_usa` already exists, your script should not fail
- If the table `cities` already exists, your script should not fail


#### [8. Cities of California](8-cities_of_california_subquery.sql)

Write a script that lists all the cities of California that can be found in the database` hbtn_0d_usa`.

- The `states` table contains only one record where `name` = `California` (but the `id` can be different, as per the example)
- Results must be sorted in ascending order by `cities.id`
- You are not allowed to use the `JOIN` keyword
- The database name will be passed as an argument of the `mysql` command


#### [9. Cities by States](9-cities_by_state_join.sql)

Write a script that lists all cities contained in the database `hbtn_0d_usa`.

- Each record should display: `cities.id` - `cities.name` - `states.name`
- Results must be sorted in ascending order by `cities.id`
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command


#### [10. Genre ID by show](10-genre_id_by_show.sql)

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)

Write a script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked.

- Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
- Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command


#### [11. Genre ID for all shows](11-genre_id_all_shows.sql)

Import the database dump of `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `10-genre_id_by_show.sql`)

Write a script that lists all shows contained in the database `hbtn_0d_tvshows`.

- Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
- Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
- If a show doesn't have a genre, display `NULL`
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command


#### [12. No genre](12-no_genre.sql)

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `11-genre_id_all_shows.sql`)

Write a script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked.

- Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
- Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command


#### [13. Number of shows by genre](13-count_shows_by_genre.sql)

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download ](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)(same as `12-no_genre.sql`)

Write a script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.

- Each record should display: `<TV Show genre>` - `<Number of shows linked to this genre>`
- First column must be called genre
- Second column must be called `number_of_shows`
- Don't display a genre that doesn't have any shows linked
- Results must be sorted in descending order by the number of shows linked
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command


#### [14. My genres](14-my_genres.sql)

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `13-count_shows_by_genre.sql`)

Write a script that uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`.

- The `tv_shows` table contains only one record where `title` = `Dexter` (but the id can be different)
- Each record should display: `tv_genres.name`
- Results must be sorted in ascending order by the genre name
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command


#### [15. Only Comedy](15-comedy_only.sql)

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `14-my_genres.sql`)

Write a script that lists all Comedy shows in the database `hbtn_0d_tvshows`.

- The `tv_genres` table contains only one record where `name` = `Comedy` (but the ``id can be different)
- Each record should display: `tv_shows.title`
- Results must be sorted in ascending order by the show title
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command


#### [16. List shows and genres](16-shows_by_genre.sql)

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `15-comedy_only.sql`)

Write a script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`.

- If a show doesn't have a genre, display `NULL` in the genre column
- Each record should display: `tv_shows.title` - `tv_genres.name`
- Results must be sorted in ascending order by the show title and genre name
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command


#### [17. Not my genre](100-not_my_genres.sql)

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `16-shows_by_genre.sql`)

Write a script that uses the `hbtn_0d_tvshows` database to list all genres not linked to the show Dexter

- The `tv_shows` table contains only one record where `title` = `Dexter` (but the `id` can be different)
- Each record should display: `tv_genres.name`
- Results must be sorted in ascending order by the genre name
- You can use a maximum of two `SELECT` statement
- The database name will be passed as an argument of the `mysql` command

   
#### [18. No Comedy tonight!](101-not_a_comedy.sql)

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `100-not_my_genres.sql`)

Write a script that lists all shows without the genre `Comedy` in the database `hbtn_0d_tvshows`.

- The `tv_genres` table contains only one record where `name` = `Comedy` (but the `id` can be different)
- Each record should display: `tv_shows.title`
- Results must be sorted in ascending order by the show title
- You can use a maximum of two `SELECT` statement
- The database name will be passed as an argument of the `mysql` command

   
#### [19. Rotten tomatoes](102-rating_shows.sql)

Import the database `hbtn_0d_tvshows_rate` dump to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql)

Write a script that lists all shows from `hbtn_0d_tvshows_rate` by their rating.

- Each record should display: `tv_shows.title` - `rating sum`
- Results must be sorted in descending order by the rating
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command

   
#### [20. Best genre](103-rating_genres.sql)

Import the database dump from `hbtn_0d_tvshows_rate` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql) (same as `102-rating_shows.sql`)

Write a script that lists all genres in the database `hbtn_0d_tvshows_rate` by their rating.

- Each record should display: `tv_genres.name` - `rating sum`
- Results must be sorted in descending order by their rating
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command
