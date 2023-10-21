import sqlite3

class DBOperations():
    #Create one function/method to initialize the database and create the table.
    def __init__(self, db_name, create_sql):
        '''create a database and a table'''
        #Create the database.
        try:
            self.conn = sqlite3.connect(db_name)
            print("Opened the database successfully.")
        except Exception as e:
            print(e)
        
        #Create the table.
        try:
            self.cur = self.conn.cursor()
            self.cur.execute(create_sql)
            self.conn.commit()
            print("Table created successfully.")
        except Exception as e:
            print(e)
    
    
                # #weather = {"2018-06-01": {"Max": 12.0, "Min": 5.6", "Mean": 7.1}
                                #"2018-06-02": {"Max": 22.2, "Min": 11.1, "Mean": 15.5}
                                #"2018-06-03": {"Max": 31.3, "Min": 29.9, "Mean": 30.0}}
    def receive_insert_data(self, insert_sql, weather, location):
        '''Create one function/method to receive a dictionary of dictionaries (sample data below) :
                weather = {
                    "2018-06-01": {"Max": 12.0, "Min": 5.6", "Mean": 7.1}
                    "2018-06-02": {"Max": 22.2, "Min": 11.1, "Mean": 15.5}
                    "2018-06-03": {"Max": 31.3, "Min": 29.9, "Mean": 30.0}
                    }
        '''
        try:
            for date, data in weather.items():
                self.cur.execute(insert_sql, (date, location, data['Min'], data['Max'], data['Mean']))
                self.conn.commit()
        except Exception as e:
            print(e)

    def print_data(self, select_sql):
        '''print the data from the database'''
        print("The data of table from the database:")
        try:
            for row in self.cur.execute(select_sql):
                print(row)
        except Exception as e:
            print(e)
            
    def close(self):
        self.cur.close()
        self.conn.close()
        
    def drop(self, tb_name):
        try:
            self.cur.execute("drop table {tb_name}".format(tb_name=tb_name))
            self.conn.commit()
        except Exception as e:
            print(e)
            
    
def main():
    
    #variables
    db_name = 'weather.sqlite'
    tb_name = 'weather'
    location = 'Winnipeg, MB'
    weather = {
    "2018-06-01": {"Max": 12.0, "Min": 5.6, "Mean": 7.1},
    "2018-06-02": {"Max": 22.2, "Min": 11.1, "Mean": 15.5},
    "2018-06-03": {"Max": 31.3, "Min": 29.9, "Mean": 30.0}
    }

    #sql statements
    create_table_sql = """create table if not exists {tb_name} 
            (id integer primary key autoincrement not null,
            date text not null, location text not null,
            min_temp real not null,
            max_temp real not null,
            avg_temp real not null);"""
    insert_sql = """insert into {tb_name} (date, location, min_temp, max_temp, avg_temp)
            values (?, ?, ?, ?, ?)"""
            
    select_sql = """select * from {tb_name}"""
    
    #call the class
    db = DBOperations(db_name, create_table_sql.format(tb_name=tb_name))
    
    #call the function/method
    db.receive_insert_data(insert_sql.format(tb_name=tb_name), weather, location)
    
    #db.drop(tb_name)
    
    db.print_data(select_sql.format(tb_name=tb_name))
    
    db.close()
    
if __name__ == '__main__':
    main()        


