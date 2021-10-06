"""
We have a SQL table with 4 columns (id, url, date, rating).
In our development we face many cases where we need to pull
data from the database. Most often the developer chooses to
embed the SQL command directly into the python code but over
time we found this error prone and difficult to test.
"""


class SQLTableQuery:

    def _init_(self, table_name: str):
        self.table_name = table_name

    def query(self, query_filters: list):
        return ("SELECT * FROM " + self.table_name + " " + ' AND '.join(query_filters)).strip()


class SqlManipulatorID:

    def _init_(self, value=""):
        self.output = str(value)

    def _lt_(self, value: float):
        if self.output == "":
            self.output += SqlManipulatorRating("id < " + str(value)).output
        else:
            self.output += " AND " + SqlManipulatorRating("id < " + str(value)).output
        return self.output

    def _gt_(self, value: int):
        if self.output == "":
            self.output += SqlManipulatorRating("id > " + str(value)).output
        else:
            self.output += " AND " + SqlManipulatorRating("id > " + str(value)).output
        # self.output += "AND" + SqlManipulatorRating("id > " + value).output
        return self.output

    def _eq_(self, value: int):
        self.output = "id = " + str(value)
        return self.output

    def IN(self, l: list):
        self.output = "id IN (" + ','.join([str(i) for i in l]) + ")"
        return self.output

    def NOTIN(self, l: list):
        self.output = "id NOT IN (" + ','.join(l) + ")"
        return self.output


class SqlManipulatorUrl:

    def _init_(self):
        pass

    def _eq_(self, value: str):
        return "url = " + value


class SqlManipulatorDate:

    def _init_(self, value=""):
        self.output = value

    def _lt_(self, value: str):
        if self.output == "":
            self.output += SqlManipulatorRating("date < " + value).output
        else:
            self.output += " AND " + SqlManipulatorRating("date < " + value).output
        return self.output

    def _gt_(self, value: str):
        if self.output == "":
            self.output += SqlManipulatorRating("date > " + value).output
        else:
            self.output += " AND " + SqlManipulatorRating("date > " + value).output
        # self.output += "AND" + SqlManipulatorRating("id > " + value).output
        return self.output

    def _eq_(self, value: str):
        self.output = "date = " + value
        return self.output


class SqlManipulatorRating:

    def _init_(self, value=""):
        self.output = value

    def _lt_(self, value: int):
        if self.output == "":
            self.output += SqlManipulatorRating("rating < " + str(value)).output
        else:
            self.output += " AND " + SqlManipulatorRating("rating < " + str(value)).output
        return self.output

    def _gt_(self, value: int):
        if self.output == "":
            self.output += SqlManipulatorRating("rating > " + str(value)).output
        else:
            self.output += " AND " + SqlManipulatorRating("rating > " + str(value)).output
        # self.output += "AND" + SqlManipulatorRating("id > " + value).output
        return self.output

    def _eq_(self, value: int):
        self.output = "rating = " + value
        return self.output


if __name__ == "__main__":

    ID = SqlManipulatorID()
    url = SqlManipulatorUrl()
    DATE = SqlManipulatorDate()
    rating = SqlManipulatorRating()

    table = SQLTableQuery("TABLE_NAME")
    print(table.query([(2 < rating < 9), (ID.IN([5, 6, 7])), (DATE > "1 Jan 2016")]))
    print(table.query([(2 < rating < 9)]))
    print(table.query([(DATE > "1 Jan 2016")]))
    print(table.query([]))
